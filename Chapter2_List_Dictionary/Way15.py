""" 이해하기 쉽도록 모든 변수 및 함수는 중복 선언합니다. """


# dictionary의 데이터 삽입이 입력된 순서로 정렬
def fn_1():
    def my_func(**kwargs):
        print(kwargs.items())
        for key, value in kwargs.items():
            print(f'{key} = {value}')

    my_func(goose='gosling', kangaroo='joey')  # 3.5와 3.7이후가 다름
    pass


# 표준 Python dictionary를 이용해 rank를 출력
def fn_2():
    votes = {
        'otter': 1281,
        'polar bear': 587,
        'fox': 863,
    }

    def populate_ranks(votes, ranks):
        names = list(votes.keys())
        names.sort(key=votes.get, reverse=True)
        for i, name in enumerate(names, 1):
            ranks[name] = i

    def get_winner(ranks):  # 첫 번째 키의 인자값을 반환
        return next(iter(ranks))

    ranks = {}
    populate_ranks(votes, ranks)
    print(ranks)
    winner = get_winner(ranks)
    print(winner)
    pass


# SortedDict를 이용해 알파벳 순으로 출력
def fn_3():
    from collections.abc import MutableMapping

    # 내용을 알파벳 순서대로 이터레이션 해주는 Class
    class SortedDict(MutableMapping):
        def __init__(self):
            self.data = {}

        def __getitem__(self, key):
            return self.data[key]

        def __setitem__(self, key, value):
            self.data[key] = value

        def __delitem__(self, key):
            del self.data[key]

        def __iter__(self):
            keys = list(self.data.keys())
            keys.sort()
            for key in keys:
                yield key

        def __len__(self):
            return len(self.data)

    def populate_ranks(votes, ranks):
        names = list(votes.keys())
        names.sort(key=votes.get, reverse=True)
        for i, name in enumerate(names, 1):
            ranks[name] = i

    def get_winner(ranks):
        return next(iter(ranks))

    votes = {
        'otter': 1281,
        'polar bear': 587,
        'fox': 863,
    }

    # 추상 메서드를 이용해 dict를 정의했지만, 원하는 값이 출력되지않는다.
    sorted_ranks = SortedDict()
    populate_ranks(votes, sorted_ranks)
    print(sorted_ranks.data)
    winner = get_winner(sorted_ranks)
    print(winner)

    # dictionary가 특정 순서로 이터레이션 된다고 가정하지않고, 별도의 도우미 함수를 구현하여 해결한다.
    def get_winner(ranks):
        for name, rank in ranks.items():
            if rank == 1:
                return name

    winner = get_winner(sorted_ranks)
    print(winner)

    # 함수 맨 앞에 특정 타입이 우리가 원하는 타입인지 검사하는 코드를 추가한다.
    def get_winner(ranks):
        if not isinstance(ranks, dict):
            raise TypeError('dict 인스턴스가 필요합니다')
        return next(iter(ranks))

    try:
        winner = get_winner(sorted_ranks)
        print(winner)
    except Exception as e:
        print(f'Error: {e}')
    pass


# 타입 애너테이션을 사용해서 get_winner에 전달되는 값이 dict 인스턴스가 되도록 강제한다.
def fn_4():
    from typing import Dict, MutableMapping

    def populate_ranks(votes: Dict[str, int],
                       ranks: Dict[str, int]) -> None:
        names = list(votes.keys())
        names.sort(key=votes.get, reverse=True)
        for i, name in enumerate(names, 1):
            ranks[name] = i

    def get_winner(ranks: Dict[str, int]) -> str:
        return next(iter(ranks))

    class SortedDict(MutableMapping[str, int]):
        def __init__(self):
            self.data = {}

        def __getitem__(self, key):
            return self.data[key]

        def __setitem__(self, key, value):
            self.data[key] = value

        def __delitem__(self, key):
            del self.data[key]

        def __iter__(self):
            keys = list(self.data.keys())
            keys.sort()
            for key in keys:
                yield key

        def __len__(self):
            return len(self.data)

    votes = {
        'otter': 1281,
        'polar bear': 587,
        'fox': 863,
    }

    sorted_ranks = SortedDict()
    populate_ranks(votes, sorted_ranks)
    print(sorted_ranks.data)
    winner = get_winner(sorted_ranks)
    print(winner)

    """
    # mypy를 이용해 검사할 경우 type에러가 발생한다. ☆
    $ python -m mypy --strict Way15.py
    
    Way15.py:155: error: Argument 2 to "populate_ranks" has incompatible type "SortedDict"; expected "Dict[str, int]"
    Way15.py:157: error: Argument 1 to "get_winner" has incompatible type "SortedDict"; expected "Dict[str, int]"    
    """
    pass


if __name__ == '__main__':
    # fn_1()
    # fn_2()
    # fn_3()
    # fn_4()
    pass
