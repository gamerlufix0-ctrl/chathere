def responder(pregunta):
    pregunta = pregunta.lower()  # todo en minúscula para comparar mejor

    if "hola" in pregunta:
        return "Hola 😏, ¿qué tal estás?"
    
    elif "cómo estás" in pregunta or "como estas" in pregunta:
        return "Funcionando al 100% ⚡"

    elif "adios" in pregunta or "bye" in pregunta:
        return "Nos vemos 😼"

    else:
        return "No entiendo eso todavía…"

# TEST rápido (opcional)
if __name__ == "__main__":
    while True:
        user = input("Tú: ")
        print("Bot:", responder(user))
