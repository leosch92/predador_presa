from predador_presa import PredadorPresa
from copy import copy


class Solucionador(object):

    def __init__(self, constantes_temporais, condicao_inicial, metodo_inicializador, metodo_calculador,
                 metodo_preditor, numero_iteracoes, numero_correcoes, inicializacoes_necessarias, variante):
        self.constantes_temporais = constantes_temporais
        self.condicao_inicial = condicao_inicial
        self.inicializacoes_necessarias = inicializacoes_necessarias
        self.metodo_inicializador = metodo_inicializador
        self.metodo_calculador = metodo_calculador
        self.metodo_preditor = metodo_preditor
        self.numero_iteracoes = numero_iteracoes
        self.numero_correcoes = numero_correcoes
        self.variante = variante
        self.t_atual = constantes_temporais['t_inicial']

    def resolve(self):
        lista_pp = self.inicializa()
        self.calcula_passos(lista_pp)

    def inicializa(self):
        lista_pp = [PredadorPresa(self.condicao_inicial[0], self.condicao_inicial[1], self.t_atual, self.variante)]
        for i in range(self.inicializacoes_necessarias):
            pp_k_mais_um = self.inicializa_pp(lista_pp[i])
            self.t_atual = self.constantes_temporais['delta_t'] * pp_k_mais_um.indice_passo
            lista_pp.append(pp_k_mais_um)
        for pp_k_mais_um in lista_pp:
            pp_k_mais_um.imprime()
        return lista_pp

    def inicializa_pp(self, pp_k):
        pp_k_mais_um = PredadorPresa(0, 0, pp_k.indice_passo + 1, self.variante)
        pp_k_mais_um.presa = self.metodo_inicializador(pp_k.presa, self.t_atual,
                                                       self.constantes_temporais['delta_t'], pp_k.f_presa)
        pp_k_mais_um.predador = self.metodo_inicializador(pp_k.predador, self.t_atual,
                                                          self.constantes_temporais['delta_t'], pp_k.f_predador)
        return pp_k_mais_um

    def calcula_passos(self, lista_pp):
        for i in range(self.numero_iteracoes - (self.inicializacoes_necessarias + 1)):
            pp_k_mais_um = self.calcula_pp(lista_pp)
            pp_k_mais_um = self.corrige(lista_pp, pp_k_mais_um)
            self.t_atual = self.constantes_temporais['delta_t'] * pp_k_mais_um.t
            lista_pp = self.atualiza_lista_pp(lista_pp, pp_k_mais_um)
            pp_k_mais_um.imprime()

    def calcula_pp(self, lista_pp):
        pp_k_mais_um = PredadorPresa(0, 0, lista_pp[-1].indice_passo + 1, self.variante)
        lista_presas = [pp.presa for pp in lista_pp]
        lista_predadores = [pp.predador for pp in lista_pp]
        pp_k_mais_um.presa = self.metodo_calculador(lista_presas, self.t_atual,
                                                    self.constantes_temporais['delta_t'], lista_pp[-1].f_presa,
                                                    metodor_preditor=self.metodo_preditor)
        pp_k_mais_um.predador = self.metodo_calculador(lista_predadores, self.t_atual,
                                                       self.constantes_temporais['delta_t'], lista_pp[-1].f_predador,
                                                       metodo_preditor=self.metodo_preditor)
        return pp_k_mais_um

    def corrige(self, lista_pp, pp_k_mais_um):
        for j in range(self.numero_correcoes):
            pp_k_mais_um = self.calcula_pp(lista_pp)
        return pp_k_mais_um

    @staticmethod
    def atualiza_lista_pp(lista_pp, pp_k_mais_um):
        lista_pp_copia = []
        for j in range(len(lista_pp) - 1):
            lista_pp_copia.append(lista_pp[j + 1])
        lista_pp_copia.append(pp_k_mais_um)
        return copy(lista_pp_copia)
