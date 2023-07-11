import csv
Manufacturer=[]
Model=[]
Sales_in_thousands=[]
Vehicle_type=[]
Price_in_thousands=[]
Engine_size=[]
Horsepower=[]
Wheelbase=[]
Width=[]
Length=[]
Curb_weight=[]
Fuel_capacity=[]
Fuel_efficiency=[]
Latest_Launch=[]

f1=open("/Users/vivekborade/Python/dataset2.csv","r")
while(True):
    data=f1.readline()
    if not data:
        break;
    #print(data)
    data=data.replace("\n","")
    temp=data.split(",")
    print(temp)
    Manufacturer.append(temp[0])
    Model.append(temp[1])
    Sales_in_thousands.append(temp[2])
    Vehicle_type.append(temp[3])
    Price_in_thousands.append(temp[4])
    Engine_size.append(temp[5])
    Horsepower.append(temp[6])
    Wheelbase.append(temp[7])
    Width.append(temp[8])
    Length.append(temp[9])
    Curb_weight.append(temp[10])
    Fuel_capacity.append(temp[11])
    Fuel_efficiency.append(temp[12])
    Latest_Launch.append(temp[13])

f1.close()

#perfoming operations
#1) finding the most expensive car

Price_in_thousands
Manufacturer
Model

print("Most expensive car is :",Manufacturer[24],Model[24])

#2)calculating average sales of all cars


#3) find the total no of passanger cars

Vehicle_type
frequency = {}
for item in Vehicle_type:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1

Sorted_frequency=sorted(frequency.items(),key=lambda x:x[1],reverse=True)

Sorted_frequency1=dict(Sorted_frequency)
print(Sorted_frequency1)

print("The total no. of passanger cars is: ",list(Sorted_frequency1.values())[0])

#4) Finding the car who has max engine size

Engine_size.pop(0)
print(Engine_size)

Max_Engine_size=max(Engine_size)
print("car which has max engine size is :",Max_Engine_size)

