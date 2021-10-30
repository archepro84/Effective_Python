""" 이해하기 쉽도록 모든 변수 및 함수는 중복 선언합니다. """


# list.append 메서드르 이용해 결과를 추가한다.
def fn_1():
    def index_words(text, search_data=' '):
        result = []
        if text:
            result.append(0)
        for index, letter in enumerate(text):
            if letter == search_data:
                result.append(index + 1)
        return result

    address = '컴퓨터(영어: Computer, 문화어: 콤퓨터, 순화어:전산기)는 진공관'
    result = index_words(address)
    print(result[:10])
    pass


# 제너레이터를 생성해 결과값을 반환한다.
def fn_2():
    def index_words_iter(text, search_data=' '):
        if text:
            yield 0
        for index, letter in enumerate(text):
            if letter == search_data:
                yield index + 1

    address = '컴퓨터(영어: Computer, 문화어: 콤퓨터, 순화어:전산기)는 진공관'
    it = index_words_iter(address)
    print(f'Next : {next(it)}')
    print(f'Next : {next(it)}')
    for i in it:  # 반환받은 제너레이터를 For문으로 연산
        print(f'For : {i}')

    result = list(index_words_iter(address))
    print(result[:10])
    pass


# itertools를 사용해
def fn_3():
    def index_file(handle, search_data=' '):
        offset = 0
        for line in handle:
            if line:
                yield offset
            for letter in line:
                offset += 1
                if letter == search_data:
                    yield offset

    try:
        import itertools

        # utf-8 형식으로 파일을 디코딩 하도록 설정.
        with open('address.txt', 'r', encoding='utf-8') as f:
            it = index_file(f)
            results = itertools.islice(it, 0, 10)
            print(list(results))
    except Exception as e:
        print(e)
    pass


if __name__ == '__main__':
    # fn_1()
    # fn_2()
    # fn_3()
    pass
