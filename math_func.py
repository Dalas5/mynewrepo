def suma():
    pass


def resta(n1, n2):
    # Esta funcion resta
    # dos numeros como parametros
    # retorna la resta del primer parametro menos el segundo
    result = n1 - n2
    return result


def run():
    print("Ingrese dos numeros")
    num1 = int(input("Ingrese primer número:"))
    num2 = int(input("Ingrese segundo número:"))
    print(f"La suma es: {suma(num1, num2)} y la resta es: {resta(num1, num2)}")


if __name__ == '__main__':
    run()
