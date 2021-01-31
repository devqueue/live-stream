
#########          STACK IMPLEMENTATION            ###########
def isempty(arr):
    if arr == []:
        return True
    else:
        return False

def push(arr, item):
    arr.append(item)
    top = len(arr) -1

def pop(arr):
    if isempty(arr):
        return "stack underflow"
    else:
        item = arr.pop()
        if len(arr)==0:
            top = None
        return item

def peek(arr):
    if isempty(arr):
        return "stack underflow"
    else:
        top = len(arr) - 1
        return arr[top]

def display(arr):
    if isempty(arr):
        return "stack underflow"
    else:
        top = len(arr) - 1
        print(arr[top], "<--- top")
        for i in range(top-1, -1, -1):
            print(arr[i])

# main program 
STACK = [1,2,3,4]
top = None

while True:
    print("Stack operantion")
    print("1. push")
    print("2. pop")
    print("3. peek")
    print("4. Display")
    print("5. Exit")

    ch = int(input("enter a choice"))

    if ch==1:
        item = input("enter your item: ")
        push(STACK, item)

    elif ch==2:
        item = pop(STACK)
        print(item)

    elif ch==3:
        item = peek(STACK)
        print(item)

    elif ch==4:
        display(STACK)
    elif ch==5:
        break
    else:
        print("invalid choice")