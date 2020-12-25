from itertools import permutations


def solution(numbers):
    nums = generatePermutation(numbers)
    nums = list(set(nums))  # delete duplicated element

    return countPrimeNumber(nums)


def generatePermutation(numbers):
    nums = []

    for i in range(1, len(numbers) + 1):
        permutation = list(map(''.join, permutations(numbers, i)))
        for j in permutation:
            nums.append(int(j))

    return nums


def countPrimeNumber(numbers):
    count = 0

    for number in numbers:
        if number == 0 or number == 1:  #  0, 1 은 확실하게 소수가 아니기 때문에 건너뜀
            continue

        if number == 2 or number == 3:  #  2, 3 은 소수 이기 때문에 카운트 증가
            count += 1
            continue

        for dividingNumber in range(2, number):
            if number % dividingNumber == 0:
                break

            if dividingNumber == number - 1:
                count += 1

    return count


if __name__ == "__main__":
    assert(solution("17") == 3)
    assert(solution("011") == 2)
    assert(solution("00000") == 0)

