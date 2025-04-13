import streamlit as st

def contact():
    st.title("📞 Contato")

    st.markdown("""
Se quiser entrar em contato para conversar sobre projetos, oportunidades ou qualquer coisa que envolva dados e estatística, seguem abaixo meus canais:

- [🔗 LinkedIn](https://www.linkedin.com/in/seu-usuario)
- [💻 GitHub](https://github.com/seu-usuario)
- 📬 Email: [thiagopcasag@gmail.com](mailto:thiagopcasag@gmail.com)
    """)

    st.markdown("---")

    st.markdown("Caso prefira copiar o email direto:")
    st.code("thiagopcasag@gmail.com", language="markdown")
