from predador_presa import PredadorPresa


def runge_kutta_2(pp_k, delta_t):
    pp_k_mais_meio = euler_modificado(pp_k, delta_t)
    presa = pp_k.presa + delta_t * pp_k_mais_meio.f_presa()
    predador = pp_k.predador + delta_t * pp_k_mais_meio.f_predador()
    return PredadorPresa(presa, predador, pp_k.t + 1)


def euler_modificado(pp_k, delta_t):
    presa = pp_k.presa + delta_t / 2.0 * pp_k.f_presa()
    predador = pp_k.predador + delta_t / 2.0 * pp_k.f_predador()
    return PredadorPresa(presa, predador, pp_k.t + 0.5)


# Quando pp_k_mais_um não é passado, temos que fazer uma predição com Runge-Kutta.
# Caso contrário, se trata de uma correção
def backward_differentiation_formula_3(lista_pp, delta_t, pp_k_mais_um=None):
    flag_predicao = False
    if pp_k_mais_um is None:
        pp_k_mais_um = runge_kutta_2(lista_pp[2], delta_t)
        flag_predicao = True

    presa = (18 * lista_pp[2].presa - 9 * lista_pp[1].presa + 2 * lista_pp[0].presa + 6 * delta_t * pp_k_mais_um.f_presa()) / 11.0
    predador = (18 * lista_pp[2].predador - 9 * lista_pp[1].predador + 2 * lista_pp[0].predador + 6 * delta_t * pp_k_mais_um.f_predador()) / 11.0
    return PredadorPresa(presa, predador, lista_pp[2].t + 1 if flag_predicao else lista_pp[2].t)
