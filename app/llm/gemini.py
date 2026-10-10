from google import genai
from google.genai import types
from app.llm.tool_definitions import all_tools
from app.core.config import settings

client = genai.Client(
    api_key = settings.gemini_api_key
)

def ask_gemini(message: str)->str:
    response = client.models.generate_content(
        model = "gemini-2.5-flash",
        contents = message,
        config = types.GenerateContentConfig(
            tools=[all_tools]
        )
    )
    return response
