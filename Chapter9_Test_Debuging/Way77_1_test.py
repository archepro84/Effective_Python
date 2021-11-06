""" 이해하기 쉽도록 모든 변수 및 함수는 중복 선언합니다. """

from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase, main


# 테스트를 진행하기 전에 임시 디렉터리를 만들고 테스트가 끝난 후 티렉터리의 내용을 지우는 TestCase
class EnvironmentTest(TestCase):
    def setUp(self):
        self.test_dir = TemporaryDirectory()
        self.test_path = Path(self.test_dir.name)

    def tearDown(self):
        self.test_dir.cleanup()

    def test_modify_file(self):
        with open(self.test_path / 'data.bin', 'w') as f:
            pass


if __name__ == '__main__':
    main()

