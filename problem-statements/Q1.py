def calculate_total_bill(amount: float, tip_percent: int) -> float:
    amount = float(amount)
    tip_percent = float(tip_percent)
    total = amount + (amount * tip_percent / 100)
    return round(total, 2)


if __name__ == "__main__":
    bill = float(input("Enter bill amount: "))
    tip = float(input("Enter tip percentage: "))
    total = calculate_total_bill(bill, tip)
    print("Total amount to pay:", total)

