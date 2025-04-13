import streamlit as st
from home import home
from skills import skills
from contact import contact
from crime_sp import crime_sp
from dashboard_kpi import dashboard_kpi
from sentimentos_nlp import sentimentos_nlp

# Configuração geral do site
st.set_page_config(page_title="Thiago Casagrande – Portfólio", page_icon="📊", layout="wide")

# Sidebar
st.sidebar.title("Navegação")
page = st.sidebar.radio("Ir para", [
    "Início",
    "Crime em SP",
    "Dashboard Operacional",
    "Análise de Sentimentos",
    "Skills",
    "Contato"
])

# Rotas
if page == "Início":
    home()
elif page == "Crime em SP":
    crime_sp()
elif page == "Dashboard Operacional":
    dashboard_kpi()
elif page == "Análise de Sentimentos":
    sentimentos_nlp()
elif page == "Skills":
    skills()
elif page == "Contato":
    contact()
