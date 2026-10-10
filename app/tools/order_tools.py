from app.db.database import SessionLocal
from app.repositories.order_repository import OrderRepository
from app.services.order_service import OrderService

def get_customer_orders(user_id: int) -> list[dict]:
    """
    Retrieve all orders belonging to a specific customer.
    """

    session = SessionLocal()

    try:
        repository = OrderRepository(session)
        service = OrderService(repository)

        orders = service.get_order_summary(user_id)

        return orders

    finally:
        session.close()

def get_active_orders(user_id: int) -> list[dict]:
    """
    Retreive active orders belonging to specific customer.
    """
    session = SessionLocal()
    
    try:
        repository = OrderRepository(session)
        service = OrderService(repository)

        orders = service.get_active_orders(user_id)

        return[
            {
                "order_id":order.id,
                "status":order.status,
                "total_amount":float(order.total_amount),
                "ordered_at":order.ordered_at,
                "items":[
                    {
                        "product_name":item.product.name,
                        "quantity":item.quantity,
                        "unit_price":float(item.unit_price),
                    }
                    for item in order.items
                ],
            }

            for order in orders
        ]
    finally:
        session.close()

