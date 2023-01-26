with open('input.txt', 'r') as file:
    data = file.read()

def signal(data, size):
    length = len(data)
    for i in range(length - size + 1):
        temp = set(data[i:i + size])
        if len(temp) == size:
            return i + size


print('Answer to the first question is:', signal(data, 4))
print('Answer to the first question is:', signal(data, 14))