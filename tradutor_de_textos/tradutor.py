import openai
import os
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_base = os.getenv("OPENAI_API_BASE")

def arquivo():
    with open("tradutor_de_textos/input/texto.txt", "r") as file:
        texto = file.read()
        return texto

def traduzir(texto, idioma):
    reponse = openai.Completion.create(
        model = "text-davinci-003",
        prompt = f"Traduza o texto para o idioma {idioma}:\nTexto: {texto}\nIdioma: {idioma}\nTradução:",
        temperature = 0.6,
        max_tokens = 2048,
        top_p = 1,
        stop = None
    )
    return print(reponse.choices[0].text)

idioma = input("Digite o idioma para traduzir: ")

# Salvar o texto traduzido em um arquivo txt
def salvar_traducao(traducao):
    with open("tradutor_de_textos/output/texto_traduzido.txt", "w") as file:
        file.write(traducao)
        return print("Tradução salva com sucesso!")

salvar_traducao(traduzir(arquivo(), idioma))