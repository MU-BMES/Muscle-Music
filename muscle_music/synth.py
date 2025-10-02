"""Minimal synth: generate tones and play using simpleaudio."""
import numpy as np
import simpleaudio as sa
from typing import Optional


def sine_wave(frequency: float, duration: float = 0.2, sample_rate: int = 44100, amplitude: float = 0.3):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    wave = amplitude * np.sin(2 * np.pi * frequency * t)
    # convert to 16-bit PCM
    audio = (wave * 32767).astype(np.int16)
    return audio.tobytes(), sample_rate


class Synth:
    def __init__(self):
        self.sample_rate = 44100

    def play_tone(self, freq: float, duration: float = 0.2):
        data, sr = sine_wave(freq, duration, self.sample_rate)
        play_obj = sa.play_buffer(data, 1, 2, sr)
        # don't block; let it play
        return play_obj
