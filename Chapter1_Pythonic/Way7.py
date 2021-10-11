# enumerate에서 루프 인덱스와 이터레이터의 다음 값으로 이뤄진 쌍을 전달받음
def fn_1():
    flavor_list = ['바닐라', '초콜릿', '피칸', '딸기']

    it = enumerate(flavor_list)
    print(next(it))  # iterator의 다음 원소를 가져온다.
    print(next(it))
    pass


# enumerate를 range 대신 for 문에서 Unpacking할 수 있다.
def fn_2():
    flavor_list = ['바닐라', '초콜릿', '피칸', '딸기']

    for i, flavor in enumerate(flavor_list):
        print(f'{i + 1} : {flavor}')
    pass


# enumerate는 index의 시작 위치를 지정하고 iterator를 조회할 수 있다.
def fn_3():
    flavor_list = ['바닐라', '초콜릿', '피칸', '딸기']

    for i, flavor in enumerate(flavor_list, 1):
        print(f'{i}: {flavor}')
    pass


if __name__ == '__main__':
    # fn_1()
    # fn_2()
    # fn_3()
    pass
