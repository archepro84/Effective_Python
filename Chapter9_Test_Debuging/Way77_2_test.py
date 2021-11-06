from unittest import TestCase, main


def setUpModule():
    print('* 모듈 설정')


def tearDownModule():
    print('* 모듈 정리')


# TestCase 클래스가 들어 있는 모듈 안에 setUpModule과 tearDownModule 메서드를 정의
class IntegrationTest(TestCase):
    def setUp(self):
        print('* 테스트 설정')

    def tearDown(self):
        print('* 테스트 정리')

    def test_end_to_end1(self):
        print('* 테스트 1')

    def test_end_to_end2(self):
        print('* 테스트 2')


if __name__ == '__main__':
    main()
    """
    * 모듈 설정
    * 테스트 설정
    * 테스트 1
    * 테스트 정리
    .* 테스트 설정
    * 테스트 2
    * 테스트 정리
    .* 모듈 정리
    """