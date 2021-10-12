#!/usr/bin/env python3

import sys
import argparse
from desconto_racional import Tabela_Price
from desconto_racional import Financiamento

"""Programa principal para testes.
"""

def main(argv=None):
    """Desconto Racional por Dentro

    Os módulos argparse e tabulate foram utilizadas na implementação deste código.
    Caso seja necessário instalar os módulos citados, use:
        - pip install argparse
        - pip install tabulate

    :argument: argumentos da linha de comando:
    -h (--help) help
    -p (--parcelas) número de parcelas.
    -t (--taxa) taxa mensal (Taxa SELIC por padrão).
    -x (--valorP) valor da compra à prazo.
    -y (--valorV) valor da compra à vista.
    -e (--entrada) indica se houve entrada (False por padrão).

    Uso:
    - AD1_2021_2.py -p 10 -t 1 -x 500 -y 450 -e True
    - AD1_2021_2.py -p 18 -t 0 -x 3297.60 -y 1999
    - AD1_2021_2.py -p 10 -x 1190 - y 1094.80 -e True
    - AD1_2021_2.py -p 8 -t 4.55 -x 111064.80 -y 23000
    - AD1_2021_2.py -p 9 -t 0 -x 134788.8 -y 63816.24
    - AD1_2021_2.py -p 4 -t 3.0 -x 1080.11 -y 1000
    - AD1_2021_2.py --parcelas 14 --taxa 4.55 --valorP 14000.50 --valorV 23000 --entrada True
    - AD1_2021_2.py --help
    """

    parser = argparse.ArgumentParser(description='Calcula desconto racional por dentro')
    parser.add_argument('-p', '--parcelas', type=int, required=True, help='Numero de parcelas')
    parser.add_argument('-t', '--taxa', type=float, help='Taxa mensal (SELIC como valor padrao)', default=5.25)
    parser.add_argument('-x', '--valorP', type=float, required=True, help='Valor da compra a prazo')
    parser.add_argument('-y', '--valorV', type=float, help='Valor da compra a vista', default=None)
    parser.add_argument('-e', '--entrada', type=bool, help='Indica se houve entrada (True/False)', default=False)
    args = parser.parse_args()

    p = args.parcelas
    t = args.taxa
    x = args.valorP
    y = args.valorV
    e = args.entrada

    f = Financiamento(p, x, y, t, e)
    print(f)

    print()
    f.recomendacao_pagamento()

    # se a taxa não for fornecida, a taxa SELIC é utilizada
    # se a taxa informada for 0, a taxa real é utilizada
    if t == 0:
        t, i = f.taxa_real()
        t *= 100

    print("\nTabela Price:")
    tb = Tabela_Price(f.numero_parcelas(), f.valor_financiado(), t, f.valor_prestacao())
    tb.imprimir_tabela()


# Para rodar o script:
if __name__ == '__main__':
    sys.exit(main())




