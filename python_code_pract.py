##Fionnaci series
def fibonacci():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b

f1=fibonacci()
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))


#sort without sort function
list=[20,23,52,458,1,5,256,22]
n=len(list)
for i in range(n):
    for j in range(i+1,n):
        if list[i]>list[j]:
            list[i],list[j]=list[j],list[i]
print(list)


# plaindrome
s="madam"
if s ==s[::-1]:
    print("yes plaindrome")
else:
    print("non_palndrome")


# sort a dictonary
dict={575:"akshay",143:"mee",254:"new",165:"aksh"}
d=sorted(dict.keys())
dict1={}
for i in d :
    dict1[i]=dict[i]
print(dict1)


# sort based on values
dict2={key:value for key , value in sorted(dict.items(), key=lambda x:x[1])}
print(dict2)




### fibanocci using recurssion
def rec_fib(n):
    if n <=1:
        return n
    else:
        return (rec_fib(n-1)+rec_fib(n-2))
nterms=int(input("how many pos integers"))
if nterms <=0:
    print("proper int please")
else:
    for i in range(nterms):
        print(rec_fib(i))


# print all pairds with given sum
l=len(list)
k=125
for i in range(n):
    for j in range(i+1,n):
        if (list[i]+list[j] <=k):
            print("starts here4")
            print(list[i],list[j])


str= "/dhhjh ahjdhjds 14 44 @#hhdjhdfj AHjhsj"
s=""
for i in str:
    if ((i>='A' and i<'Z')| (i>='a' and i<'z')| (i==' ')):
        s=s+i
print(s)


s='istynnsshannn'
ch={}
for i in s:
    if i in ch:
        ch[i]+=1
    else:
        ch[i]=1