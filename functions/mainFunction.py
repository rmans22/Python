def doMultiplation(start_number, multiply_by , end_number):
    answer = start_number*multiply_by
    for start_number in range(end_number):
        answer = start_number*multiply_by
        print(start_number, ' X ', multiply_by, ' = ', answer)