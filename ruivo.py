def exercício1():
    idade = int(input("Digite sua idade: "))
    
    if idade <= 11:
        print("Você é criança")
    elif idade > 11 and idade <= 18:
        print("Você é um adolecente")
    elif idade > 18 and idade <= 24:
        print("Você é um Jovem")
    elif idade > 24 and idade <= 40:
        print("Você é um Adulto")
    elif idade > 40 and idade <= 60:
        print("Você é um Meia idade")
    elif idade > 60:
        print("Você é um Idoso")
    
exercício1()

def exercício2():
    primeiro_valor = int(input("Digite um valor: "))
    segundo_valor = int( input("Digite um valor: "))
    print("Primeiro" if primeiro_valor>segundo_valor else "Segundo valor")

exercício2()

def exercício3():
    numeros =[1,3,6,10,5,23]
    numero_digitado = int(input("Digite um número: "))
    if numero_digitado in numeros:
        print(f"O número {numero_digitado} está na lista")
    else:
        print(f"O número {numero_digitado} não está na lista")
    exercício3()
    
def exercício4():
    num = int(input("Digite um valor entre 0 e 9"))
    if num >= 0 and num <= 9:
        print("Valor correto")
    else:
        print("Valor incorreto")
        
    exercício4()

def exercício5()
    turno = str(int("Qual é o seu turno de trabalho? (Manhã/Noturno): "))
    print(f"Turno de trabaldo:{turno}")
    qntd = int(input("Quantas horas duram o turno?: "))
    print(f"Horas trabalhadas: {qntd}")
    
    horas = 45
    
    if turno == "Noturno":
        print(f"Salário: R$ {"{:.2f}" .fort(qntd * horas)}")
    else:
        print(f"Salário: R$ {"{:.2f}" .format(qntd * (horas - 7.5))}")
    exercício5()
    