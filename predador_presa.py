class PredadorPresa(object):

    def __init__(self, presa, predador, t):
        self.presa = presa
        self.predador = predador
        self.t = t

    def f_presa(self):
        alpha, beta = 0.8, 0.004
        return alpha * self.presa - beta * self.presa * self.predador

    def f_predador(self):
        gama, delta = 0.8, 0.001
        return -gama * self.predador + delta * self.presa * self.predador

    def imprime(self):
        print("Pop.Presa: {:.0f}, Pop.Predador: {:.0f}, t={}".format(self.presa, self.predador, self.t))
