import openai
import subprocess
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_ENV")

def gerar_comando_shell(texto):
    resposta = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f'Gerar comando shell: {texto}',
        max_tokens=2048,
        temperature=0.3,
        top_p=1,
        stop=None
    )
    return resposta.choices[0].text

def executar_comando_shell(comando):
    try:
        resposta = subprocess.run(comando, shell=True, capture_output=True)
        return resposta
    except subprocess.CalledProcessError as error:
        return error
    
descricao_comando = input("Digite o comando shell: ")
comando = gerar_comando_shell(descricao_comando)
print(comando)

aceitar = input("Executar o comando? (s/n): ")

if aceitar == "s":
    executar_comando_shell(comando)

