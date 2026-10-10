from app.tools.order_tools import get_customer_orders,get_active_orders


def main():
    orders = get_active_orders(1)

    print(f"Orders returned: {len(orders)}")

    for order in orders:
        print(
            f"Order #{order['order_id']} | "
            f"Status: {order['status']} | "
            f"Total: ₹{order['total_amount']} | ")
        for item in order["items"]:
            print(
                f"  - {item['product_name']} "
                f"x {item['quantity']}"
            )
        


if __name__ == "__main__":
    main()