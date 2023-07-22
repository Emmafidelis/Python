#for x in range(4):
    #for y in range(3):
        #print(f"({x}, {y})")

numbers = [2, 2, 2, 2, 10]
for n in numbers:
    output = ''
    for count in range(n):
        output += '*'
    print(output)