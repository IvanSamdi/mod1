def send_email(message, recipient, sender="university.help@gmail.com"):
    recipient_ = recipient.find('@') >= 0 and recipient.endswith((".com", ".ru", ".net"))
    if recipient_ == False:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif recipient == sender:
        print("Нельзя отправить письмо самому себе")
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}")
    elif sender != "university.help@gmail.com":
        print(f"Нестандартный отправитель! Письмо отправлено с адреса {sender} на адрес {recipient}")


send_email('message', 'ivan.malin@gmail.com', 'university.help@gmail.com')
send_email('message', 'ivan.malin@gmail.com', 'university.@gmail.com')
send_email('message', 'ivan.malin@gmail.au', 'university.help@gmail.com')
send_email('message', 'university.help@gmail.com')
