""" 이해하기 쉽도록 모든 변수 및 함수는 중복 선언합니다. """


# get과 대입식으로 key가 dictionary에 있는지 확인
def fn_1():
    pictures = {}
    path = 'profile_1234.png'

    if (handle := pictures.get(path)) is None:
        try:
            handle = open(path, 'a+b')
        except OSError:
            print(f'경로를 열 수 없습니다: {path}')
            raise
        else:
            pictures[path] = handle
    print(pictures)
    pass


# path가 dictionary에 존재하지않으면 __missing__ 특별메소드로 key를 생성
def fn_2():
    path = 'profile_1234.png'

    def open_picture(profile_path):
        try:
            return open(profile_path, 'a+b')
        except OSError:
            print(f'경로를 열 수 없습니다: {profile_path}')
            raise

    class Pictures(dict):
        def __missing__(self, key):
            value = open_picture(key)
            self[key] = value
            return value

    pictures = Pictures()
    handle = pictures[path]  # 최초 호출시 __missing__ 특별 메소드 호출
    handle.seek(0)  # 파일 객체를 읽는 포인터 위치를 처음으로 변경
    image_data = handle.read()
    print(image_data)
    pass


if __name__ == '__main__':
    # fn_1()
    # fn_2()
    pass
