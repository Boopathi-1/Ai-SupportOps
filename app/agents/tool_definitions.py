from google.genai import types


get_payment_history_tool = types.FunctionDeclaration(
    name="get_payment_history",
    description="Retrieve the payment history of the current customer.",
    parameters=types.Schema(
        type="OBJECT",
        properties={},
    ),
)


get_active_orders_tool = types.FunctionDeclaration(
    name="get_active_orders",
    description="Retrieve all active orders belonging to the current customer.",
    parameters=types.Schema(
        type="OBJECT",
        properties={},
    ),
)


payment_tools = types.Tool(
    function_declarations=[
        get_payment_history_tool,
    ]
)


order_tools = types.Tool(
    function_declarations=[
        get_active_orders_tool,
    ]
)


all_tools = types.Tool(
    function_declarations=[
        get_payment_history_tool,
        get_active_orders_tool,
    ]
)