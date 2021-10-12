#!/usr/bin/env python3

import met_numerico
from tabulate import tabulate


class Financiamento:
    """Classe Financiamento contém todas as informações referentes ao financiamento realizado.
    """
    def __init__(self, p, x, y, t, e):
        """Construtor da classe financiamento para inicializar o objeto.

        :param p: numero de parcelas
        :param x: valor à prazo
        :param y: valor à vista
        :param t: taxa mensal
        :param e: entrada
        """
        self.p = p
        self.x = x
        self.y = y
        self.t = t / 100
        self.e = e

        if t == 0:
            self.t, i = self.taxa_real()

        self.CF = self.t / (1 - ((1 + self.t) ** (-self.p)))

        if not y:
            self.y = self.valor_presente()

    def __str__(self):
        """Representa o objeto do tipo financiamento como string.
        """
        if self.e:
            parcelas = "1+" + str(self.p - 1)
        else:
            parcelas = str(self.p)

        tf, i = self.taxa_real()
        return ("Parcelas: " + parcelas + "\n"
             "Taxa: " + str(round(self.t * 100, 4)) + "% \n"
             "Preço à Prazo: R$" + str(round(self.x, 2)) + "\n"
             "Preço à Vista: R$" + str(round(self.y, 2)) + "\n"
             "Valor Financiado: R$" + str(round(self.valor_financiado(), 2)) + "\n"
             "Taxa Real(" + str(i) + " iterações, fator aplicado = " + str(round(self.fator_k(), 4)) + "): " + str(round(tf * 100, 4)) + "% \n"
             "Coeficiente de Financiamento: " + str(round(self.CF, 5)) + "\n"
             "Prestação: R$" + str(round(self.valor_prestacao(), 2)))


    def valor_prestacao(self):
        """Calcula o valor das prestações do financiamento.

        :return: valor de cada prestação
        """
        if self.e:
            pmt = self.y * (self.CF / (1 + self.t))
        else:
            pmt = self.y * self.CF
        return pmt

    def valor_presente(self):
        """Calcula o preço atualizado no instante da compra.

        :return: valor presente
        """
        k = self.fator_k()
        return self.x * k

    def fator_k(self):
        """Calcula o fator que produz o preço atualizado no instante da compra.

        :return: fator k
        """
        if self.e:
            return (1 + self.t) / (self.CF * self.p)
        return 1 / (self.CF * self.p)

    def valor_financiado(self):
        """Calcula o valor financiado, o que depende se houve entrada ou não.

        :return: valor financiado
        """
        if self.e:
            return self.y - self.valor_prestacao()
        return self.y

    def numero_parcelas(self):
        """Calcula o número de parcelas restantes do financiamento.

        :return: número de parcelas
        """
        if self.e:
            return self.p - 1
        return self.p

    def taxa_real(self):
        """Acha a taxa que produz o preço à vista pelo método de Newton.

        :return: taxa real e número de iterações
        """
        t0 = self.x / self.y
        i = 0
        tf, i = met_numerico.metodo_newton(self.x, self.y, self.p, t0, i, self.e)

        return tf, i

    def recomendacao_pagamento(self):
        """Imprime uma recomendação de pagamento com base na comparação entre a taxa mensal fornecida no momento do
        financiamento e a taxa real aplicada.
        """
        taxaReal, i = self.taxa_real()
        if self.t < taxaReal:
            print("O valor à vista é menor do que o valor total corrigido: pague à vista.")
            print(self.percentual_a_mais())
        elif self.t > taxaReal:
            print("O valor à vista é maior do que o valor total corrigido: pague à prazo.")
        else:
            print("O valor à vista é igual ao valor total corrigido.")

    def percentual_a_mais(self):
        """Retorna o percentual pago a mais no caso do valor total corrigido ser maior que o valor a vista.
        """
        valor = round(((self.valor_presente() - self.y) / self.valor_presente()) * 100, 2)
        if 0 <= valor < 1:
            return "Percentual pago a mais = " + str(valor) + "%: Valor Baixo."
        elif 1 <= valor < 3:
            return "Percentual pago a mais = " + str(valor) + "%: Valor Aceitável."
        elif 3 <= valor < 5:
            return "Percentual pago a mais = " + str(valor) + "%: Está Caro."
        else:
            return "Percentual pago a mais = " + str(valor) + "%: Você Está Sendo Roubado!"


class Tabela_Price:
    """Classe Tabela_Price contém todas as operações necessárias para imprimir a tabela.
    """

    def __init__(self, np, pv, t, pmt):
        """Construtor da classe TabelaPrice para inicializar o objeto.

        :param np: numero de parcelas
        :param pv: valor financiado
        :param t: taxa mensal
        :param pmt: valor de cada parcela
        """
        self.np = np
        self.pv = pv
        self.t = t / 100
        self.pmt = pmt
        self.data = self.criar_tabela()

    def criar_tabela(self):
        """Realiza os cálculos necessários para criar a tabela price

        :return: matriz com os dados da tabela price
        """
        data = []
        saldo_devedor = self.pv
        j_total = 0
        a_total = 0
        for p in range(self.np):
            j = self.t * saldo_devedor
            j_total += j

            amortizacao = self.pmt - j
            a_total += amortizacao

            saldo_devedor -= amortizacao
            data.append([p + 1, round(self.pmt, 2), round(j, 2), round(amortizacao, 2), round(saldo_devedor, 2)])

        data.append(["Total", round((self.pmt * self.np), 2), round(j_total, 2), round(a_total, 2), round(saldo_devedor, 2)])
        return data

    def imprimir_tabela(self):
        """Imprime a tabela price utilizando uma matriz de dados.
        """
        print(tabulate(self.data, headers=["Mês", "Prestação", "Juros", "Amortização", "Saldo Devedor"],
                       tablefmt="pretty", numalign="center"))
