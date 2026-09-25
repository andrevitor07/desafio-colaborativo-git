def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        return "Erro: não é possível dividir por zero."
    return a / b


def main():
    print("=== CALCULADORA ===")

    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))

    print("\nEscolha uma operação:")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")

    opcao = input("Digite a opção: ")

    if opcao == "1":
        resultado = somar(numero1, numero2)
    elif opcao == "2":
        resultado = subtrair(numero1, numero2)
    elif opcao == "3":
        resultado = multiplicar(numero1, numero2)
    elif opcao == "4":
        resultado = dividir(numero1, numero2)
    else:
        resultado = "Opção inválida."

    print(f"\nResultado: {resultado}")


if __name__ == "__main__":
    main()

