""" 이해하기 쉽도록 모든 변수 및 함수는 중복 선언합니다. """


# 인자를 배열로 받는 정규화 함수 정의
def fn_1():
    def normalize(numbers):
        total = sum(numbers)
        result = []
        for value in numbers:
            percent = 100 * value / total
            result.append(percent)
        return result

    # 제너레이터를 반환
    def read_visits(data_path):
        with open(data_path) as f:
            for line in f:
                yield int(line)

    it = read_visits('my_numbers.txt')
    percentages = normalize(it)  # 반환받은 제너레이터를 삽입한다.
    print(type(it))
    print(percentages)
    print()

    it = read_visits('my_numbers.txt')
    print(list(it))  # 제너레이터의 모든 원소를 출력
    print(list(it))  # 제너레이터의 모든 원소가 소진되어 있음
    pass


# 입력 이터레이터를 명시적으로 소진시키고 전체 내용을 리스트에 넣어 오류를 검출
def fn_2():
    def normalize_copy(numbers):
        numbers_copy = list(numbers)  # 이터레이터 복사
        total = sum(numbers_copy)
        result = []
        for value in numbers_copy:
            percent = 100 * value / total
            result.append(percent)
        return result

    # 제너레이터를 반환
    def read_visits(data_path):
        with open(data_path) as f:
            for line in f:
                yield int(line)

    it = read_visits('my_numbers.txt')
    percentages = normalize_copy(it)
    print(percentages)
    assert sum(percentages) == 100.0

    pass


# 호출될 때마다 새로운 이터레이터를 반환하는 함수를 생성
def fn_3():
    def normalize_func(get_iter):
        total = sum(get_iter())  # 새 이터레이터
        result = []
        for value in get_iter():  # 새 이터레이터
            percent = 100 * value / total
            result.append(percent)
        return result

    # 제너레이터를 반환
    def read_visits(data_path):
        with open(data_path) as f:
            for line in f:
                yield int(line)

    path = 'my_numbers.txt'
    # 매번 제너레이터를 호출해서 새 이터레이터를 만들어냄
    percentages = normalize_func(lambda: read_visits(path))
    print(percentages)
    assert sum(percentages) == 100.0
    pass


# 이터레이터 프로토콜(iterator protocol)을 구현한 새로운 컨테이너 클래스를 제공
def fn_4():
    def normalize(numbers):
        total = sum(numbers)  # 새로운 이터레이터 객체를 할당
        result = []
        for value in numbers:  # 새로운 이터레이터 객체를 할당
            percent = 100 * value / total
            result.append(percent)
        return result

    class ReadVisits:
        def __init__(self, data_path):
            self.data_path = data_path

        # __iter__를 호출할 때마다 파일을 읽음
        def __iter__(self):
            with open(self.data_path) as f:
                for line in f:
                    yield int(line)

    path = 'my_numbers.txt'
    visits = ReadVisits(path)
    percentages = normalize(visits)
    print(percentages)
    assert sum(percentages) == 100.0
    pass


# 입력값이 반복적으로 이터레이션할 수 없는 경우 TypeError를 발생시켜 인자를 거부한다.
def fn_5():
    def normalize_defensive(numbers):
        if iter(numbers) is numbers:  # 이터레이터 -- 나쁨!
            raise TypeError('컨테이너를 제공해야 합니다')
        total = sum(numbers)
        result = []
        for value in numbers:
            percent = 100 * value / total
            result.append(percent)
        return result

    # 제너레이터를 반환
    def read_visits(data_path):
        with open(data_path) as f:
            for line in f:
                yield int(line)

    path = 'my_numbers.txt'
    visits = read_visits(path)
    try:
        percentages = normalize_defensive(visits)
        print(percentages)
        assert sum(percentages) == 100.0
    except Exception as e:
        print(e)
    pass


# collections.abc 내장 모듈은 isinstance를 통해 잠재적인 문제를 검사할 수 있는 Iterator 클래스를 제공한다.
def fn_6():
    from collections.abc import Iterator

    def normalize_defensive(numbers):
        if isinstance(numbers, Iterator):  # 반복 가능한 이터레이터인지 검사하는 다른 방법
            raise TypeError('컨테이너를 제공해야 합니다')
        total = sum(numbers)
        result = []
        for value in numbers:
            percent = 100 * value / total
            result.append(percent)
        return result

    class ReadVisits:
        def __init__(self, data_path):
            self.data_path = data_path

        # __iter__를 호출할 때마다 파일을 읽음
        def __iter__(self):
            with open(self.data_path) as f:
                for line in f:
                    yield int(line)

    path = 'my_numbers.txt'

    # List 입력
    visits = [15, 35, 80]
    percentages = normalize_defensive(visits)
    assert sum(percentages) == 100.0
    print(type(visits))
    print(percentages)

    # ReadVisits 입력
    visits = ReadVisits(path)
    percentages = normalize_defensive(visits)
    assert sum(percentages) == 100.0
    print(type(visits))
    print(percentages)

    # 컨테이너가 아닌 이터레이터
    try:
        visits = [15, 35, 80]
        it = iter(visits)
        print(type(it))
        normalize_defensive(it)
    except Exception as e:
        print(e)
    pass


if __name__ == '__main__':
    # fn_1()
    # fn_2()
    # fn_3()
    # fn_4()
    # fn_5()
    # fn_6()
    pass
