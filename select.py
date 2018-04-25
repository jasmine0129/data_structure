def select(a):
    for i in range(len(a)):
        min = a[i]
        index = i
        for j in range(i,len(a)):
            if(min>=a[j]):
                min=a[j]
                index=j
        a[index]= a[i]
        a[i] = min
    return a

a=[1,4,7,2,5,2,1]
print(select(a))
