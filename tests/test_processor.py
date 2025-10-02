from muscle_music.processor import MovingAverage, EnvelopeDetector, EventDetector


def test_moving_average():
    ma = MovingAverage(window_size=3)
    assert ma.update(1) == 1
    assert ma.update(2) == 1.5
    assert ma.update(4) == (1 + 2 + 4) / 3


def test_envelope():
    env = EnvelopeDetector(alpha=0.5)
    v1 = env.update(0)
    v2 = env.update(10)
    assert v2 >= 0


def test_event_detector():
    called = {'v': 0}

    def on_event():
        called['v'] += 1

    ed = EventDetector(threshold=5, on_event=on_event)
    ed.update(1)
    ed.update(6)
    assert called['v'] == 1
    # go below hysteresis
    ed.update(3)
    ed.update(6)
    assert called['v'] == 2
