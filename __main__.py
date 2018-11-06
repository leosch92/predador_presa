#!/usr/bin/env python
# -*- coding: utf-8 -*-
from solucionador import Solucionador


def main():
    constantes_temporais = {'t_final': 100.0, 't_inicial': 0.0, 'delta_t': 0.1}
    numero_correcoes = 2
    populacao_presa_inicial, populacao_predador_inicial = 1000, 100

    opcao = captura_input()
    loop = True

    while loop:
        if opcao in (1, 2):
            solucionador = Solucionador(constantes_temporais, (populacao_presa_inicial, populacao_predador_inicial),
                                        numero_correcoes, opcao, 1)
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


if __name__ == "__main__":
    main()
