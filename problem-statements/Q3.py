def average_passing_grades(grades: list[int]) -> float:
    total = 0
    count = 0

    for grade in grades:
        if grade >= 50:
            total += grade
            count += 1

    if count == 0:
        return 0.0

    return float(total / count)


if __name__ == "__main__":
    # Take input as space-separated numbers
    grades_input = list(map(int, input("Enter grades separated by space: ").split()))
    
    result = average_passing_grades(grades_input)
    print("Average of passing grades:", result)
