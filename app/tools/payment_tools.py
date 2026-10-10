from app.db.database import SessionLocal
from app.repositories.payment_repository import PaymentRepository
from app.services.payment_service import PaymentService
from langchain_core.tools import tool
@tool
def get_payment_history(user_id:int)-> list[dict]:
    """
    Retreive payment history belonging to specific customer
    """

    session = SessionLocal()

    try:
        repository = PaymentRepository(session)
        service = PaymentService(repository)

        payments = service.get_payment_history(user_id)

        return payments
    
    finally:
        session.close()
@tool
def get_order_payment_status(user_id: int,order_id: int)->list[dict]:
    """
    Retreive payment status of specific order of specific customer
    """

    session = SessionLocal()

    try:
        repository = PaymentRepository(session)
        service = PaymentService(repository)

        status = service.get_order_payment_status(user_id,order_id)

        return status
    finally:
        session.close()