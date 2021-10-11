names = ['Cecilia', '남궁민수', '毛泽东']
counts = [len(n) for n in names]  # 리스트 컴프리헨션으로 새로운 리스트 생성


# names의 소스 리스트 길이를 이용해 이터레티션
def fn_1():
    longest_name = None
    max_count = 0

    for i in range(len(names)):
        count = counts[i]
        if count > max_count:
            longest_name = names[i]
            max_count = count
    print(longest_name, max_count)
    pass


# range(len())을 enumerate로 변경
def fn_2():
    longest_name = None
    max_count = 0

    for i, name in enumerate(names):
        count = counts[i]
        if count > max_count:
            longest_name = name
            max_count = count
    print(longest_name, max_count)
    pass


# zip를 이용해 2개 이상의 이터레이터를 tuple로 묶어준다.
def fn_3():
    longest_name = None
    max_count = 0

    for name, count in zip(names, counts):
        if count > max_count:
            longest_name = name
            max_count = count
    print(longest_name, max_count)
    pass


# 입력받은 이터레이터의 길이 중 가장 짧은 길이만큼 tuple을 생성한다.
def fn_4():
    names.append('New Parameter')
    print(names)
    for name, count in zip(names, counts):
        print(name)
    pass


# zip과는 다르게 존재하지 않는 값을 자신에게 전달된 fillvalue로 대신한다. (Default = None)
def fn_5():
    import itertools

    names.append('New Parameter')
    print(names)

    for name, count in itertools.zip_longest(names, counts, fillvalue=0):
        print(f'{name}: {count}')
    pass


if __name__ == '__main__':
    # fn_1()
    # fn_2()
    # fn_3()
    # fn_4()
    # fn_5()
    pass
