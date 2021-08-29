import math
import random


def generate_signal_fn1(x_signal, y_signal):
    for i in range(150):
        angle = random.uniform(0, 100)
        x_signal.append(150 * math.cos(angle))
        y_signal.append(150 * math.sin(angle))
        angle += math.pi * 2
