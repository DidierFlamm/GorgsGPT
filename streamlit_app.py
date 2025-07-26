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


st.sidebar.subheader("📽️ Videals", divider=True)

ambiance = st.sidebar.radio(
    "Select ambiance",
    ("🔇 Silent mode", "👫 La KIN 201", "💃 Strass Academy"),
    label_visibility="collapsed",
)

if ambiance.startswith("👫"):
    video_url = "https://www.youtube.com/watch?v=CJVtr9vUwCQ"
    st.sidebar.video(video_url, autoplay=True, muted=False)

    st.sidebar.markdown(
        """
    <div style='text-align: center; font-size: small; color: gray;'>
    © 2001 Road feat. Dany
    </div>
    """,
        unsafe_allow_html=True,
    )


elif ambiance.startswith("💃"):
    video_url = "https://www.youtube.com/watch?v=PhQeyRZGu-4"
    st.sidebar.video(video_url, autoplay=True, muted=False)

    st.sidebar.markdown(
        """
    <div style='text-align: center; font-size: small; color: gray;'>
    © 2001 Strass Academy
    </div>
    """,
        unsafe_allow_html=True,
    )

st.sidebar.subheader("👾 Join Discord", divider=True)

st.sidebar.markdown(
    """
    <a href="https://discord.gg/6bxmWMW3GM" target="_blank">
        <img src="https://github.com/DidierFlamm/GorgsGPT/raw/main/data/GorgsGPT.png" width="100%"; />
    </a>
    """,
    unsafe_allow_html=True,
)


st.sidebar.subheader("🤓 View K'PTN' 42 apps", divider=True)

st.sidebar.markdown(
    """
    <a href="https://share.streamlit.io/user/didierflamm" target="_blank">
        <img src="https://github.com/DidierFlamm/DidierFlamm/raw/main/DID.png" width="100%"; />
    </a>
    """,
    unsafe_allow_html=True,
)

st.sidebar.subheader("Site de la Soce", divider=True)

st.sidebar.markdown(
    """
    <a href="https://www.arts-et-metiers.asso.fr" target="_blank">
        <img src="https://github.com/DidierFlamm/GorgsGPT/raw/main/data/Amalumni.webp" width="100%"; />
    </a>
    """,
    unsafe_allow_html=True,
)

st.sidebar.subheader("A la Fratern's !", divider=True)

st.sidebar.markdown(
    """
    <a href="https://www.arts-et-metiers.asso.fr" target="_blank">
        <img src="https://github.com/DidierFlamm/GorgsGPT/raw/main/data/Amtradszaloeil.png" width="100%"; />
    </a>
    """,
    unsafe_allow_html=True,
)

###############################################################################################################

st.image("https://github.com/DidierFlamm/GorgsGPT/raw/main/data/GorgsGPT.png")

st.subheader("French to Argad'z")

french = st.text_input(
    "Prompt en Français",
    key="french",
)

to_argadz = french  #####################

st_gothic("🚧 " + to_argadz + " 🚧")

script = f"""
<script>
    var msgARGADZ = new SpeechSynthesisUtterance({to_argadz!r});
    msgARGADZ.lang = 'FR-fr';
    msgARGADZ.rate = 1.1;



    function speak() {{
        window.speechSynthesis.cancel();
        window.speechSynthesis.speak(msgARGADZ);
        
    }}

    function stop() {{
        window.speechSynthesis.cancel();
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
        script + """<button onclick="stop()">🔇<br>Sacque toi !</button>""",
        height=45,
    )

st.divider()  ########################################################################################

st.subheader("Argad'z to French")

argadz = st.text_input(
    "Prompt en Argad'z",
    key="argadz",
)


to_french = argadz  #######################

st_gothic("🚧 " + to_french + " 🚧")

script = f"""
<script>
    var msgFRENCH = new SpeechSynthesisUtterance({to_french!r});
    msgFRENCH.lang = 'FR-fr';
    msgFRENCH.rate = 1.1;



    function speak() {{
        window.speechSynthesis.cancel();
        window.speechSynthesis.speak(msgFRENCH);
        
    }}

    function stop() {{
        window.speechSynthesis.cancel();
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
        script + """<button onclick="stop()">🔇<br>La gerbe !</button>""",
        height=45,
    )

st.divider()  ############################################################################################

st.subheader("Vocab's")

with st.expander("📖 Afficher le dictionnaire"):
    st.write("🚧🤓🚧")

st.divider()

st.markdown(
    """
    <div style='text-align: center; font-size: small; color: gray;'>
    🎁 GorgsGPT est une application Open Source offerte à la prom's KIN 226 par sa prom's marraine KIN 201 🎁<br>
    🤗 Les réponses de GorgsGPT sont générées via l'API Open Source de 
    <a href="https://huggingface.co/" target="_blank" style="color:gray; text-decoration:none;">Hugging Face</a> 🤗<br>
    © 2025 Didier FLAMM feat. KIN 201 🫶
    </div>
    """,
    unsafe_allow_html=True,
)
