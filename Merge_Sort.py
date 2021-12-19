def mergeSort(list):

    # 완전히 다 쪼개질 때 까지 실행
    if len(list) > 1 :
        mid = len(list) // 2

        left = list[:mid]
        right = list[mid:]
    
        # 왼쪽, 오른쪽 부분 쪼개기
        print("left: ", left)
        mergeSort(left)

        print("right:", right)
        mergeSort(right)
        # Big O = log2(n)

        
        #합치는 과정

        i=0
        j=0
        k=0

        # 일단 임시로 정렬
        while i < len(left) and j < len(right) :
            if left[i] < right[j] :
                list[k] = left[i]
                i +=1
            else:
                list[k] = right[j]
                j += 1
            k += 1

        print("임시로 list 정렬:", list)
        # 왼쪽에 남은 애들이 있을때 정렬
        while i < len(left) :
            list[k] = left[i]
            i += 1
            k +=1

        # 오른쪽에 애들이 남아 있을때 정렬
        while j < len(right) :
            list[k] = right
            j += 1
            k += 1

        print("최종적으로 정렬된 list:" , list)
        print("")
        # Big O = O(n)

#전체 Big O = O(nlogn)
list = [38, 27, 43, 4, 9, 82, 10]
mergeSort(list)
