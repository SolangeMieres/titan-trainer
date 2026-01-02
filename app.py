import streamlit as st
import random
import time

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="TITAN PLANNER", page_icon="🦍", layout="centered")

# CSS para ocultar elementos de Streamlit y dar look App Nativa
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #ffffff; }
    h1 { color: #ff3333 !important; text-transform: uppercase; font-style: italic; }
    .stButton>button {
        background-color: #ff3333; color: white; border: none;
        border-radius: 5px; padding: 15px; font-weight: bold; width: 100%;
    }
    .exercise-title {
        font-size: 22px; font-weight: bold; color: #ff3333; margin-top: 20px;
    }
    .exercise-meta { color: #cccccc; font-size: 16px; margin-bottom: 10px; }
    /* Ocultar menú de hamburguesa y footer para que parezca app real */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- DATOS (VIDEOS DE YOUTUBE) ---
exercises_db = {
    "Pecho y Tríceps": [
        {"name": "Flexiones Diamante", "reps": "3 series x 12", "video": "https://youtu.be/J0DnG1_S92I"},
        {"name": "Fondos en Silla", "reps": "3 series x 10", "video": "https://youtu.be/0326dy_-CzM"},
        {"name": "Flexiones Explosivas", "reps": "3 series x 8", "video": "https://youtu.be/tWjBnT3p0Fk"},
    ],
    "Espalda y Bíceps": [
        {"name": "Dominadas / Remo Puerta", "reps": "3 series x Falla", "video": "https://youtu.be/tQPLf327cKY"},
        {"name": "Chin-ups", "reps": "3 series x 8", "video": "https://youtu.be/brhRXlOhsAM"},
        {"name": "Superman", "reps": "3 series x 40s", "video": "https://youtu.be/cc6UVRS7PW4"},
    ],
    "Piernas": [
        {"name": "Sentadilla Búlgara", "reps": "3 series x 10 c/u", "video": "https://youtu.be/2C-uNgKwPLE"},
        {"name": "Zancadas Salto", "reps": "3 series x 20", "video": "https://youtu.be/1-XN95d-wCs"},
        {"name": "Puente Glúteo", "reps": "3 series x 15", "video": "https://youtu.be/ovM3L68Q1K4"},
    ],
    "Cardio & Core": [
        {"name": "Burpees", "reps": "15 repeticiones", "video": "https://youtu.be/auBLPXO8Fww"},
        {"name": "Mountain Climbers", "reps": "45 segundos", "video": "https://youtu.be/zT-9L3CEcmk"},
        {"name": "Plancha", "reps": "Aguntar 1 min", "video": "https://youtu.be/pSHjTRKQxqc"},
    ]
}

st.title("🦍 TITAN PLANNER")
st.write("ENTRENAMIENTO GRATUITO DE ÉLITE")

# Selectores
focus = st.selectbox("OBJETIVO DE HOY", list(exercises_db.keys()))

if st.button("GENERAR RUTINA ⚡"):
    with st.spinner('Cargando sistema...'):
        time.sleep(1)
    
    # Selecciona 3 ejercicios al azar
    rutina = random.sample(exercises_db[focus], 3)
    
    st.success(f"OBJETIVO: {focus.upper()}")
    st.progress(100)
    
    for ex in rutina:
        st.markdown(f'<div class="exercise-title">{ex["name"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="exercise-meta">Objetivo: {ex["reps"]}</div>', unsafe_allow_html=True)
        
        # VIDEO DIRECTO (Sin clicks, aparece grande)
        st.video(ex["video"])
        st.markdown("---")
