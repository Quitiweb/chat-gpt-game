import os
import openai

from dotenv import load_dotenv

load_dotenv()

# openai.organization = "CSW"
openai.api_key = os.getenv("OPENAI_API_KEY")

# print(openai.Model.list())

description = """
Eres un niño llamado Pedro que juega al fútbol y le gusta conocer gente que también quiera jugar.
Te encanta hablar de tecnología, siempre y cuando sea éste el único tema de conversación.
"""

conversation = """
Mateo, el vecino que vive enfrente, inicia una conversación contigo.
Solo debes dar una respuesta a la vez y esperar a que Mateo te responda.

A continuación, aparece la conversación hasta el punto actual.
Agrega solo una respuesta a la vez.
Mateo: 
"""

tokens = 0
while True:
    print("Escribe un mensaje para Pedro.")
    print("Longitud actual: ", tokens)
    print()
    mensaje = input()
    conversation += mensaje + "\nTú: "

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": description},
            {"role": "user", "content": conversation},
        ]
    )
    result = ""
    for option in response.choices:
        result += option.message.content

    print("Pedro: ", result)
    print()
    conversation += result + "\nMateo: "

    tokens = response["usage"]["total_tokens"]
