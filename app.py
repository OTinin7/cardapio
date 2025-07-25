import streamlit as st
import urllib.parse

st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] {
        background-color: #ffe4e1 !important;
    }

    .block-container {
        background-color: transparent !important;
        padding: 2rem;
    }

    h1, h2, h3, h4, h5, h6 {
        color: #808080 !important;
    }

    .stMarkdown, .stTextInput, .stSelectbox, label, span, p, div {
        color: blue !important;
    }

    div[data-baseweb="select"] > div {
        background-color: #fff176 !important;
        color: #808080 !important;
    }

    input[type="text"] {
        background-color: #fff176 !important;
        color: #333 !important;
    }

    .stButton > button {
        background-color: #fff176 !important;
        color: #333 !important;
        font-weight: bold;
    }

    
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
    "Brigadeiros- R$ 0,80/unid(15g) || R$ 1,30/unid(25g)": "brigadeiros.jpeg",
    "Fatia Gourmet - R$ 7,50": "fatias.jpeg",
    "Torta (1,5KG-R$60,00)(2,5KG-R$95,00)": "torta.jpeg",
    "Torta Vitrine (2,0KG-R$120,00)": "bolovit.jpeg",
    "Kit festa (A partir de R$140,00)": "kitfesta.jpeg",
    "Bolo Decorado (R$65/kg -sem topo)": "bolodecorado.jpeg"
}

st.subheader("Escolha o que você tem interesse:")
bolo = st.selectbox("Opção", list(escolha.keys()))

for nome_bolo, imagem_bolo in escolha.items():
    if imagem_bolo:
        st.image(imagem_bolo, width=300)
        st.markdown(
            f"<p style='text-align: center; font-size: 20px; color: black; font-weight: bold;'>{nome_bolo}</p>",
            unsafe_allow_html=True
        )




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