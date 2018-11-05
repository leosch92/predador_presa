def runge_kutta_2(y_k, t_k, delta_t, f):
    y_k_mais_meio = euler_auxiliar(y_k, t_k, delta_t, f)
    return y_k + delta_t * f(y_k_mais_meio, t_k + 0.5)


def euler_auxiliar(y_k, t_k, delta_t, f):
    return y_k + delta_t / 2.0 * f(y_k, t_k)


def backward_differentiation_formula_3(lista_y, t_k, delta_t, f, y_k_mais_um=None, metodo_preditor=None):
    y_k_mais_um = checa_e_faz_predicao(y_k_mais_um, lista_y[2], t_k, delta_t, metodo_preditor)
    return (18 * lista_y[2] - 9 * lista_y[1] + 2 * lista_y[0] + 6 * delta_t * f(y_k_mais_um, t_k + 1)) / 11.0


def adams_moulton_3(lista_y, t_k, delta_t, f, y_k_mais_um=None, metodo_preditor=None):
    y_k_mais_um = checa_e_faz_predicao(y_k_mais_um, t_k, metodo_preditor, lista_y[1], delta_t)
    return lista_y[1] + (delta_t / 12) * (-1 * lista_y[0] + 8 * lista_y[1] + 5 * y_k_mais_um)


def checa_e_faz_predicao(y_k_mais_um, y_k, t_k, delta_t, metodo_preditor):
    if y_k_mais_um is None:
        return metodo_preditor(y_k, t_k, delta_t)
    return y_k_mais_um
