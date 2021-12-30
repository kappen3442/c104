import csv  
with open("weight.csv",newline="")as f:
    reader=csv.reader(f)
    data=list(reader)
    data.pop(0)

    newdata=[]
    for i in range(len(data)):
        n=data[i][1]
        newdata.append(float(n))

    view=(len(newdata))   
    total=0
    for counter in newdata:
        total+=counter
        median=int(newdata[counter//2])

    print(total)
    print(view)
    m=total/view
    print (m)
    
    print(median)