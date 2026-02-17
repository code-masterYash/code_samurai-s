def get_ticket_price(age: int, is_student: bool) -> int:
    if age < 12:
        return 8
    elif age >= 65:
        return 10
    else:
        if is_student:
            return 12
        else:
            return 15


if __name__ == "__main__":
    age_input = int(input("Enter age: "))
    student_input = input("Is the person a student? (True/False): ")

    # Convert string input to boolean
    is_student = student_input.strip().lower() == "true"

    price = get_ticket_price(age_input, is_student)
    print("Ticket price:", price)
