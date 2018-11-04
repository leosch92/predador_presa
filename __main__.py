from predador_presa import PredadorPresa
from metodos_numericos import runge_kutta_2, backward_differentiation_formula_3, adam_moulton_3
from copy import copy


def main():
    constantes_temporais = define_constantes_temporais()
    numero_correcoes = 2
    numero_iteracoes = calcula_numero_iteracoes(constantes_temporais)
    populacao_presa_inicial, populacao_predador_inicial = 1000, 100

    opcao = captura_input()
    loop = True

    while loop:
        if opcao == 1:
            inicializacoes_necessarias = 2
            lista_pp = inicializa(constantes_temporais['delta_t'], populacao_presa_inicial, populacao_predador_inicial,
                                  inicializacoes_necessarias, runge_kutta_2)
            calcula_passos(constantes_temporais['delta_t'], lista_pp, numero_iteracoes, inicializacoes_necessarias,
                           numero_correcoes, backward_differentiation_formula_3, runge_kutta_2)
            opcao = captura_input()
        elif opcao == 2:
            inicializacoes_necessarias = 1
            lista_pp = inicializa(constantes_temporais['delta_t'], populacao_presa_inicial, populacao_predador_inicial,
                                  inicializacoes_necessarias, runge_kutta_2)
            calcula_passos(constantes_temporais['delta_t'], lista_pp, numero_iteracoes, inicializacoes_necessarias,
                           numero_correcoes, adam_moulton_3, runge_kutta_2)
            opcao = captura_input()
        elif opcao == 9:
            loop = False
        else:
            opcao = captura_input()


def captura_input():
    print("\n")
    try:
        return int(input("Escolha o método desejado:\n1-BDF3\n2-AM3\n9-Exit\n"))
    except ValueError:
        return 0


def define_constantes_temporais():
    return {'t_final': 100.0, 't_inicial': 0.0, 'delta_t': 0.1}


def calcula_numero_iteracoes(ct):
    return int((ct['t_final'] - ct['t_inicial'])/ct['delta_t'])


def inicializa(delta_t, pop_presa, pop_predador, inicializacoes, metodo):
    lista_pp = [PredadorPresa(pop_presa, pop_predador, 0)]
    for i in range(inicializacoes):
        pp = metodo(lista_pp[i], delta_t)
        pp.t += 1
        lista_pp.append(pp)
    for pp in lista_pp:
        pp.imprime()
    return lista_pp


def calcula_passos(delta_t, lista_pp, n_iter, inicializacoes, n_correcoes, metodo_calculador, metodo_preditor):
    for i in range(n_iter - (inicializacoes + 1)):
        pp_k_mais_um = metodo_calculador(lista_pp, delta_t, metodo_preditor=metodo_preditor)
        pp_k_mais_um = corrige(lista_pp, pp_k_mais_um, n_correcoes, delta_t, metodo_calculador)
        pp_k_mais_um.t += 1
        lista_pp_copia = []
        for j in range(len(lista_pp) - 1):
            lista_pp_copia.append(lista_pp[j + 1])
        lista_pp_copia.append(pp_k_mais_um)
        #lista_pp_copia[0], lista_pp_copia[1], lista_pp_copia[2] = lista_pp[1], lista_pp[2], pp_k_mais_um
        lista_pp = copy(lista_pp_copia)
        pp_k_mais_um.imprime()


def corrige(lista_pp, pp_k_mais_um, n_correcoes, delta_t, metodo):
    for j in range(n_correcoes):
        pp_k_mais_um = metodo(lista_pp, delta_t, pp_k_mais_um)
    return pp_k_mais_um


if __name__ == "__main__":
    main()
