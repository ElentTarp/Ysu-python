#Problem 01, Dictionaries
#Construct a Dictionary cities_AM that corresponds to largest 5 Armenian cities their population
cities_AM={'Yerevan':1077.6, 'Gyumri':114.5, 'Vanadzor':79.3, 'Abovyan':44.6, 'Kapan':42.5}
#Print the names of cities
print(cities_AM.keys())
#Print the sum of population in largest 5 Armenian cities
sum_=0
for i in cities_AM.values():
    sum_+=i                         
print(sum_)
#Get the name of the second largest (by population) city in Armenia (not by a hand, of course  ⌣¨  )
def my_sort(dict_):
    my_list = list(dict_.items())
    print(my_list)
    length = len(my_list)
    for i in range(length):
        for j in range(length - 1):
            if my_list[i][1] > my_list[j][1]:
                my_list[i], my_list[j] = my_list[j], my_list[i]
    cities_AM = dict(my_list)
    return cities_AM
   
second_largest_city = list(my_sort(cities_AM).items())[1]  
print('Second largest city is', second_largest_city)

#Find information about the surface areas of cities, and update dictionary to include tuples (population, area) for each city.
area=[223, 152, 32, 54, 36, 4.6]
all_key=[i for i in cities_AM.keys()]
cities_AM.update({all_key[i]:(cities_AM[all_key[i]],area[i]) for i in range(len(cities_AM))})
print(cities_AM)
#Construct a similar dictionary cities_GE for Germany 2 largest cities, and create a new Dictionary, with keys "Armenia", "Germany", and values as the constructed dictionaries
 
cities_GE = {'Berlin':3237857, 'Hamburg':1749659}
all_countries = {'Armenia': cities_AM, 'Germany': cities_GE}
print(all_countries) 
#Problem 02, Control flows
#Consider the list x = [1, -2, 3, 9, 0, 1, 3, 2, -2, -4, 1, -3] . Construct two lists, x_neg and x_pos containng, correspondingly, all negative and all positive elements of x in the same order. Costruct also lists ind_neg and ind_pos which will contain the indices of all negative and positive elements of x, respectively.
x = [1, -2, 3, 9, 0, 1, 3, 2, -2, -4, 1, -3]
x_pos=[]
x_neg=[]
ind_pos=[]
ind_neg=[]
length=len(x)
for i in range(length):
    if x[i]>0:
        x_pos.append(x[i])
    if x[i]<0:
        x_neg.append(x[i])
print(x_neg)
print(x_pos)
for i in range(length):
    if x[i]>0:
        ind_pos.append(i)
    if x[i]<0:
        ind_neg.append(i)
print(ind_neg)
print(ind_pos)   
#Find the sum
i=0
sum1=0
while i<102:
    sum1+=i
    i+=2
print (sum1)
#Calculate the sum
sum2=0
for j in range(1,101,2):
    if j%2==0:
        sum2+=1/j
    else:
        sum2+=j
print(sum2)
#Calculate the semifactorial  20!! , without using any Python built-in factorial calculation functions
semifactorial=1
for j in range(2,21,2):
    semifactorial*=i
print(semifactorial)
#Calculate the sum
sum_=0
factorial=1
for k in range(0,21):
    factorial*=i
    sum_+=-1**i/factorial
print(sum_)
#Given a list of real numbers, find the maximum element of that list, without using any built-in Python max function
numbers= list(map(int,input("Enter a number:" ).split()))
max_=numbers[0]
for i in range(len(numbers)):
    if max_<numbers[i]:
        max_=numbers[i]
print (max_)
def bubble_sort(numbers):
    for k in range(len(numbers)):
        for j in range(len(numbers) - 1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
bubble_sort(numbers)
print(numbers)

