def suma():
print("Ingrese dos numeros")
num1 = input("Ingrese primer número:")
num2 = input("Ingrese segundo número:")
numero_suma = num1 + num2
print(f"La suma es: {suma(num1, num2)} y la resta es: {resta(num1, num2)})


def resta():
    pass

def run():
    print("Ingrese dos numeros")
    num1 = input("Ingrese primer número:")
    num2 = input("Ingrese segundo número:")
    print(f"La suma es: {suma(num1, num2)} y la resta es: {resta(num1, num2)})    
    


if __name__ == '__main__':
    run()
