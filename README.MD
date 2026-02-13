# 🤖 Assistente Inteligente com Gemini

Assistente conversacional estilo ChatGPT desenvolvido em Python, utilizando a API do Google Gemini e interface web com Streamlit.

Este projeto demonstra integração real com um LLM externo, controle de histórico de conversa, arquitetura modular e boas práticas de desenvolvimento.

---

## 🎯 Objetivo

Construir um assistente inteligente utilizando um modelo de linguagem externo (LLM), com foco em:

- Integração com API real de IA
- Controle de contexto e histórico
- Arquitetura organizada e modular
- Interface web interativa
- Boas práticas de versionamento

O objetivo é ir além do simples consumo de API, aplicando conceitos de engenharia de software no desenvolvimento de aplicações com LLMs.

---

## 🛠️ Tecnologias Utilizadas

- Python 3.11+
- Google Gemini API (`google-genai`)
- Streamlit
- python-dotenv
- Git

---

## 🏗️ Arquitetura

Fluxo da aplicação:

Usuário  
↓  
Interface Web (Streamlit)  
↓  
Gerenciamento de Histórico  
↓  
Função `ask_llm()`  
↓  
Google Gemini API  
↓  
Resposta exibida na interface  

Estrutura do projeto:

