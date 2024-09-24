def main():
    n = int(input("Ingrese un número entero positivo para los términos de Fibonacci: "))  #Aqui declaro la variable yyy lo que va a contener la variable

    if n <= 0:
        print("Por favor, ingrese un número entero positivo.")  # Si el número es menor o igual a 0, se muestra "error"
        return  # Termina si 'n' no es válido

    fibonacci = [0, 1]  # Inicializamos la lista con los primeros números de la secuencia de Fibonacci (0 y 1)

    for i in range(2, n):  # Bucle que genera los números de Fibonacci desde el tercer término hasta el término 'n'
        siguiente = fibonacci[i - 1] + fibonacci[i - 2]  # -1 es el ultimo y el -2 es el antes, y pues, se suman para sacar el siguiente número, por eso dice -1 y -2, no porque se resten si no que solo indican el espacio
        fibonacci.append(siguiente)  # Añadir el nuevo número a la lista fibonacci

    if n == 1:
        fibonacci = fibonacci[:1]  # Si 'n' es 1, ajustamos la lista para que solo tenga el primer término 

    print(fibonacci)  #Imprimimos la lista de números de Fibonacci

main()  
