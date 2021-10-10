# immutable 순서쌍을 생성하는 tuple 내장 타입
def fn_1():
    snack_calories = {
        '감자칩': 140,
        '팝콘': 80,
        '땅콩': 190,
    }
    items = tuple(snack_calories)
    print(items)
    print(items[0], '&', items[1])
    pass


# tuple의 인자값을 Unpacking
def fn_2():
    item = ('호박엿', '식혜')
    first, second = item
    print(first, '&', second)
    pass


# 여러 계층의 iterable을 가진 dictionary를 Unpacking
def fn_3():
    favorite_snacks = {
        '짭조름한 과자': ('프레즐', 100),
        '달콤한 과자': ('쿠키', 180),
        '채소': ('당근', 20),
    }

    ((type1, (name1, cals1)),
     (type2, (name2, cals2)),
     (type3, (name3, cals3))) = favorite_snacks.items()

    print(f'제일 좋아하는 {type1} 는 {name1}, {cals1} 칼로리입니다.')
    print(f'제일 좋아하는 {type2} 는 {name2},  {cals2} 칼로리입니다.')
    print(f'제일 좋아하는 {type3} 는 {name3},  {cals3} 칼로리입니다.')
    pass


# Unpacking을 이용해 내부 원소를 맞바꾸기 ☆
def fn_4():
    names = ['프레즐', '당근', '쑥갓', '베이컨']
    names[1], names[0] = names[0], names[1]
    print(names)
    pass


# Unpacking을 이용해 내부의 모든 원소를 맞바꾸기 ☆
def fn_5():
    snacks = [('베이컨', 350), ('도넛', 240), ('머핀', 190)]

    for rank, (name, calories) in enumerate(snacks, 1):
        print(f'#{rank}: {name} 은 {calories} 칼로리입니다.')
    pass


if __name__ == '__main__':
    # fn_1()
    # fn_2()
    # fn_3()
    # fn_4()
    fn_5()
    pass