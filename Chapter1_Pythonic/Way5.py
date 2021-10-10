from urllib.parse import parse_qs

my_values = parse_qs('빨강=5&파랑=0&초록=',
                     keep_blank_values=True)


# dictionary의 Key값이 존재하는지 확인하는 도우미 함수
def fn_1():
    def get_first_int(values, key, default=0):
        found = values.get(key, [''])
        if found[0]:
            return int(found[0])
        return default

    print(get_first_int(my_values, '빨강'))
    print(get_first_int(my_values, '초록'))
    print(get_first_int(my_values, '검정'))
    pass


if __name__ == '__main__':
    fn_1()
    pass
