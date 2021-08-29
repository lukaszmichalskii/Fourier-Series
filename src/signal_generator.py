from src.generate_strategy import generate_signal_fn1


class SignalGenerator:

    def __init__(self):
        self.x_signal = []
        self.y_signal = []
        self.generate_fn = generate_signal_fn1

    def generate_signal(self):
        self.generate_fn(self.x_signal, self.y_signal)

        return self.x_signal, self.y_signal
