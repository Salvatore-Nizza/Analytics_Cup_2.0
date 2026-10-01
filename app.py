import streamlit as st
import matplotlib.pyplot as plt
from mplsoccer import Pitch
from src.data_loader import load_match_data

st.set_page_config(page_title="Analytics Cup 2.0", layout="wide")
st.title("Esplorazione Dati Calcio - SkillCorner")

# Carica il dataset della partita
with st.spinner("Caricamento frame di tracking in corso..."):
    dataset = load_match_data("4039")

st.success(f"Dati caricati correttamente! La partita contiene {len(dataset.frames)} frame di tracking.")

st.subheader("Mappa di Gioco")

# Disegno del campo con mplsoccer ottimizzato per i dati SkillCorner
pitch = Pitch(
    pitch_type='skillcorner', 
    pitch_length=105, 
    pitch_width=68, 
    pitch_color='#22312b', 
    line_color='#c7d5cc'
)
fig, ax = pitch.draw(figsize=(10, 7))

# Mostra il grafico sull'interfaccia web
st.pyplot(fig)