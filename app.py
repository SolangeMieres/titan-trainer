import streamlit as st
import random
import time

# --- CONFIGURACIÓN DE PÁGINA (ESTÉTICA DARK/MONSTER) ---
st.set_page_config(page_title="TITAN PLANNER", page_icon="🦍", layout="centered")

# CSS para forzar el look "Muscle Monster" (Fondo negro, texto blanco/rojo)
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
    }
    .metric-card {
        background-color: #262730;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #ff4b4b;
    }
    </style>
    """, unsafe_allow_html=True)

# --- BASE DE DATOS DE EJERCICIOS (Calistenia/Monster style) ---
exercises_db = {
    "Pecho y Tríceps": [
        {"name": "Flexiones Diamante", "reps": "12-15", "xp": 50},
        {"name": "Fondos (Dips)", "reps": "10-12", "xp": 60},
        {"name": "Flexiones Explosivas", "reps": "8-10", "xp": 70},
        {"name": "Flexiones Archer", "reps": "8 por lado", "xp": 80},
    ],
    "Espalda y Bíceps": [
        {"name": "Dominadas (Pull-ups)", "reps": "6-10", "xp": 100},
        {"name": "Chin-ups", "reps": "8-12", "xp": 90},
        {"name": "Remo Invertido (Mesa/Barra)", "reps": "12-15", "xp": 50},
        {"name": "Superman Hold", "reps": "45 seg", "xp": 40},
    ],
    "Piernas de Acero": [
        {"name": "Sentadilla Búlgara", "reps": "10 por pierna", "xp": 90},
        {"name": "Pistol Squat (asistida)", "reps": "5 por pierna", "xp": 120},
        {"name": "Zancadas con Salto", "reps": "20 totales", "xp": 70},
        {"name": "Puente de Glúteo a 1 pierna", "reps": "15 por lado", "xp": 60},
    ],
    "Core & Cardio": [
        {"name": "Burpees", "reps": "15", "xp": 80},
        {"name": "Mountain Climbers", "reps": "40 seg", "xp": 50},
        {"name": "Plancha Comando", "reps": "12", "xp": 60},
        {"name": "Leg Raises (Elevación piernas)", "reps": "15", "xp": 50},
    ]
}

# --- INTERFAZ PRINCIPAL ---
st.title("🦍 TITAN TRAINER")
st.markdown("<h3 style='text-align: center; color: gray;'>DESATA TU POTENCIAL</h3>", unsafe_allow_html=True)

st.divider()

# Sección de entrada (Input del usuario)
col1, col2 = st.columns(2)
with col1:
    focus = st.selectbox("OBJETIVO DE HOY", list(exercises_db.keys()))
with col2:
    intensity = st.select_slider("NIVEL DE ENERGÍA", options=["Baja", "Media", "MODO BESTIA"], value="Media")

# Factor de multiplicación según intensidad
multiplier = 1
if intensity == "Baja": multiplier = 0.8
if intensity == "MODO BESTIA": multiplier = 1.5

# Botón generador de "IA"
if st.button("GENERAR RUTINA MONSTER ⚡"):
    with st.spinner('Analizando biometría... Generando plan de ataque...'):
        time.sleep(1.5) # Efecto dramático de "cargando"
    
    st.success(f"PLAN ACTIVO: {focus.upper()}")
    
    # Seleccionar 3 ejercicios aleatorios del grupo muscular
    daily_routine = random.sample(exercises_db[focus], 3)
    
    total_xp = 0
    
    for i, ex in enumerate(daily_routine):
        st.markdown(f"""
        <div class="metric-card">
            <h4>🔥 Ejercicio {i+1}: {ex['name']}</h4>
            <p style="font-size: 18px;"><b>Objetivo:</b> {ex['reps']}</p>
        </div>
        <br>
        """, unsafe_allow_html=True)
        total_xp += ex['xp']
    
    # Gamificación final
    final_xp = int(total_xp * multiplier)
    st.markdown("---")
    st.metric(label="XP POTENCIAL DE ESTA SESIÓN", value=f"+{final_xp} XP", delta="Rango: Bestia")
    st.info("💡 Tip: Descansa 90 segundos entre series. Repite el circuito 3 o 4 veces.")

else:
    st.markdown("""
    <div style="text-align: center; margin-top: 50px; opacity: 0.6;">
        Seleccioná tu objetivo y presioná el botón para recibir órdenes.
    </div>
    """, unsafe_allow_html=True)