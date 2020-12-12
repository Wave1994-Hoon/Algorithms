"""
프로그래머스 Sort 문제 Level 2, H-Index 문제
url = https://programmers.co.kr/learn/courses/30/lessons/42747
"""


def countCitationInList(citations, length, hIndex):
    upCount, downCount = 0, 0

    for index in range(length):
        if citations[index] >= hIndex:
            upCount += 1
            continue

        downCount += 1

    return upCount, downCount


def checkHIndex(hIndex, upCount, downCount):
    if downCount <= hIndex <= upCount:
        return True

    return False


def solution(citations):
    hIndex = 0
    length = len(citations)
    maxCitation = max(citations)

    while hIndex < maxCitation:
        upCount, downCount = countCitationInList(citations, length, hIndex)

        if checkHIndex(hIndex, upCount, downCount):
            hIndex += 1
            continue

        return hIndex - 1

    return hIndex


if __name__ == "__main__":
    assert solution([3, 0, 6, 1, 5]) == 3
    assert solution([0, 0, 0, 0]) == 0
