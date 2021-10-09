# % 형식화 연산자
def fn_1():
    a = 0b10111011
    b = 0xc5f
    print('이진수: %d, 십육진수; %d' % (a, b))
    pass


# 형식화 식에서 오른족에 있는 tuple 내 데이터 값의 순서를 바꾸거나 값의 타입을 바꾸면 타입 변환이 불가능
def fn_2():
    key = 'my_var'
    value = 1.234
    formatted = '%-10s = %.2f' % (key, value)
    print(formatted)
    reordered_tuple = '%-10s = %.2f' % (value, key)
    pass


# 형식화 식의 형식 문자열의 순서를 변경하면 에러 발생
def fn_3():
    key = 'my_var'
    value = 1.234
    reordered_string = '%.2f = %-10s' % (key, value)
    pass


# 형식화를 하기 전에 값을 변경해야 한다면 식을 읽기가 매우 어려워진다.
def fn_4():
    pantry = [
        ('아보카도', 1.25),
        ('바나나', 2.5),
        ('체리', 15),
    ]
    for i, (item, count) in enumerate(pantry):
        print('#%d: %-10s = %.2f' % (i, item, count))
    pass


# 출력된 메시지를 변경, tuple의 길이가 너무 길어져, 그로 인해 가독성이 나빠진다.
def fn_5():
    pantry = [
        ('아보카도', 1.25),
        ('바나나', 2.5),
        ('체리', 15),
    ]
    for i, (item, count) in enumerate(pantry):
        print('#%d: %-10s = %d' % (
            i + 1,
            item.title(),
            round(count)
        ))
    pass


# 형식화 문자열에서 같은 값을 여러 번 사용하고 싶다면 튜플에서 같은 값을 여러 번 반복해야 한다
def fn_6():
    template = '%s는 음식을 좋아해. %s가 요리하는 모습을 봐요'
    name = '철수'
    formatted = template % (name, name)
    print(formatted)
    pass


# title 메소드가 추가된 formatted 호출
def fn_7():
    template = '%s는 음식을 좋아해. %s가 요리하는 모습을 봐요'
    name = '영희'
    formatted = template % (name.title(), name.title())
    print(formatted)
    pass


# %연산자의 Dictionary를 이용한 형식화
def fn_8():
    key = 'my_var'
    value = 1.234

    old_way = '%-10s = %.2f' % (key, value)

    new_way = '%(key)-10s = %(value).2f' % {'key': key, 'value': value}  # 원래 방식
    reordered = '%(key)-10s = %(value).2f' % {'value': value, 'key': key}  # 바꾼 방식

    assert old_way == new_way == reordered
    pass


# 형식화에 Dictionary를 사용하면 여러 형식 지정자에 같은 키를 지정할 수 있어서 같은 값을 반복하지 않아도 된다.
def fn_9():
    name = '철수'
    template = '%s는 음식을 좋아해. %s가 요리하는 모습을 봐요'

    before = template % (name, name)  # Tuple
    template = '%(name)s는 음식을 좋아해. %(name)s가 요리하는 모습을 봐요'
    after = template % {'name': name}  # Dictionary
    print(before)
    print(after)

    assert before == after
    pass


# Dictionary 형식 문자열의 문제
def fn_10():
    pantry = [
        ('아보카도', 1.25),
        ('바나나', 2.5),
        ('체리', 15),
    ]
    for i, (item, count) in enumerate(pantry):
        before = '#%d: %-10s = %d' % (
            i + 1,
            item.title(),
            round(count))

        after = '#%(loop)d: %(item)-10s = %(count)d' % {
            'loop': i + 1,
            'item': item.title(),
            'count': round(count),
        }

        assert before == after
    pass


def fn_11():
    pass


def fn_12():
    pass


def fn_13():
    pass


def fn_14():
    pass


def fn_15():
    pass


def fn_16():
    pass


def fn_17():
    pass


def fn_18():
    pass


def fn_19():
    pass


if __name__ == '__main__':
    # fn_1()
    # fn_2()
    # fn_3()
    # fn_4()
    # fn_5()
    # fn_6()
    # fn_7()
    # fn_8()
    # fn_9()
    fn_10()
    # fn_11()
    # fn_12()
    # fn_13()
    # fn_14()
    # fn_15()
    # fn_16()
    # fn_17()
    # fn_18()
    # fn_19()
    pass
