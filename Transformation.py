str = input().casefold()
q = int(input())

for i in range(q):
    command = input().split()
    a = int(command[1])
    b = int(command[2])
    if command[0] == "print":
        print(str[a:b+1])
    elif command[0] == 'reverse':
        str = str[a] + str[a:b+1][::-1] + str[b+a:]
    elif command[0] == "replace":
        str = str[:a] +command[3] + str[b+1:]
