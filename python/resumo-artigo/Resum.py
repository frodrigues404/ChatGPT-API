import openai 
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_ENV")

def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r', encoding ='utf-8') as arquivo:
        return arquivo.read()

def resumo(texto, max_tokens=2048, temperature=0.3, top_p=1):
    resposta = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f'Resuma o seguinte texto: {texto}',
        max_tokens=max_tokens,
        temperature=temperature,
        top_p=top_p,
        stop=None
    )
    return resposta.choices[0].text

arquivo = 'Texto.txt'

texto = ler_arquivo(arquivo)

print(resumo(texto))