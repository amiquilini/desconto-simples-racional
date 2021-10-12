## CEDERJ - PIG/AD1_2021_2 - *Desconto Simples Racional por Dentro*
Aplicação em console para calcular desconto simples racional por dentro e imprimir a tabela PRICE de um financiamento.

### Descrição:
- o valor de uma mercadoria/empréstimo a prazo é x reais e à vista é y reais;
- o valor é pago em p prestações mensais com ou sem entrada;
- o mercado adota uma remuneração bancária fixa de t% ao mês (taxa);
- o valor presente do financiamento determina se vale a pena ou não pagar a prazo;
- o percentual pago a mais é classificado da seguinte forma: baixo, aceitável, caro, roubo;
- caso a taxa de juros empregada não seja conhecida, a taxa SELIC é utilizada;
- caso a taxa de juros empregada seja anunciada como 0, a taxa real é calculada pelo método de Newton.

### Dependências
```python
pip install -r requirements.txt
```

### Argumentos
```python
-h (--help) help
-p (--parcelas) número de parcelas.
-t (--taxa) taxa mensal (Taxa SELIC por padrão).
-x (--valorP) valor da compra à prazo.
-y (--valorV) valor da compra à vista.
-e (--entrada) indica se houve entrada (False por padrão).
```

### Uso
```python
- AD1_2021_2.py -p 10 -t 1 -x 500 -y 450 -e True
- AD1_2021_2.py -p 18 -t 0 -x 3297.60 -y 1999
- AD1_2021_2.py -p 10 -x 1190 - y 1094.80 -e True
- AD1_2021_2.py -p 8 -t 4.55 -x 111064.80 -y 23000
- AD1_2021_2.py -p 9 -t 0 -x 134788.8 -y 63816.24
- AD1_2021_2.py -p 4 -t 3.0 -x 1080.11 -y 1000
- AD1_2021_2.py --parcelas 14 --taxa 4.55 --valorP 14000.50 --valorV 23000 --entrada True
- AD1_2021_2.py --help
```

###### Para mais informações, conferir a documentação (AD1_2021_2_Doxygen.pdf)