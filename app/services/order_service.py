from app.repositories.order_repository import OrderRepository


ACTIVE_STATUSES = {
    "PROCESSING",
    "CONFIRMED",
    "SHIPPED",
    "OUT_FOR_DELIVERY",
    "DELAYED",
}


class OrderService:

    def __init__(self, repository: OrderRepository):
        self.repository = repository

    def get_customer_orders(self, user_id: int) -> list:
        return self.repository.get_orders_by_user(user_id)

    def get_active_orders(self, user_id: int) -> list:
        orders = self.repository.get_orders_by_user(user_id)

        return [
            order
            for order in orders
            if order.status in ACTIVE_STATUSES
        ]

    def get_order_summary(self, user_id: int) -> list[dict]:
        orders = self.repository.get_orders_by_user(user_id)

        summaries = []

        for order in orders:
            summaries.append(
                {
                    "order_id": order.id,
                    "status": order.status,
                    "total_amount": float(order.total_amount),
                    "ordered_at": order.ordered_at,
                    "item_count": len(order.items),
                    "payment_count": len(order.payments),
                }
            )

        return summaries