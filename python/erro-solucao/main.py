from GPT import solucao
var1 = input("Digite um valor: ")

def fib(n):
    try:
        a, b = 0, 1
        while a < n:
            print(a, end=' ')
            a, b = b, a + b
        print()
    except TypeError as error:

        with open("Error.log", "w") as file:
            file.write(str(error))

        print("--------------------")
        print(error)
        print("--------------------")
        
        solucao()
  
fib(var1)
