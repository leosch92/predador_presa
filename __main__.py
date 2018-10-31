from predador_presa import PredadorPresa
from metodos_numericos import runge_kutta_2

def main():
    constantes_temporais = define_constantes_temporais()
    numero_iteracoes = calcula_numero_iteracoes(constantes_temporais)

    pp0 = PredadorPresa(1000, 100, 0)
    pp1 = inicializa_com_runge_kutta_2(pp0, constantes_temporais['delta_t'])
    print(pp1.presa, pp1.predador)

def define_constantes_temporais():
    return {'t_final': 1.0, 't_inicial': 0.0, 'delta_t': 0.1}

def calcula_numero_iteracoes(ct):
    return int((ct['t_final'] - ct['t_inicial'])/ct['delta_t'])

# Recebe sistema predador-presa inicial e o inicializa com RK2
def inicializa_com_runge_kutta_2(pp0, delta_t):
    return runge_kutta_2(pp0, delta_t)

if __name__ == "__main__":
    main()