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


# getting the mean
n=len(new_data)  
total=0
for x in new_data:
    total +=x

mean=total/n

print("Mean/ average is :  " + str(mean))
