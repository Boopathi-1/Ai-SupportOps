from app.tools.order_tools import (
    get_customer_orders,
    get_active_orders,
)

from app.tools.payment_tools import (
    get_payment_history,
    get_order_payment_status,
)


TOOL_DISPATCHER = {
    "get_customer_orders": get_customer_orders,
    "get_active_orders": get_active_orders,
    "get_payment_history": get_payment_history,
    "get_order_payment_status": get_order_payment_status,
}

def execute_tool(function_call, user_id: int):
    tool_name = function_call.name
    arguments = function_call.args

    tool = TOOL_DISPATCHER.get(tool_name)

    if tool is None:
        raise ValueError(f"Unknown tool: {tool_name}")

    if tool_name == "get_payment_history":
        return tool(user_id)
    elif tool_name == "get_active_orders":
        return tool(user_id)

    return tool(**arguments)