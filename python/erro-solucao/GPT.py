import openai 
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_ENV")

def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r', encoding ='utf-8') as arquivo:
        return arquivo.read()

codigo = ler_arquivo("main.py")
erro = ler_arquivo("Error.log")

def solucao():
    while True:
        resposta = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f'Possível solução do codigo (Descrever o motivo e apresentar a solução) {codigo}: {erro}',
            max_tokens=2048,
            temperature=0.3,
            top_p=1,
            stop=None
        )

        print(resposta.choices[0].text)

        accept = input("Aceita a solução? (s/n): ")
        if accept == "s":
            break