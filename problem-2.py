fibonacci = []
result = []

one = 0
two = 1

while True:
    new_num = one + two
    if new_num > 4000000:
        break
    one = two
    two = new_num
    fibonacci.append(new_num)
    # print(new_num)

for val in fibonacci:
    if val % 2 == 0:
        result.append(val)

print(sum(result))