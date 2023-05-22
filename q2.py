# Nome: Thiago Levi Ramos da Costa
# RU: 4335565
print('Bem vindo a lanchonete do Thiago Levi')
print('-----------------------CARDÁPIO ----------------------')
print('| Código | |          Descrição          |  |  Valor |')
print('|  100   | |       Cachorro Quente       |  |  9,00  |')
print('|  101   | |     Cachorro Quente Duplo   |  |  11,00 |')
print('|  102   | |           X-Egg             |  |  12,00 |')
print('|  103   | |         X-Salada            |  |  12,00 |')
print('|  104   | |         X-Bacon             |  |  14,00 |')
print('|  105   | |         X-Tudo              |  |  17,00 |')
print('|  200   | |    Refrigerante de Lata     |  |  5,00  |')
print('|  201   | |        Chá Gelado           |  |  4,00  |')


# Deve-se utilizar estruturas if, elif e else (EXIGÊNCIA 1 de 3);

valorDaConta = 0

# Deve-se utilizar while, break, continue (EXIGÊNCIA 3 de 3);

while True:
    codigo = input("Entre com o código desejado: ")

    # Se a pessoa digitar um NÚMERO diferente dos da tabela printar na tela: ‘opção inválida’ e voltar para o menu (EXIGÊNCIA 2 de 3);
    if codigo != "100" and codigo != "101" and codigo != "102" and codigo != "103" and codigo != "104" and "105" and codigo != "200" and codigo != "201":
        print('Opção inválida! Digite somente um código válido.')
        continue

    if codigo == "100":
        print('Você pediu Cachorro Quente')
        valorDaConta += 9
        print('Valor da conta {:.2f}' .format(valorDaConta))
    elif codigo == "101":
        print('Você pediu Cachorro Quente Duplo')
        valorDaConta += 11
        print('Valor da conta {:.2f}'.format(valorDaConta))
    elif codigo == "102":
        print('Você pediu X-Egg')
        valorDaConta += 12
        print('Valor da conta {:.2f}'.format(valorDaConta))
    elif codigo == "103":
        print('Você pediu X-Salada')
        valorDaConta += 12
        print('Valor da conta {:.2f}'.format(valorDaConta))
    elif codigo == "104":
        print('Você pediu X-Bacon')
        valorDaConta += 14

        print('Valor da conta {:.2f}'.format(valorDaConta))
    elif codigo == "105":
        print('Você pediu X-Tudo')
        valorDaConta += 17

        print('Valor da conta {:.2f}'.format(valorDaConta))
    elif codigo == "200":
        print('Você pediu Refrigerante de Lata')
        valorDaConta += 5

        print('Valor da conta {:.2f}'.format(valorDaConta))
    elif codigo == "201":
        print('Você pediu Chá Gelado')
        valorDaConta += 4

        print('Valor da conta {:.2f}'.format(valorDaConta))

    sairOuContinuar = input("Deseja pedir mais alguma coisa? \n S - Sim \n Qualquer outra tecla - Sair \n")
    sairOuContinuar = sairOuContinuar.upper()

# Deve-se utilizar while, break, continue (EXIGÊNCIA 3 de 3);
    if sairOuContinuar == "S":
        continue
    else:
        print('Valor total da conta --> R$ {:.2f} ' .format(valorDaConta))
        break
