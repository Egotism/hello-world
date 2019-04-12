temp=input("请输入一个数:")
floatp=float(temp)-int(float(temp))
if floatp < 0.5:
    num=int(float(temp))
else:
    num=int(float(temp))+1
print(num)
