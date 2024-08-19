import streamlit as st
import hydralit_components as hc


def home():
    st.html(
        """
        <style>
        .container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 50vh;
            background-color: aliceblue;
            padding: 24px;
        }
        
        .title {
            font-size: 48px;
            font-weight: bold;
            color: #333333;
            margin-bottom: 24px;
        }
        
        .description {
            font-size: 24px;
            color: #666666;
            margin-bottom: 48px;
        }

        .contact {
            font-size: 18px;
            color: #999999;
            margin-bottom: 12px;
        }
        
        .contact-link {
            font-size: 18px;
            color: blue;
            text-decoration: none;
        }
        </style>

        <div class="container">
            <h1 class="title">Welcome to Light Skim!</h1>

            <p class="description">Use the Navbar to navigate to different pages.</p>
            <div class="contact">
                You can reach out <a class="contact-link"  href="http://aaronontoyin.tech" target="_blank">here</a>.
            </div>
        </div>
        """
    )

    cols = st.columns(3)
    with cols[0]:
        hc.info_card(
            title="Summarizer",
            content="Summarize PDFs, Youtube videos or Websites",
            sentiment="good",
            bar_value=95,
        )
    with cols[1]:
        hc.info_card(
            title="Experimental play!",
            content="Control Appliaction with Gesture using Deep Learning",
            sentiment="good",
            bar_value=75,
        )
    with cols[2]:
        hc.info_card(
            title="About Us",
            content="Learn more about the team behind the app",
            sentiment="neutral",
            bar_value=90,
        )
