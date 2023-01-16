import sys

input()
a = list(sum(map(int,n.split())) for n in sys.stdin)

for n in a:
    print(n)