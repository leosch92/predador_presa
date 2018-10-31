from predador_presa import PredadorPresa

def runge_kutta_2(pp_k, delta_t):
    pp_kmaismeio = euler_modificado(pp_k, delta_t)
    presa = pp_k.presa + delta_t * pp_kmaismeio.f_presa()
    predador = pp_k.predador + delta_t * pp_kmaismeio.f_predador()
    return PredadorPresa(presa, predador, pp_k.t + 1)

def euler_modificado(pp_k, delta_t):
    presa = pp_k.presa + delta_t / 2.0 * pp_k.f_presa()
    predador = pp_k.predador + delta_t / 2.0 * pp_k.f_predador()
    return PredadorPresa(presa, predador, pp_k.t + 0.5)
