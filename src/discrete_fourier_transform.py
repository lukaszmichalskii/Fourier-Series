import math


def discrete_fourier_transform(x):
    X = []
    N = len(x)
    for k in range(N):
        re = 0
        im = 0
        for n in range(N):
            phi = (2 * math.pi * k * n) / N
            re += x[n] * math.cos(phi)
            im -= x[n] * math.sin(phi)

        re = re / N
        im = im / N

        frequency = k
        amplitude = math.sqrt(math.pow(re, 2) + math.pow(im, 2))
        phase = math.atan2(im, re)

        X.append({'re': re, 'im': im, 'freq': frequency, 'amp': amplitude, 'phase': phase})

    return X
