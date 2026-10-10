from app.db.database import SessionLocal
from app.models.user import User
from app.repositories.order_repository import OrderRepository
from app.services.order_service import OrderService


def main():
    session = SessionLocal()

    try:
        user = (
            session.query(User)
            .filter(User.email == "surya@shopflow.dev")
            .first()
        )

        repository = OrderRepository(session)
        service = OrderService(repository)

        active_orders = service.get_active_orders(user.id)

        print(f"Customer: {user.name}")
        print(f"Active orders: {len(active_orders)}")

        for order in active_orders:
            print(
                f"Order #{order.id} | "
                f"Status: {order.status} | "
                f"Total: ₹{order.total_amount}"
            )

    finally:
        session.close()


if __name__ == "__main__":
    main()