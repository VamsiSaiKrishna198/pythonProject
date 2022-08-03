a=[1,2,3,4,5]
print(tuple(a))
b=(3,4,5,6)
print(list(b))
c={7,8,9,10}
data={"name" : "vamsi","id":2100031403}
datas=[('name','vamsi'),('id',210031403)]
print(list(data))
print(dict(datas))

vamsi={"name": "vamsi","id":21000}
print(list(vamsi))
a=0
b=1
n=int(input())
for i in range(2,n+1):
    res=a+b
    a=b
    b=res

print(res)
if (n%2)==1:
    print("positive number")
else:
    print("negative number")
a=[1,2,3,4,5]
sum=0
i=0
while(i<len(a)):
    sum=sum+a[i]
    i=i+1
print(sum)
print(a[3])