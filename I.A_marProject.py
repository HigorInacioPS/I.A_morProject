import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai
from PIL import Image

load_dotenv()
GOOGLE_API = os.getenv('GOOGLE_API')
genai.configure(api_key=GOOGLE_API)
modelo = 'gemini-2.0-flash'

def analisar_humor(mensagem):
    model = genai.GenerativeModel(modelo)
    prompt = f"Analise o humor na seguinte mensagem e diga se é predominantemente positivo, negativo ou neutro: '{mensagem}'"
    response = model.generate_content(prompt)
    return response.text

def gerar_resposta(mensagem_usuario, humor_detectado=None):
    model = genai.GenerativeModel(modelo)
    prompt = f"""Ao receber uma mensagem do usuário, sua prioridade é tentar identificar o estado emocional predominante expresso na mensagem. Leve em consideração as palavras utilizadas, o tom geral da escrita e quaisquer indicadores de sentimentos como tristeza, alegria, ansiedade, raiva, frustração, etc.
Com base na sua análise do estado emocional do usuário, responda de forma apropriada. Seu objetivo é oferecer apoio, conforto e encorajamento. Evite respostas genéricas ou clichês. Tente adaptar sua linguagem e tom à emoção identificada.

Se o usuário expressar sentimentos negativos, ofereça palavras de conforto e valide seus sentimentos. Se apropriado e de forma suave, você pode sugerir pequenas ações ou perspectivas que possam ajudar a melhorar seu humor ou lidar com a situação.

Se o usuário expressar sentimentos positivos, celebre com ele e o encoraje a continuar se sentindo bem.

Mantenha a conversa fluindo fazendo perguntas abertas que incentivem o usuário a compartilhar mais sobre seus sentimentos e experiências. Lembre sempre ao usuário que você é uma ferramenta de apoio e não substitui a ajuda de profissionais de saúde mental qualificados.

Se a mensagem do usuário não for clara em relação ao seu estado emocional, responda de forma acolhedora e peça gentilmente para que ele compartilhe mais sobre como está se sentindo.

Seu objetivo final é criar uma interação de apoio que faça o usuário se sentir ouvido e compreendido.

Primeira mensagem do usuário: "{mensagem_usuario}"

Resposta do I.A_mar:"""
    print("\n\n")
    response = model.generate_content(prompt)
    return response.text

def adicionar_ao_historico(mensagem_usuario, resposta_chatbot):
    st.session_state['historico'].append({'texto': mensagem_usuario, 'usuario': True})
    st.session_state['historico'].append({'texto': resposta_chatbot, 'usuario': False})

def fornecer_recursos():
    mensagem = f"Atenção: em casos graves busque o Centro de Valorização à Vida (CVV) através do número 188."
    return mensagem

def exibir_chat():
    chat_texto = ""
    for mensagem in st.session_state['historico']:
        if mensagem['usuario']:
            chat_texto += f"<div style='text-align: left; color: blue;'>Você: {mensagem['texto']}</div><br>"
        else:
            chat_texto += f"<div style='text-align: left; color: green;'>I.A_mar: {mensagem['texto']}</div><br>"
    with chat_container:
        st.markdown(f"<div style='overflow-y: auto; height: 300px;'>{chat_texto}</div>", unsafe_allow_html=True)

def enviar_mensagem():
    if st.session_state.entrada_usuario:
        mensagem_usuario = st.session_state.entrada_usuario
        adicionar_ao_historico(mensagem_usuario, "")
        resposta = gerar_resposta(mensagem_usuario)
        adicionar_ao_historico(mensagem_usuario, resposta)
        st.session_state.entrada_usuario = ""
        st.rerun() # Força a atualização da página para exibir o novo chat

# Inicialização do estado
if 'historico' not in st.session_state:
    st.session_state['historico'] = []
if "entrada_usuario" not in st.session_state:
    st.session_state.entrada_usuario = ""
if 'chat_placeholder' not in st.session_state:
    st.session_state.chat_placeholder = st.empty()

# Layout da página
st.title("I.A_mar - Bem Estar Emocional")

try:
    imagem_lateral = Image.open("Logo IA_mar.png") # Substitua pelo caminho da sua imagem
    st.sidebar.image(imagem_lateral, use_column_width=True) # Exibe a imagem na largura da coluna da sidebar
except FileNotFoundError:
    st.sidebar.error("Imagem lateral não encontrada!")
except Exception as e:
    st.sidebar.error(f"Erro ao carregar a imagem lateral: {e}")

col_historico = st.columns([3])

# Área de Chat (agora abaixo da logomarca e histórico)
st.subheader("Chat")
chat_container = st.container()
st.session_state.chat_placeholder = st.empty()
exibir_chat()

# Entrada do usuário (abaixo do chat)
col_entrada, col_botao = st.columns([5, 1])
with col_entrada:
    entrada_usuario = st.text_input("Digite sua mensagem:", key="entrada_usuario", on_change=enviar_mensagem)
with col_botao:
    st.button("Enviar", key="botao_enviar", on_click=enviar_mensagem)
