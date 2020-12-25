"""
카카오 문 2020 문제, 괄호변환, Level2
url = https://programmers.co.kr/learn/courses/30/lessons/60058?language=python3
"""


# "(" == ")" 조건이 성립하면 split
def splitBalancedStringAndOther(s):
    countLeft, countRight = 0, 0

    for i in range(len(s)):
        if s[i] == "(":
            countLeft += 1
        if s[i] == ")":
            countRight += 1

        if countLeft == countRight:
            break

    return s[:i + 1], s[i + 1:]


# 항상 '(' 개수가 ')' 보다 많아야된다.
def checkRightString(s):
    countLeft, countRight = 0, 0

    for i in range(len(s)):
        if s[i] == "(":
            countLeft += 1
        if s[i] == ")":
            countRight += 1

        if countLeft < countRight:
            return False

    return True


def generateStringIfStringIsWrong(u, v):
    result = "(" + solution(v) + ")"
    u = u[1:-1]

    for i in range(len(u)):
        if u[i] == "(":
            result += ")"
        if u[i] == ")":
            result += "("

    return result


def solution(p):
    if p == "":
        return p
    u, v = splitBalancedStringAndOther(p)

    if checkRightString(u):
        return u + solution(v)
    return generateStringIfStringIsWrong(u, v)


if __name__ == "__main__":
    assert solution("(()())()") == "(()())()"
    print(solution("(()())()"))

    assert solution(")(") == "()"
    print(solution(")("))

    assert solution("()))((()") == "()(())()"
    print(solution("()))((()"))
