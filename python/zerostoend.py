numbers = [0, 1, 0, 3, 12, 0, 5]

result = []

for n in numbers:
    if n != 0:
        result.append(n)

result += [0] * (len(numbers) - len(result))

print(result)