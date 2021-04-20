import sys

stack = []

def push(element):
    stack.append(element)

def pop():
    if len(stack) == 0 : return -1
    else: return stack.pop()

def size():
    return len(stack)

def empty():
    if len(stack) == 0 : return 1
    else : return 0

def top():
    if len(stack) == 0 : return -1
    else : return stack[-1]

orderCount = int(input())

orderArr = []

# input order
for _ in range(orderCount):
    orderArr.append(list(sys.stdin.readline().split()))

print(orderArr)