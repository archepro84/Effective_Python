""" 이해하기 쉽도록 모든 변수 및 함수는 중복 선언합니다. """


# dictionary의 setdefault와 get메서드와 대입식을 구현
def fn_1():
    visits = {
        '미국': {'뉴욕', '로스엔젤레스'},
        '일본': {'하코네'},
    }

    visits.setdefault('프랑스', set()).add('칸')  # 짧다

    if (japan := visits.get('일본')) is None:  # 길다
        visits['일본'] = japan = set()

    japan.add('교토')

    print(visits)
    pass


# Visits 클래스의 add 도우미 메서드를 이용해 setdefault의 가독성을 높혀준다.
def fn_2():
    class Visits:
        def __init__(self):
            self.data = {}

        def add(self, country, city):
            city_set = self.data.setdefault(country, set())  # country가 없을 경우 set 생성
            city_set.add(city)

    visits = Visits()
    visits.add('Russia', '예카테린부르크')
    visits.add('Tanzania', '잔지바르')
    print(visits.data)
    pass


# collections.defaultdict : key가 없을 때 자동으로 Default Value를 저장한다.
def fn_3():
    from collections import defaultdict

    class Visits:
        def __init__(self):
            self.data = defaultdict(set)

        def add(self, country, city):
            self.data[country].add(city)

    visits = Visits()
    visits.add('영국', '바스')
    visits.add('영국', '런던')
    print(visits.data)
    pass


if __name__ == '__main__':
    # fn_1()
    # fn_2()
    # fn_3()
    pass
