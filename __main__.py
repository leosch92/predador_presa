from predador_presa import PredadorPresa
from metodos_numericos import runge_kutta_2, backward_differentiation_formula_3
from copy import copy


def main():
    constantes_temporais = define_constantes_temporais()
    numero_correcoes = 2
    inicializacoes_necessarias = 2
    numero_iteracoes = calcula_numero_iteracoes(constantes_temporais)
    populacao_presa_inicial, populacao_predador_inicial = 1000, 100

    lista_pp = inicializa(constantes_temporais['delta_t'], populacao_presa_inicial, populacao_predador_inicial, inicializacoes_necessarias, runge_kutta_2)

    calcula_passos(constantes_temporais['delta_t'], lista_pp, numero_iteracoes, inicializacoes_necessarias, numero_correcoes, backward_differentiation_formula_3)


def define_constantes_temporais():
    return {'t_final': 100.0, 't_inicial': 0.0, 'delta_t': 0.1}


def calcula_numero_iteracoes(ct):
    return int((ct['t_final'] - ct['t_inicial'])/ct['delta_t'])


def inicializa(delta_t, pop_presa, pop_predador, inicializacoes, metodo):
    lista_pp = [PredadorPresa(pop_presa, pop_predador, 0)]
    for i in range(inicializacoes):
        lista_pp.append(metodo(lista_pp[i], delta_t))
    for x in lista_pp:
        x.imprime()
    return lista_pp


def calcula_passos(delta_t, lista_pp, n_iter, inicializacoes, n_correcoes, metodo):
    lista_pp_copia = copy(lista_pp)
    for i in range(n_iter - inicializacoes):
        lista_pp_copia[2] = metodo(lista_pp, delta_t)
        lista_pp_copia[2] = corrige(lista_pp, lista_pp_copia[2], n_correcoes, delta_t, metodo)
        lista_pp_copia[0], lista_pp_copia[1] = lista_pp[1], lista_pp[2]
        lista_pp = lista_pp_copia
        lista_pp_copia[2].imprime()


def corrige(lista_pp, pp_k_mais_um, n_correcoes, delta_t, metodo):
    for j in range(n_correcoes):
        pp_k_mais_um = metodo(lista_pp, delta_t, pp_k_mais_um)
    return pp_k_mais_um


if __name__ == "__main__":
    main()
