from collections import deque, defaultdict

# mas = [1, 1, 2, 3, 4, 2, 1]
mas = [1, 1, 1, 2, 2, 2, 2, 11, 3, 3]
freq_dict = defaultdict(int)

for el in mas:
    freq_dict[el] += 1

stack = deque()
result = [0 for i in range(len(mas))]
for i in range(len(mas) - 1, -1, -1):
    if len(stack) != 0:
        while len(stack) != 0 and freq_dict[stack[-1]] <= freq_dict[mas[i]]:
            stack.pop()
    result[i] = -1 if len(stack) == 0 else stack[-1]
    stack.append(mas[i])

print(result)
