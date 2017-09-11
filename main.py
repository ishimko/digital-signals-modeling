from math import pi

import matplotlib.pyplot as plt

import drawer
from signals import HarmonicParameters, harmonic_signal, polyharmonic_signal


def main():
    show_phases()
    show_frequencies()
    show_amplitudes()


def show_phases():
    phases = [0, pi, pi/6, pi/4, pi/2]
    params = lambda x: HarmonicParameters(amplitude=10, phase=x, frequency=2)
    drawer.draw_plots('Phases', harmonic_signal, params, phases)


def show_frequencies():
    params = lambda x: HarmonicParameters(amplitude=3, phase=pi/2, frequency=x)
    frequencies = [5, 4, 2, 6, 3]
    drawer.draw_plots('Frequences', harmonic_signal, params, frequencies)


def show_amplitudes():
    params = lambda x: HarmonicParameters(amplitude=x, phase=pi/2, frequency=1)
    amplitudes = [2, 3, 6, 5, 1]
    drawer.draw_plots('Amplitudes', harmonic_signal, params, amplitudes)


if __name__ == '__main__':
    main()
