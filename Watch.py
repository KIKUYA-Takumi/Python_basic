import sys
S = input()
sec = int(S)
if(sec < 86400):
    if(sec >= 0):
        h = int(sec / 3600)
        sec = sec % 3600
        m = int(sec / 60)
        s = sec % 60
        print(h,end="")
        print(":",end="")
        print(m,end="")
        print(":",end="")
        print(s)