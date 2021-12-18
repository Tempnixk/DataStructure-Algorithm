def bubbleSort(list):

    # 크기 = 5
    length =len(list)

    #가장 마지막에 수행되는 알고리즘은 1개의 원소만 비교하기에 수행할 필요 없음 
    for i in range(0, length - 1) :
            
        print("")
        print("i:",i)
        swap = False    
        #정렬 수행 후 맨 오른쪽 원소는 가장 크므로 다음 수행에 들어올 필요 없
        for j in range(0,length - 1 - i):

            # Big O = O(n^2)

            print("j :",j)
            
            if(list[j] > list[j+1]):


               list[j], list[j+1] = list[j+1], list[j]
               swap = True
               
        if swap == False:
               break

list = [5,1,4,2,8]
bubbleSort(list)
print(list)
                    
