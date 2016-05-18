while True:
    Input = input().split()
    H = int(Input[0])
    W = int(Input[1])
    if H == 0 and W == 0:
        break
    if H >= 3 and W <= 100:
        for i in range(H):
            for j in range(W):
                if j == W - 1:
                     print("#")
                elif i == 0 or i == H - 1 or j == 0:
                     print("#",end="")
                else:
                    print(".",end="")
                if i == H - 1 and j == W - 1:
                    print("")
