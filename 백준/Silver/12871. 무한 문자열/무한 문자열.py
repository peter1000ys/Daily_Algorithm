import math

s = input()
t = input()
if s*(math.lcm(len(s), len(t))//len(s)) == t*(math.lcm(len(s), len(t))//len(t)):
    print(1)
else:
    print(0)