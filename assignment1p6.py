numbers = [14, 8, 21, 21, 5, 17, 14]

largest = None
second_largest = None

for number in numbers:
    if largest is None or number > largest:
        if number != largest:
            second_largest = largest
            largest = number

    elif number != largest and (second_largest is None or number > second_largest):
        second_largest = number

if second_largest is None:
    print("Fewer than two distinct values")
else:
    print("Largest distinct value:", largest)
    print("Second-largest distinct value:", second_largest)