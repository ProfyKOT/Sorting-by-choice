def BigElemFunc(list):
    bigElem = list[0]
    bigElem_index = 0
    for i in range(1,len(list)):
        if list[i] > bigElem:
            bigElem = list[i]
            bigElem_index = i
    return bigElem_index

def ChoiseSort(list):
    newArr = []
    for i in range(len(list)):
        bigElemInArr = BigElemFunc(list)
        newArr.append(list.pop(bigElemInArr))
    return newArr
t = [4,5,1,5,7284,2,88]
print(ChoiseSort(t))