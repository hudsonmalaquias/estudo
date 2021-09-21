def conta():
    print("Selecione o número da operação desejada:")
    print('\n')
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print('\n')
    operac = input("Digite sua opção (1/2/3/4): ")
    print('\n')
    op = ''
    
    
    if not operac.isdigit():
        print("Opção Inválida!")
        print('\n')
        conta()
    else:
        op = int(operac)
    
    if op > 4 or op == 0:
        print("Opção Inválida!")
        print('\n')
        conta()
           
    
    n1 = input("Digite o primeiro número: ")
    print('\n')
    n2 = input("Digite o segundo número: ")
    print('\n')
    
    num1 = int(n1)
    num2 = int(n2)

    if op == 1:
        result = (num1 + num2)
        print("%i + %i = %i" % (num1,num2,result))
        print('\n')
        conta()
        
    if op == 2:
        result = (num1 - num2)
        print("%i - %i = %i" % (num1,num2,result))
        print('\n')
        conta()
        
    if op == 3:
        result = (num1 * num2)
        print("%i x %i = %i" % (num1,num2,result))
        print('\n')
        conta()
        
    if op == 4:
        result = (num1 / num2)
        print("%i / %i = %i" % (num1,num2,result))
        print('\n')
        conta()
    
conta()