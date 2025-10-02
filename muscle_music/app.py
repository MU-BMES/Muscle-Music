"""A small Tkinter app that shows live EMG envelope and triggers sounds."""
import threading
import tkinter as tk
from tkinter import ttk
from typing import Optional

from .emg_reader import EMGSimulator, SerialEMGReader
from .processor import MovingAverage, EnvelopeDetector, EventDetector
from .synth import Synth


class MuscleMusicApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Muscle Music")

        self.canvas = tk.Canvas(root, width=400, height=100, bg='black')
        self.canvas.pack(padx=8, pady=8)

        control_frame = ttk.Frame(root)
        control_frame.pack(fill='x', padx=8)

        ttk.Label(control_frame, text='Threshold:').pack(side='left')
        self.threshold_var = tk.DoubleVar(value=200.0)
        ttk.Scale(control_frame, from_=0, to=1023, variable=self.threshold_var, orient='horizontal').pack(fill='x', expand=True, side='left', padx=8)

        self.status = ttk.Label(root, text='Status: starting')
        self.status.pack(fill='x', padx=8, pady=4)

        # processing chain
        self.ma = MovingAverage(window_size=5)
        self.env = EnvelopeDetector(alpha=0.2)
        self.synth = Synth()

        self.event_detector = EventDetector(threshold=self.threshold_var.get(), on_event=self.on_event)

        # data for drawing
        self._env_history = [0] * 400

        # choose reader: try serial, else simulator
        self.reader = None
        try:
            # user may set port variable here or modify code to pass a port
            self.reader = SerialEMGReader(port='COM3', baudrate=115200, callback=self._on_sample) if SerialEMGReader else None
        except Exception:
            self.reader = None

        if not self.reader:
            self.reader = EMGSimulator(callback=self._on_sample, rate_hz=200)

        # start reader
        threading.Thread(target=self.reader.start, daemon=True).start()

        # polling UI
        self._update_ui()

    def _on_sample(self, value: int):
        # called from reader thread
        avg = self.ma.update(value)
        e = self.env.update(avg)
        self.event_detector.threshold = self.threshold_var.get()
        self.event_detector.update(e)
        # push history and schedule canvas redraw
        self._env_history.append(e)
        if len(self._env_history) > 400:
            self._env_history.pop(0)

    def on_event(self):
        # play a tone when event detected
        print('Event!')
        self.synth.play_tone(440.0, duration=0.2)

    def _update_ui(self):
        # draw envelope
        self.canvas.delete('all')
        w = 400
        h = 100
        maxv = max(max(self._env_history) if self._env_history else 1, 1)
        points = []
        for i, v in enumerate(self._env_history):
            x = i
            y = h - int((v / maxv) * h)
            points.append((x, y))
        for i in range(1, len(points)):
            x0, y0 = points[i - 1]
            x1, y1 = points[i]
            self.canvas.create_line(x0, y0, x1, y1, fill='lime')

        self.status.config(text=f'Status: env={self._env_history[-1]:.1f} threshold={self.threshold_var.get():.1f}')
        self.root.after(50, self._update_ui)


def run_app():
    root = tk.Tk()
    app = MuscleMusicApp(root)
    root.mainloop()

if __name__ == '__main__':
    run_app()
