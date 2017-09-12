from math import sin, pi
from collections import namedtuple, Sequence

HarmonicParameters = namedtuple('HarmonicParameters', ['amplitude', 'phase', 'frequency'])


def validate_N(N):
    if (N < 512) or not is_power_of_2(N):
        raise ValueError('N should be "512, 1024, 2048..."')


def is_power_of_2(number):
    return number and not number & (number - 1)


def harmonic(harmonic_params, N, i):
    return harmonic_params.amplitude * sin((2*pi*harmonic_params.frequency*i) / N + harmonic_params.phase)


def harmonic_signal(harmonic_params, N):
    validate_N(N)
    for i in range(N):
        yield harmonic(harmonic_params, N, i)


def polyharmonic_signal(harmonics_params, N):    
    validate_N(N)

    for i in range(N):
        single_harmonic = lambda params: harmonic(params, N, i)
        yield sum((single_harmonic(params) for params in harmonics_params))
