def get_list_number_divisors(number):
    list_divisors = []
    for divisor in range(1, number + 1):
        if number % divisor == 0:
            list_divisors.append(divisor)

    return list_divisors


print(get_list_number_divisors(23))
print(get_list_number_divisors(2 ** 16))
