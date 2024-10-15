from huggingface_hub import InferenceClient

# Coloca aquí tu clave API
client = InferenceClient(api_key="YOUR_API_KEY")

def generar_cuento(genero, personajes, tono, final):
    # Crear el mensaje (prompt) que se enviará al modelo
    prompt = (f"Escribe un cuento de {genero} con los personajes {personajes}. "
              f"El tono debe ser {tono} y el cuento debe tener un final {final}.")
    
    # Variable para acumular las partes del cuento generado
    cuento_completo = ""

    # Llamada al modelo Phi-3.5-mini-instruct con streaming activado
    for message in client.chat_completion(
        model="microsoft/Phi-3.5-mini-instruct",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1000,
        stream=True,
    ):
        # Acumular las partes del cuento en la variable 'cuento_completo'
        cuento_completo += message.choices[0].delta.content
    
    # Retornar el cuento completo una vez finalizado el bucle
    return cuento_completo
    
def iniciar_chatbot():
    print("¡Hola! Soy un chatbot que genera cuentos. ¿Qué tipo de cuento te gustaría?")
    genero = input("Elige un género (aventura, fantasía, terror, ciencia ficción): ")
    personajes = input("Dime los nombres y características de los personajes principales: ")
    tono = input("¿Qué tono prefieres para el cuento? (divertido, serio, misterioso): ")
    final = input("¿Cómo te gustaría que termine el cuento? (feliz, triste, sorprendente): ")
    
    print("\nGenerando tu cuento...\n")
    cuento = generar_cuento(genero, personajes, tono, final)
    print(cuento)
    return cuento

def guardar_cuento(cuento):
    with open("cuento_generado.txt", "w") as file:
        file.write(cuento)
    print("Tu cuento ha sido guardado.")

# Lógica para continuar generando cuentos o guardarlos
def continuar_chat(cuento):
    while True:
        respuesta = input("¿Te gustaría generar otro cuento o guardar este? (generar/guardar/salir): ").lower()
        if respuesta == "generar":
            cuento = iniciar_chatbot()
        elif respuesta == "guardar":
            guardar_cuento(cuento)
            break
        elif respuesta == "salir":
            print("¡Gracias por usar el chatbot generador de cuentos!")
            break
        else:
            print("Por favor elige una opción válida.")



def Genera_cuentos():
    cuento = iniciar_chatbot()
    continuar_chat(cuento)