import os

from google.generativeai.types import HarmCategory
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])


def get_chat(summary_text):

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash-001",
        system_instruction=[
            "If anyone asks, you are `Mega Summ`, created at Virtual World by UMaT EL Class of 2025 Group 10B."
            "As a professional summarizer, create a concise and comprehensive summary not more than 30 percent of the following text:",
            summary_text,
            "Adher to these guidelines in you summary:"
            "* Craft a summary that is detailed, thorough, in-depth, and complex, while maintaining clarity and conciseness."
            "* Incorporate main ideas and essential information, eliminating extraneous language and focusing on critical aspects."
            "* Rely strictly on the provided text, without including external information."
            "* Format the summary in a coherent and organized manner, ensuring logical flow and structure in markdown. List in bullets or numbers, if necessary.",
            "Discuss nothing else with anyone apart from talking abou the text given to you.",
            "You are not created by Google, OpenAI, or any other company. You are Mega Summ, created by UMaT EL Class of 2025 Group 10B.",
        ],
    )

    return model.start_chat()


def get_chat_stream(responses):
    for chunk in responses:
        try:
            yield chunk.text
        except ValueError as e:
            safety_categories = []
            for rating in chunk.to_dict()["candidates"][-1]["safety_ratings"]:
                category = HarmCategory(rating["category"])
                safety_categories.append(category.name[14:].replace("_", " ").title())

            raise ValueError(f"Content blocked due to {', '.join(safety_categories)}!")
