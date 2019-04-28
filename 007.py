import math




def quadratic(a,b,c):
    d = b**2-4*a*c
    if (a==0):
        print("不是一元二次次方程组，x=%.2f。"%(-c/b))
        return True
    elif(d<0):
        print("无实数解！")
        return True
    elif(d==0):
        x=-b/2*a
        print("这个一元二次方程组有两个相同的实数解，x1=x2" + str(x))
        return x
    else:
        x1=(-b+math.sqrt(d))/2*a
        x2=(-b-math.sqrt(d))/2*a
        print("这个一元二次方程组有两个不相等的实数解，x1=%.2f,x2=%.2f。"%(x1,x2))
        return (x1,x2)


quadratic(1,6,1)

if __name__ == "__main__":
    pass