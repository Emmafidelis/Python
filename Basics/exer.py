"""n = ""
started = False
while True:
    n = input("> ").lower()
    if n == "start":
        if started:
            print("car already started!")
        else:
            started = True
            print("car started...")
    elif n == "stop":
        if not started:
            print("car already stopped!")
        else:
            started = False
            print("car stopped")
    elif n == "help":
        print('''
start - to start the car
stop - to stop the car
quit - to quit
        ''')
    elif n == "quit":
        break
    else:
        print("sorry I don't understand that!")
"""

sentence = "This is a common interview"

unique = {}
for item in sentence:
    if item in unique:
        unique[item] += 1
    else:
        unique[item] = 1
print(unique)

print(unique)