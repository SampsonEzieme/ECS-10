def greater(list1, list2):
    finallist= []
    for i in range(0, len(list1)):
        if list1[i] > list2[i]:
            finallist.append(list1[i])
        elif list1[i] < list2[i]:
            finallist.append(list2[i])
        else:
            finallist.append(list1[i])
    return finallist
