from math import sin
from numpy import array


class PredadorPresa(object):

    def __init__(self, presa, predador, indice_passo, variante):
        self.presa = presa
        self.predador = predador
        self.indice_passo = indice_passo
        self.variante = variante

    def f(self, y, t):
        alpha, beta, gama, delta = 0.8, 0.004, 0.8, 0.001
        coeficiente = self.define_coeficiente(t)
        f_presa = coeficiente * alpha * y[0] - beta * y[0] * y[1]
        f_predador = -gama * y[1] + delta * y[0] * y[1]
        return array([f_presa, f_predador])

    def define_coeficiente(self, t):
        if self.variante == 1:
            return 1
        elif self.variante == 2:
            return 1.5 + sin(t)

    def imprime(self):
        print("Pop.Presa: {:.0f}, Pop.Predador: {:.0f}, k={}".format(self.presa, self.predador, self.indice_passo))
