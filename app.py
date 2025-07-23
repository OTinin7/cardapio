import streamlit as st
import urllib.parse

st.markdown(
    """
    <style>
    /* Fundo rosa claro */
    [data-testid="stAppViewContainer"] {
        background-color: #ffe4e1 !important;
    }

    .block-container {
        background-color: transparent !important;
        padding: 2rem;
    }

    /* Cor cinza nos títulos */
    h1, h2, h3, h4, h5, h6 {
        color: #808080 !important;
    }

    /* Cor cinza nos textos normais */
    .stMarkdown, .stTextInput, .stSelectbox, label, span, p, div {
        color: #808080 !important;
    }

    /* Fundo amarelo para o selectbox */
    div[data-baseweb="select"] > div {
        background-color: #fff176 !important;
        color: #808080 !important;
    }

    /* Fundo amarelo para o campo de nome */
    input[type="text"] {
        background-color: #fff176 !important;
        color: #333 !important;
    }

    /* Fundo amarelo para o botão */
    .stButton > button {
        background-color: #fff176 !important;
        color: #333 !important;
        font-weight: bold;
    }

    /* Legendas das imagens com fonte maior e cor personalizada */
    .stImage > figure > figcaption {
        font-size: 30px !important;
        font-weight: bold;
        color: #808080 !important;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.set_page_config(page_title="Pedido de Bolo", layout="centered")
st.title("Pedido de Bolo via WhatsApp")

# Seu nome
nome = st.text_input("Seu nome")

# Dicionário de bolos com imagens
escolha = {
    "Não tenho interesse": None,
    "Bolo de Pote-R$7,00": "bolodepote.jpeg",
    "Brigadeiros- RS 0,80/unid(15g) || RS 1,30/unid(25g)": "brigadeiros.jpeg",
    "Fatia Gourmet - R$ 7,50": "fatias.jpeg",
    "Torta (1,5KG-RS60,00)(2,5KG-RS95,00)": "torta.jpeg",
    "Torta Vitrine (2,0KG-R$120,00)": "bolovit.jpeg",
    "Kit festa (A partir de R$140,00)": "kitfesta.jpeg",
    "Bolo Decorado (65RS/kg -sem topo)": "bolodecorado.jpeg"
}

st.subheader("Escolha o que você tem interesse:")
bolo = st.selectbox("Opção", list(escolha.keys()))

for nome_bolo, imagem_bolo in escolha.items():
    if imagem_bolo:
        st.image(imagem_bolo, width=300, caption=nome_bolo)





if st.button("🍰 Gerar pedido no WhatsApp"):
    if not nome.strip():
        st.error("Por favor, preencha seu nome.")
    else:
        mensagem = f"Olá! Me interessei em fazer o pedido de: {bolo}. Meu nome é {nome}."
        mensagem_codificada = urllib.parse.quote(mensagem)
        numero = "5581985043578" 
        link = f"https://wa.me/{numero}?text={mensagem_codificada}"

        st.success("Pronto! Clique abaixo para enviar o pedido:")
        st.markdown(f"[Enviar pedido no WhatsApp]({link})", unsafe_allow_html=True)