def sortStack(stack):
    tmpStack=[]

    while(stack):
        num=stack.pop()
        while(tmpStack and (tmpStack[-1]<num)):
            stack.append(tmpStack[-1])
            tmpStack.pop()
        tmpStack.append(num)
    return tmpStack        