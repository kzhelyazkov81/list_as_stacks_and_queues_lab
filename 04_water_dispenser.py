from collections import deque
quantity = int(input())
queue = deque()

while True:
    command = input()
    if command == 'Start':
        break
    else:
        queue.append(command)

while True:
    command = input()
    if command == 'End':
        break
    elif command.startswith('refill'):
        command = command.split(' ')
        quantity += int(command[1])
    else:
        person = queue.popleft()
        if int(command) <= quantity:
            print(f'{person} got water')
            quantity -= int(command)
        else:
            print(f'{person} must wait')

print(f'{quantity} liters left')
