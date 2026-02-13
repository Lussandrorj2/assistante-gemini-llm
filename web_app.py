import streamlit as st
from llm import ask_llm
from prompts import SYSTEM_PROMPT

st.set_page_config(page_title="Assistente Inteligente", page_icon="🤖")

st.title("🤖 Assistente com Gemini")
st.markdown("Projeto 2 - LLM externo gratuito")

# Inicializa histórico na sessão
if "messages" not in st.session_state:
    st.session_state.messages = [SYSTEM_PROMPT]

# Exibe histórico na tela
for msg in st.session_state.messages[1:]:  # ignora system prompt
    if msg["role"] == "user":
        st.chat_message("user").write(msg["content"])
    else:
        st.chat_message("assistant").write(msg["content"])

# Campo de entrada
if prompt := st.chat_input("Digite sua pergunta..."):

    # Mostra mensagem do usuário
    st.chat_message("user").write(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.spinner("Pensando..."):
        resposta = ask_llm(st.session_state.messages)

    st.chat_message("assistant").write(resposta)
    st.session_state.messages.append({"role": "assistant", "content": resposta})

# Botão limpar conversa
if st.button("🔄 Limpar conversa"):
    st.session_state.messages = [SYSTEM_PROMPT]
    st.rerun()
