#EDS Assignment 2
import csv

Product_Details=[]
Store_Customer_Details=[]
Store_Supplier_Details={}
Gender={}

f1=open("/Users/vivekborade/Python/Sales.csv","r")
while(True):
    data=f1.readline()
    if not data:
        break;
    #print(data)
    data=data.replace("\n","")
    temp=data.split(",")
    print(temp)
    Product_Details.append(temp[1])
    Store_Customer_Details.append(temp[3])
    Store_Supplier_Details.update({temp[0]:temp[2]})
    Gender.update({temp[3]:temp[4]})

f1.close()

Store_Customer_Details=tuple(Store_Customer_Details)
print(type(Store_Customer_Details))

#Performing Operations 
#1) Finding the most popular product for sale.
Product_Details
frequency = {}
for item in Product_Details:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1

Sorted_frequency=sorted(frequency.items(),key=lambda x:x[1],reverse=True)

Sorted_frequency1=dict(Sorted_frequency)

print("Most popular product is: ",list(Sorted_frequency1.keys())[0])

#2) Finding the best supplier for sales.

Store_Supplier_Details.values()
frequency={}
for item in Store_Supplier_Details.values():
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1

Sorted_frequency=sorted(frequency.items(),key=lambda x:x[1],reverse=True)

Sorted_frequency1=dict(Sorted_frequency)

print("Best supplier for sales is: ",list(Sorted_frequency1.keys())[0])


#3) Find the customer who buys most of the products.

Store_Customer_Details
frequency = {}
for item in Store_Customer_Details:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1

Sorted_frequency=sorted(frequency.items(),key=lambda x:x[1],reverse=True)

Sorted_frequency1=dict(Sorted_frequency)

print("Most popular product is: ",list(Sorted_frequency1.keys())[0])

#4) Find the number of customers who are ‘Female’

Gender.values()
frequency={}
for item in Gender.values():
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1

Sorted_frequency=sorted(frequency.items(),key=lambda x:x[1],reverse=True)

Sorted_frequency1=dict(Sorted_frequency)


print("The number of customers who are ‘Female’ is: ",list(Sorted_frequency1.values())[1])

