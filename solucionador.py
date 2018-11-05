from predador_presa import PredadorPresa
from copy import copy


class Solucionador(object):

    def __init__(self, delta_t, condicao_inicial, metodo_inicializador, metodo_calculador,
                 metodo_preditor, numero_iteracoes, numero_correcoes, inicializacoes_necessarias):
        self.delta_t = delta_t
        self.condicao_inicial = condicao_inicial
        self.inicializacoes_necessarias = inicializacoes_necessarias
        self.metodo_inicializador = metodo_inicializador
        self.metodo_calculador = metodo_calculador
        self.metodo_preditor = metodo_preditor
        self.numero_iteracoes = numero_iteracoes
        self.numero_correcoes = numero_correcoes

    def resolve(self):
        lista_pp = self.inicializa()
        self.calcula_passos(lista_pp)

    def inicializa(self):
        lista_pp = [PredadorPresa(self.condicao_inicial[0], self.condicao_inicial[1], 0)]
        for i in range(self.inicializacoes_necessarias):
            pp = self.metodo_inicializador(lista_pp[i], self.delta_t)
            pp.t += 1
            lista_pp.append(pp)
        for pp in lista_pp:
            pp.imprime()
        return lista_pp

    def calcula_passos(self, lista_pp):
        for i in range(self.numero_iteracoes - (self.inicializacoes_necessarias + 1)):
            pp_k_mais_um = self.metodo_calculador(lista_pp, self.delta_t, metodo_preditor=self.metodo_preditor)
            pp_k_mais_um = self.corrige(lista_pp, pp_k_mais_um)
            pp_k_mais_um.t += 1
            lista_pp_copia = []
            for j in range(len(lista_pp) - 1):
                lista_pp_copia.append(lista_pp[j + 1])
            lista_pp_copia.append(pp_k_mais_um)
            lista_pp = copy(lista_pp_copia)
            pp_k_mais_um.imprime()

    def corrige(self, lista_pp, pp_k_mais_um):
        for j in range(self.numero_correcoes):
            pp_k_mais_um = self.metodo_calculador(lista_pp, self.delta_t, pp_k_mais_um)
        return pp_k_mais_um
