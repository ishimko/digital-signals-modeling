from math import pi

import matplotlib.pyplot as plt

import drawer
from signals import HarmonicParameters, harmonic_signal, polyharmonic_signal


def main():    
    results = []
    for i, viewer in enumerate([show_phases, show_frequencies, show_amplitudes, show_polyharmonic]):
        plt.subplot(2, 2, i + 1)
        results.append(viewer())    
    plt.show()


def show_phases():
    phases = [0, pi, pi/6, pi/4, pi/2]
    params = lambda x: HarmonicParameters(amplitude=10, phase=x, frequency=2)
    drawer.draw_plots(r'\phi', harmonic_signal, params, phases)


def show_frequencies():
    params = lambda x: HarmonicParameters(amplitude=3, phase=pi/2, frequency=x)
    frequencies = [5, 4, 2, 6, 3]
    drawer.draw_plots(r'f', harmonic_signal, params, frequencies)


def show_amplitudes():
    params = lambda x: HarmonicParameters(amplitude=x, phase=pi/2, frequency=1)
    amplitudes = [2, 3, 6, 5, 1]
    drawer.draw_plots(r'a', harmonic_signal, params, amplitudes)


def show_polyharmonic():
    params = list(map(lambda x: HarmonicParameters(*x), [
        (1, 0, 1),
        (1, pi/4, 2),
        (1, pi/6, 3),
        (1, 2*pi, 4),
        (1, pi, 5)
    ]))
    return drawer.draw_polyharmonic(polyharmonic_signal, params)


if __name__ == '__main__':
    main()
