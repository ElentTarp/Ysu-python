
#Problem 1 Calculate the values of the Expression
print(pow((20**10+3**10),2))
#Problem 2 
x=[1,1,2,3,2,3,1,1,2,3,4,1]
#Get the length of 𝑥 in the variable 𝑙
l=len(x)
print(l)
#Change the last element of  𝑥  by 5
x[11]=5
print(x)
#Add elements 5,6,7,8,9,10 at the end of the list  𝑥
x+=[5,6,7,8,9,10]
print(x)
#Extract all odd-indexed elements of  𝑥  in the list  𝑦 , and all even-indexed elements of  𝑥  into the list  𝑧
y=x[: :2]
print(y)
z=x[1: :2]
print(z)
#Get all even elements of  𝑥  in the list  𝑦1  and all odd elements of  𝑥  in the list  𝑧1
y1 = [x[i] for i in range(0,len(x)) if x[i] % 2 == 0]

z1 = [x[i] for i in range(0,len(x)) if x[i] % 2 == 1]
print(y1,z1)
#Replace all odd elements of  𝑥  by 0
for i in range(0,len(x),2):
    x[i]=0
print(x)
#Find the maximal and minimal elements of  𝑥 , without using the max and min functions
min_=x[0]
max_=x[0]
for i in range(len(x)):
    if max_<x[i]:
        max_=x[i]
    if min_>x[i]:
        min_=x[i]
print(min_)
print(max_)
#Find the sum of the elements of  𝑥
print(sum(x))
#Construct a list  𝐼  consisting of all reciprocals of the elements of  𝑥
x.reverse()
print(x)
#Find the value of the sum
sum_=sum([1/3**k for k in list(range(1,11))])
print(sum_)
#Problem 3
word="Pneumonoultramicroscopicsilicovolcanoconiosis"
#Find the number of letters in this word
print(len(word))
#Find the number of letters "o" in this word
o=word.count('o')
print(o)

