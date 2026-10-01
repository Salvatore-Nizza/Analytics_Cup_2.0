import streamlit as st
from kloppy import skillcorner

@st.cache_data
def load_match_data(match_id="4039"):
    """Carica i metadati e il tracking di una partita calcistica dal dataset clonato."""
    # Percorsi relativi alla cartella dove hai clonato il repository SkillCorner
    meta_path = f"data/opendata/data/matches/{match_id}/metadata.json"
    tracking_path = f"data/opendata/data/matches/{match_id}/tracking.json"
    
    dataset = skillcorner.load(
        meta_data=meta_path,
        raw_data=tracking_path
    )
    return dataset