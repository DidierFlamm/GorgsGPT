# -*- coding: utf-8 -*-
import streamlit as st
import streamlit.components.v1 as components
import time

# set_page_config() can only be called once per app page, and must be called as the first Streamlit command in your script.


st.set_page_config(
    page_title="GorgsGPT",
    page_icon="https://github.com/DidierFlamm/GorgsGPT/raw/main/data/Amtradszaloeil.png",
    initial_sidebar_state="collapsed",
    menu_items={
        "Get Help": None,
        "Report a bug": "mailto:contact@diveintodata.ai?subject=Reporting%20a%20bug%20in%20GorgsGPT%20app&body=OS%20(Windows,%20macOS,%20Linux,%20Android,%20iOS):%0ABrowser:%0ABug%20you%20encountered:%0A%0AThanks!",
        "About": """## GorgsGPT
© 2025 K'PTN' 42 @ KIN 201
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


st.sidebar.subheader(":green[N² Prom's]", divider=True)  ########################

st.sidebar.link_button(
    "📜 Liste d'élèves d'Arts et Métiers ParisTech",
    "https://fr.wikipedia.org/wiki/Liste_d%27%C3%A9l%C3%A8ves_d%27Arts_et_M%C3%A9tiers_ParisTech",
    use_container_width=True,
)

st.sidebar.link_button(
    "🔎  Annuaire de la Société des Anciens Élèves des Écoles Nationales d'Arts et Métiers",
    "https://gallica.bnf.fr/ark:/12148/bd6t543083231/f3.item.double.item",
    use_container_width=True,
)

st.sidebar.link_button(
    "🗃️ Archives Arts et Métiers",
    "https://francearchives.gouv.fr/fr/subject/221557278?aug=True&es_publisher=26288058&indexentry=221557278&restrict_to_single_etype=False&sort=-sortdate",
    use_container_width=True,
)

st.sidebar.divider()

tabagns = st.sidebar.selectbox(
    "Choisis un Tabagn's:",
    (
        "KIN (Aix-en-Provence)",
        "Boquette (Angers)",
        "Bordel's (Bordeaux)",
        "Châlon's (Châlons-en-Champagne)",
        "Clun's (Cluny)",
        "Karlsberg's ❔ (Karlsruhe)",
        "Bir's (Lille)",
        "Cyber's (Metz)",
    ),
)

anns = st.sidebar.select_slider(
    "Choisis une Ann's:", options=range(-17, 226), value=201
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
        st.write("© 225 Claire Barrin")

st.sidebar.divider()

pg = st.sidebar.selectbox(
    "Choisis un PG:",
    (
        "PG Norm's",
        "Rom's 9️⃣9️⃣9️⃣",
    ),
)


if pg.endswith("9️⃣9️⃣9️⃣"):
    video_url = "https://www.youtube.com/watch?v=PhQeyRZGu-4"
    st.sidebar.video(video_url, autoplay=False, muted=False)

    st.sidebar.link_button(
        f"Envoyer un 📧 à Rom's",
        f"mailto:999{tabagns.split(" ")[0]}{anns}@gadz.org",
        use_container_width=True,
    )
else:

    st.sidebar.caption(
        "⚠️ En respect des obligations RGPD et du droit à la vie privée (Code civil, article 9), la liste des PGs sera limitée aux Bucques + Fam’s."
    )

    st.sidebar.write(
        ":green[1. contenu personnel à l'initiative de chaque PG (optionnel)]"
    )

    uploaded_file = st.sidebar.file_uploader("Choisis un fichier:", key="pg")
    if uploaded_file is not None:
        st.sidebar.info(
            "Merci d'avoir testé mais pour l'instant ça ne fonctionne pas désolé.",
            icon="😅",
        )

    st.sidebar.write(":violet[2. 📧 <fams><tabagns><anns>@gadz.org]")

    st.sidebar.link_button(
        "Envoyer un 📧 au PG Norm's",
        f"mailto:'fams''tabagns''anns'@gadz.org",
        use_container_width=True,
    )

    st.sidebar.caption(
        "⚠️ L'adresse mail @gadz.org sera générée automatiquement par l'appli sans être stockée nulle part pour éviter toute fuite de données."
    )

    st.sidebar.write(":blue[3. infos pro via API LinkedIn]")
    st.sidebar.caption(
        "⚠️ Connexion LinkedIn requise : vous choisissez d’autoriser ou non GorgsGPT à accéder aux infos publiques de votre profil LinkedIn."
    )

    st.sidebar.link_button(
        "🏡 Se connecter à LinkedIn",
        "https://www.linkedin.com/groups/13343076/",
        use_container_width=True,
    )

st.sidebar.subheader(
    ":violet[🎛️ YouGorgs]", divider=True
)  ########################################

st.sidebar.caption(
    "⚠️ GorgsGPT vous offre un accès gratuit et illimité à son abonnement YouTube Premium: vous pouvez profiter des vidéos Trad's sans publicité (à condition de ne pas cliquer sur la mention YouTube présente sur toutes les vidéos) en HD plein écran ou bien avec l'écran de votre mobile verrouillé 🙊"
)

with st.sidebar.expander("🔞 J'ai plus de 18 ans ✋"):

    video_url = "https://www.youtube.com/watch?v=CJVtr9vUwCQ"
    st.video(video_url, autoplay=False, muted=False)
    st.markdown(
        """<p style="text-align:center; font-size:0.8em; color:gray;">© Kin 201 🤓</p>
        """,
        unsafe_allow_html=True,
    )

    video_url = "https://www.youtube.com/watch?v=S_eslL8DIuU"
    st.video(video_url, autoplay=False, muted=False)
    st.markdown(
        """<p style="text-align:center; font-size:0.8em; color:gray;">© Kin 212 Gorgu FM 👆👇</p>
        """,
        unsafe_allow_html=True,
    )

    video_url = "https://www.youtube.com/watch?v=LFAl0xnc300"
    st.video(video_url, autoplay=False, muted=False)
    st.markdown(
        """<p style="text-align:center; font-size:0.8em; color:gray;">© Kin 212 Version Karaoké 🎤</p>
        """,
        unsafe_allow_html=True,
    )

    video_url = "https://www.youtube.com/watch?v=Rts_R1cx6oE"
    st.video(video_url, autoplay=False, muted=False)
    st.markdown(
        """<p style="text-align:center; font-size:0.8em; color:gray;">© Li 212 🧢</p>
        """,
        unsafe_allow_html=True,
    )

    video_url = "https://www.youtube.com/watch?v=mAUj_nAe2x4"
    st.video(video_url, autoplay=False, muted=False)
    st.markdown(
        """<p style="text-align:center; font-size:0.8em; color:gray;">© Cl 219 🖤</p>
        """,
        unsafe_allow_html=True,
    )

    video_url = "https://www.youtube.com/watch?v=lNfAtaURtBI"
    st.video(video_url, autoplay=False, muted=False)
    st.markdown(
        """<p style="text-align:center; font-size:0.8em; color:gray;">© 222 Charlotte Cardin 📛</p>
        """,
        unsafe_allow_html=True,
    )

    video_url = "https://www.youtube.com/watch?v=4m73Cm2H0xM"
    st.video(video_url, autoplay=False, muted=False)
    st.markdown(
        """<p style="text-align:center; font-size:0.8em; color:gray;">© 222 Kream 🏃</p>
        """,
        unsafe_allow_html=True,
    )

    video_url = "https://www.youtube.com/watch?v=wDYoed0wVgM"
    st.video(video_url, autoplay=False, muted=False)
    st.markdown(
        """<p style="text-align:center; font-size:0.8em; color:gray;">© 224 DJ THT 💣</p>
        """,
        unsafe_allow_html=True,
    )

    video_url = "https://www.youtube.com/watch?v=wi288eHFk18"
    st.video(video_url, autoplay=False, muted=False)
    st.markdown(
        """<p style="text-align:center; font-size:0.8em; color:gray;">© 224 Lupage feat. Joe Kox 😎😎</p>
        """,
        unsafe_allow_html=True,
    )


st.sidebar.file_uploader("Upload ta videal Trad's:", disabled=True, key="strass")
st.sidebar.caption("🤙 Soumis à la valid's préalable de l'ensemble de tes co-prom's.")

st.sidebar.write(
    "⚠️ En attendant la valid's de tes co-strass, tu peux tester ta videal Trad's en collant le lien YouTube ci-dessous:"
)

yt = st.sidebar.text_input(
    "Lien YouTube:",
)

if yt:
    try:
        st.sidebar.video(yt)
    except Exception:
        st.sidebar.error("Desol's, le Gorgs ne trouve pas ta videal Trad's")

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
    ":green[💬 GorgsGPT sur WhatsApp]", divider=True
)  ########################################

st.sidebar.markdown(
    """
    <a href="https://social.mtdv.me/GorgsGPT" target="_blank">
        <img src="https://github.com/DidierFlamm/GorgsGPT/raw/main/data/WA.png" width="100%"; />
    </a>
    """,
    unsafe_allow_html=True,
)


st.sidebar.subheader(":blue[🌐 Gadzarts sur Wikipedia]", divider=True)

st.sidebar.markdown(
    """
    <a href="https://fr.wikipedia.org/wiki/Gadzarts" target="_blank">
        <img src="https://github.com/DidierFlamm/GorgsGPT/raw/main/data/Wikipedia.png" width="100%"; />
    </a>
    """,
    unsafe_allow_html=True,
)


st.sidebar.subheader(
    ":orange[Soce Arts et Métiers]", divider=True
)  ####################################

st.sidebar.markdown(
    """
    <a href="https://www.arts-et-metiers.asso.fr" target="_blank">
        <img src="https://github.com/DidierFlamm/GorgsGPT/raw/main/data/Amalumni.webp" width="100%"; />
    </a>
    """,
    unsafe_allow_html=True,
)
st.sidebar.subheader(
    ":blue[Fondation Arts et Métiers]", divider=True
)  ####################################

st.sidebar.markdown(
    """
    <a href="https://fondationartsetmetiers.org/" target="_blank">
        <img src="https://github.com/DidierFlamm/GorgsGPT/raw/main/data/FondationAM.jpg" width="100%"; />
    </a>
    """,
    unsafe_allow_html=True,
)


st.sidebar.subheader("🛠️ Boîte à Oüt's", divider=True)


st.sidebar.link_button(
    "Contacter WikiGorgs",
    "https://fr.wikipedia.org/wiki/Wikip%C3%A9dia:Contact",
    use_container_width=True,
    icon="📡",
)

st.sidebar.link_button(
    "Contacter Streamlit",
    "https://discuss.streamlit.io/",
    use_container_width=True,
    icon="💬",
)


st.sidebar.link_button(
    "Gérer votre compte",
    "https://foundation.wikimedia.org/wiki/Policy:Privacy_policy#your-account-info",
    use_container_width=True,
    icon="🔑",
)

st.sidebar.link_button(
    "Voir Privacy Policy",
    "https://foundation.wikimedia.org/wiki/Policy:Privacy_policy",
    use_container_width=True,
    icon="🚔",
)


st.sidebar.link_button(
    "Lar's important",
    "https://foundation.wikimedia.org/wiki/Policy:Privacy_policy#Important_info",
    use_container_width=True,
    icon="‼️",
)

st.sidebar.subheader(
    ":blue[🌊 App's de K'PTN' 42 🏄‍♂️]", divider=True
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
    "<p style='text-align: center; font-size: 14px; color: gray;'>© 2023 Didier Flamm</p>",
    unsafe_allow_html=True,
)


st.sidebar.subheader(
    ":green[💲 Keud's de Fratern's]", divider=True
)  ########################################

ad = st.sidebar.toggle("Votre pub ici pour...")

if ad:
    st.sidebar.write(":green[rien au monde ! 💸]")

st.sidebar.subheader(
    ":violet[💜 Fratern's]", divider=True
)  ########################################

video_url = "https://www.youtube.com/watch?v=k8ytZ_Zcius"
st.sidebar.video(video_url, autoplay=False, muted=False)
st.sidebar.markdown(
    """<p style="text-align:center; font-size:0.8em; color:gray;">© 2022 Syrine Kaouane @ Bo 221</p>
    """,
    unsafe_allow_html=True,
)

st.sidebar.divider()

st.sidebar.image(
    "https://github.com/DidierFlamm/GorgsGPT/raw/main/data/Amtradszaloeil.png",
    caption="© 206 Guiral LACOTTE",
)

st.sidebar.markdown(
    """
    <p style="text-align:center; font-size:0.8em; color:gray;">
    Image digitalisée, nettoyée et vectorialisée par un utilisateur
    <a href="https://fr.m.wikipedia.org/wiki/Utilisateur" target="_blank">homonyme</a> 👀
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

on = st.toggle(
    "I consent to anonymously submitting a translation template to train GorgsGPT."
)

st.divider()

if not on:

    st.image(
        "https://github.com/DidierFlamm/GorgsGPT/raw/main/data/M.ENSAM.H.A.png",
        caption="© 226 GorgsGPT",
    )

else:

    st.segmented_control(
        "🫗 Source language",
        ["🏳️ Argad'Z", "🇫🇷 FRench", "🇬🇧 ENglish", "🏳️‍🌈 AUto-detect"],
        key="departure",
        selection_mode="single",
    )

    st.segmented_control(
        "🎯 Target language",
        ["🏁 Argad'Z", "🇫🇷 FRench", "🇬🇧 ENglish", "🏳️‍🌈 AUto-detect"],
        key="arrival",
        selection_mode="single",
    )

    with st.expander("View 'Pierre de Rosette' random samples"):
        st.code(
            """AZ Le carn's des trad's du vénérable Dav's est lar's étal's.  
FR Le carnet traditionnel de David l'énervé est très validable."""
        )

        st.write("Evaluate this 1st random template:")
        selected_1 = st.feedback("thumbs", key="f1")
        if selected_1 is not None:
            if selected_1 == 1:
                st.write("🥹")
            else:
                st.text_input(
                    "Offer a better translation template if you can...",
                    "Your translation suggestion",
                    key="input_1",
                )

        st.divider()

        st.code(
            """EN The administration of engineering school Arts & Métiers teaches solidarity through student hazing.
AZ La Strass des Trad's est lar's fratern's, bel eff's pour cette Usin's à Gad'z."""
        )
        st.write("Evaluate this 2nd random template:")
        selected_2 = st.feedback("thumbs", key="f2")

        if selected_2 is not None:
            if selected_2 == 1:
                st.write("🥹")
            else:
                st.text_input(
                    "Offer a better translation template if you can...",
                    "Your translation suggestion",
                    key="input_2",
                )

    st.write("Scan a new personal translation template:")

    enable = st.checkbox("Enable camera")
    picture = st.camera_input("Scan your translation template", disabled=not enable)

    if picture:

        st.error(
            """Unable to detect Source language and/or Target language.  
            Please press ⏳ Rerun to give it a deeper look or ✖️ Clear Photo above to scan a new template.""",
            icon="⁉️",
        )
        if st.button("⏳ Rerun"):
            with st.spinner("Wait for it...", show_time=True):
                time.sleep(5)
            st.warning(
                """Oops! A translation error was detected in your template. Please review it and try again later.""",
                icon="😬",
            )

    st.divider()

    st.subheader(":violet[🚧 French to Argad'z 🚧]")

    french = st.text_input(
        "Prompt en Français",
        value="J'entrave que dalle à cette pseudo app, y a rien qui marche ou quoi ? Explique-moi comment ça fonctionne ton truc au lieu de nous prendre la tête, stp 🤗",
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

    st.subheader(":green[✅ GorgsGPT]")
    st.text_area("coming soon...", disabled=True)

    st.divider()  ############################################################################################

    st.subheader(":violet[🚨 Vocab's]")

    with st.expander("📖 Afficher le dictionnaire Argad'z"):
        st.write("🚧 👷 🚧")

        st.image(
            "https://upload.wikimedia.org/wikipedia/commons/archive/6/69/20180210154153%21Carnet_de_traditions_gadzarts_%2C_dictionnaire.JPG"
        )

        st.video("https://www.youtube.com/watch?v=U7CZcd-UYmU")

        st.image(
            "https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Carnet_de_traditions_gadzarts_%2C_dictionnaire.JPG/960px-Carnet_de_traditions_gadzarts_%2C_dictionnaire.JPG",
        )
        st.markdown(
            """
        <div style='text-align: center; font-size: 0.8em; color: gray;'>
        © 218 <a href="https://commons.wikimedia.org/wiki/User:Jean_GUERIN_2" target="_blank">Jean GUERIN 2</a> 
        
        </div>
        """,
            unsafe_allow_html=True,
        )

st.divider()

st.subheader(":blue[💙 Rate this app's]")

sentiment_mapping = [
    "L'app's foüt la méga gerbe au phi's !",
    "Keud's de fratern's pour l'app's !",
    "C'est trop fay's pour GorgsGPT",
    "Bel eff's du phi's à l'app's !",
    "Le phi's HM lar's l'app's !",
]
selected = st.feedback("faces")
if selected is not None:
    st.markdown(f"{sentiment_mapping[selected]}")


st.divider()

st.markdown(
    """
    <div style='text-align: center; font-size: 0.8em; color: gray;'>
    🎁 À KIN 226 et à toutes les Prom's, ce cadeau de bienvenue vous est offert par la puissance des Trad's de notre réseau Gad'z !<br>
    🤗 <a href="https://GorgsGPT.com/" target="_blank">GorgsGPT</a> est un chatbot open source utilisant l’API de <a href="https://huggingface.co/" target="_blank">Hugging Face</a>.<br>
    ⚠️ Licence <a href="https://creativecommons.org/licenses/by-sa/4.0/deed.fr" target="_blank">CC BY-SA 4.0</a> sauf <a href="https://foundation.wikimedia.org/wiki/Policy:Privacy_policy/Frequently_asked_questions#needaccount" target="_blank">rares circonstances</a>.<br>
    © 226 KIN 201<br>🫶
    </div>
    """,
    unsafe_allow_html=True,
)

if "balloons" not in st.session_state:
    st.balloons()
    st.session_state.balloons = True
