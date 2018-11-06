#!/usr/bin/env python
# -*- coding: utf-8 -*-
from solucionador import Solucionador


def main():
    constantes_temporais = {'t_final': 100.0, 't_inicial': 0.0, 'delta_t': 0.1}
    numero_correcoes = 2
    populacao_presa_inicial, populacao_predador_inicial = 1000, 100

    metodo, variante = captura_input()
    loop = True

    while loop:
        if metodo in (1, 2) and variante in (1, 2):
            solucionador = Solucionador(constantes_temporais, (populacao_presa_inicial, populacao_predador_inicial),
                                        numero_correcoes, metodo, variante)
            solucionador.resolve()
            metodo, variante = captura_input()
        elif variante == 3:
            #TODO implementar terceira variante, incluindo no primeiro if
            print("Ainda não implementado")
            metodo, variante = captura_input()
        elif variante == 9:
            loop = False
        else:
            metodo, variante = captura_input()


def captura_input():
    print("\n")
    try:
        return int(input("Escolha o método desejado:\n1- BDF3\n2- AM3\n")), \
               int(input("Escolha a variante do problema desejada:\n"
                         "1- Crescimento da população ilimitado\n"
                         "2- Coeficiente de fertilidade com comportamente cíclico\n"
                         "3- Limitação superior à população de presas\n"
                         "9- Sair\n"))
    except ValueError:
        return 0, 0


if __name__ == "__main__":
    main()
