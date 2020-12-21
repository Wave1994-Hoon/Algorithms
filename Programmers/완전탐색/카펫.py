'''
프로그래머스 완전탐색 문제 Level 2, 카펫 문제
url = https://programmers.co.kr/learn/courses/30/lessons/42842


# 문제 조건

  □ □ □ □
  □ ■ ■ □
  □ □ □ □

--> X: 가로, Y: 세로
--> Yellow = X * Y
--> Brown = 2(X + Y) + 4(상하좌우 끝 점)
--> Brown' X = Yellow' X + 2

--> 위 조건을 만족하는 X, Y를 찾아야 한다.
--> Yellow = x * Y 를 만족하는 X, Y를 찾은 후 Brown 조건을 만족하는지 확인

'''


def solution(brown, yellow):
    for x in range(yellow, 0, -1):   # int(yellow ** 0.5) --> 제곱근으로도 접근 가능
        if yellow % x == 0:
            y = yellow // x

            if 2 * (x + y) + 4 == brown:  # check brown
                return [x + 2, y + 2]


if __name__ == "__main__":
    assert(solution(10, 2) == [4,3])
    assert(solution(8, 1) == [3,3])
    assert(solution(24, 24) == [8,6])
    assert(solution(50, 22) == [24, 3])