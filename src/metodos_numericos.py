def runge_kutta_2(y_k, t_k, delta_t, f):
    k1 = f(y_k, t_k)
    k2 = f(y_k + delta_t * k1, t_k+delta_t)
    return y_k + (delta_t/2) * (k1 + k2)

def backward_differentiation_formula_3(lista_y, t_k, delta_t, f, y_k_mais_um=None, metodo_preditor=None):
    y_k_mais_um = checa_e_faz_predicao(y_k_mais_um, lista_y[-1], t_k, delta_t, metodo_preditor, f)
    return (18 * lista_y[2] - 9 * lista_y[1] + 2 * lista_y[0] + 6 * delta_t * f(y_k_mais_um, t_k + delta_t)) / 11.0


def adams_moulton_3(lista_y, t_k, delta_t, f, y_k_mais_um=None, metodo_preditor=None):
    y_k_mais_um = checa_e_faz_predicao(y_k_mais_um, lista_y[-1], t_k, delta_t, metodo_preditor, f)
    return lista_y[1] + (delta_t/12) * (-f(lista_y[0], t_k - delta_t) + 8 * f(lista_y[1], t_k) + 5 * f(y_k_mais_um, t_k + delta_t))


def checa_e_faz_predicao(y_k_mais_um, y_k, t_k, delta_t, metodo_preditor, f):
    if y_k_mais_um is None:
        return metodo_preditor(y_k, t_k, delta_t, f)
    return y_k_mais_um
