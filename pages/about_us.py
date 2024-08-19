import streamlit as st


def about_us():
    st.markdown(
        """
        <style>
            body {
                font-family: Arial, sans-serif;
                color: #333;
                line-height: 1.6;
            }
            .container {
                max-width: 800px;
                margin: auto;
                padding: 20px;
            }
            .section {
                margin-bottom: 40px;
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
            <div class="section">
                <h2>About Us</h2>
                <p>We are Group 10B for the course, Data Science and Machine Learning from the University of Mines and Technology, Electrical and Electronics Engineering Department. Soon to be class of 2025.</p>
            </div>
            <div class="section">
                <h2>Our Project</h2>
                <p>We developed this project for the end of course project work. Our project showcases the skills and knowledge we have acquired throughout the course.</p>
            </div>
            <div class="section">
                <h2>Course Tutor</h2>
                <p>Our course tutor is Mr. Kobina Abakah Painstil, who has guided us through the concepts of Data Science and Machine Learning.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
