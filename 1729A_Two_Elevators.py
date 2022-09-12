t = int(input())
def elevators(a,b,c):
    if(a==1):
        print(1)
    else:
        first = abs(a-1)
        if(c==1):
            second = abs(b-c)
            if(first<second):
                print(1)
            elif(second<first):
                print(2)
            else:
                print(3)
        else:
            second=abs(b-c) + (c-1)
            if(first<second):
                print(1)
            elif(second<first):
                print(2)
            else:
                print(3)


while t!=0:
    a = int(input())
    b=int(input())
    c=int(input())
    elevators(a,b,c)
    t-=1