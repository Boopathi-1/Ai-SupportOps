from google.genai import types

from app.llm.gemini import ask_gemini, client
from app.llm.tool_definitions import all_tools
from app.tools.dispatcher import execute_tool


def main():
    current_user_id = 1

    user_message = "Show me my active orders"

    # Keep the conversation history
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=user_message)
            ],
        )
    ]

    # -----------------------------
    # 1. Ask Gemini
    # -----------------------------
    response = ask_gemini(user_message)

    function_call = None

    for part in response.candidates[0].content.parts:
        if part.function_call:
            function_call = part.function_call
            break

    if function_call is None:
        print("Gemini did not request a tool.")
        print(response.text)
        return

    print("Tool Name:", function_call.name)
    print("Tool Args:", function_call.args)

    # -----------------------------
    # 2. Execute backend tool
    # -----------------------------
    result = execute_tool(
        function_call,
        current_user_id,
    )

    print("\nTool Result:")
    print(result)

    # -----------------------------
    # 3. Add Gemini's tool call
    # -----------------------------
    contents.append(
        response.candidates[0].content
    )

    # -----------------------------
    # 4. Send tool result to Gemini
    # -----------------------------
    function_response_part = types.Part.from_function_response(
        name=function_call.name,
        response={
            "result": result
        },
        
    )

    contents.append(
        types.Content(
            role="user",
            parts=[function_response_part],
        )
    )

    # -----------------------------
    # 5. Ask Gemini for final answer
    # -----------------------------
    final_response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=contents,
        config=types.GenerateContentConfig(
            tools=[all_tools]
        ),
    )

    print("\nFinal Gemini Response:")
    print(final_response.text)


if __name__ == "__main__":
    main()