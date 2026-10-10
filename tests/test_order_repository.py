from app.db.database import SessionLocal
from app.models.user import User
from app.repositories.order_repository import OrderRepository


def main():
    session = SessionLocal()

    try:
        # Find Surya
        user = (
            session.query(User)
            .filter(User.email == "surya@shopflow.dev")
            .first()
        )

        if not user:
            print("Surya not found")
            return

        repository = OrderRepository(session)

        orders = repository.get_orders_by_user(user.id)

        print(f"\nCustomer: {user.name}")
        print(f"User ID: {user.id}")
        print(f"Total orders: {len(orders)}")

        print("\nOrders:")

        for order in orders:
            print(
                f"Order #{order.id} | "
                f"Status: {order.status} | "
                f"Total: ₹{order.total_amount} | "
                f"Items: {len(order.items)} | "
                f"Payments: {len(order.payments)}"
            )

    finally:
        session.close()


if __name__ == "__main__":
    main()