def get_ticket_price(age, is_student):
    if age < 12:
        return 8
    if age >= 65:
        return 10
    if is_student:
        return 12
    return 15

