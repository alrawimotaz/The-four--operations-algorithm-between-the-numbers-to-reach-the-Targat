import random

# 1 digit 5 random numbers
numbers = [random.randint(1,9) for i in range(5)]

#Number with ten floors with 2 digits
numbers2 = [random.randint(1,9)*10 for i in range(1)]
numbers=numbers+numbers2

# target
target_number = random.randint(100, 999)

# fun for all opertions
def calculate(numbers, target_number):
    operators = ['+', '-', '*', '/']
    results = []
    for i in range(5):
        for j in range(5):
            if i != j:
                for k in range(4):
                    if k == 3 and numbers[j] == 0:
                        continue
                    expression = str(numbers[i]) + operators[k] + str(numbers[j])
                    try:
                        result = eval(expression)
                        if result == target_number:
                            return target_number, expression
                        results.append((result, expression))
                    except ZeroDivisionError:
                        continue
    for i in range(len(results)):
        for j in range(i, len(results)):
            if i != j:
                for k in range(4):
                    if k == 3 and results[j][0] == 0:
                        continue
                    expression = results[i][1] + operators[k] + results[j][1]
                    try:
                        result = eval(expression)
                        if result == target_number:
                            return target_number, expression
                        results.append((result, expression))
                    except ZeroDivisionError:
                        continue
    closest_result = min(results, key=lambda x: abs(x[0]-target_number))
    return closest_result[0], closest_result[1]

# Calculating the results
result, expression = calculate(numbers, target_number)

# print the results
print("random numbers: ", numbers)
print("target: ", target_number)
print("expression: ", expression)
print("result: ", result)
