import openai
import os
from dotenv import load_dotenv
load_dotenv()

# Resumos de texto usando a API do OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_base = os.getenv("OPENAI_API_BASE")

def texto():
    with open("gerador_de_resumos/input/texto.txt", "r") as file:
        texto = file.read()
        return texto

def resumir(texto):
    response = openai.Completion.create(
        model = "gpt-3.5-turbo",
        prompt = f"Resuma o texto abaixo:\nTexto: {texto}\nResumo:",
        temperature = 0.7,
        max_tokens = 2048,
        top_p = 1,
        frequency_penalty = 0,
        presence_penalty = 0,
        stop = None
    )
    return response.choices[0].text

# Salva o resumo em um arquivo txt
def salvar_resumo(resumo):
    with open("gerador_de_resumos/output/resumo.txt", "w") as file:
        file.write(resumo)
        return print("Resumo salvo com sucesso!")
    
salvar_resumo(resumir(texto()))