hight = 1.75
weight = 80.5
BIM = weight/(hight*hight)
if BIM < 18.5:
    print('过轻')
elif BIM >18.5 and BIM < 25:
    print('正常')
elif BIM > 25 and BIM < 28:
    print('过重')
elif BIM >28 and BIM < 32:
    print('肥胖')
else:
    print('严重肥胖')