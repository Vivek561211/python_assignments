import csv
def top_5_emp(d3):
    d3.sort(key = lambda x: int(x[4],reverse=True))
    print("sorted data:",d3)
    
f1=open("/Users/vivekborade/Downloads/Python/Sales.csv","r")
f2=open("/Users/vivekborade/Python/sal.csv","r")
f3=open("/Users/vivekborade/Python/sal-emp.csv","w")

d1=list(csv.reader(f1,delimiter=","))
d2=list(csv.reader(f2,delimiter=","))
d3=[]
for i in range(len(d1)):
    d3.append(d1[i]+d2[i])
print(d3)

d3.sort(key=lambda x:int(x[4]),reverse=True)
print(d3)

for i in range(5):
    print(d3[i][1])

cw=csv.writer(f3)
cw.writerows(d3)