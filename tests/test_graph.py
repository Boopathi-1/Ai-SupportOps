
from langchain_core.messages import HumanMessage
from app.agents.graph import app


result = app.invoke(
    {
        "messages": [
            HumanMessage(
                content="Show me my active orders and payment history"
            )
        ],
        "user_id": 1,
        "next_agent": "finish",
        "completed_specialists": [],
    },
    config={
        "recursion_limit": 15
    },
)

print("\n--- FINAL RESPONSE ---")
print(result["messages"][-1].content)

print("\n--- COMPLETED SPECIALISTS ---")
print(result["completed_specialists"])
