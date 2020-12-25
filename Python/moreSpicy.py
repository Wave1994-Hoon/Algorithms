"""
프로그래머스 Heap 문제 Level 2, 더 맵게
url = https://programmers.co.kr/learn/courses/30/lessons/42626

"""


import heapq


def solution(scoville, K):
    count = 0
    heapq.heapify(scoville)

    for i in range(len(scoville) - 1):
        count += 1
        scovilleLevel = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
        heapq.heappush(scoville, scovilleLevel)  # heappop으로 나온 element 계산 후 바로 push -> out of index 방지

        if K <= scovilleLevel:
            if scoville[0] >= K:  # min() 사용 x: 시간 복잡도 증가
                return count

    return -1


if __name__ == "__main__":
    # Case 1
    scoville = [1, 2, 3, 9, 10, 12]
    K = 7

    assert(solution(scoville, K) == 2)

    # Case 2
    scoville = [1, 2, 3]
    K = 11

    assert(solution(scoville, K) == 2)
