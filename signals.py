from collections import namedtuple
from math import pi, sin

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
    for i in plotting_range(N):
        yield harmonic(harmonic_params, N, i)


def polyharmonic_signal(harmonics_params, N):
    validate_N(N)

    for i in plotting_range(N):
        single_harmonic = lambda params: harmonic(params, N, i)
        yield sum((single_harmonic(params) for params in harmonics_params))


def polyharmonic_linear(harmonic_params, N):
    amplitude_function = lambda x, i: x * (i%N) * 0.001
    phase_function = lambda x, i: x * (i%N) * 0.001
    frequency_function = lambda x, i: x * (i%N) * 0.001
    current_params = harmonic_params
    for i in plotting_range(N*2):
        yield harmonic(current_params, N, i%N)
        phase = phase_function(harmonic_params.phase, i)
        amplitude = amplitude_function(harmonic_params.amplitude, i)
        frequency = frequency_function(harmonic_params.frequency, i)
        current_params = HarmonicParameters(amplitude, phase, frequency)


def plotting_range(N):
    return range(N)
