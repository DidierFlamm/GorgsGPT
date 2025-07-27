# -*- coding: utf-8 -*-
import streamlit as st
import streamlit.components.v1 as components

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


st.sidebar.subheader(":violet[Prom's]", divider=True)  ########################

tabagns = st.sidebar.selectbox(
    "Choisis un Tabagn's",
    (
        "KIN (Aix-en-Provence)",
        "Boquette (Angers)",
        "Bordel's (Bordeaux)",
        "Châlon's (Châlons-en-Champagne)",
        "Clun's (Cluny)",
        "Bir's (Lille)",
        "Cyber's (Metz)",
    ),
)

anns = st.sidebar.select_slider("Choisis une Ann's", options=range(150, 226), value=201)


st.sidebar.subheader(
    f":violet[{tabagns.split(" ")[0]} {anns}]", divider=True
)  ########################

st.sidebar.write(":green[photo et/ou video YouTube]")

pg = st.sidebar.selectbox(
    "Choisis un PG",
    (
        "Road Runner 999",
        "...",
    ),
)

if pg.endswith(str(999)):
    video_url = "https://www.youtube.com/watch?v=CJVtr9vUwCQ"
    st.sidebar.video(video_url, autoplay=False, muted=False)
else:
    st.sidebar.write(":green[photo 2001]")
    st.sidebar.write(":green[photo 2025]")
    st.sidebar.write(":green[Video (optionnelle)]")

strass = st.sidebar.selectbox(
    "Choisis une Strass",
    (
        "Strass Academy",
        "...",
    ),
)

if strass == "Strass Academy":
    video_url = "https://www.youtube.com/watch?v=PhQeyRZGu-4"
    st.sidebar.video(video_url, autoplay=False, muted=False)
else:
    st.sidebar.write(":green[photo et/ou video YouTube]")

st.sidebar.subheader(
    ":violet[👾 Rejoins notre Discord]", divider=True
)  ########################################

st.sidebar.markdown(
    """
    <a href="https://discord.gg/gxBZvWWVyX" target="_blank">
        <img src="https://github.com/DidierFlamm/GorgsGPT/raw/main/data/GorgsGPT.png" width="100%"; />
    </a>
    """,
    unsafe_allow_html=True,
)


st.sidebar.subheader(
    ":violet[Site de la Soce]", divider=True
)  ####################################

st.sidebar.markdown(
    """
    <a href="https://www.arts-et-metiers.asso.fr" target="_blank">
        <img src="https://github.com/DidierFlamm/GorgsGPT/raw/main/data/Amalumni.webp" width="100%"; />
    </a>
    """,
    unsafe_allow_html=True,
)

st.sidebar.subheader(":violet[Les Gadzarts sur Wikipedia]", divider=True)

st.sidebar.link_button("Aller sur Wikipedia", "https://fr.wikipedia.org/wiki/Gadzarts")

st.sidebar.subheader(
    ":violet[🤓 Les apps de K'PTN' 42]", divider=True
)  ########################################

st.sidebar.markdown(
    """
    <a href="https://share.streamlit.io/user/didierflamm" target="_blank">
        <img src="https://github.com/DidierFlamm/DidierFlamm/raw/main/DID.png" width="100%"; />
    </a>
    """,
    unsafe_allow_html=True,
)

st.sidebar.subheader(":violet[💜 Fratern's]", divider=True)

st.sidebar.image(
    "https://github.com/DidierFlamm/GorgsGPT/raw/main/data/Amtradszaloeil.png"
)

###############################################################################################################

st.image("https://github.com/DidierFlamm/GorgsGPT/raw/main/data/GorgsGPT.png")

st.subheader(":violet[French to Argad'z]")

french = st.text_input(
    "Prompt en Français",
    value="Je ne comprends rien à cette appli, explique-moi comment ça fonctionne !",
    key="french",
)

to_argadz = french  #####################

st_gothic("🚧 " + to_argadz + " 🚧")

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

st.subheader(":violet[Argad'z to French]")

argadz = st.text_input(
    "Prompt en Argad'z",
    value="Il est pas norm's ton Num's ! Le Gorg's a la méga gerbe... Bel eff's !",
    key="argadz",
)


to_french = argadz  #######################

st_norms("🚧 " + to_french + " 🚧")

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

st.subheader(":violet[ChatBot]")
st.text_area("coming soon...", disabled=True)

st.divider()  ############################################################################################

st.subheader(":violet[Vocab's]")

with st.expander("📖 Afficher le dictionnaire Argad'z"):
    st.write("🚧🤓🚧")

st.divider()

st.markdown(
    """
    <div style='text-align: center; font-size: small; color: gray;'>
    🎁 À KIN 226, ce cadeau de bienvenue offert par ta prom's ma² KIN 201 s’appuie sur la puissance des Trad's de notre réseau Gad'z !<br>
    🤗 GorgsGPT est un ChatBot Open Source basé sur l'API Open Source de <a href="https://huggingface.co/" target="_blank" style="color:gray; text-decoration:none;">Hugging Face</a>.<br>
    © 2026 KIN 201 🫶
    </div>
    """,
    unsafe_allow_html=True,
)
