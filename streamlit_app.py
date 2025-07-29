# -*- coding: utf-8 -*-
import streamlit as st
import streamlit.components.v1 as components
import time

# set_page_config() can only be called once per app page, and must be called as the first Streamlit command in your script.


st.set_page_config(
    page_title="GorgsGPT for KIN 226",
    page_icon="🎁",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": None,
        "Report a bug": "mailto:contact@diveintodata.ai?subject=Reporting%20a%20bug%20in%20GorgsGPT%20app&body=OS%20(Windows,%20macOS,%20Linux,%20Android,%20iOS):%0ABrowser:%0ABug%20you%20encountered:%0A%0AThanks!",
        "About": """## GorgsGPT
© 2025 Didier Flamm  
✉️ [contact@diveintodata.ai](mailto:contact@diveintodata.ai) – 💬 [LinkedIn](https://www.linkedin.com/in/didier-flamm) – 📁 [Portfolio](https://share.streamlit.io/user/didierflamm)  
""",
    },
)

st.logo(
    "https://github.com/DidierFlamm/GorgsGPT/raw/main/data/Amtradszaloeil.png",
    size="large",
)

# Charger la police gothique Arts & Métiers via Google Fonts
GOTHIC_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=UnifrakturCook:wght@700&display=swap');

.gothic-text {
    font-family: 'UnifrakturCook', cursive;
    font-size: 2em;
    color: black;
}
</style>
"""

st.markdown(GOTHIC_CSS, unsafe_allow_html=True)


def st_gothic(text: str, size: str = "2em"):
    html = f"""
    <div class="gothic-text" style="font-size:{size}; color: inherit;">{text}</div>
    """
    st.markdown(html, unsafe_allow_html=True)


def st_norms(text: str, size: str = "2em"):
    html = f"""
    <div style="font-size:{size}; color: inherit;">{text}</div>
    """
    st.markdown(html, unsafe_allow_html=True)


st.sidebar.subheader(":green[Prom's]", divider=True)  ########################

tabagns = st.sidebar.selectbox(
    "Choisis un Tabagn's:",
    (
        "KIN (Aix-en-Provence)",
        "Boquette (Angers)",
        "Bordel's (Bordeaux)",
        "Châlon's (Châlons-en-Champagne)",
        "Clun's (Cluny)",
        "Karlsberg's (Karlsruhe)",
        "Bir's (Lille)",
        "Cyber's (Metz)",
    ),
)

anns = st.sidebar.select_slider(
    "Choisis une Ann's:", options=range(150, 226), value=201
)


st.sidebar.subheader(
    f"{tabagns.split(" ")[0]} {anns}", divider=True
)  ########################


vimeo_embed = """
<iframe src="https://player.vimeo.com/video/1097107734?h=40d724f3ee" 
    width="100%" height="180" frameborder="0" allow="autoplay; fullscreen" allowfullscreen>
</iframe>
"""


with st.sidebar:
    components.html(vimeo_embed, height=180)

with st.sidebar:
    col1, col2 = st.columns([1, 2])  # 2 colonnes, col2 plus large

    with col1:
        st.image(
            "https://i.vimeocdn.com/portrait/115967603_72x72",
            use_container_width=True,
            caption="portrait de l'auteur.e (en option)",
        )

    with col2:
        st.write("© 2025 Claire Barrin")


pg = st.sidebar.selectbox(
    "Choisis un PG:",
    (
        "[Bucque] [Fam's]",
        "exemple: Road 999",
    ),
)


if pg.endswith(str(999)):
    video_url = "https://www.youtube.com/watch?v=CJVtr9vUwCQ"
    st.sidebar.video(video_url, autoplay=False, muted=False)
else:

    st.sidebar.caption(
        "⚠️ En respect des obligations RGPD et du droit à la vie privée (Code civil, article 9), la liste sera limitée aux Bucques + Fam’s de chaque PG."
    )

    st.sidebar.write(
        ":green[1. contenu personnel à l'initiative de chaque PG (optionnel)]"
    )

    uploaded_file = st.sidebar.file_uploader("Choisis un fichier:")
    if uploaded_file is not None:
        st.sidebar.info(
            "Merci d'avoir testé mais pour l'instant ça ne fonctionne pas désolé.",
            icon="😅",
        )

    st.sidebar.write(":violet[2. 📧 <fams><tabagns><anns>@gadz.org]")

    st.sidebar.caption(
        "⚠️ L'adresse mail @gadz.org sera générée automatiquement par l'appli sans être stockée nulle part pour éviter toute fuite de données."
    )

    st.sidebar.write(":blue[3. infos pro via API LinkedIn]")
    st.sidebar.caption(
        "⚠️ Connexion LinkedIn requise : vous choisissez d’autoriser ou non GorgsGPT à accéder aux infos publiques de votre profil LinkedIn."
    )

strass = st.sidebar.selectbox(
    "Choisis une Strass:",
    ("[Strass]", "exemple: Strass Academy"),
)

if strass.endswith("Strass Academy"):
    video_url = "https://www.youtube.com/watch?v=PhQeyRZGu-4"
    st.sidebar.video(video_url, autoplay=False, muted=False)
else:
    st.sidebar.write(
        ":orange[4. contenu artistique à l'initiative de chaque strass (optionnel)]"
    )
    st.sidebar.caption(
        "⚠️ Soumis à la valid's 🤙 préalable par l'ensemble des co-strass."
    )

st.sidebar.subheader(
    ":blue[🫂 GorgsGPT sur LinkedIn]", divider=True
)  ########################################

st.sidebar.markdown(
    """
    <a href="https://www.linkedin.com/groups/13343076/" target="_blank">
        <img src="https://github.com/DidierFlamm/GorgsGPT/raw/main/data/LinkedIn.webp" width="100%"; />
    </a>
    """,
    unsafe_allow_html=True,
)

st.sidebar.subheader(
    ":violet[👾 GorgsGPT sur Discord]", divider=True
)  ########################################

st.sidebar.markdown(
    """
    <a href="https://discord.gg/gxBZvWWVyX" target="_blank">
        <img src="https://github.com/DidierFlamm/GorgsGPT/raw/main/data/Discord.webp" width="100%"; />
    </a>
    """,
    unsafe_allow_html=True,
)

st.sidebar.subheader(
    ":green[🫦 GorgsGPT sur WhatsApp]", divider=True
)  ########################################

st.sidebar.write(
    ":green[Tu savais que le Gorg's était encore sur WhatsApp en 2025 ? 🥸]"
)

st.sidebar.subheader(
    ":orange[🤝 Site de la Soce]", divider=True
)  ####################################

st.sidebar.markdown(
    """
    <a href="https://www.arts-et-metiers.asso.fr" target="_blank">
        <img src="https://github.com/DidierFlamm/GorgsGPT/raw/main/data/Amalumni.webp" width="100%"; />
    </a>
    """,
    unsafe_allow_html=True,
)

st.sidebar.subheader(":blue[🌐 Gadzarts sur Wikipedia]", divider=True)

st.sidebar.link_button(
    "Ouvrir l’article Wikipédia",
    "https://fr.wikipedia.org/wiki/Gadzarts",
    use_container_width=True,
)

st.sidebar.subheader(
    "🌊 App's de K'PTN' 42 👀", divider=True
)  ########################################

st.sidebar.markdown(
    """
    <a href="https://share.streamlit.io/user/didierflamm" target="_blank">
        <img src="https://github.com/DidierFlamm/DidierFlamm/raw/main/DID.png" width="100%"; />
    </a>
    """,
    unsafe_allow_html=True,
)
st.sidebar.markdown(
    "<p style='text-align: center; font-size: 14px; color: gray;'>© Didier FLAMM</p>",
    unsafe_allow_html=True,
)

st.sidebar.subheader(
    ":green[💲 Keud's de Fratern's]", divider=True
)  ########################################

ad = st.sidebar.toggle("Votre pub ici pour...")

if ad:
    st.sidebar.write(":green[rien au monde ! 💸]")

st.sidebar.subheader(
    ":orange[🪇 Le Pian's de l'Em's]", divider=True
)  ########################################


st.sidebar.write("Chants randomizés:")

video_url = "https://www.youtube.com/watch?v=wi288eHFk18"
st.sidebar.video(video_url, autoplay=False, muted=False)

st.sidebar.markdown(
    """<p style="text-align:center; font-size:0.8em; color:gray;">© 224 Lupage feat. Joe Kox</p>
    """,
    unsafe_allow_html=True,
)

st.sidebar.subheader(
    ":violet[💜 Fratern's]", divider=True
)  ########################################

st.sidebar.image(
    "https://github.com/DidierFlamm/GorgsGPT/raw/main/data/Amtradszaloeil.png",
    caption="© 2006 Guiral LACOTTE",
)

st.sidebar.markdown(
    """
    <p style="text-align:center; font-size:0.8em; color:gray;">
    Image digitalisée, nettoyée et vectorialisée par l'utilisateur
    <a href="https://fr.m.wikipedia.org/wiki/Utilisateur" target="_blank">Beretta_vexee</a> 👀
    </p>
    """,
    unsafe_allow_html=True,
)

st.sidebar.divider()

st.sidebar.markdown(
    """<p style="text-align:center; font-size:0.8em; color:gray;">👉 
    <a href="https://fr.wikipedia.org/wiki/Wikip%C3%A9dia:Contact" target="_blank">Wikipedia: Contact</a>
    </p>
    """,
    unsafe_allow_html=True,
)

st.sidebar.markdown(
    """<p style="text-align:center; font-size:0.8em; color:gray;">👉 
    <a href="https://foundation.wikimedia.org/wiki/Policy:Privacy_policy" target="_blank">Wikimedia: Privacy Policy</a>
    </p>
    """,
    unsafe_allow_html=True,
)
###############################################################################################################

st.image("https://github.com/DidierFlamm/GorgsGPT/raw/main/data/GorgsGPT.png")

st.markdown(
    """
    <h1 style="text-align:center;">
        Connecting Gadzarts
    </h1>
    """,
    unsafe_allow_html=True,
)

st.divider()

on = st.toggle("I consent to anonymously submitting a template to train GorgsGPT.")

if on:

    st.segmented_control(
        "Source language",
        ["Argad'Z", "FRench", "ENglish", "AUto-detect"],
        key="departure",
        selection_mode="single",
    )

    st.segmented_control(
        "Target language",
        ["Argad'Z", "FRench", "ENglish", "AUto-detect"],
        key="arrival",
        selection_mode="single",
    )

    with st.expander("View 'Pierre de Rosette' random samples"):
        st.code(
            """AZ Le carn's des trad's du vénérable Dav's est lar's étal's.  
FR Le carnet traditionnel de David l'énervé est très validé."""
        )
        st.code(
            """EN The head of engineering school Arts & Métiers teaches solidarity through student hazing.
AZ La Strass des Gadzarts est lar's fratern's, zamer's pour cette Usin's à Gad'z."""
        )

    st.write("Scan your translation template")

    enable = st.checkbox("Enable camera")
    picture = st.camera_input("Scan your translation template", disabled=not enable)

    if picture:

        st.error(
            """Unable to detect Source language and/or Target language.  
            Please press Rerun or ✖️ Clear Photo to scan a new template.""",
            icon="⁉️",
        )
        if st.button("Rerun"):
            with st.spinner("Wait for it...", show_time=True):
                time.sleep(5)
            st.warning(
                """Oops! A translation error was detected. Please review your template and try again.""",
                icon="😬",
            )


st.divider()

st.subheader(":violet[🚧 French to Argad'z 🚧]")

french = st.text_input(
    "Prompt en Français",
    value="J'entrave que dalle à cette appli, y a rien qui marche ou quoi ? Explique-moi comment ça fonctionne ton truc au lieu de nous prendre la tête, stp 🤗",
    key="french",
)

to_argadz = french  #####################

st_gothic("💬 " + to_argadz)

script = f"""
<script>
    var msgARGADZ = new SpeechSynthesisUtterance({to_argadz!r});
    msgARGADZ.lang = 'FR-fr';
    msgARGADZ.rate = 1.1;

    var msgSTOP = new SpeechSynthesisUtterance("Sacque toï !");
    msgARGADZ.lang = 'FR-fr';
    msgARGADZ.rate = 1.1;


    function speak() {{
        window.speechSynthesis.cancel();
        window.speechSynthesis.speak(msgARGADZ);
        
    }}

    function stop() {{
        window.speechSynthesis.cancel();
        window.speechSynthesis.speak(msgSTOP)
    }}
</script>
"""

(col1, col2, *_) = st.columns(4, vertical_alignment="center")

with col1:
    components.html(
        script + """<button onclick="speak()">🗣️<br>Affole les Watts !</button>""",
        height=45,
    )

with col2:
    components.html(
        script + """<button onclick="stop()">🔇<br>Sacque toï !</button>""",
        height=45,
    )

st.divider()  ########################################################################################

st.subheader(":violet[🚧 Argad'z to French 🚧]")

argadz = st.text_input(
    "Prompt en Argad'z",
    value="Il est pas norm's ton Num's, bord's ! Le Gorg's est très 😡 alors on se sacque au fond du Tabagn's... mon 😤 !",
    key="argadz",
)


to_french = argadz  #######################

st_norms("💬 " + to_french)

script = f"""
<script>
    var msgFRENCH = new SpeechSynthesisUtterance({to_french!r});
    msgFRENCH.lang = 'FR-fr';
    msgFRENCH.rate = 1.1;

    var msgSTOP = new SpeechSynthesisUtterance("Sacque toï !");
    msgARGADZ.lang = 'FR-fr';
    msgARGADZ.rate = 1.1;

    function speak() {{
        window.speechSynthesis.cancel();
        window.speechSynthesis.speak(msgFRENCH);
    }}

    function stop() {{
        window.speechSynthesis.cancel();
        window.speechSynthesis.speak(msgSTOP)
    }}
</script>
"""

(col1, col2, *_) = st.columns(4, vertical_alignment="center")

with col1:
    components.html(
        script + """<button onclick="speak()">🗣️<br>Keud's de Watts !</button>""",
        height=45,
    )

with col2:
    components.html(
        script + """<button onclick="stop()">🔇<br>Sacque toï !</button>""",
        height=45,
    )

st.divider()  ########################################################################################

st.subheader(":violet[🚧 GorgsGPT 🚧]")
st.text_area("coming soon...", disabled=True)

st.divider()  ############################################################################################

st.subheader(":violet[🚨 Vocab's]")

with st.expander("📖 Afficher le dictionnaire Argad'z"):
    st.write("🚧 👷 🚧")


st.divider()

st.subheader(":blue[💙 Rate this app's]")

sentiment_mapping = [
    "GorgsGPT a la méga gerbe !",
    "Keud's de fratern's pour l'app's !",
    "Fay's pour GorgsGPT",
    "Bel eff's du phi's à l'app's !",
    "Phi's HM lar's GorgsGPT !",
]
selected = st.feedback("stars")
if selected is not None:
    st.markdown(f"{sentiment_mapping[selected]}")

st.divider()

st.markdown(
    """
    <div style='text-align: center; font-size: 0.8em; color: gray;'>
    🎁 À KIN 226 et à toutes les Prom's, ce cadeau de bienvenue vous est offert par la puissance des Trad's de notre réseau Gad'z !<br>
    🤗 GorgsGPT est un chatbot open source utilisant l’API de <a href="https://huggingface.co/" target="_blank">Hugging Face</a>.<br>
    ⚠️ Licence <a href="https://creativecommons.org/licenses/by-sa/4.0/deed.fr" target="_blank">CC BY-SA 4.0</a> sauf mention contraire.<br>
    © 2026 KIN 201<br>🫶
    </div>
    """,
    unsafe_allow_html=True,
)

if "balloons" not in st.session_state:
    st.balloons()
    st.session_state.balloons = True
