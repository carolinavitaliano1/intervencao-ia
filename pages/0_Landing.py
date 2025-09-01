import streamlit as st


st.set_page_config(
    page_title="NeurotechEvoluir",
    page_icon="🧠",
    layout="wide",
)


# Redireciona para a página de Login quando acessado com ?goto=login
try:
    params = st.query_params  # Streamlit >= 1.32
except Exception:
    try:
        params = st.experimental_get_query_params()  # Streamlit < 1.32
    except Exception:
        params = {}

goto = None
if isinstance(params, dict):
    val = params.get("goto")
    if isinstance(val, list):
        goto = val[0] if val else None
    else:
        goto = val
else:
    goto = params.get("goto")

if goto == "login":
    st.switch_page("pages/0_Login.py")


def section_header(title: str, subtitle: str | None = None):
    st.markdown(f"<h2 style='color:#6b21a8;margin-bottom:0'>{title}</h2>", unsafe_allow_html=True)
    if subtitle:
        st.markdown(f"<p style='color:#4b5563;margin-top:6px'>{subtitle}</p>", unsafe_allow_html=True)


def card(icon: str, title: str, description: str):
    st.markdown(
        f"""
        <div style="background:#fff;border-radius:14px;padding:18px;border:1px solid #eee;box-shadow:0 2px 10px rgba(0,0,0,.04);">
          <div style="font-size:28px">{icon}</div>
          <div style="font-weight:700;font-size:18px;margin:8px 0">{title}</div>
          <div style="color:#6b7280;line-height:1.5">{description}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# Header
with st.container():
    cols = st.columns([1, 2, 1])
    with cols[1]:
        st.markdown(
            """
            <header style="position:sticky;top:0;background:#fff;border:1px solid #eee;border-radius:16px;padding:22px 28px;display:flex;align-items:center;justify-content:space-between;z-index:10;box-shadow:0 6px 24px rgba(0,0,0,.06)">
              <div style="font-weight:800;color:#6b21a8;font-size:28px">NeurotechEvoluir</div>
              <nav style="display:flex;gap:28px;font-size:18px;font-weight:600">
                <a href="#modulos" style="text-decoration:none;color:#6b7280;padding:8px 6px">Módulos</a>
                <a href="#impacto" style="text-decoration:none;color:#6b7280;padding:8px 6px">Impacto</a>
                <a href="#contato" style="text-decoration:none;color:#6b7280;padding:8px 6px">Contato</a>
              </nav>
              <a href="/?goto=login" style="background:#7c3aed;color:#fff;padding:12px 24px;border-radius:999px;text-decoration:none;font-size:18px;font-weight:700">Entrar</a>
            </header>
            """,
            unsafe_allow_html=True,
        )


# Hero
st.markdown("<div style='height:28px'></div>", unsafe_allow_html=True)
hero_cols = st.columns([1, 2, 1])
with hero_cols[1]:
    st.markdown(
        """
        <section style="text-align:center;padding:40px 12px;background:linear-gradient(to bottom,#faf5ff,#ffffff);border-radius:18px;border:1px solid #f1e9ff">
          <h1 style="font-size:46px;margin:0;color:#6b21a8;font-weight:900">NeurotechEvoluir</h1>
          <p style="margin-top:16px;color:#6b7280;font-size:18px">A Plataforma de Gestão, Inclusão e Inteligência Pedagógica para o Futuro da Educação.</p>
          <div style="margin-top:22px">
            <a href="#modulos" style="background:#7c3aed;color:#fff;padding:12px 22px;border-radius:999px;text-decoration:none;font-weight:600;font-size:16px">Comece Agora</a>
          </div>
        </section>
        """,
        unsafe_allow_html=True,
    )


# Módulos
st.markdown("<a id='modulos'></a>", unsafe_allow_html=True)
st.markdown("<div style='height:18px'></div>", unsafe_allow_html=True)
section_header("Módulos da Plataforma")
st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)
mod_cols = st.columns(4)
with mod_cols[0]:
    card("🗂️", "Módulo do Aluno", "Prontuário Digital Único: perfil do aprendiz, histórico escolar, documentos e linha do tempo educacional.")
with mod_cols[1]:
    card("🎯", "Planejamento — PEI & PAEE", "Modelos inteligentes, metas claras e monitoramento ativo do progresso.")
with mod_cols[2]:
    card("💬", "Colaboração Multidisciplinar", "Canal seguro entre escola, família e equipe terapêutica, com histórico e engajamento ativo.")
with mod_cols[3]:
    card("🧠", "Módulo Pedagógico Inteligente", "Busca BNCC, seleção de habilidades e adaptação de atividades com IA para inclusão.")


# Impacto
st.markdown("<a id='impacto'></a>", unsafe_allow_html=True)
st.markdown("<div style='height:28px'></div>", unsafe_allow_html=True)
section_header("Impacto da NeurotechEvoluir")
st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)
imp_cols = st.columns(4)
with imp_cols[0]:
    card("🚀", "Economiza tempo", "Reduz burocracia e gera relatórios automáticos.")
with imp_cols[1]:
    card("👥", "Integra equipes", "Favorece a comunicação e evita retrabalho.")
with imp_cols[2]:
    card("📖", "História do aluno", "Cria um dossiê evolutivo único para cada aprendiz.")
with imp_cols[3]:
    card("🧠", "Personalização", "Atividades adaptadas ao perfil e às metas de cada estudante.")


# Footer
st.markdown("<a id='contato'></a>", unsafe_allow_html=True)
st.markdown("<div style='height:32px'></div>", unsafe_allow_html=True)
with st.container():
    st.markdown(
        """
        <footer style="background:#6b21a8;color:#fff;padding:28px 16px;border-radius:16px;text-align:center">
          <div style="font-weight:700">© 2025 NeurotechEvoluir</div>
          <div style="margin-top:6px;opacity:.9">Um hub de gestão inclusiva e inovação pedagógica.</div>
        </footer>
        """,
        unsafe_allow_html=True,
    )

