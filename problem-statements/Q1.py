def calculate_total_bill(amount, tip_percent):
    total = amount + (amount * tip_percent / 100)
    return round(total, 2)


# Test Cases
assert calculate_total_bill(100.0, 15) == 115.0
assert calculate_total_bill(55.50, 20) == 66.6
assert calculate_total_bill(200, 0) == 200.0
assert calculate_total_bill(12.99, 10) == 14.29
assert calculate_total_bill(0, 15) == 0.0

print("All test cases passed")
