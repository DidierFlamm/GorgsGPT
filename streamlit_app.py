# -*- coding: utf-8 -*-
import streamlit as st

# set_page_config() can only be called once per app page, and must be called as the first Streamlit command in your script.
st.set_page_config(
    menu_items={
        "Get Help": None,
        "Report a bug": "mailto:contact@diveintodata.fr?subject=Reporting%20a%20bug%20in%20titanic-survival-predictor%20Streamlit%20app&body=OS%20(Windows,%20macOS,%20Linux,%20Android,%20iOS):%0ABrowser:%0ABug%20you%20encountered:%0A%0AThanks!",
        "About": """## GorgsGPT
© 2025 Didier Flamm  
✉️ [contact@diveintodata.fr](mailto:contact@diveintodata.fr) – 💬 [LinkedIn](https://www.linkedin.com/in/didier-flamm) – 📁 [Portfolio](https://share.streamlit.io/user/didierflamm)  
""",
    }
)

st.logo(
    "https://img.icons8.com/?size=100&id=s5NUIabJrb4C&format=png&color=000000",
    size="large",
)


ambiance = st.sidebar.radio(
    "Select ambiance",
    ("🔇 Silent mode", "👫 KIN 201", "💃 Strass Academy"),
    label_visibility="collapsed",
)

if ambiance.startswith("👫"):
    video_url = "https://www.youtube.com/watch?v=CJVtr9vUwCQ"
    st.sidebar.video(video_url, autoplay=True, muted=False)

    st.sidebar.markdown(
        """
    <div style='text-align: center; font-size: small; color: gray;'>
    © 2001 KIN 201
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

st.sidebar.divider()

st.sidebar.image(
    "https://github.com/DidierFlamm/GorgsGPT/raw/main/data/Amtradszaloeil.png"
)

st.image("https://github.com/DidierFlamm/GorgsGPT/raw/main/data/GorgsGPT.png")

st.write("French to Argad'z")

st.text_input(
    "Prompt en Français",
    key="french",
)

if st.button("Affole les Watts!"):
    st.write("🚧😬🚧")

st.divider()

st.write("Argad'z to French")

st.text_input(
    "Prompt en Argad'z",
    key="argadz",
)

if st.button("Keud's de Watts!"):
    st.write("🚧😅🚧")

st.divider()
