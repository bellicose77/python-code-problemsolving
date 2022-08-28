t=int(input())
def image(x,y):
    #print("xxsx")
    z=x+y
    re = ''.join(sorted(z))
    #print("re",re)
    l=0
    s=1
    while l!=3:
        if(re[l]!=re[l+1]):
            #print("koto bar l",l)
            s+=1
            #print("ss",s)
        l+=1
    return s
while t!=0:
    x=input()
    y=input()
    result = image(x,y)
    print(result-1)
    t-=1