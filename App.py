import streamlit as st
import streamlit.components.v1 as components

# Charger ton fichier HTML
with open("index.html", "r", encoding="utf-8") as f:
    html_code = f.read()

# Affichage dans Streamlit
st.set_page_config(page_title="Sen3timate", layout="wide")
st.title("Bienvenue sur Sen3timate 🧵")
components.html(html_code, height=800, scrolling=True)
