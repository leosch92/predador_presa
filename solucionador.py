from predador_presa import PredadorPresa
from lista_utils import atualiza_lista
from numpy import array
from metodos_numericos import runge_kutta_2, backward_differentiation_formula_3, adams_moulton_3


class Solucionador(object):

    def __init__(self, constantes_temporais, condicao_inicial, numero_correcoes, opcao_metodo, variante):
        self.constantes_temporais = constantes_temporais
        self.condicao_inicial = condicao_inicial
        self.metodo_inicializador = runge_kutta_2
        self.metodo_preditor = runge_kutta_2
        self.numero_iteracoes = self.calcula_numero_iteracoes()
        self.numero_correcoes = numero_correcoes
        self.t_atual = constantes_temporais['t_inicial']
        self.inicializacoes_necessarias = 0
        self.opcao_metodo = opcao_metodo
        self.metodo_calculador = self.escolhe_metodo_calculador()
        self.variante = variante

    def calcula_numero_iteracoes(self):
        return int((self.constantes_temporais['t_final'] -
                    self.constantes_temporais['t_inicial']) / self.constantes_temporais['delta_t'])

    def escolhe_metodo_calculador(self):
        if self.opcao_metodo == 1:
            return backward_differentiation_formula_3
        else:
            return adams_moulton_3

    def resolve(self):
        if self.opcao_metodo == 1:
            self.inicializacoes_necessarias = 2
        elif self.opcao_metodo == 2:
            self.inicializacoes_necessarias = 1
        lista_pp = self.inicializa()
        self.calcula_passos(lista_pp)

    def inicializa(self):
        lista_pp = [PredadorPresa(self.condicao_inicial[0], self.condicao_inicial[1], 0, self.variante)]
        for i in range(self.inicializacoes_necessarias):
            pp_k_mais_um = self.inicializa_pp(lista_pp[i])
            self.t_atual = self.constantes_temporais['delta_t'] * pp_k_mais_um.indice_passo
            lista_pp.append(pp_k_mais_um)
        for pp_k_mais_um in lista_pp:
            pp_k_mais_um.imprime()
        return lista_pp

    def inicializa_pp(self, pp_k):
        pp_k_mais_um = PredadorPresa(0, 0, pp_k.indice_passo + 1, self.variante)
        y_k_mais_um = self.metodo_inicializador(array([pp_k.presa, pp_k.predador]), self.t_atual,
                                                self.constantes_temporais['delta_t'], pp_k.f)
        pp_k_mais_um.presa, pp_k_mais_um.predador = y_k_mais_um[0], y_k_mais_um[1]
        return pp_k_mais_um

    def calcula_passos(self, lista_pp):
        for i in range(self.numero_iteracoes - (self.inicializacoes_necessarias + 1)):
            pp_k_mais_um = self.calcula_pp(lista_pp)
            pp_k_mais_um = self.corrige(lista_pp, pp_k_mais_um)
            self.t_atual = self.constantes_temporais['delta_t'] * pp_k_mais_um.indice_passo
            lista_pp = atualiza_lista(lista_pp, pp_k_mais_um)
            pp_k_mais_um.imprime()

    def calcula_pp(self, lista_pp):
        pp_k_mais_um = PredadorPresa(0, 0, lista_pp[-1].indice_passo + 1, self.variante)
        lista_y = [array([pp.presa, pp.predador]) for pp in lista_pp]
        y_k_mais_um = self.metodo_calculador(lista_y, self.t_atual, self.constantes_temporais['delta_t'],
                                             lista_pp[-1].f, metodo_preditor=self.metodo_preditor)
        pp_k_mais_um.presa, pp_k_mais_um.predador = y_k_mais_um[0], y_k_mais_um[1]
        return pp_k_mais_um

    def corrige(self, lista_pp, pp_k_mais_um):
        for j in range(self.numero_correcoes):
            pp_k_mais_um = self.calcula_pp(lista_pp)
        return pp_k_mais_um
