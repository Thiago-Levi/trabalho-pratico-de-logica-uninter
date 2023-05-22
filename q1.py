
# Nome: Thiago Levi Ramos da Costa
# RU: 4335565

print("Bem Vindo a loja do Thiago Levi")

#Entre com o valor unitário do produto (Lembrar que número decimal é feito com ponto e não vírgula);
valorUnitarioDoProduto = float(input('Digite o valor unitário do produto: '))

# Entre com a quantidade desse produto;
quantidadeDeProdutos = int(input('Digite a Quantidade de produtos: '))

#Processamento
# Deve-se utilizar estruturas if, elif e else (EXIGÊNCIA 1 de 1);
#A variável placeholder é apenas para informar o percentual de desconto.

if quantidadeDeProdutos >= 10 and quantidadeDeProdutos <= 99:
    descontoPorUnidade = 0.05
    placeholder = "(desconto 5%)"
elif quantidadeDeProdutos >= 100 and quantidadeDeProdutos <= 999:
    descontoPorUnidade = 0.1
    placeholder = "(desconto 10%)"
elif quantidadeDeProdutos >= 1000:
    descontoPorUnidade = 0.15
    placeholder = "(desconto 15%)"
else:
    descontoPorUnidade = 0.00
    placeholder = ""

# O programa deve retornar o valor total sem desconto;
#calculo do preço final sem desconto
valorTotalSemDesconto = quantidadeDeProdutos * valorUnitarioDoProduto

# O programa deve retornar o valor total após o desconto;
#calculo do preço final com desconto
valorTotalAposDesconto = valorTotalSemDesconto - (descontoPorUnidade * valorTotalSemDesconto)




#saida de dados
#Retornos

if quantidadeDeProdutos <= 9:
    print('Valor total  --> R$ {} '.format(valorTotalSemDesconto))
else:
    print('Valor total sem desconto --> R$ {:.2f} '.format(valorTotalSemDesconto))
    print("Valor Total após o desconto --> {:.2f}  {}".format(valorTotalAposDesconto, placeholder))



