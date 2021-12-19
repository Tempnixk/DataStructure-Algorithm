# pivot을 기준으로 쪼갭니다
def zzogaeggi (list, low, high):

    # pivot 값 정하기
    pivot = list[high]

    
    # i는 피봇을 기준으로
    # list를 정렬해주는 역할입니다.

    i = low - 1
    print("")
    print("pivot:", pivot)

    # j를 통해서 list를 훑습니다.
    for j in range(low, high) :

        if list[j] < pivot :

            i = i + 1
            # Swap
            list[i], list[j] = list[j], list[i]
            print("list:", list)

    # 마지막으로
    #pivot이 들어갈 위치를 바꿔줍니다.
    list[i+1], list[high] = list[high], list[i+1]
    print("list_after_pivot:", list)

    return i +1
    


def quickSort(list, low, high):

    # pivot이 알맞은 위치에 있어서
    # QuickSort를 실행해줘도 되는지 확인하는 부분

    if low < high :

        # pivot 기준으로 쪼개기 위해서, pivot 위치를 가져옵니다.
        pivot_position = zzogaeggi(list, low, high)

        #그리고 왼쪽과 오른쪽 부분을 쪼갭니다.
        quickSort(list, low, pivot_position - 1)
        quickSort(list, pivot_position + 1, high)



# list를 쪼개는 과정은 merge sort처럼 O(log2(n))
# 크기 비교하면서 정렬 O(n)
# pivot이 계속 가장 큰 수/ 가장 작은수가 나올때
# worst case가 존재 O(n^2)
# 쪼개는 과정이 O(n)

list = [10, 80, 30, 90, 40, 50, 70]
n = len(list)
quickSort(list, 0, n-1)
print(list)
