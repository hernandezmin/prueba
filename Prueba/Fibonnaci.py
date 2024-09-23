def main():
    n = int(input("Ingrese un número entero positivo para los términos de Fibonacci: "))

    if n <= 0:
        print("Por favor, ingrese un número entero positivo.")
        return

    fibonacci = [0, 1]  

    for i in range(2, n):
        siguiente = fibonacci[i - 1] + fibonacci[i - 2]
        fibonacci.append(siguiente)

    
    if n == 1:
        fibonacci = fibonacci[:1]

    print(fibonacci)

main()
