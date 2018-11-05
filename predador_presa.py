from math import sin

class PredadorPresa(object):

    def __init__(self, presa, predador, indice_passo, variante):
        self.presa = presa
        self.predador = predador
        self.indice_passo = indice_passo
        self.variante = variante

    def f_presa(self, t):
        alpha, beta = 0.8, 0.004
        coeficiente = self.define_coeficiente(t)
        return coeficiente * alpha * self.presa - beta * self.presa * self.predador

    def f_predador(self):
        gama, delta = 0.8, 0.001
        return -gama * self.predador + delta * self.presa * self.predador

    def define_coeficiente(self, t):
        if self.variante == 1:
            return 1
        elif self.variante == 2:
            return 1.5 + sin(t)

    def imprime(self):
        print("Pop.Presa: {:.0f}, Pop.Predador: {:.0f}, t={}".format(self.presa, self.predador, self.indice_passo))
