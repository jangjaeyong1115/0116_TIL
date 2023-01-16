import sys

number = int(input())

for number in range(number):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print(f'Case #{number+1}: {a} + {b} = {a+b}')