from google import genai
from google.genai import types
from app.llm.gemini import client
from app.agents.tool_definitions import order_tools
from app.tools.dispatcher import execute_tool


def run_order_agent(user_request: str,user_id: int):
    contents = [
        types.Content(
            role="user",
            parts=[types.Part(text=user_request)]
        )
    ]

    response = client.models.generate_content(
        model = "gemini-2.5-flash",
        contents = contents,
        config = types.GenerateContentConfig(
            tools=[order_tools]
        )
    )

    if not response.function_calls:
        return response.text

    contents.append(response.candidates[0].content)

    for function_call in response.function_calls:
        result = execute_tool(function_call, user_id)

        contents.append(
            types.Content(
                role="tool",
                parts=[
                    types.Part.from_function_response(
                        name=function_call.name,
                        response={"result": result}
                    )
                ]
            )
        )
            

    
    

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=contents,
        config=types.GenerateContentConfig(
            tools=[order_tools]
        )
    )

    return response.text




# response = run_order_agent("Show me my active orders")
# print(response)