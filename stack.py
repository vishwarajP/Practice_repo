stack = []

def push():
    if len(stack) == n:
        print("stack is full")
    else:
        for i in range(n):
            k = int(input("enter the elements in stack"))
            stack.append(k)
            print(stack)

def pop():
    if not stack:
        print("its empty")
    else:
        e = stack.pop()
        print("removed elements" , e)
        print(stack)


n = int(input("enter the total len"))
while True:
    print("choose the options 1.push 2.pop 3.quit")
    d = int(input("enter the your choice"))
    if d == 1:
        push()
    elif d == 2:
        pop()
    elif d == 3:
        break
    else:
        print("select right option")



