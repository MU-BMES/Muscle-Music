"""EMG reader utilities: real serial reader and a simulator for testing."""
import threading
import time
import random
from collections import deque
from typing import Callable, Optional


class EMGSimulator:
    """Simulate EMG amplitude values (0-1023) at a given sample rate."""

    def __init__(self, callback: Callable[[int], None], rate_hz: float = 100.0):
        self.callback = callback
        self.rate_hz = rate_hz
        self._running = False
        self._thread: Optional[threading.Thread] = None

    def start(self):
        self._running = True
        self._thread = threading.Thread(target=self._run, daemon=True)
        self._thread.start()

    def stop(self):
        self._running = False
        if self._thread:
            self._thread.join(timeout=1.0)

    def _run(self):
        period = 1.0 / self.rate_hz
        base = 50
        while self._running:
            # produce bursts to mimic muscle contractions
            if random.random() < 0.02:
                # contraction burst
                for _ in range(random.randint(5, 30)):
                    val = min(1023, int(base + random.gauss(400, 150)))
                    self.callback(val)
                    time.sleep(period)
                continue

            # baseline noise
            val = max(0, int(base + random.gauss(0, 20)))
            self.callback(val)
            time.sleep(period)


try:
    import serial

    class SerialEMGReader:
        """Read integer EMG amplitude values from a serial port.

        Expects newline-separated integers.
        """

        def __init__(self, port: str, baudrate: int = 115200, callback: Optional[Callable[[int], None]] = None):
            self.port = port
            self.baudrate = baudrate
            self.callback = callback
            self._running = False
            self._thread: Optional[threading.Thread] = None
            self._ser: Optional[serial.Serial] = None

        def start(self):
            self._ser = serial.Serial(self.port, self.baudrate, timeout=1)
            self._running = True
            self._thread = threading.Thread(target=self._read_loop, daemon=True)
            self._thread.start()

        def stop(self):
            self._running = False
            if self._thread:
                self._thread.join(timeout=1.0)
            if self._ser and self._ser.is_open:
                self._ser.close()

        def _read_loop(self):
            while self._running:
                try:
                    line = self._ser.readline().decode(errors='ignore').strip()
                    if not line:
                        continue
                    val = int(line)
                    if self.callback:
                        self.callback(val)
                except Exception:
                    # ignore malformed lines and continue
                    continue

except Exception:
    # serial not available; define a stub to avoid import errors
    SerialEMGReader = None
