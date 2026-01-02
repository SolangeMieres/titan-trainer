import streamlit as st
import random
import time

# --- CONFIGURACIÓN DE PÁGINA (ESTÉTICA DARK/MONSTER) ---
st.set_page_config(page_title="TITAN PLANNER", page_icon="🦍", layout="centered")

st.markdown("""
    <style>
    .stApp {
        background-color: #0e1117;
        color: #fafafa;
    }
    h1 {
        color: #ff4b4b !important;
        text-transform: uppercase;
        font-weight: 800;
        text-align: center;
    }
    .stButton>button {
        background-color: #ff4b4b;
        color: white;
        border-radius: 20px;
        font-weight: bold;
        width: 100%;
        border: none;
        padding: 15px;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        background-color: #ff1c1c;
        transform: scale(1.02);
    }
    .metric-card {
        background-color: #262730;
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #ff4b4b;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- BASE DE DATOS CON VIDEOS ---
# Usamos videos cortos de Youtube para que cargue rápido.
exercises_db = {
    "Pecho y Tríceps": [
        {"name": "Flexiones Diamante", "reps": "12-15", "xp": 50, "video": "https://youtu.be/J0DnG1_S92I"},
        {"name": "Fondos (Dips) en Silla/Banco", "reps": "10-12", "xp": 60, "video": "https://youtu.be/0326dy_-CzM"},
        {"name": "Flexiones Explosivas", "reps": "8-10", "xp": 70, "video": "https://youtu.be/tWjBnT3p0Fk"},
        {"name": "Flexiones Archer (o abiertas)", "reps": "8 por lado", "xp": 80, "video": "https://youtu.be/2NnSSO-d8do"},
    ],
    "Espalda y Bíceps": [
        {"name": "Dominadas (o Remo en puerta)", "reps": "6-10", "xp": 100, "video": "https://youtu.be/tQPLf327cKY"},
        {"name": "Chin-ups (Bíceps)", "reps": "8-12", "xp": 90, "video": "https://youtu.be/brhRXlOhsAM"},
        {"name": "Remo Invertido (Mesa)", "reps": "12-15", "xp": 50, "video": "https://youtu.be/t9nJ9c6O8d4"},
        {"name": "Superman Hold", "reps": "45 seg", "xp": 40, "video": "https://youtu.be/cc6UVRS7PW4"},
    ],
    "Piernas de Acero": [
        {"name": "Sentadilla Búlgara", "reps": "10 por pierna", "xp": 90, "video": "https://youtu.be/2C-uNgKwPLE"},
        {"name": "Pistol Squat (Asistida)", "reps": "5 por pierna", "xp": 120, "video": "https://youtu.be/PZilDfGHhPc"},
        {"name": "Zancadas con Salto", "reps": "20 totales", "xp": 70, "video": "https://youtu.be/1-XN95d-wCs"},
        {"name": "Puente de Glúteo (1 pierna)", "reps": "15 por lado", "xp": 60, "video": "https://youtu.be/ovM3L68Q1K4"},
    ],
    "Core & Cardio": [
        {"name": "Burpees", "reps": "15", "xp": 80, "video": "https://youtu.be/auBLPXO8Fww"},
        {"name": "Mountain Climbers", "reps": "40 seg", "xp": 50, "video": "https://youtu.be/zT-9L3CEcmk"},
        {"name": "Plancha Comando", "reps": "12", "xp": 60, "video": "https://youtu.be/pSHjTRKQxqc"},
        {"name": "Leg Raises", "reps": "15", "xp": 50, "video": "https://youtu.be/JB2oyawG9KI"},
    ]
}

# --- INTERFAZ PRINCIPAL ---
st.title("🦍 TITAN TRAINER")
st.markdown("<h3 style='text-align: center; color: gray;'>DESATA TU POTENCIAL</h3>", unsafe_allow_html=True)
st.divider()

# Input
col1, col2 = st.columns(2)
with col1:
    focus = st.selectbox("OBJETIVO DE HOY", list(exercises_db.keys()))
with col2:
    intensity = st.select_slider("NIVEL DE ENERGÍA", options=["Baja", "Media", "MODO BESTIA"], value="Media")

multiplier = 0.8 if intensity == "Baja" else 1.5 if intensity == "MODO BESTIA" else 1

# Generador
if st.button("GENERAR RUTINA MONSTER ⚡"):
    with st.spinner('Analizando biometría... Generando plan de ataque...'):
        time.sleep(1.5)
    
    st.success(f"PLAN ACTIVO: {focus.upper()}")
    
    daily_routine = random.sample(exercises_db[focus], 3)
    total_xp = 0
    
    for i, ex in enumerate(daily_routine):
        # Tarjeta del ejercicio
        st.markdown(f"""
        <div class="metric-card">
            <h4>🔥 Ejercicio {i+1}: {ex['name']}</h4>
            <p style="font-size: 18px; margin-bottom: 0;"><b>Objetivo:</b> {ex['reps']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # VIDEO DESPLEGABLE (Aquí está la magia visual)
        with st.expander(f"🎥 Ver cómo se hace: {ex['name']}"):
            st.video(ex['video'])
            
        total_xp += ex['xp']
    
    final_xp = int(total_xp * multiplier)
    st.markdown("---")
    st.metric(label="XP POTENCIAL", value=f"+{final_xp} XP", delta="Rango: Bestia")
    st.info("💡 Tip: Descansa 90 segundos entre series. Repite el circuito 3 o 4 veces.")

else:
    st.markdown("""
    <div style="text-align: center; margin-top: 50px; opacity: 0.6;">
        Seleccioná tu objetivo y presioná el botón para recibir órdenes.
    </div>
    """, unsafe_allow_html=True)
