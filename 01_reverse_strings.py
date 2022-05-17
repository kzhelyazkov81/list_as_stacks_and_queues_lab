original_string = input()
s = []
for ch in original_string:
    s.append(ch)

reversed_string = ''

while s:
    reversed_string += s[-1]
    s.pop()

print(reversed_string)
