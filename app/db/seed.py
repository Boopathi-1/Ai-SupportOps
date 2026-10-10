from decimal import Decimal

from sqlalchemy import select
from app.db.database import SessionLocal
from datetime import datetime, timedelta, timezone

from app.models import (
    User,
    Product,
    Order,
    OrderItem,
    Payment,
)
USERS = [
    {
        "name": "Surya",
        "email": "surya@shopflow.dev",
        "password_hash": "demo_hash_surya",
        "role": "customer",
    },
    {
        "name": "Arun",
        "email": "arun@shopflow.dev",
        "password_hash": "demo_hash_arun",
        "role": "customer",
    },
    {
        "name": "Priya",
        "email": "priya@shopflow.dev",
        "password_hash": "demo_hash_priya",
        "role": "customer",
    },
    {
        "name": "Karthik",
        "email": "karthik@shopflow.dev",
        "password_hash": "demo_hash_karthik",
        "role": "customer",
    },
    {
        "name": "Divya",
        "email": "divya@shopflow.dev",
        "password_hash": "demo_hash_divya",
        "role": "customer",
    },
    {
        "name": "ShopFlow Support",
        "email": "support@shopflow.dev",
        "password_hash": "demo_hash_support",
        "role": "admin",
    },
]


PRODUCTS = [
    {
        "name": "Nike Air Max",
        "description": "Comfortable everyday sneakers with lightweight cushioning.",
        "price": Decimal("7499.00"),
        "stock": 42,
    },
    {
        "name": "Bluetooth Headphones",
        "description": "Wireless over-ear headphones with active noise cancellation.",
        "price": Decimal("3499.00"),
        "stock": 65,
    },
    {
        "name": "Laptop Stand",
        "description": "Adjustable aluminum laptop stand for desk setups.",
        "price": Decimal("1899.00"),
        "stock": 38,
    },
    {
        "name": "Mechanical Keyboard",
        "description": "Compact mechanical keyboard with tactile switches.",
        "price": Decimal("4299.00"),
        "stock": 27,
    },
    {
        "name": "Wireless Mouse",
        "description": "Ergonomic wireless mouse with adjustable DPI.",
        "price": Decimal("1299.00"),
        "stock": 80,
    },
    {
        "name": "USB-C Hub",
        "description": "Multi-port USB-C hub with HDMI, USB and SD card support.",
        "price": Decimal("2199.00"),
        "stock": 51,
    },
    {
        "name": "Smart Watch",
        "description": "Fitness-focused smartwatch with heart-rate and activity tracking.",
        "price": Decimal("5999.00"),
        "stock": 31,
    },
    {
        "name": "Running Shoes",
        "description": "Lightweight running shoes designed for daily training.",
        "price": Decimal("3299.00"),
        "stock": 44,
    },
    {
        "name": "Backpack",
        "description": "Water-resistant laptop backpack with multiple compartments.",
        "price": Decimal("2499.00"),
        "stock": 57,
    },
    {
        "name": "Webcam",
        "description": "Full HD webcam suitable for meetings and streaming.",
        "price": Decimal("2799.00"),
        "stock": 24,
    },
    {
        "name": "Power Bank",
        "description": "20000mAh fast-charging portable power bank.",
        "price": Decimal("1699.00"),
        "stock": 73,
    },
    {
        "name": "Desk Lamp",
        "description": "LED desk lamp with adjustable brightness and color temperature.",
        "price": Decimal("1199.00"),
        "stock": 46,
    },
    {
        "name": "Water Bottle",
        "description": "Insulated stainless-steel bottle suitable for everyday use.",
        "price": Decimal("899.00"),
        "stock": 92,
    },
    {
        "name": "Yoga Mat",
        "description": "Non-slip exercise mat suitable for yoga and home workouts.",
        "price": Decimal("999.00"),
        "stock": 61,
    },
    {
        "name": "Phone Stand",
        "description": "Adjustable desktop phone stand for video calls and viewing.",
        "price": Decimal("599.00"),
        "stock": 105,
    },
]


def seed_users(session):
    created = 0

    for data in USERS:
        existing = session.scalar(
            select(User).where(User.email == data["email"])
        )

        if existing:
            continue

        session.add(User(**data))
        created += 1

    session.flush()

    print(f"Users: created {created}, total seed users {len(USERS)}")


def seed_products(session):
    created = 0

    for data in PRODUCTS:
        existing = session.scalar(
            select(Product).where(Product.name == data["name"])
        )

        if existing:
            continue

        session.add(Product(**data))
        created += 1

    session.flush()

    print(f"Products: created {created}, total seed products {len(PRODUCTS)}")

def seed_orders(session):
    users = {
        user.name: user
        for user in session.query(User).all()
    }

    products = {
        product.name: product
        for product in session.query(Product).all()
    }

    order_definitions = [
        # -------------------------
        # SURYA
        # -------------------------
        {
            "customer": "Surya",
            "status": "DELIVERED",
            "days_ago": 120,
            "items": [
                ("Nike Air Max", 1, Decimal("7299.00")),
                ("Water Bottle", 1, Decimal("849.00")),
            ],
        },
        {
            "customer": "Surya",
            "status": "DELIVERED",
            "days_ago": 90,
            "items": [
                ("Mechanical Keyboard", 1, Decimal("3999.00")),
                ("Wireless Mouse", 1, Decimal("1199.00")),
            ],
        },
        {
            "customer": "Surya",
            "status": "DELIVERED",
            "days_ago": 60,
            "items": [
                ("Backpack", 1, Decimal("2299.00")),
            ],
        },
        {
            "customer": "Surya",
            "status": "SHIPPED",
            "days_ago": 5,
            "items": [
                ("Bluetooth Headphones", 1, Decimal("3299.00")),
            ],
        },
        {
            "customer": "Surya",
            "status": "OUT_FOR_DELIVERY",
            "days_ago": 2,
            "items": [
                ("Power Bank", 1, Decimal("1599.00")),
                ("Phone Stand", 2, Decimal("549.00")),
            ],
        },
        {
            "customer": "Surya",
            "status": "DELAYED",
            "days_ago": 8,
            "items": [
                ("Smart Watch", 1, Decimal("5799.00")),
            ],
        },
        {
            "customer": "Surya",
            "status": "PROCESSING",
            "days_ago": 1,
            "items": [
                ("Laptop Stand", 1, Decimal("1799.00")),
                ("USB-C Hub", 1, Decimal("2099.00")),
            ],
        },
        {
            "customer": "Surya",
            "status": "CANCELLED",
            "days_ago": 30,
            "items": [
                ("Webcam", 1, Decimal("2699.00")),
            ],
        },

        # -------------------------
        # ARUN
        # -------------------------
        {
            "customer": "Arun",
            "status": "DELIVERED",
            "days_ago": 150,
            "items": [
                ("Running Shoes", 1, Decimal("3099.00")),
            ],
        },
        {
            "customer": "Arun",
            "status": "DELIVERED",
            "days_ago": 75,
            "items": [
                ("Desk Lamp", 2, Decimal("1099.00")),
                ("Phone Stand", 1, Decimal("549.00")),
            ],
        },
        {
            "customer": "Arun",
            "status": "SHIPPED",
            "days_ago": 4,
            "items": [
                ("Nike Air Max", 1, Decimal("7399.00")),
            ],
        },
        {
            "customer": "Arun",
            "status": "DELIVERED",
            "days_ago": 20,
            "items": [
                ("Bluetooth Headphones", 1, Decimal("3399.00")),
                ("Power Bank", 1, Decimal("1599.00")),
            ],
        },

        # -------------------------
        # PRIYA
        # -------------------------
        {
            "customer": "Priya",
            "status": "DELIVERED",
            "days_ago": 100,
            "items": [
                ("Yoga Mat", 1, Decimal("899.00")),
            ],
        },
        {
            "customer": "Priya",
            "status": "PROCESSING",
            "days_ago": 1,
            "items": [
                ("Smart Watch", 1, Decimal("5899.00")),
            ],
        },
        {
            "customer": "Priya",
            "status": "SHIPPED",
            "days_ago": 3,
            "items": [
                ("Backpack", 1, Decimal("2399.00")),
                ("Water Bottle", 1, Decimal("849.00")),
            ],
        },
        {
            "customer": "Priya",
            "status": "OUT_FOR_DELIVERY",
            "days_ago": 1,
            "items": [
                ("Wireless Mouse", 1, Decimal("1199.00")),
            ],
        },
        {
            "customer": "Priya",
            "status": "RETURNED",
            "days_ago": 45,
            "items": [
                ("Mechanical Keyboard", 1, Decimal("4099.00")),
            ],
        },

        # -------------------------
        # KARTHIK
        # -------------------------
        {
            "customer": "Karthik",
            "status": "DELIVERED",
            "days_ago": 180,
            "items": [
                ("Laptop Stand", 1, Decimal("1699.00")),
            ],
        },
        {
            "customer": "Karthik",
            "status": "DELIVERED",
            "days_ago": 110,
            "items": [
                ("Webcam", 1, Decimal("2599.00")),
                ("USB-C Hub", 1, Decimal("1999.00")),
            ],
        },
        {
            "customer": "Karthik",
            "status": "PROCESSING",
            "days_ago": 2,
            "items": [
                ("Mechanical Keyboard", 1, Decimal("4199.00")),
                ("Wireless Mouse", 1, Decimal("1199.00")),
            ],
        },
        {
            "customer": "Karthik",
            "status": "DELIVERED",
            "days_ago": 25,
            "items": [
                ("Power Bank", 1, Decimal("1599.00")),
            ],
        },

        # -------------------------
        # DIVYA
        # -------------------------
        {
            "customer": "Divya",
            "status": "DELIVERED",
            "days_ago": 140,
            "items": [
                ("Running Shoes", 1, Decimal("3199.00")),
            ],
        },
        {
            "customer": "Divya",
            "status": "SHIPPED",
            "days_ago": 5,
            "items": [
                ("Smart Watch", 1, Decimal("5799.00")),
            ],
        },
        {
            "customer": "Divya",
            "status": "DELAYED",
            "days_ago": 9,
            "items": [
                ("Bluetooth Headphones", 1, Decimal("3199.00")),
                ("Phone Stand", 1, Decimal("549.00")),
            ],
        },
        {
            "customer": "Divya",
            "status": "PROCESSING",
            "days_ago": 2,
            "items": [
                ("Yoga Mat", 1, Decimal("949.00")),
                ("Water Bottle", 1, Decimal("849.00")),
            ],
        },
        {
            "customer": "Divya",
            "status": "DELIVERED",
            "days_ago": 35,
            "items": [
                ("Backpack", 1, Decimal("2299.00")),
            ],
        },
    ]

    created = 0
    seed_now = datetime(2026, 10, 3, 12, 0, 0, tzinfo=timezone.utc)
    for definition in order_definitions:
        customer = users[definition["customer"]]

        # Stable identification for idempotency:
        # customer + ordered date + status + first product
        ordered_at = seed_now - timedelta(
                    days=definition["days_ago"]
        )
        

        existing = (
            session.query(Order)
            .filter(
                Order.user_id == customer.id,
                Order.ordered_at == ordered_at,
            )
            .first()
        )

        if existing:
            continue

        total = sum(
            quantity * unit_price
            for _, quantity, unit_price in definition["items"]
        )

        order = Order(
            user_id=customer.id,
            status=definition["status"],
            total_amount=total,
            ordered_at=ordered_at,
            expected_delivery=(
                ordered_at + timedelta(days=5)
                if definition["status"] not in ["CANCELLED", "RETURNED"]
                else None
            ),
        )

        session.add(order)
        session.flush()

        for product_name, quantity, unit_price in definition["items"]:
            product = products[product_name]

            item = OrderItem(
                order_id=order.id,
                product_id=product.id,
                quantity=quantity,
                unit_price=unit_price,
            )

            session.add(item)

        created += 1

    session.flush()

    print(f"Orders: created {created}, total definitions {len(order_definitions)}")

def seed_payments(session):
    orders = session.query(Order).all()

    created = 0

    for order in orders:
        # Skip if this order already has payments.
        if order.payments:
            continue

        # Default payment for most orders.
        payment_status = "SUCCESS"
        payment_method = "UPI"

        # Deliberate edge cases based on customer + order status.
        if order.user.name == "Karthik" and order.status == "PROCESSING":
            payment_status = "FAILED"
            payment_method = "CARD"

        elif order.user.name == "Priya" and order.status == "RETURNED":
            payment_status = "REFUNDED"
            payment_method = "UPI"

        elif order.user.name == "Divya" and order.status == "DELAYED":
            payment_status = "SUCCESS"
            payment_method = "CREDIT_CARD"

        payment = Payment(
            order_id=order.id,
            amount=order.total_amount,
            status=payment_status,
            payment_method=payment_method,
            transaction_reference=f"TXN-{order.id}-001",
            created_at=order.ordered_at,
        )

        session.add(payment)
        created += 1

    session.flush()

    print(f"Payments: created {created}")

def seed_payment_edge_cases(session):
    created = 0

    # -----------------------------------------
    # ARUN — DUPLICATE PAYMENT
    # -----------------------------------------

    arun = (
        session.query(User)
        .filter(User.name == "Arun")
        .first()
    )

    if arun:
        arun_order = (
            session.query(Order)
            .filter(
                Order.user_id == arun.id,
                Order.status == "SHIPPED",
            )
            .first()
        )

        if arun_order:
            payment_count = (
                session.query(Payment)
                .filter(Payment.order_id == arun_order.id)
                .count()
            )

            if payment_count == 1:
                duplicate_payment = Payment(
                    order_id=arun_order.id,
                    amount=arun_order.total_amount,
                    status="SUCCESS",
                    payment_method="UPI",
                    transaction_reference=f"TXN-{arun_order.id}-002",
                    created_at=arun_order.ordered_at,
                )

                session.add(duplicate_payment)
                created += 1

    # -----------------------------------------
    # DIVYA — REFUNDED PAYMENT
    # -----------------------------------------

    divya = (
        session.query(User)
        .filter(User.name == "Divya")
        .first()
    )

    if divya:
        divya_order = (
            session.query(Order)
            .filter(
                Order.user_id == divya.id,
                Order.status == "DELIVERED",
            )
            .first()
        )

        if divya_order:
            existing_refund = (
                session.query(Payment)
                .filter(
                    Payment.order_id == divya_order.id,
                    Payment.status == "REFUNDED",
                )
                .first()
            )

            if not existing_refund:
                refunded_payment = Payment(
                    order_id=divya_order.id,
                    amount=divya_order.total_amount,
                    status="REFUNDED",
                    payment_method="CARD",
                    transaction_reference=f"REFUND-{divya_order.id}-001",
                    created_at=divya_order.ordered_at,
                )

                session.add(refunded_payment)
                created += 1
        # -----------------------------------------
    # SURYA — PENDING PAYMENT
    # -----------------------------------------

    surya = (
        session.query(User)
        .filter(User.name == "Surya")
        .first()
    )

    if surya:
        surya_order = (
            session.query(Order)
            .filter(
                Order.user_id == surya.id,
                Order.status == "PROCESSING",
            )
            .first()
        )

        if surya_order:
            existing_pending = (
                session.query(Payment)
                .filter(
                    Payment.order_id == surya_order.id,
                    Payment.status == "PENDING",
                )
                .first()
            )

            if not existing_pending:
                pending_payment = Payment(
                    order_id=surya_order.id,
                    amount=surya_order.total_amount,
                    status="PENDING",
                    payment_method="UPI",
                    transaction_reference=f"TXN-{surya_order.id}-PENDING",
                    created_at=surya_order.ordered_at,
                )

                session.add(pending_payment)
                created += 1

    session.flush()

    print(f"Payment edge cases: created {created}")

def seed():
    session = SessionLocal()

    try:
        print("Starting ShopFlow database seed...")

        seed_users(session)
        seed_products(session)
        seed_orders(session)
        seed_payments(session)
        seed_payment_edge_cases(session)

        session.commit()

        print("Seed completed successfully.")

    except Exception:
        session.rollback()
        print("Seed failed. Transaction rolled back.")
        raise

    finally:
        session.close()


if __name__ == "__main__":
    seed()