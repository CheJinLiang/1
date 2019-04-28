import math
def yiyuan(a,b,c):
    d = b*b-4*a*c
    if (a==0):
        print("这不是一元二次方程！")
    elif (d<0):
        print("无实数解！")
      
    elif (d==0):
        print("有两个相等的实数解，x1=x2"%(-b/2*a))
        
    else:
        x1=(-b+math.sqrt(d))/2*a
        x2=(-b-math.sqrt(d))/2*a
        print("有两个不相等的实数解，x1=%.2f,x2=%.2f"%(x1,x2))
        
yiyuan(0,5,5)