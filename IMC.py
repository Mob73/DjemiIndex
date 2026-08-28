import streamlit as st

st.set_page_config(
    page_title="Djemi Index",
    page_icon="⚖️",
    layout="centered",
    initial_sidebar_state="collapsed",
)

if "theme" not in st.session_state:
    st.session_state.theme = "light"

if "result" not in st.session_state:
    st.session_state.result = None

if "sex" not in st.session_state:
    st.session_state.sex = "Homme"

if st.session_state.theme == "light":
    BG = "#f8f9fa"
    CARD = "#ffffff"
    TEXT = "#1a1d20"
    MUTED = "#6c757d"
    BORDER = "#dee2e6"
    INPUT = "#f1f3f5"
    SHADOW = "0 10px 30px rgba(0, 0, 0, 0.05)"
else:
    BG = "#121417"
    CARD = "#1e2227"
    TEXT = "#f8f9fa"
    MUTED = "#98a2b3"
    BORDER = "#2c323b"
    INPUT = "#262b33"
    SHADOW = "0 10px 30px rgba(0, 0, 0, 0.2)"

st.markdown(
    f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Playfair+Display:wght@600;700&display=swap');

        :root {{
            --bg: {BG};
            --card: {CARD};
            --text: {TEXT};
            --muted: {MUTED};
            --border: {BORDER};
            --input: {INPUT};
            --shadow: {SHADOW};
        }}

        * {{
            box-sizing: border-box;
        }}

        html, body, [class*="css"] {{
            font-family: "DM Sans", sans-serif;
        }}

        body {{
            background: var(--bg);
            color: var(--text);
            transition: all .35s ease;
        }}

        .stApp {{
            background: var(--bg);
            min-height: 100vh;
        }}

        [data-testid="stHeader"] {{
            background: transparent;
        }}

        [data-testid="stToolbar"] {{
            visibility: hidden;
        }}

        .block-container {{
            max-width: 1100px;
            padding: 28px 20px 60px;
        }}

        .topbar {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 52px;
        }}

        .brand {{
            display: flex;
            align-items: center;
            gap: 12px;
        }}

        .brand-icon {{
            width: 42px;
            height: 42px;
            display: grid;
            place-items: center;
            border-radius: 12px;
            color: #ffffff;
            font-size: 21px;
            background: #212529;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        }}

        .brand-name {{
            font-family: "Playfair Display", serif;
            font-size: 25px;
            font-weight: 700;
            letter-spacing: -.5px;
            color: var(--text);
        }}

        .brand-name span {{
            color: #495057;
        }}

        .hero {{
            text-align: center;
            margin-bottom: 38px;
        }}

        .eyebrow {{
            display: inline-flex;
            align-items: center;
            gap: 7px;
            color: var(--muted);
            background: var(--input);
            border: 1px solid var(--border);
            padding: 8px 13px;
            border-radius: 999px;
            font-size: 12px;
            font-weight: 700;
            letter-spacing: .4px;
            text-transform: uppercase;
        }}

        .hero h1 {{
            margin: 18px 0 10px;
            color: var(--text);
            font-family: "Playfair Display", serif;
            font-size: clamp(38px, 7vw, 70px);
            line-height: 1.03;
            letter-spacing: -2px;
        }}

        .hero h1 span {{
            color: #495057;
        }}

        .hero p {{
            max-width: 560px;
            margin: auto;
            color: var(--muted);
            font-size: 16px;
            line-height: 1.7;
        }}

        .glass-card {{
            background: var(--card);
            border: 1px solid var(--border);
            border-radius: 24px;
            box-shadow: var(--shadow);
            padding: 30px;
        }}

        .section-title {{
            color: var(--text);
            font-size: 18px;
            font-weight: 800;
            margin-bottom: 20px;
        }}

        .field-label {{
            color: var(--muted);
            font-size: 13px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: .8px;
            margin: 22px 0 8px;
        }}

        .value-display {{
            color: var(--text);
            font-size: 31px;
            font-weight: 800;
            margin-bottom: 3px;
        }}

        .value-display small {{
            color: var(--muted);
            font-size: 16px;
            font-weight: 700;
        }}

        div[data-testid="stSlider"] {{
            padding-top: 4px;
        }}

        div[data-testid="stSlider"] [role="slider"] {{
            background: #212529;
        }}

        /* Bouton principal de calcul */
        .stButton > button {{
            width: 100%;
            min-height: 56px;
            border: 0;
            border-radius: 14px;
            color: #ffffff;
            background: #212529;
            font-family: "DM Sans", sans-serif;
            font-size: 16px;
            font-weight: 800;
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.15);
            transition: transform .22s ease, background .22s ease;
            margin-top: 24px;
        }}

        .stButton > button:hover {{
            background: #343a40;
            transform: translateY(-2px);
        }}

        /* Bouton du thème */
        .theme-button .stButton > button {{
            min-height: 42px;
            width: 48px;
            padding: 0;
            margin: 0;
            border-radius: 12px;
            font-size: 18px;
            background: var(--card);
            border: 1px solid var(--border);
            box-shadow: none;
            color: var(--text);
        }}
        
        .theme-button .stButton > button:hover {{
            background: var(--input);
            transform: none;
        }}

        /* Boutons de sélection du Sexe */
        .sex-container {{
            display: flex;
            gap: 12px;
            margin-bottom: 10px;
        }}

        .result-card {{
            margin-top: 24px;
            padding: 30px;
            text-align: center;
            border-radius: 24px;
            color: #ffffff;
            background: #212529;
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.2);
            animation: resultIn .65s cubic-bezier(.2,.8,.2,1);
        }}

        .result-card h2 {{
            margin: 0 0 18px;
            font-family: "Playfair Display", serif;
            font-size: 26px;
        }}

        .bmi-number {{
            font-size: clamp(60px, 12vw, 92px);
            font-weight: 800;
            letter-spacing: -5px;
            line-height: .95;
        }}

        .bmi-status {{
            display: inline-block;
            margin-top: 18px;
            padding: 8px 15px;
            border: 1px solid rgba(255,255,255,.2);
            border-radius: 999px;
            background: rgba(255,255,255,.1);
            font-weight: 800;
        }}

        .recommendation {{
            margin-top: 20px;
            padding: 18px;
            color: rgba(255,255,255,.9);
            text-align: left;
            border-radius: 14px;
            background: rgba(0,0,0,.2);
            font-size: 14px;
            line-height: 1.65;
        }}

        .footer-note {{
            margin-top: 22px;
            color: var(--muted);
            font-size: 12px;
            text-align: center;
            line-height: 1.6;
        }}

        @keyframes resultIn {{
            from {{ opacity: 0; transform: translateY(22px) scale(.97); }}
            to {{ opacity: 1; transform: translateY(0) scale(1); }}
        }}

        @media (max-width: 650px) {{
            .block-container {{
                padding: 18px 14px 42px;
            }}
            .topbar {{
                margin-bottom: 38px;
            }}
            .glass-card {{
                padding: 22px 18px;
            }}
        }}
    </style>
    """,
    unsafe_allow_html=True,
)

with st.container():
    st.markdown(
        """
        <div class="topbar">
            <div class="brand">
                <div class="brand-icon">⚖️</div>
                <div class="brand-name">Djemi <span>Index</span></div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

theme_col, _ = st.columns([1, 8])
with theme_col:
    st.markdown('<div class="theme-button">', unsafe_allow_html=True)
    theme_icon = "☀️" if st.session_state.theme == "dark" else "🌙"
    if st.button(theme_icon, key="theme_switch", help="Changer le thème"):
        st.session_state.theme = (
            "dark" if st.session_state.theme == "light" else "light"
        )
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown(
    """
    <div class="hero">
        <div class="eyebrow">✦ Votre équilibre, simplifié</div>
        <h1>Comprenez votre <span>corps</span>.</h1>
        <p>
            Un aperçu simple et personnalisé de votre indice de masse corporelle,
            pour mieux prendre soin de vous au quotidien.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

left, right = st.columns([1, 1], gap="large")

with left:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Vos informations</div>', unsafe_allow_html=True)

    st.markdown('<div class="field-label">Sexe</div>', unsafe_allow_html=True)
    
    # Boutons séparés pour Homme et Femme
    col_h, col_f = st.columns(2)
    with col_h:
        is_homme = st.session_state.sex == "Homme"
        btn_type_h = "primary" if is_homme else "secondary"
        if st.button("👨 Homme", key="btn_homme", use_container_width=True):
            st.session_state.sex = "Homme"
            st.rerun()
    with col_f:
        is_femme = st.session_state.sex == "Femme"
        if st.button("👩 Femme", key="btn_femme", use_container_width=True):
            st.session_state.sex = "Femme"
            st.rerun()

    st.markdown('<div class="field-label">Taille</div>', unsafe_allow_html=True)
    height = st.slider(
        "Taille",
        min_value=1.20,
        max_value=2.20,
        value=1.75,
        step=0.01,
        format="%.2f m",
        label_visibility="collapsed",
    )
    st.markdown(
        f'<div class="value-display">{height:.2f} <small>mètre</small></div>',
        unsafe_allow_html=True,
    )

    st.markdown('<div class="field-label">Poids</div>', unsafe_allow_html=True)
    weight = st.slider(
        "Poids",
        min_value=35,
        max_value=180,
        value=70,
        step=1,
        format="%d kg",
        label_visibility="collapsed",
    )
    st.markdown(
        f'<div class="value-display">{weight} <small>kg</small></div>',
        unsafe_allow_html=True,
    )

    calculate = st.button("Calculer mon indice  →", key="calculate")
    st.markdown("</div>", unsafe_allow_html=True)

if calculate:
    st.session_state.result = round(weight / (height * height), 1)

with right:
    if st.session_state.result is None:
        st.markdown(
            """
            <div class="glass-card" style="height:100%;display:flex;align-items:center;justify-content:center;text-align:center;">
                <div>
                    <div style="font-size:58px;margin-bottom:14px;">✨</div>
                    <div style="font-size:21px;font-weight:800;color:var(--text);margin-bottom:8px;">
                        Votre résultat apparaîtra ici
                    </div>
                    <div style="color:var(--muted);font-size:14px;line-height:1.6;">
                        Renseignez vos informations puis lancez le calcul
                        pour découvrir votre indice.
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        bmi = st.session_state.result

        if bmi < 18.5:
            status = "Insuffisance pondérale"
            recommendation = (
                "Votre IMC est inférieur à la moyenne recommandée. "
                "Une alimentation équilibrée et suffisamment énergétique peut être utile. "
                "Demandez conseil à un professionnel de santé pour une évaluation personnalisée."
            )
        elif bmi < 25:
            status = "Corpulence normale"
            recommendation = (
                "Votre IMC se situe dans la zone généralement considérée comme équilibrée. "
                "Continuez à privilégier une alimentation variée, une bonne hydratation "
                "et une activité physique régulière."
            )
        elif bmi < 30:
            status = "Surpoids"
            recommendation = (
                "Votre IMC est supérieur à la zone de référence. "
                "De petits changements progressifs dans l'alimentation et l'activité physique "
                "peuvent contribuer à améliorer votre santé. Un avis professionnel est recommandé."
            )
        else:
            status = "Obésité"
            recommendation = (
                "Votre IMC se situe dans une zone élevée. "
                "Un accompagnement personnalisé par un médecin ou un nutritionniste "
                "peut vous aider à définir des objectifs adaptés et durables."
            )

        st.markdown(
            f"""
            <div class="result-card">
                <h2>Votre résultat ({st.session_state.sex})</h2>
                <div class="bmi-number">{bmi:.1f}</div>
                <div class="bmi-status">{status}</div>
                <div class="recommendation">
                    <strong>Recommandation professionnelle</strong><br>
                    {recommendation}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown(
    """
    <div class="footer-note">
        L’IMC est un indicateur général et ne remplace pas un avis médical.
        Les recommandations ne constituent pas un diagnostic.
    </div>
    """,
    unsafe_allow_html=True,
)
import streamlit as st

st.set_page_config(
    page_title="Djemi Index",
    page_icon="⚖️",
    layout="centered",
    initial_sidebar_state="collapsed",
)

if "theme" not in st.session_state:
    st.session_state.theme = "light"

if "result" not in st.session_state:
    st.session_state.result = None

if "sex" not in st.session_state:
    st.session_state.sex = "Homme"

if "estimated_height" not in st.session_state:
    st.session_state.estimated_height = 1.75

if st.session_state.theme == "light":
    BG = "#f8f9fa"
    CARD = "#ffffff"
    TEXT = "#1a1d20"
    MUTED = "#6c757d"
    BORDER = "#dee2e6"
    INPUT = "#f1f3f5"
    SHADOW = "0 10px 30px rgba(0, 0, 0, 0.05)"
else:
    BG = "#121417"
    CARD = "#1e2227"
    TEXT = "#f8f9fa"
    MUTED = "#98a2b3"
    BORDER = "#2c323b"
    INPUT = "#262b33"
    SHADOW = "0 10px 30px rgba(0, 0, 0, 0.2)"

st.markdown(
    f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Playfair+Display:wght@600;700&display=swap');

        :root {{
            --bg: {BG};
            --card: {CARD};
            --text: {TEXT};
            --muted: {MUTED};
            --border: {BORDER};
            --input: {INPUT};
            --shadow: {SHADOW};
        }}

        * {{
            box-sizing: border-box;
        }}

        html, body, [class*="css"] {{
            font-family: "DM Sans", sans-serif;
        }}

        body {{
            background: var(--bg);
            color: var(--text);
            transition: all .35s ease;
        }}

        .stApp {{
            background: var(--bg);
            min-height: 100vh;
        }}

        [data-testid="stHeader"] {{
            background: transparent;
        }}

        [data-testid="stToolbar"] {{
            visibility: hidden;
        }}

        .block-container {{
            max-width: 1100px;
            padding: 28px 20px 60px;
        }}

        .topbar {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 52px;
        }}

        .brand {{
            display: flex;
            align-items: center;
            gap: 12px;
        }}

        .brand-icon {{
            width: 42px;
            height: 42px;
            display: grid;
            place-items: center;
            border-radius: 12px;
            color: #ffffff;
            font-size: 21px;
            background: #212529;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        }}

        .brand-name {{
            font-family: "Playfair Display", serif;
            font-size: 25px;
            font-weight: 700;
            letter-spacing: -.5px;
            color: var(--text);
        }}

        .brand-name span {{
            color: #495057;
        }}

        .hero {{
            text-align: center;
            margin-bottom: 38px;
        }}

        .eyebrow {{
            display: inline-flex;
            align-items: center;
            gap: 7px;
            color: var(--muted);
            background: var(--input);
            border: 1px solid var(--border);
            padding: 8px 13px;
            border-radius: 999px;
            font-size: 12px;
            font-weight: 700;
            letter-spacing: .4px;
            text-transform: uppercase;
        }}

        .hero h1 {{
            margin: 18px 0 10px;
            color: var(--text);
            font-family: "Playfair Display", serif;
            font-size: clamp(38px, 7vw, 70px);
            line-height: 1.03;
            letter-spacing: -2px;
        }}

        .hero h1 span {{
            color: #495057;
        }}

        .hero p {{
            max-width: 560px;
            margin: auto;
            color: var(--muted);
            font-size: 16px;
            line-height: 1.7;
        }}

        .glass-card {{
            background: var(--card);
            border: 1px solid var(--border);
            border-radius: 24px;
            box-shadow: var(--shadow);
            padding: 30px;
        }}

        .section-title {{
            color: var(--text);
            font-size: 18px;
            font-weight: 800;
            margin-bottom: 20px;
        }}

        .field-label {{
            color: var(--muted);
            font-size: 13px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: .8px;
            margin: 22px 0 8px;
        }}

        .value-display {{
            color: var(--text);
            font-size: 31px;
            font-weight: 800;
            margin-bottom: 3px;
        }}

        .value-display small {{
            color: var(--muted);
            font-size: 16px;
            font-weight: 700;
        }}

        div[data-testid="stSlider"] {{
            padding-top: 4px;
        }}

        div[data-testid="stSlider"] [role="slider"] {{
            background: #212529;
        }}

        .stButton > button {{
            width: 100%;
            min-height: 56px;
            border: 0;
            border-radius: 14px;
            color: #ffffff;
            background: #212529;
            font-family: "DM Sans", sans-serif;
            font-size: 16px;
            font-weight: 800;
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.15);
            transition: transform .22s ease, background .22s ease;
            margin-top: 24px;
        }}

        .stButton > button:hover {{
            background: #343a40;
            transform: translateY(-2px);
        }}

        .theme-button .stButton > button {{
            min-height: 42px;
            width: 48px;
            padding: 0;
            margin: 0;
            border-radius: 12px;
            font-size: 18px;
            background: var(--card);
            border: 1px solid var(--border);
            box-shadow: none;
            color: var(--text);
        }}
        
        .theme-button .stButton > button:hover {{
            background: var(--input);
            transform: none;
        }}

        .result-card {{
            margin-top: 24px;
            padding: 30px;
            text-align: center;
            border-radius: 24px;
            color: #ffffff;
            background: #212529;
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.2);
            animation: resultIn .65s cubic-bezier(.2,.8,.2,1);
        }}

        .result-card h2 {{
            margin: 0 0 18px;
            font-family: "Playfair Display", serif;
            font-size: 26px;
        }}

        .bmi-number {{
            font-size: clamp(60px, 12vw, 92px);
            font-weight: 800;
            letter-spacing: -5px;
            line-height: .95;
        }}

        .bmi-status {{
            display: inline-block;
            margin-top: 18px;
            padding: 8px 15px;
            border: 1px solid rgba(255,255,255,.2);
            border-radius: 999px;
            background: rgba(255,255,255,.1);
            font-weight: 800;
        }}

        .recommendation {{
            margin-top: 20px;
            padding: 18px;
            color: rgba(255,255,255,.9);
            text-align: left;
            border-radius: 14px;
            background: rgba(0,0,0,.2);
            font-size: 14px;
            line-height: 1.65;
        }}

        .footer-note {{
            margin-top: 22px;
            color: var(--muted);
            font-size: 12px;
            text-align: center;
            line-height: 1.6;
        }}

        @keyframes resultIn {{
            from {{ opacity: 0; transform: translateY(22px) scale(.97); }}
            to {{ opacity: 1; transform: translateY(0) scale(1); }}
        }}

        @media (max-width: 650px) {{
            .block-container {{
                padding: 18px 14px 42px;
            }}
            .topbar {{
                margin-bottom: 38px;
            }}
            .glass-card {{
                padding: 22px 18px;
            }}
        }}
    </style>
    """,
    unsafe_allow_html=True,
)

with st.container():
    st.markdown(
        """
        <div class="topbar">
            <div class="brand">
                <div class="brand-icon">⚖️</div>
                <div class="brand-name">Djemi <span>Index</span></div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

theme_col, _ = st.columns([1, 8])
with theme_col:
    st.markdown('<div class="theme-button">', unsafe_allow_html=True)
    theme_icon = "☀️" if st.session_state.theme == "dark" else "🌙"
    if st.button(theme_icon, key="theme_switch", help="Changer le thème"):
        st.session_state.theme = (
            "dark" if st.session_state.theme == "light" else "light"
        )
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown(
    """
    <div class="hero">
        <div class="eyebrow">✦ Votre équilibre, simplifié</div>
        <h1>Comprenez votre <span>corps</span>.</h1>
        <p>
            Un aperçu simple et personnalisé de votre indice de masse corporelle,
            pour mieux prendre soin de vous au quotidien.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

left, right = st.columns([1, 1], gap="large")

with left:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Vos informations</div>', unsafe_allow_html=True)

    st.markdown('<div class="field-label">Sexe</div>', unsafe_allow_html=True)
    
    col_h, col_f = st.columns(2)
    with col_h:
        is_homme = st.session_state.sex == "Homme"
        if st.button("👨 Homme", key="btn_homme", use_container_width=True):
            st.session_state.sex = "Homme"
            st.rerun()
    with col_f:
        is_femme = st.session_state.sex == "Femme"
        if st.button("👩 Femme", key="btn_femme", use_container_width=True):
            st.session_state.sex = "Femme"
            st.rerun()

    st.markdown('<div class="field-label">Taille</div>', unsafe_allow_html=True)
    
    # Option d'aide si l'utilisateur ne connait pas sa taille
    unknown_height = st.checkbox("Je ne connais pas ma taille exacte")

    if unknown_height:
        st.info("💡 Astuce : Estimez votre taille en choisissant votre profil ou tranche ci-dessous.")
        est_option = st.selectbox(
            "Comment vous décrivez-vous ?",
            [
                "Petite stature (ex: Moins de 1,60 m)",
                "Stature moyenne / standard (ex: Entre 1,60 m et 1,75 m)",
                "Grande stature (ex: Plus de 1,75 m)"
            ]
        )
        if "Petite" in est_option:
            st.session_state.estimated_height = 1.58 if st.session_state.sex == "Femme" else 1.65
        elif "moyenne" in est_option:
            st.session_state.estimated_height = 1.65 if st.session_state.sex == "Femme" else 1.75
        else:
            st.session_state.estimated_height = 1.78 if st.session_state.sex == "Femme" else 1.85
            
        height = st.slider(
            "Taille estimée",
            min_value=1.20,
            max_value=2.20,
            value=st.session_state.estimated_height,
            step=0.01,
            format="%.2f m",
            label_visibility="collapsed",
        )
    else:
        height = st.slider(
            "Taille",
            min_value=1.20,
            max_value=2.20,
            value=st.session_state.estimated_height,
            step=0.01,
            format="%.2f m",
            label_visibility="collapsed",
        )

    st.markdown(
        f'<div class="value-display">{height:.2f} <small>mètre</small></div>',
        unsafe_allow_html=True,
    )

    st.markdown('<div class="field-label">Poids</div>', unsafe_allow_html=True)
    weight = st.slider(
        "Poids",
        min_value=35,
        max_value=180,
        value=70,
        step=1,
        format="%d kg",
        label_visibility="collapsed",
    )
    st.markdown(
        f'<div class="value-display">{weight} <small>kg</small></div>',
        unsafe_allow_html=True,
    )

    calculate = st.button("Calculer mon indice  →", key="calculate")
    st.markdown("</div>", unsafe_allow_html=True)

if calculate:
    st.session_state.result = round(weight / (height * height), 1)

with right:
    if st.session_state.result is None:
        st.markdown(
            """
            <div class="glass-card" style="height:100%;display:flex;align-items:center;justify-content:center;text-align:center;">
                <div>
                    <div style="font-size:58px;margin-bottom:14px;">✨</div>
                    <div style="font-size:21px;font-weight:800;color:var(--text);margin-bottom:8px;">
                        Votre résultat apparaîtra ici
                    </div>
                    <div style="color:var(--muted);font-size:14px;line-height:1.6;">
                        Renseignez vos informations puis lancez le calcul
                        pour découvrir votre indice.
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        bmi = st.session_state.result

        if bmi < 18.5:
            status = "Insuffisance pondérale"
            recommendation = (
                "Votre IMC est inférieur à la moyenne recommandée. "
                "Une alimentation équilibrée et suffisamment énergétique peut être utile. "
                "Demandez conseil à un professionnel de santé pour une évaluation personnalisée."
            )
        elif bmi < 25:
            status = "Corpulence normale"
            recommendation = (
                "Votre IMC se situe dans la zone généralement considérée comme équilibrée. "
                "Continuez à privilégier une alimentation variée, une bonne hydratation "
                "et une activité physique régulière."
            )
        elif bmi < 30:
            status = "Surpoids"
            recommendation = (
                "Votre IMC est supérieur à la zone de référence. "
                "De petits changements progressifs dans l'alimentation et l'activité physique "
                "peuvent contribuer à améliorer votre santé. Un avis professionnel est recommandé."
            )
        else:
            status = "Obésité"
            recommendation = (
                "Votre IMC se situe dans une zone élevée. "
                "Un accompagnement personnalisé par un médecin ou un nutritionniste "
                "peut vous aider à définir des objectifs adaptés et durables."
            )

        st.markdown(
            f"""
            <div class="result-card">
                <h2>Votre résultat ({st.session_state.sex})</h2>
                <div class="bmi-number">{bmi:.1f}</div>
                <div class="bmi-status">{status}</div>
                <div class="recommendation">
                    <strong>Recommandation professionnelle</strong><br>
                    {recommendation}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown(
    """
    <div class="footer-note">
        L’IMC est un indicateur général et ne remplace pas un avis médical.
        Les recommandations ne constituent pas un diagnostic.
    </div>
    """,
    unsafe_allow_html=True,
)