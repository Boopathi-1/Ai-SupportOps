from app.repositories.payment_repository import PaymentRepository


class PaymentService:

    def __init__(self, repository: PaymentRepository):
        self.repository = repository

    def get_payment_history(self, user_id: int):
        payment_history = self.repository.get_payments_by_user(user_id)

        return [
            {
                "order_id": payment.order_id,
                "amount": float(payment.amount),
                "status": payment.status,
                "payment_method": payment.payment_method,
                "created_at": payment.created_at,
            }
            for payment in payment_history
        ]

    def get_order_payment_status(
        self,
        user_id: int,
        order_id: int,
    ):
        payments = self.repository.get_payments_for_order(
            user_id,
            order_id,
        )

        return [
            {
                "order_id": payment.order_id,
                "amount": float(payment.amount),
                "status": payment.status,
                "payment_method": payment.payment_method,
                "created_at": payment.created_at,
            }
            for payment in payments
        ]