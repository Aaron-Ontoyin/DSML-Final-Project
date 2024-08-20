import streamlit as st
import hydralit_components as hc

from pages import home, exp_play, about_us, account, content_summariser


st.set_page_config(
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)

menu_data = [
    {
        "icon": "bi bi-arrow-down-left",
        "label": "Content Summariser",
        "ttip": "Summarizer PDFs, Youtube videos or Websites",
    },
    {
        "icon": "bi bi-hand-index-thumb",
        "label": "Ex-P",
        "ttip": "Experimental play! Gesture Controls",
    },
    {"icon": "bi bi-collection", "label": "About Us"},
]

st.text("")
menu_id = hc.nav_bar(
    menu_definition=menu_data,
    override_theme={"txc_inactive": "#FFFFFF", "menu_background": "blue"},
    home_name={"id": "home", "label": "Home", "icon": "fa fa-home"},
    login_name={
        "id": "account",
        "label": "Account",
        "icon": "fa fa-user-circle",
        "ttip": "Account settings",
    },
    hide_streamlit_markers=True,
    sticky_nav=True,
    sticky_mode="pinned",
)


def main():
    match menu_id:
        case "home":
            home()
        case "account":
            account()
        case "Content Summariser":
            content_summariser()
        case "Ex-P":
            exp_play()
        case "About Us":
            about_us()


if __name__ == "__main__":
    main()
