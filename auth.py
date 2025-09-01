import streamlit as st


def is_authenticated() -> bool:
    return bool(st.session_state.get("authenticated"))


def enforce_login() -> None:
    if not is_authenticated():
        st.info("Você precisa estar autenticado para acessar esta página.")
        try:
            st.switch_page("pages/0_Login.py")
        except Exception:
            st.stop()

