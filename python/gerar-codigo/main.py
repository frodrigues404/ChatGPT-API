import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_ENV")

def gerar_codigo(linguagem, texto):
    resposta = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f'Gerar o seguinte codigo em {linguagem}: {texto}',
        max_tokens=2048,
        temperature=0.3,
        top_p=1,
        stop=None
    )
    return resposta.choices[0].text

desc_codigo = input("Digite o codigo a ser feito: ")
linguagem = input("Digite a linguagem: ")
codigo = gerar_codigo(linguagem, desc_codigo)
print(codigo)

