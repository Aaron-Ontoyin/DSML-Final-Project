from google.generativeai.types import HarmCategory, HarmBlockThreshold

import streamlit as st
import hydralit_components as hc
from pypdf import PdfReader

from utils.llms.gemini import get_chat, get_chat_stream
from utils.youtube.transcript import get_transcript
from utils.websites.web_scrapper import get_site_content


option_data = [
    {"icon": "bi bi-file-earmark-text", "label": "PDF---- Summarizer"},
    {"icon": "bi bi-youtube", "label": "Youtube Summarizer"},
    {"icon": "bi bi-globe", "label": "Website Summarizer"},
]

over_theme = {
    "txc_inactive": "black",
    "menu_background": "aliceblue",
    "txc_active": "white",
    "option_active": "blue",
}


def content_summariser():
    menu_col, _, _, _, upload_col = st.columns(5)
    with menu_col:
        tool_option = hc.option_bar(
            option_definition=option_data,
            title="Choose a tool",
            key="PrimaryOption",
            override_theme=over_theme,
            horizontal_orientation=False,
        )

    with upload_col:
        if st.session_state.get("LLM_API_KEY"):
            content_form = st.form(key="content_form")
            uploaded_file = youtube_url = website_url = None
            if tool_option == "PDF---- Summarizer":
                uploaded_file = content_form.file_uploader(
                    f"Upload a PDF file:", type=["pdf"]
                )
            elif tool_option == "Youtube Summarizer":
                youtube_url = content_form.text_input(f"Enter a Youtube Video ID: ")
            elif tool_option == "Website Summarizer":
                website_url = content_form.text_input(f"Enter a Website URL: ")
        else:
            st.warning(
                "Please provide your Gemini API key in the `aacounts` section to use this tool."
            )
            return

    if content_form.form_submit_button("Load content"):
        if uploaded_file:
            with st.spinner("Extracting text..."):
                pdf_reader = PdfReader(uploaded_file)
                summary_text = f"This is a PDF file named, {uploaded_file.name}.\n\n"
                for page in pdf_reader.pages:
                    summary_text += page.extract_text()

                if len(summary_text) > 40000:
                    st.warning(
                        "The text is too long. Please try a shorter document or (provide your own API key)."
                    )
                    return
        elif youtube_url:
            with st.spinner("Taking a look at the video..."):
                summary_text = (
                    f"This is the transcript of the Youtube video at {youtube_url}.\n\n"
                )
                try:
                    transcript = get_transcript(youtube_url)
                except ValueError as e:
                    st.warning(
                        "I'm sorry, I'm unable to watch this video. No transcript found."
                    )
                    return

                for line in transcript:
                    summary_text += f"{line['text']}\n"
        elif website_url:
            with st.spinner("Reading site content..."):
                summary_text = (
                    f"This is the content of the website at {website_url}.\n\n"
                )
                website_content = get_site_content(website_url)
                if not website_content:
                    st.warning(
                        f"Could not retrieve any content from the {website_url}. Be sure to provide a valid URL."
                    )
                summary_text += website_content
        else:
            st.info(
                f"You have selected `{tool_option}`. Please provide a {'file' if tool_option == 'PDF---- Summarizer' else 'URL'}."
            )
            return
        st.session_state.chat = get_chat(summary_text)
        st.session_state.messages = []
    elif "chat" in st.session_state:
        pass
    else:
        st.info(
            f"You have selected `{tool_option}`. Please provide a {'file' if tool_option == 'PDF---- Summarizer' else 'URL'}."
        )
        return

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    chat = st.session_state.chat
    uploaded_file_name = uploaded_file.name if uploaded_file else None
    if prompt := st.chat_input(
        f"Ask me about or to summarize {uploaded_file_name or youtube_url or website_url}..."
    ):
        with st.chat_message("user"):
            st.markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.chat_message("assistant"):
            try:
                responses = chat.send_message(
                    prompt,
                    safety_settings={
                        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_ONLY_HIGH,
                        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_ONLY_HIGH,
                        HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_ONLY_HIGH,
                        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_ONLY_HIGH,
                    },
                    stream=True,
                )
            except Exception as e:
                if "API_KEY_INVALID" in str(e):
                    st.error(
                        "Your Gemini API key is invalid. Please provide a valid API key in the `accounts` section."
                    )
                    st.session_state.pop("chat", None)
                    st.session_state.pop("LLM_API_KEY", None)
                    return

            try:
                full_response = st.write_stream(get_chat_stream(responses))
            except ValueError as e:
                st.error(str(e))
                return
            st.session_state.messages.append(
                {"role": "assistant", "content": full_response}
            )
