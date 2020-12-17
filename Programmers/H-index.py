"""
프로그래머스 Sort 문제 Level 2, H-Index 문제
url = https://programmers.co.kr/learn/courses/30/lessons/42747

"""



// TODO: 내장함수 써보기

def solution(citations):
    hIndex = 0  # 인용
    length = len(citations)
    maxCitation = max(citations)

    while hIndex < maxCitation:
        upCount, downCount = countCitationInList(citations, length, hIndex)

        if checkHIndex(hIndex, upCount, downCount):
            hIndex += 1
            continue

        return hIndex - 1

    return hIndex


""" 인용 횟수 체크 -> hIndex 값 보다 큰(작은) 수 개수 찾기 """
def countCitationInList(citations, length, hIndex):
    upCount, downCount = 0, 0

    for index in range(length):
        if citations[index] >= hIndex:
            upCount += 1
            continue

        downCount += 1

    return upCount, downCount


""" 인용 횟수 비교 """
def checkHIndex(hIndex, upCount, downCount):
    if downCount <= hIndex <= upCount:
        return True

    return False



if __name__ == "__main__":
    # TestCase 1
    citations = [3, 0, 6, 1, 5]
    assert(solution(citations) == 3)

    # TestCase 2
    # citations = [0, 0, 0, 0]
    # assert(solution(citations) == 0)
