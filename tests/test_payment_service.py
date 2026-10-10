from app.db.database import SessionLocal
from app.repositories.payment_repository import PaymentRepository
from app.services.payment_service import PaymentService


def test_payment_service():
    session = SessionLocal()

    try:
        repository = PaymentRepository(session)
        service = PaymentService(repository)

        print("\n=== PAYMENT HISTORY: SURYA ===")
        payment_history = service.get_payment_history(1)

        for payment in payment_history:
            print(payment)

        print("\n=== ORDER #7 PAYMENT STATUS ===")
        order_payments = service.get_order_payment_status(
            user_id=1,
            order_id=7,
        )

        for payment in order_payments:
            print(payment)

    finally:
        session.close()


if __name__ == "__main__":
    test_payment_service()