""" 이해하기 쉽도록 모든 변수 및 함수는 중복 선언합니다. """


# Walrus operator로 변수 생성을 줄인다.
def fn_1():
    fresh_fruit = {
        '사과': 10,
        '바나나': 8,
        '레몬': 5,
    }

    def make_lemonade(count):
        n = 1
        print(f'레몬 {count * n} 개로 레모네이드 {count // n} 개를 만듭니다.')
        fresh_fruit['레몬'] -= (count * n)
        print(f'레몬이 {fresh_fruit["레몬"]} 개 남았습니다.')

    def out_of_stock():
        print(f'제료가 부족합니다. 재료를 보충해 주세요.')

    if count := fresh_fruit.get('레몬', 0):
        make_lemonade(count)
    else:
        out_of_stock()
    pass


# Walrus operator로 대입 후 평가한다.
def fn_2():
    fresh_fruit = {
        '사과': 10,
        '바나나': 8,
        '레몬': 5,
    }

    def make_cider(count):
        n = 4
        print(f'사과 {count} 개로 사과주스 {count // n} 개를 만듭니다.')
        fresh_fruit['사과'] -= (n * (count // n))
        print(f'사과가 {fresh_fruit["사과"]} 개 남았습니다.')

    def out_of_stock():
        print(f'제료가 부족합니다. 재료를 보충해 주세요.')

    if (count := fresh_fruit.get('사과', 0)) >= 4:
        make_cider(count)
    else:
        out_of_stock()
    pass


# Walrus 연산자를 이용해 pieces 변수의 중요성을 명확하게 이해할 수 있다.
def fn_3():
    fresh_fruit = {
        '사과': 10,
        '바나나': 8,
        '레몬': 5,
    }

    def slice_bananas(count):
        print(f'바나나 {count} 개를 슬라이스합니다.')
        fresh_fruit['바나나'] -= count
        return count

    class OutOfBananas(Exception):
        pass

    def make_smoothies(count):
        n = 2
        if count > n:
            print(f'바나나 슬라이스 {count} 개로 스무디 {count // n} 개를 만듭니다.')
            print(f'바나나가 {fresh_fruit["바나나"]} 개 남았습니다.')
        else:
            raise OutOfBananas

    def out_of_stock():
        print(f'제료가 부족합니다. 재료를 보충해 주세요.')

    pieces = 0
    if (count := fresh_fruit.get('바나나', 0)) >= 2:
        pieces = slice_bananas(count)

    try:
        smoothies = make_smoothies(pieces)
    except OutOfBananas:
        out_of_stock()
    pass


# Walrus 연산자를 이용해 들여쓰기와 내포를 줄여서 구현
def fn_4():
    fresh_fruit = {
        '사과': 10,
        '바나나': 8,
        '레몬': 5,
    }

    def slice_bananas(count):
        print(f'바나나 {count} 개를 슬라이스합니다.')
        fresh_fruit['바나나'] -= count
        return count

    class OutOfBananas(Exception):
        pass

    def make_smoothies(count):
        n = 2
        if count > n:
            print(f'바나나 슬라이스 {count} 개로 스무디 {count // n} 개를 만듭니다.')
            print(f'바나나가 {fresh_fruit["바나나"]} 개 남았습니다.')
        else:
            raise OutOfBananas

    def make_cider(count):
        n = 4
        print(f'사과 {count} 개로 사과주스 {count // n} 개를 만듭니다.')
        fresh_fruit['사과'] -= (n * (count // n))
        print(f'사과가 {fresh_fruit["사과"]} 개 남았습니다.')

    def make_lemonade(count):
        n = 1
        print(f'레몬 {count * n} 개로 레모네이드 {count // n} 개를 만듭니다.')
        fresh_fruit['레몬'] -= (count * n)
        print(f'레몬이 {fresh_fruit["레몬"]} 개 남았습니다.')

    if (count := fresh_fruit.get('바나나', 0)) >= 2:
        pieces = slice_bananas(count)
        to_enjoy = make_smoothies(pieces)
    elif (count := fresh_fruit.get('사과', 0)) >= 4:
        to_enjoy = make_cider(count)
    elif count := fresh_fruit.get('레몬', 0):
        to_enjoy = make_lemonade(count)
    else:
        to_enjoy = '아무것도 없음'
    pass


# Walrus 연산자로 while 문을 짧고 읽기 쉽게 구현
def fn_5():
    import random

    def pick_fruit():
        if random.randint(1, 10) > 2:  # 80% 확률로 새 과일 보충
            return {
                '사과': random.randint(0, 10),
                '바나나': random.randint(0, 10),
                '레몬': random.randint(0, 10),
            }
        else:
            return None

    def make_juice(fruit, count):
        if fruit == '사과':
            return [('사과주스', count / 4)]
        elif fruit == '바나나':
            return [('바나나스무디', count / 2)]
        elif fruit == '레몬':
            return [('레모네이드', count / 1)]
        else:
            return []

    bottles = []
    while fresh_fruit := pick_fruit():
        for fruit, count in fresh_fruit.items():
            batch = make_juice(fruit, count)
            bottles.extend(batch)

    for bottle in bottles:
        print(bottle)
    pass


# Switch/case를 대체하는 match/case
def fn_6():
    fruit = '사과'
    match fruit:
        case '사과':
            print(f'fruit는 사과 입니다.')
        case '바나나':
            print(f'fruit는 바나나 입니다.')
        case '레몬':
            print(f'fruit는 레몬 입니다.')
    pass


if __name__ == '__main__':
    # fn_1()
    # fn_2()
    # fn_3()
    # fn_4()
    # fn_5()
    # fn_6()
    pass
