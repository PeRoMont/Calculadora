from time import sleep #BIBLIOTECA PARA ADICIONAR UM TEMPORIZADOR

print('=' * 43)
print('\tCALCULADORA')
print('=' * 43)

while True: #LAÇO PARA QUE O USUÁRIO POSSA FAZER AS CONTAS MAIS DE UMA VEZ SEM QUE PRECISE RODAR O PROGRAMA NOVAMENTE
    num1 = int(input('Olá, primeiro insira o 1° valor: ')) #PEDIR O PRIMEIRO VALOR
    num2 = int(input('Agora insira o 2° valor: ')) #PEDIR O SESGUNDO VALOR

    option = int(input(f'O que você quer fazer com os números {num1} e {num2}?\n[1] - SOMAR\n[2] - SUBTRAIR\n[3] - MULTIPLICAR\n[4] - DIVIDIR\nInsira a opção desejada: ')) #INSERIR A OPÇÃO DESEJADA 

    def soma(num1, num2): #FUNÇÃO DE SOMAR
        return num1 + num2
    def subtração(num1, num2): #FUNÇÃO DE SUBTRAIR
        return num1 - num2
    def multiplicar(num1, num2): #FUNÇÃO DE MULTIPLICAR
        return num1 * num2
    def dividir(num1, num2): #FUNÇÃO DE DIVIDIR
        return num1 / num2

    if option == 1: #SOMA
        print(f'A soma entre {num1} e {num2} é: {soma(num1, num2)}')

    elif option == 2: #DIVISÃO
        print(f'A subtração entre {num1} e {num2} é: {subtração(num1, num2)}')

    elif option == 3: #MULTIPLICAÇÃO
        print(f'A multiplicação de {num1} e {num2} é: {multiplicar(num1, num2)}')

    else: #DIVISÃO
        print(f'A divisão entre {num1} e {num2} é: {dividir(num1, num2)}')
    
    sleep(1.5) #TEMPORIZADOR
    continuar = str(input('Você quer fazer com outros números?\n[SIM ou NÃO]:')).upper().strip()[0] #ESCOLHA SE AINDA VAI QUERER CONTINUAR O PROGRAMA OU NÃO

    if continuar == 'N': #STOP NO PROGRAMA
        break

print('\tATÉ LOGO😄!')