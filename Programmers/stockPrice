"""
프로그래머스 Stack 문제 Level 2, 주식 가격 문제
url = https://programmers.co.kr/learn/courses/30/lessons/42584
"""


def solution(prices):
    answer = []
    size = len(prices)

    for i in range(size):
        indexCount = 0

        for j in range(i + 1, size):
            indexCount += 1
            if j == size - 1:
                answer.append(indexCount)
                break

            if prices[i] > prices[j]:
                answer.append(indexCount)
                break
    answer.append(0)

    return answer


if __name__ == "__main__":
    assert solution([1, 2, 3, 2, 3]) == [4, 3, 1, 1, 0]
    print(solution([1, 2, 3, 2, 3]))
