"""
프로그래머스 Sort 문제 Level 2, 가장 큰 수 문제
url = https://programmers.co.kr/learn/courses/30/lessons/42746
"""


def solution(numbers):
    if set(numbers) == {0}:
        return "0"

    for index in range(len(numbers)):
        numbers[index] = str(numbers[index])

    return "".join(doQuickSort(numbers))


def doQuickSort(numbers):
    if len(numbers) <= 1:
        return numbers

    pivot = numbers[0]
    greater, lesser = [], []

    for element in numbers[1:]:
        isGreater = compareNumber(element, pivot)

        if isGreater:
            greater.append(element)
            continue

        if not isGreater:
            lesser.append(element)

    return doQuickSort(lesser) + [pivot] + doQuickSort(greater)


def compareNumber(element, pivot):
    if len(element) == len(pivot):
        return element <= pivot
    return element + pivot <= pivot + element


if __name__ == "__main__":
    # TestCase 1
    numbers = [6, 10, 2]
    assert(solution(numbers) == "6210")

    # TestCase 2
    # numbers = [3, 30, 34, 5, 9]
    # assert(solution(numbers) == "9534330")