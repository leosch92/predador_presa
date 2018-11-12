import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def plot_presa_predador(data, title="Presa e Predador vs Tempo", x_label="Tempo",
                        y_label="Quantidade", ):

    fig = plt.figure(figsize=(10, 6))
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    historico_presa = data['presa']
    historico_predador = data['predador']

    delta = data['delta_t']

    x_ticks = [x * delta for x in range(0, len(historico_presa))]
    plt.plot(x_ticks, historico_presa, label="Presa")
    plt.plot(x_ticks, historico_predador, label="Predador")

    max_y = max(np.max(historico_presa), np.max(historico_predador))
    plt.ylim((0, max_y))

    plt.legend()
    plt.show()


