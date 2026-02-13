from llm import ask_llm
from prompts import SYSTEM_PROMPT

MAX_HISTORY = 6 # Aé 6 interações

messages = [SYSTEM_PROMPT]

print("🤖 Assistente iniciado (digite 'sair')")

while True:
    user_input = input("Você: ")
    if user_input.lower() == "sair":
        break

    messages.append({"role": "user", "content": user_input})

    #Limita histórico
    if len(messages) > MAX_HISTORY:
        messages = [SYSTEM_PROMPT] + messages[-MAX_HISTORY:]

    print("Pensando...")    
    resposta = ask_llm(messages)
    
    messages.append({"role": "assistant", "content": resposta})

    print("\n🤖 Resposta:")
    print(resposta)
