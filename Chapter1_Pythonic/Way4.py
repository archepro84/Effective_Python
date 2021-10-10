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


# 형식화 식에 Dictionary를 사용하면 문장이 번잡스러워진다.
def fn_11():
    soup = 'lenti'
    formatted = 'Today\'s soup is %(soup)s.' % {'soup': soup}
    print(formatted)
    pass


# 긴 형식화 식을 여러 줄로 나눠 써서 하나로 합치고, 형식화에 사용할 Dictionary에 넣을 값을 한 줄에 나열해야 한다.
def fn_12():
    menu = {
        'soup': 'lentil',
        'oyster': 'tongyoung',
        'special': 'scnitzel',
    }
    template = ("Today\'s soup is %(soup)s, "
                "buy one get two %(oyster)s oysters, "
                "and our special entree is %(special)s.")
    formatted = template % menu
    print(formatted)
    pass


# format 내장 함수 : 오래된 C 스타일 형식화 문자열보다 더 표현력이 좋은 고급 문자열 형식화 기능
def fn_13():
    a = 1234.5678
    formatted = format(a, ',.2f')  # 천 단위의 구분자를 표시
    print(formatted)

    b = 'my 문자열'
    formatted = format(b, '^20s')  # ^ : 중앙에 값을 표시
    print('*', formatted, '*')
    pass


# str.format : %d와 같은 C 스타일 형식화 지정자를 사용하는 대신 위치 지정자 {}를 사용할 수 있다.
def fn_14():
    key = 'my_var'
    value = 1.234

    formatted = '{} = {}'.format(key, value)
    print(formatted)
    pass


# 위치 지정자는 콜론 뒤에 형식 지정자를 붙여 넣어 문자열에 값을 넣을 때 어떤 형식으로 변환할 지 정할 수 있다.
def fn_15():
    key = 'my_var'
    value = 1.234

    formatted = '{:<10} = {:.2f}'.format(key, value)
    print(formatted)
    pass


# C 스타일 형식화 문자열에서 %를 표시하고 싶으면 %%로 이스케이프해야 한다.
def fn_16():
    print('%.2f%%' % 12.5)
    print('{} replaces {{}}'.format(1.23))
    pass


# 위치 지정자 중괄호에 위치 인덱스, 전달된 인자의 순서를 전달할 수 있다.
def fn_17():
    key = 'my_var'
    value = 1.234

    formatted = '{1} = {0}'.format(key, value)
    print(formatted)

    # 위치 인덱스를 여러번 사용할 수 있다.
    name = '철수'
    formatted = '{0}는 음식을 좋아해. {0}가 요리하는 모습을 봐요.'.format(name)
    print(formatted)
    pass


# 형식화를 하기 전에 값을 변경해야 하는 경우에는 코드 읽기가 어려워진다.
def fn_18():
    pantry = [
        ('아보카도', 1.25),
        ('바나나', 2.5),
        ('체리', 15),
    ]

    for i, (item, count) in enumerate(pantry):
        old_style = '#%d: %-10s = %d' % (
            i + 1,
            item.title(),
            round(count))

        new_style = '#{}: {:<10s} = {}'.format(
            i + 1,
            item.title(),
            round(count))

    assert old_style == new_style
    pass


# str.format과 함께 사용하는 형식 지정자에는 dictionary Key나 list Index를 조합해 사용하거나 유니코드나 repr 문자열로 변환한다.
def fn_19():
    menu = {
        'soup': 'lentil',
        'oyster': 'tongyoung',
        'special': 'scnitzel',
    }

    formatted = '첫번째 글자는 {menu[oyster][0]!r}'.format(
        menu=menu)
    print(formatted)
    pass


# f-문자열
def fn_20():
    key = 'my_var'
    value = 1.234
    formatted = f'{key} = {value}'
    print(formatted)

    formatted = f'{key!r:<10} = {value:.2f}'
    print(formatted)
    pass


# f-String에 형식 지정자 옵션을 변수를 사용해 적용 ☆
def fn_21():
    places = 3
    number = 1.23456
    print(f'내가 고른 숫자는 {number:.{places}f}')
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
    # fn_10()
    # fn_11()
    # fn_12()
    # fn_13()
    # fn_14()
    # fn_15()
    # fn_16()
    # fn_17()
    # fn_18()
    # fn_19()
    # fn_20()
    # fn_21()
    pass
