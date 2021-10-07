import csv
with open("data.csv") as f:
    reader=csv.reader(f)
    file_data=list(reader)

file_data.pop(0)
#print(file_data)

# sorting data to get the height of people
new_data=[]
for i in range(len(file_data)):
    n_num=file_data[i][2]
    new_data.append(float(n_num))


# getting the median
n=len(new_data)  
new_data.sort()

#use floor division method to get nearest whole number
# floor division is shown by //

if n%2 ==0:
    #getting the first number
    median1=float(new_data[n//2])

    #getting the second number
    median2=float(new_data[n//2-1])

    #mean of both numbers

    median=(median1+median2)

else:
    median=new_data[n//2]
    print(n)



print("Median is :  " + str(median))
