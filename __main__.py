from solucionador import Solucionador
from metodos_numericos import runge_kutta_2, backward_differentiation_formula_3, adams_moulton_3


def main():
    constantes_temporais = {'t_final': 100.0, 't_inicial': 0.0, 'delta_t': 0.1}
    numero_correcoes = 2
    numero_iteracoes = calcula_numero_iteracoes(constantes_temporais)
    populacao_presa_inicial, populacao_predador_inicial = 1000, 100

    opcao = captura_input()
    loop = True

    while loop:
        if opcao == 1:
            solucionador = Solucionador(constantes_temporais['delta_t'],
                                        (populacao_presa_inicial, populacao_predador_inicial),
                                        runge_kutta_2, backward_differentiation_formula_3, runge_kutta_2,
                                        numero_iteracoes, numero_correcoes, inicializacoes_necessarias=2)
            solucionador.resolve()
            opcao = captura_input()
        elif opcao == 2:
            solucionador = Solucionador(constantes_temporais['delta_t'],
                                        (populacao_presa_inicial, populacao_predador_inicial),
                                        runge_kutta_2, adams_moulton_3, runge_kutta_2,
                                        numero_iteracoes, numero_correcoes, inicializacoes_necessarias=1)
            solucionador.resolve()
            opcao = captura_input()
        elif opcao == 9:
            loop = False
        else:
            opcao = captura_input()


def captura_input():
    print("\n")
    try:
        return int(input("Escolha o método desejado:\n1-BDF3\n2-AM3\n9-Sair\n"))
    except ValueError:
        return 0


def calcula_numero_iteracoes(ct):
    return int((ct['t_final'] - ct['t_inicial'])/ct['delta_t'])


if __name__ == "__main__":
    main()
