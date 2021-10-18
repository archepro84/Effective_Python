""" 이해하기 쉽도록 모든 변수 및 함수는 중복 선언합니다. """


# Closure를 이용해 외부 변수를 참조하는 정렬 도우미 함수
def fn_1():
    def sort_priority(values, group):
        def helper(x):
            if x in group:
                return (0, x)
            return (1, x)

        values.sort(key=helper)

    numbers = [8, 3, 1, 2, 5, 4, 7, 6]
    group = {2, 3, 5, 7}
    sort_priority(numbers, group)
    print(numbers)
    pass


# nonlocal문을 사용해 Closure 밖으로 데이터를 끌어낸다.
def fn_2():
    def sort_priority2(numbers, group):
        found = False

        def helper(x):
            nonlocal found  # Closure 밖으로 found 변수를 끌어낸다.
            if x in group:
                found = True
                return (0, x)
            return (1, x)

        numbers.sort(key=helper)
        return found

    numbers = [8, 3, 1, 2, 5, 4, 7, 6]
    group = {2, 3, 5, 7}
    sort_priority2(numbers, group)
    print(numbers)
    pass


# 사용 방식이 복잡해지면 도우미 함수로 상태를 감싸, nonlocal을 대체한다.
def fn_3():
    class Sorter:
        def __init__(self, group):
            self.group = group
            self.found = False

        def __call__(self, x):
            if x in self.group:
                self.found = True
                return (0, x)
            return (1, x)

    numbers = [8, 3, 1, 2, 5, 4, 7, 6]
    group = {2, 3, 5, 7}

    sorter = Sorter(group)
    numbers.sort(key=sorter)
    assert sorter.found is True
    pass


if __name__ == '__main__':
    # fn_1()
    # fn_2()
    # fn_3()
    pass
