import os
import streamlit as st


def account():
    st.markdown(
        """
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #f0f2f6;
                color: #333;
            }
            .container {
                max-width: 800px;
                margin: auto;
                padding: 20px;
                background: rgba(255, 255, 255, 0.8);
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            }
            .header {
                text-align: center;
                padding-bottom: 20px;
            }
            .header h1 {
                color: #007BFF;
                margin-bottom: 0;
            }
            .section {
                margin-bottom: 20px;
            }
            .section h2 {
                color: #007BFF;
                border-bottom: 2px solid #007BFF;
                padding-bottom: 10px;
            }
            .section p {
                margin: 10px 0;
            }
        </style>
        <div class="container">
            <div class="header">
                <h1>Account</h1>
                <p>Here you can change your account settings.</p>
            </div>
            <div class="section">
                <h2>Future Plans</h2>
                <p>Later, we'll give users the chance to use the most popular LLMs such as various ChatGPT flavors, Gemini flavors, etc. For now, we're only using Gemini 1.5 Flash.</p>
            </div>
            <div class="section">
                <h2>API Key Integration</h2>
                <p>In the future, users will be able to use their own API keys to access these models for various tasks supported by this application.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
