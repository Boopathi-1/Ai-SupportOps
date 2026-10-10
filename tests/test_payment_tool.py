from app.tools.payment_tools import get_payment_history,get_order_payment_status

def main():
    payment_history = get_payment_history(2)
    print(payment_history)

    surya_order_payment = get_order_payment_status(1, 7)
    print(surya_order_payment)

    wrong_user_payment = get_order_payment_status(2, 7)
    print(wrong_user_payment)

if __name__ =="__main__":
    main()