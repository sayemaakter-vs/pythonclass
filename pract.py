values=[12,-5,0,7,-3,0,18,-1]
positive=[]
negative=[]
zero=[]
count1=0
count2=0
count3=0
for i in values:
    if i>0:
        positive.append(i)
        count1=count1+1
    elif i<0:
        negative.append(i)
        count2=count2+1
    else:
        zero.append(i)
        count3=count3+1
print("Positive:",positive)
print("Negative:",negative)
print("Zero:",zero)
print("Counts:",count1, count2, count3)

        
        