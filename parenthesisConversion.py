"""
url = https://programmers.co.kr/learn/courses/30/lessons/60058?language=python3
"""


# "(" == ")" 조건이 성립하면 split
def splitBalancedStringAndOther(s):
    countLeft = 0
    countRight = 0

    for i in range(len(s)):
        if s[i] == "(":
            countLeft += 1
        elif s[i] == ")":
            countRight += 1
        else:
            raise Exception("invalid data")

        if countLeft == countRight:
            break

    return s[:i + 1], s[i + 1:]


# 항상 '(' 개수가 ')' 보다 많아야된다.
def checkRightString(s):
    countLeft = 0
    countRight = 0

    for i in range(len(s)):
        if s[i] == "(":
            countLeft += 1
        elif s[i] == ")":
            countRight += 1
        else:
            raise Exception("invalid data")

        if countLeft < countRight:
            return False

    return True


def doGenerateStringIfStringIsWrong(u, v):
    result = "(" + solution(v) + ")"
    u = u[1:-1]

    for i in range(len(u)):
        if u[i] == "(":
            result += ")"
        elif u[i] == ")":
            result += "("
        else:
            raise Exception("invalid data")

    return result


def solution(p):
    if p == "":
        return p

    u, v = splitBalancedStringAndOther(p)

    if checkRightString(u):
        return u + solution(v)
    else:
        return doGenerateStringIfStringIsWrong(u, v)


if __name__ == "__main__":
    assert solution("(()())()") == "(()())()"
    print(solution("(()())()"))

    assert solution(")(") == "()"
    print(solution(")("))

    assert solution("()))((()") == "()(())()"
    print(solution("()))((()"))
