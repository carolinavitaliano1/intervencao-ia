import os
import streamlit as st


st.set_page_config(page_title="Login • NeurotechEvoluir", page_icon="🔐", layout="wide")


def get_credentials() -> dict[str, str]:
    env_user = os.getenv("APP_USERNAME")
    env_pass = os.getenv("APP_PASSWORD")
    if env_user and env_pass:
        return {env_user: env_pass}
    # Credenciais padrão para demonstração
    return {"admin@neurotech.com": "admin123"}


def ensure_session_defaults() -> None:
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
    if "current_user" not in st.session_state:
        st.session_state.current_user = None


def try_login(username: str, password: str) -> bool:
    creds = get_credentials()
    return creds.get(username) == password


def render_header() -> None:
    st.markdown(
        """
        <div style="background:#fff;border:1px solid #eee;border-radius:16px;padding:22px 28px;display:flex;align-items:center;justify-content:space-between;box-shadow:0 6px 24px rgba(0,0,0,.06);margin-bottom:18px">
          <div style="font-weight:800;color:#6b21a8;font-size:28px">NeurotechEvoluir</div>
          <div style="font-size:16px;color:#6b7280">Acesse sua conta para continuar</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_login_form() -> None:
    with st.container(border=True):
        st.subheader("Entrar")
        st.caption("Use as credenciais definidas via variáveis APP_USERNAME/APP_PASSWORD ou as de demonstração.")
        with st.form("login_form", enter_to_submit=True):
            username = st.text_input("E-mail ou usuário", value="")
            password = st.text_input("Senha", type="password", value="")
            col_a, col_b = st.columns([1, 3])
            with col_a:
                submit = st.form_submit_button("Entrar", use_container_width=True)
            with col_b:
                st.write("")
        if submit:
            if not username or not password:
                st.error("Preencha usuário e senha.")
            elif try_login(username, password):
                st.session_state.authenticated = True
                st.session_state.current_user = username
                st.success("Login realizado com sucesso! Redirecionando…")
                st.switch_page("app.py")
            else:
                st.error("Credenciais inválidas.")


def render_already_logged() -> None:
    with st.container(border=True):
        st.success(f"Você já está autenticado como: {st.session_state.current_user}")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Ir para Home", use_container_width=True):
                st.switch_page("app.py")
        with col2:
            if st.button("Sair", use_container_width=True):
                st.session_state.authenticated = False
                st.session_state.current_user = None
                st.rerun()


def main() -> None:
    ensure_session_defaults()
    render_header()
    st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)
    center = st.columns([1, 1.2, 1])
    with center[1]:
        if st.session_state.authenticated:
            render_already_logged()
        else:
            render_login_form()


if __name__ == "__main__":
    main()

