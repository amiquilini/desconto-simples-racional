#!/usr/bin/env python3

def metodo_newton(x, y, p, ti, i, e):
    """Método de Newton para encontrar a taxa real.

    :param x: valor à prazo
    :param y: valor à vista
    :param p: número de parcelas
    :param ti: taxa inicial
    :param i: número de iterações
    :param e: entrada

    :return: taxa final e número de iterações realizadas
    """
    i += 1
    if e:
        tf = ti - (fe(x, y, p, ti) / dfe(x, y, p, ti))
    else:
        tf = ti - (f(x, y, p, ti) / df(x, y, p, ti))

    if abs(tf - ti) > 0.0001:
        return metodo_newton(x, y, p, tf, i, e)
    else:
        return tf, i


# Funções auxiliares para o método de Newton: fe e dfe (com entrada), f e df (sem entrada)
def fe(x, y, p, t):
    """Função auxiliar para o método de Newton com entrada."""
    return (y * t * ((1 + t) ** (p - 1))) - (x / p) * (((1 + t) ** p) - 1)


def dfe(x, y, p, t):
    """Derivada da função auxiliar para o método de Newton com entrada."""
    return (y * (((1 + t) ** (p - 1)) + t * (p - 1) * ((1 + t) ** (p - 2)))) - (x * ((1 + t) ** (p - 1)))


def f(x, y, p, t):
    """Função auxiliar para o método de Newton sem entrada."""
    return (y * t) - (x / p) * (1 - ((1 + t) ** (-p)))


def df(x, y, p, t):
    """Derivada da função auxiliar para o método de Newton sem entrada."""
    return y - (x * ((1 + t) ** (-p - 1)))
