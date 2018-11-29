from math import sin
from numpy import array


class PredadorPresa(object):

    def __init__(self, constantes_populacionais, indice_passo, variante):
        self.presa = constantes_populacionais['populacao_presa_inicial']
        self.predador = constantes_populacionais['populacao_predador_inicial']
        self.presa_max = constantes_populacionais['populacao_presa_maxima']
        self.indice_passo = indice_passo
        self.variante = variante

    def f(self, y, t):
        alpha, beta, gama, delta = 0.8, 0.004, 0.8, 0.001
        aumento_presa = self.define_aumento_presa(y, t, alpha)
        f_presa = aumento_presa - beta * y[0] * y[1]
        f_predador = -gama * y[1] + delta * y[0] * y[1]
        return array([f_presa, f_predador])

    def define_aumento_presa(self, y, t, alpha):
        if self.variante == 1:
            return alpha * y[0]
        elif self.variante == 2:
            return (1.5 + sin(t))* alpha * y[0]
        elif self.variante == 3:
            return (self.presa_max - y[0])/self.presa_max * alpha * y[0]

    def imprime(self):
        print("Pop.Presa: {:.0f}, Pop.Predador: {:.0f}, k={}".format(self.presa, self.predador, self.indice_passo))
