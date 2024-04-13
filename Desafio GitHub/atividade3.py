def adicionar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    return x / y

print("Selecione a operação desejada.")
print("1. Adicionar")
print("2. Subtrair")
print("3. Multiplicar")
print("4. Dividir")

while True:
    escolha = input("Digite a opção (1/2/3/4): ")

    if escolha in ('1', '2', '3', '4'):
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if escolha == '1':
            print(num1, "+", num2, "=", adicionar(num1, num2))

        elif escolha == '2':
            print(num1, "-", num2, "=", subtrair(num1, num2))

        elif escolha == '3':
            print(num1, "*", num2, "=", multiplicar(num1, num2))

        elif escolha == '4':
            if num2 != 0:
                print(num1, "/", num2, "=", dividir(num1, num2))
            else:
                print("Erro! Divisão por zero não é permitida.")

        novo_calculo = input("Deseja realizar outra operação? (s/n): ")
        if novo_calculo.lower() != 's':
            break
    else:
        print("Opção Inválida!")