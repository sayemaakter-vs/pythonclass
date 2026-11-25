n = int(input("Enter a positive integer: "))

if n <= 0:
    print("Invalid input")

else:
    even_sum = 0
    odd_count = 0
    divisible_sum = 0
    total_sum = 0

    for i in range(1, n + 1):
        total_sum += i

        if i % 2 == 0:
            even_sum += i
        else:
            odd_count += 1

        if i % 15 == 0:
            divisible_sum += i

    average = total_sum / n

    print("Sum of even numbers:", even_sum)
    print("Number of odd numbers:", odd_count)
    print("Sum of numbers divisible by both 3 and 5:", divisible_sum)
    print("Average:", average)