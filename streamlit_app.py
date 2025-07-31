# -*- coding: utf-8 -*-
import streamlit as st
import streamlit.components.v1 as components
import time

# set_page_config() can only be called once per app page, and must be called as the first Streamlit command in your script.


st.set_page_config(
    page_title="GorgsGPT",
    page_icon="https://github.com/DidierFlamm/GorgsGPT/raw/main/data/Amtradszaloeil.png",
    initial_sidebar_state=None,
    menu_items={
        "Get Help": None,
        "Report a bug": "mailto:contact@diveintodata.ai?subject=Reporting%20a%20bug%20in%20GorgsGPT%20app&body=OS%20(Windows,%20macOS,%20Linux,%20Android,%20iOS):%0ABrowser:%0ABug%20you%20encountered:%0A%0AThanks!",
        "About": """## GorgsGPT
© 226 K'ptn' 42 @ Kin 201
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
    "🗃️ Archives nationales des Arts et Métiers",
    "https://francearchives.gouv.fr/fr/subject/221557278?aug=True&es_publisher=26288058&indexentry=221557278&restrict_to_single_etype=False&sort=-sortdate",
    use_container_width=True,
)

st.sidebar.divider()

options = [
    "Bir's",
    "Boquette",
    "Bordel's",
    "Châlon's",
    "Clun's",
    "Cyber's",
    "Karlsberg's",
    "Kin",
]

tabagns = st.sidebar.segmented_control(
    "Choisis un Tabagn's:", options, selection_mode="single", default="Kin"
)

anns = st.sidebar.number_input(
    "Choisis une Ann's:", min_value=-17, max_value=226, value=201, step=1
)


st.sidebar.subheader(f"{tabagns} {anns}", divider=True)  ########################


vimeo_embed = """
<iframe src="https://player.vimeo.com/video/1097107734?h=40d724f3ee" 
    width="100%" height="180" frameborder="0" allow="autoplay; fullscreen" allowfullscreen>
</iframe>
"""


with st.sidebar:
    components.html(vimeo_embed, height=180)

st.sidebar.divider()

pg = st.sidebar.selectbox(
    "Choisis un PG:",
    (
        "PG Moy's",
        "Banga 1️⃣1️⃣3️⃣",
    ),
)


if pg.endswith("1️⃣1️⃣3️⃣"):
    video_url = "https://www.youtube.com/watch?v=PhQeyRZGu-4"
    st.sidebar.video(video_url, autoplay=False, muted=False)

    st.sidebar.link_button(
        f"📧 {pg}",
        f"mailto:113{tabagns}{anns}@gadz.org",
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

    st.sidebar.write(":violet[2. 📧 fam's|tabagn's|ann's@gadz.org]")

    st.sidebar.link_button(
        "📧 PG Moys's",
        f"mailto:fams|tabagns|anns@gadz.org",
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
    "⚠️ GorgsGPT vous offre un accès gratuit et illimité à un abonnement YouTube Cloud Premium des Trad's: vous pouvez profiter des vidéos Trad's sans publicité (à condition de ne pas cliquer sur la mention YouTube présente sur toutes les vidéos) en HD plein écran ou bien avec l'écran de votre mobile verrouillé 🙊"
)

with st.sidebar.expander(
    "🔞 Je ✋ sur la tête de mon carn's que je n'ai plus 18 ans depuis n² tap's."
):

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
st.sidebar.caption("🤙 Soumis à la valid's préalable de l'ensemble de tes coprom's.")

st.sidebar.write(
    "⚠️ En attendant la valid's de tes coprom's, tu peux tester ta videal Trad's en collant n'importe quel lien YouTube ci-dessous:"
)

yt = st.sidebar.text_input(
    "Lien YouTube:",
)

if yt:
    try:
        st.sidebar.video(yt)
    except Exception:
        st.sidebar.error(
            "Desol's, le Gorgs ne trouve pas ta videal Trad's sur YouTube.", icon="❌"
        )


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

st.sidebar.subheader(
    ":green[💲 Keud's de Fratern's]", divider=True
)  ########################################

ad = st.sidebar.toggle("Votre pub ici pour...")

if ad:
    st.sidebar.write(":green[rien au monde ! 💸]")

st.sidebar.divider()

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


st.sidebar.subheader(
    ":blue[🌊 Portfolio K'PTN' 42 🏄‍♂️]", divider=True
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

st.sidebar.divider()

st.sidebar.subheader(":orange[🛠️ Boîte à Oüt's]", divider=True)


st.sidebar.link_button(
    "Contacter WikiGorgs",
    "https://fr.wikipedia.org/wiki/Wikip%C3%A9dia:Contact",
    use_container_width=True,
    icon="📡",
)

check1 = st.sidebar.checkbox(
    "J'ai compilé et validé la procédure de contact WikiGorgs."
)

st.sidebar.link_button(
    "Contacter Streamlit",
    "https://discuss.streamlit.io/",
    use_container_width=True,
    icon="💬",
)

check2 = st.sidebar.checkbox(
    "J'ai compilé et validé la procédure de contact Streamlit."
)

st.sidebar.link_button(
    "Contacter Hugging Face",
    "https://huggingface.co/chat",
    use_container_width=True,
    icon="🤗",
)

check3 = st.sidebar.checkbox(
    "J'ai compilé et validé la procédure de contact Hugging Face."
)

st.sidebar.link_button(
    "Voir Privacy Policy",
    "https://foundation.wikimedia.org/wiki/Policy:Privacy_policy",
    use_container_width=True,
    icon="🚔",
)

check4 = st.sidebar.checkbox("J'ai compilé et validé la Privacy Policy de GorgsGPT.")

st.sidebar.link_button(
    "Informations importantes",
    "https://foundation.wikimedia.org/wiki/Policy:Privacy_policy#Important_info",
    use_container_width=True,
    icon="🚨",
)

check5 = st.sidebar.checkbox(
    "J'ai compilé et validé les informations importantes de GorgsGPT."
)

st.sidebar.link_button(
    "Licence CC BY-SA 4.0",
    "https://creativecommons.org/licenses/by-sa/4.0/deed.fr",
    use_container_width=True,
    icon="📜",
)

check6 = st.sidebar.checkbox("J'ai compilé et validé les CGU de GorgsGPT.")

st.sidebar.link_button(
    "Circonstances Particulières",
    "https://foundation.wikimedia.org/wiki/Policy:Privacy_policy/Frequently_asked_questions#needaccount",
    use_container_width=True,
    icon="⚠️",
)

check7 = st.sidebar.checkbox("J'ai compilé et validé les CPU de GorgsGPT.")

disable_acc = True

if check1 and check2 and check3 and check4 and check5 and check6 and check7:

    st.sidebar.success(
        "Bel eff's ! Tu as validé toutes les étapes nécessaires à la création de ton compte GorgsGPT. Il ne te reste plus qu'à cliquer sur le bouton ci-dessous pour accéder (enfin) à l'interface de gestion simplifiée grâce à ton login et mot de passe de la Soce. Tiens bon, tu as déjà fait au moins 90% de ce parcours du combattant 🦾",
        icon="🏆",
    )

    disable_acc = False

st.sidebar.link_button(
    "Gérer votre compte",
    "https://foundation.wikimedia.org/wiki/Policy:Privacy_policy#your-account-info",
    use_container_width=True,
    icon="🔐",
    disabled=disable_acc,
)

st.sidebar.divider()

st.sidebar.link_button(
    "Contacter Wikimedia Foundation",
    "https://meta.wikimedia.org/wiki/User:AKeton_(WMF)",
    use_container_width=True,
    icon="🆘",
)

st.sidebar.divider()

st.sidebar.subheader("🖤 Trad's", divider=True)


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

# Scroll forcé en haut dès le début de l'app
st.markdown("<script>window.scrollTo(0, 0);</script>", unsafe_allow_html=True)

st.image("https://github.com/DidierFlamm/GorgsGPT/raw/main/data/GorgsGPT.png")

st.markdown(
    """
    <h1 style="text-align:center;">
        Connecting Gadzarts
    </h1>
    """,
    unsafe_allow_html=True,
)
subh = st.empty()
st.caption(":blue[© 226 Gorgs GadzUntrainedTransformer]")

# Initialisation de l'historique si besoin
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Affichage dans un conteneur avec hauteur limitée
st.write("History of your great conversations with GorgsGUT:")
messages = st.container(height=300)

# Affichage de l'historique
with messages:
    for role, msg in st.session_state.chat_history:
        messages.chat_message(role).write(msg)


# Récupération de l'entrée utilisateur
with st.expander("💬 Control panel", expanded=True):
    col1, col2, col3 = st.columns(3)

    col1.toggle("YouGorgs", disabled=True)

    if col2.button("🧹 Clean up"):
        st.session_state.chat_history = []
        st.rerun()

    
    rate = col3.feedback("thumbs")

    if rate is None:
        subh.subheader(":blue[🥸 GorgsGUT]")
    elif rate == 1:
        subh.subheader(":blue[🥹 GorgsGUT]")
    else:
        subh.subheader(":blue[😢 GorgsGUT]")

    if prompt := st.chat_input("Say something to GorgsGUT™"):

        # Ajout du message utilisateur
        st.session_state.chat_history.append(("user", prompt))

        # Réponse de GorgsGPT
        response = f"Thanks for the {prompt} — but you’ll need to register via the toolbox at the bottom of the sidebar if you want a reply 😈"
        st.session_state.chat_history.append(("assistant", response))

        # Affichage immédiat dans le container
        messages.chat_message("user").write(prompt)
        messages.chat_message("assistant").write(response)

st.divider()

st.subheader(":red[🚨 Vocab's]")

with st.expander("📖 Afficher le dictionnaire Argad'z"):
    st.write("🚧 👷 🚧")

    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/archive/6/69/20180210154153%21Carnet_de_traditions_gadzarts_%2C_dictionnaire.JPG"
    )

    if st.button("Pages suivantes", icon="⏩"):
        st.video(
            "https://www.youtube.com/watch?v=U7CZcd-UYmU", autoplay=True, muted=False
        )
        st.image(
            "https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Carnet_de_traditions_gadzarts_%2C_dictionnaire.JPG/960px-Carnet_de_traditions_gadzarts_%2C_dictionnaire.JPG",
        )
    st.markdown(
        """
    <div style='text-align: center; font-size: 0.8em; color: gray;'>
    © 218 <a href="https://fr.wikipedia.org/wiki/Utilisateur:Jean_GUERIN_2" target="_blank">Jean Guerin 2</a> 
    
    </div>
    """,
        unsafe_allow_html=True,
    )

st.divider()

on = st.toggle(
    "I'm happy to contribute to this project and agree to anonymously submit a translation template to help train GorgsGPT (required)."
)

troll = st.toggle(
    "I want to receive analytics at least three times a day on the evolution of GorgsGUT™ imbalanced accuracy (even though, honestly, no one should want that)."
)

if troll:
    st.toggle(
        "I certify being over 18 (disabled if you are not yet registered or if you can't prove it)",
        disabled=True,
    )

if not on:

    st.divider()

    st.image(
        "https://github.com/DidierFlamm/GorgsGPT/raw/main/data/M.ENSAM.H.A.png",
        caption="© 226 MEHA by GorgsGPT",
    )

    st.link_button(
        "Order now your MAGA Baseball Cap ! 🤑",
        "https://www.amazon.fr/Chapeau-cheveux-R%C3%A9glable-Casquette-baseball/dp/B0CX9J72ZK/?th=1&psc=1",
        use_container_width=True,
        icon="⚾",
    )

else:

    st.subheader("Setup your submission:", divider=True)

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
            """🏳️ Le carn's des trad's du vénérable Dav's est lar's étal's. ⁉️  
🇫🇷 Le carnet traditionnel de 'David l`énervé' est très validable. ✅

"""
        )

        st.write("Evaluate the green patterns above:")
        selected_1 = st.feedback("thumbs", key="f1")
        if selected_1 is not None:
            if selected_1 == 1:
                st.write("❤️‍🔥")
            else:
                st.text_input(
                    "Seriously ? Offer a better translation template if you are as fluent as you pretend to be... You, Mr. Know-it-all PG 😤",
                    "Your translation suggestion:",
                    key="input_1",
                )

        st.divider()

        st.code(
            """🏳️‍🌈 The administration of engineering school Arts & Métiers teaches solidarity through student hazing. ⁉️
🏁 La Strass des Trad's est lar's fratern's, bel eff's pour cette Usin's à Gad'z. ✅
"""
        )
        st.write("Evaluate the green patterns above:")
        selected_2 = st.feedback("thumbs", key="f2")

        if selected_2 is not None:
            if selected_2 == 1:
                st.write("❤️‍🔥")
            else:
                st.text_input(
                    "You dit it again ? ... You, Mr. Know-it-all PG 🤬",
                    "Your translation suggestion:",
                    key="input_2",
                )

    st.subheader("Scan a new personal translation template:", divider=True)

    enable = st.checkbox("Enable camera")
    picture = st.camera_input("Scan a document", disabled=not enable)

    if picture:
        st.write("Review your scan:")
        st.image(picture)
        if st.button("Upload your scan", icon="📤"):
            with st.spinner("Wait for it...", show_time=True):
                time.sleep(5)
            st.error(
                """Oops! A translation error was detected in your template. Please review it and try again later.""",
                icon="😬",
            )

    st.subheader("Record a new personal translation template:", divider=True)
    audio_value = st.audio_input("Record a voice message")
    if audio_value:
        st.write("Review your record:")
        st.audio(audio_value)
        st.caption(
            "⚠️ You can adjust the playback speed or freely download your own recording by clicking on the three-dot menu located on the right side of the audio bar."
        )

        if st.button("Upload your record", icon="📤"):
            with st.spinner("Wait for it...", show_time=True):
                time.sleep(5)
            st.error(
                """Oops! A translation error was detected in your template. Please review it and try again later.""",
                icon="😬",
            )

    st.divider()

    st.subheader(":violet[🚧 French to Argad'z 🚧]")

    french = st.text_input(
        "Prompt en Français",
        value="J'entrave que dalle à cette app's, y a rien qui marche ou quoi ? Explique-moi comment ça fonctionne ton truc au lieu de nous prendre la tête, stp 🤗",
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

    st.write("Evaluate this transcription:")
    st.feedback("thumbs", key="f3")

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

    st.write("Evaluate this transcription:")
    st.feedback("thumbs", key="f4")

st.divider()  ############################################################################################


st.subheader(":blue[💙 Rate this app's]")

sentiment_mapping = [
    "💬 L'app's foüt la méga gerbe au phi's !",
    "💬 Keud's de fratern's pour l'app's !",
    "💬 C'est le phi's qui te fait payser ?",
    "💬 Bel eff's du phi's à l'app's !",
    "💬 Le phi's HM lar's l'app's !",
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
