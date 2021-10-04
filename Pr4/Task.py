print("первая программа")
a = int(input())
b = int(input())
for i in range(a,b+1):
    print(i)

print("вторая программа")
b = int(input())
a = int(input())
if a<b:
    for i in range(a, b+1):
        print(i)
else:
    for i in range(a,b-1,-1):
        print(i)

print("третья программа")
b = int(input())
a = int(input())
for i in range (a,b-1, -1):
    if i%2 == 1:
        
        print (i)
print("четвёртая программа")
a = int(input())
count = 0
for i in range(a):
    i = int(input())
    count = count + i
print (count)
print("пятая программа")
a = int(input())
count = 0
for i in range(a+1):
    count = i**3 + count
print(count)
print("шестая программа")
a = int(input())
count = 0
s = 1
for i in range(1, a+1):
    s = s * i
print(s)
print("седьмая программа")
a = int(input())
s = 1
s2 = 0
for i in range(1,a+1):
    s = s * i
    s2 = s2 + s
print(s2)
print("восьмая программа")
a = int(input())
for i in range(1,a+1):
    for k in range(1,i+1):
        print(k,end='')
    print()
print("девятая программа")
a = int(input())
ch1 = 0
ch2 = 1
summ = 0
i = 0
while i<a-2:
    ch3 = ch1+ch2
    ch1 = ch2
    ch2 = ch3
    i+=1
    summ = summ + ch3
print(summ+1)
    
print("десятая программа")
a = int(input())
b = int(input())
ch1 = 0
ch2 = 1
summ = 0
i = 0
while i<a-2:
    ch3 = ch1+ch2
    ch1 = ch2
    ch2 = ch3
    i+=1
    if i >= b:
        summ=summ+ch3
print(summ)
