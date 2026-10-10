from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.payment import Payment
from app.models.order import Order


class PaymentRepository:
    def __init__(self,session: Session):
        self.session = session
    def get_payments_by_user(self,user_id: int) -> list[Payment]:
        statement = (
            select(Payment)
            .join(Order)
            .where(Order.user_id == user_id)
            .order_by(Payment.created_at.desc())
        )

        result = self.session.scalars(statement)

        return list(result)

    def get_payments_for_order(self,user_id,order_id) -> list[Payment]:
        statement = (
            select(Payment)
            .join(Order)
            .where(
                Order.user_id==user_id,
                Order.id==order_id,
            )
            
        )

        result = self.session.scalars(statement)

        return list(result)