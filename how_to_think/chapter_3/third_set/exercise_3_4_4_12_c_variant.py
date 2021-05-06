n = -123456789.0
original_n = n

count = 0

if n < 0:
    count += 1  # should the minus sign count as a digit?
    n *= -1

while n != 0:
    if n % 2 == 0:
        count += 1
    n = n // 10


print(original_n, "has", count, "digits")
