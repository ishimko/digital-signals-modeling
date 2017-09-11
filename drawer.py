import matplotlib.pyplot as plt

def draw_plots(title, signal, params_builder, variable_parameter):
    plt.gcf().canvas.set_window_title(title)
    for phase in variable_parameter:
        plt.plot(list(signal(params_builder(phase), 512)))
    plt.show()
