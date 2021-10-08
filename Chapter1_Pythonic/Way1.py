# $ python --version

# sys 모듈을 이용한 Python version 출력
def fn_1():
    import sys
    print(sys.version_info)
    print(sys.version)


if __name__ == '__main__':
    fn_1()

