"""l=[10,20,30,40]
l1=[20,40,60]
l2=l+l1
print(l3)

a=1
while a<5:
    print(a);
    a+=1 """

n = int(input("Enter the value:"))
temp = n
sum=0
r = 0
while (n > 0):
    r = n % 10
    c = r ** 3
    sum =sum+ c
    n = n / 10
if (temp == sum):
    print("armstrong")
else:
    print("not armstrong")

