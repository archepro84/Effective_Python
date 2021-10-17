""" 이해하기 쉽도록 모든 변수 및 함수는 중복 선언합니다. """


# 결과를 5자리의 튜플로 반환하는 함수 제작
def fn_1():
    lengths = [63, 73, 72, 60, 67, 66, 71, 61, 72, 70]

    def get_stats(numbers):
        minimum = min(numbers)
        maximum = max(numbers)
        count = len(numbers)
        average = sum(numbers) / count
        sorted_numbers = sorted(numbers)
        middle = count // 2
        if count % 2 == 0:
            lower = sorted_numbers[middle - 1]
            upper = sorted_numbers[middle]
            median = (lower + upper) / 2
        else:
            median = sorted_numbers[middle]

        return minimum, maximum, average, median, count

    minimum, maximum, average, median, count = get_stats(lengths)

    print(f'최소 길이: {minimum}, 최대 길이: {maximum}')
    print(f'평균: {average}, 중앙값: {median}, 개수: {count}')

    pass


# 함수를 호출하는 부분과 반환 값을 언패킹하는 부분이 길어지고, 코드 줄이 바뀔 수 있어 가독성이 나빠진다.
def fn_2():
    lengths = [63, 73, 72, 60, 67, 66, 71, 61, 72, 70]

    def get_stats(numbers):
        minimum = min(numbers)
        maximum = max(numbers)
        count = len(numbers)
        average = sum(numbers) / count
        sorted_numbers = sorted(numbers)
        middle = count // 2
        if count % 2 == 0:
            lower = sorted_numbers[middle - 1]
            upper = sorted_numbers[middle]
            median = (lower + upper) / 2
        else:
            median = sorted_numbers[middle]

        return minimum, maximum, average, median, count

    # 반환값이 늘어날 수록 언패킹할 변수의 갯수가 늘어나며 코드의 길이도 늘어난다.
    minimum, maximum, average, median, count = get_stats(
        lengths)

    minimum, maximum, average, median, count = \
        get_stats(lengths)

    (minimum, maximum, average,
     median, count) = get_stats(lengths)

    (minimum, maximum, average, median, count
     ) = get_stats(lengths)

    print(minimum, maximum, average, median, count)
    pass


if __name__ == '__main__':
    # fn_1()
    # fn_2()
    pass
