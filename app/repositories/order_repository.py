from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload

from app.models.order import Order


class OrderRepository:

    def __init__(self, session: Session):
        self.session = session

    def get_orders_by_user(self, user_id: int) -> list[Order]:
        statement = (
            select(Order)
            .where(Order.user_id == user_id)
            .options(
                selectinload(Order.items),
                selectinload(Order.payments),
            )
            .order_by(Order.ordered_at.desc())
        )

        result = self.session.scalars(statement)

        return list(result)
    