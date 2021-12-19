def insertSort(list):

    #첫번째 원소는 비교하지 않기에 1부터 시작
    for i in range(1, len(list)) :

        key = list[i]

        j = i - 1

        print("key:", key)

        while j >= 0 and key < list[j] :

            list[j + 1] = list[j]

            j -= 1

        print("list1:", list)
        list[j + 1] = key
        print("list2:", list)


list =[12, 11,13,5,6]
insertSort(list)
