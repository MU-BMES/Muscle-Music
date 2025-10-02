"""Signal processing helpers for EMG: smoothing, envelope detection, and event detection."""
from collections import deque
from typing import Callable, Deque, Optional


class MovingAverage:
    def __init__(self, window_size: int = 5):
        self.window_size = max(1, window_size)
        self.buffer: Deque[float] = deque(maxlen=self.window_size)

    def update(self, value: float) -> float:
        self.buffer.append(value)
        return sum(self.buffer) / len(self.buffer)


class EnvelopeDetector:
    """Simple envelope using exponential smoothing on rectified signal."""

    def __init__(self, alpha: float = 0.1):
        self.alpha = alpha
        self.env: Optional[float] = None

    def update(self, value: float) -> float:
        rect = abs(value)
        if self.env is None:
            self.env = rect
            return rect
        self.env = self.alpha * rect + (1 - self.alpha) * self.env
        return self.env


class EventDetector:
    """Detect when envelope crosses a threshold and invoke a callback once per event."""

    def __init__(self, threshold: float, on_event: Optional[Callable[[], None]] = None):
        self.threshold = threshold
        self.on_event = on_event
        self._above = False

    def update(self, env_value: float):
        if not self._above and env_value >= self.threshold:
            self._above = True
            if self.on_event:
                self.on_event()
        elif self._above and env_value < self.threshold * 0.8:
            # hysteresis to avoid rapid re-triggering
            self._above = False
