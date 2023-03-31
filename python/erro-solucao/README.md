Armazena o erro no arquivo Error.log;

O GPT verifica o erro e apresenta uma possível solução.

Exemplo:

Digite um valor: 10
--------------------
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
Aceita a solução? (s/n):