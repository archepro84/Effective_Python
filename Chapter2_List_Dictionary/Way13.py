""" 이해하기 쉽도록 모든 변수 및 함수는 중복 선언합니다. """


# 언패킹할 원소의 갯수를 모를 경우 오류가 발생한다.
def fn_1():
    try:
        car_ages = [0, 9, 4, 8, 7, 20, 19, 1, 6, 15]
        car_ages_descending = sorted(car_ages, reverse=True)  # 20 0 [19, 15, 9, 8, 7, 6, 4, 1]
        oldest, second_oldest = car_ages_descending
    except Exception as e:
        print(e)  # too many values to unpack (expected 2)
    pass


# starred expression을 이용해 나머지 모든 값을 변수에 담는다.
def fn_2():
    car_ages = [0, 9, 4, 8, 7, 20, 19, 1, 6, 15]
    car_ages_descending = sorted(car_ages, reverse=True)
    print(car_ages_descending)  # [20, 19, 15, 9, 8, 7, 6, 4, 1, 0]

    oldest, *result = car_ages_descending
    print(oldest, result)  # 20 [19, 15, 9, 8, 7, 6, 4, 1, 0]

    oldest, second_oldest, *others = car_ages_descending
    print(oldest, second_oldest, others)  # 20 19 [15, 9, 8, 7, 6, 4, 1, 0]
    pass


# Unpacking 해야만 하는 값 외에 여분의 슬라이스가 하나 또는 나머지를 모두 잡아낼 때 사용할 수 있다.
def fn_3():
    car_ages = [0, 9, 4, 8, 7, 20, 19, 1, 6, 15]
    car_ages_descending = sorted(car_ages, reverse=True)
    print(car_ages_descending)  # [20, 19, 15, 9, 8, 7, 6, 4, 1, 0]

    oldest, *others, youngest = car_ages_descending
    print(oldest, youngest, others)  # 20 0 [19, 15, 9, 8, 7, 6, 4, 1]

    *others, second_youngest, youngest = car_ages_descending
    print(youngest, second_youngest, others)  # 0 1 [20, 19, 15, 9, 8, 7, 6, 4]
    pass


# 한 수준의 Unpacking 패턴에서 별표 식을 두 개 이상 사용할 수 없다.
def fn_4():
    # first, *middle, *second_middle, last = [1, 2, 3, 4]
    pass


# 여러 계층으로 이뤄진 구조를 Unpacking할 때는 서로 다른 부분에서는 별표 식을 여럿 사용해도 된다.
def fn_5():
    car_inventory = {
        '시내': ('그랜저', '아반테', '티코'),
        '공항': ('제네시스 쿠페', '소나타', 'K5', '악센트'),
    }

    ((loc1, (best1, *rest1)),
     (loc2, (best2, *rest2))) = car_inventory.items()
    print(f'{loc1} 최고는 {best1}, 나머지는 {len(rest1)} 종')
    print(f'{loc2} 최고는 {best2}, 나머지는 {len(rest2)} 종')
    print(rest1)  # ['아반테', '티코']
    print(rest2)  # ['소나타', 'K5', '악센트']
    pass


# Unpacking 결과값에 남는 원소가 없다면 별표 식 인스턴스는 빈 리스트가 된다. []
def fn_6():
    short_list = [1, 2]
    first, second, *rest = short_list
    print(first, second, rest)
    pass


# iterator의 내용을 Header와 Body로 쉽게 나눠서 처리할 수 있고, 깔끔하게 코드를 구성할 수 있다.
def fn_7():
    def generate_csv():
        yield ('날짜', '제조사', '모델', '연식', '가격')
        for i in range(100):
            yield ('2019-03-25', '현대', '소나타', '2010', '2400만원')
            yield ('2019-03-26', '기아', '프라이드', '2008', '1400만원')

    it = generate_csv()  # csv 제너레이터 생성
    header, *rows = it
    print('CSV 헤더:', header)
    print('행 수: ', len(rows))
    pass


if __name__ == '__main__':
    # fn_1()
    # fn_2()
    # fn_3()
    # fn_4()
    # fn_5()
    # fn_6()
    fn_7()
    pass
