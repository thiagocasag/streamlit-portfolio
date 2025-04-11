import streamlit as st
from home import home
from projects import projects
from skills import skills
from contact import contact

# tema do site 
st.set_page_config(page_title="Meu Portfólio", page_icon="📊", layout="wide")

# Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Inicio", "Projetos", "Skills", "Contato"])


# Home Page
if page == "Inicio":
    home()

# Projects Page
elif page == "Projetos":
    projects()

# Skills Page
elif page == "Skills":
    skills()

# Contact Page
elif page == "Contato":
    contact()


