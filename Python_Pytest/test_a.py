import pytest


def func(x):
    return x + 1


@pytest.mark.parametrize('a,b', [
    (1, 2),
    (2, 5),
    (6, 9)
])
def test_answer1(a, b):
    assert func(a) == b


def test_answer2():
    assert func(4) == 5


@pytest.fixture()
def login():
    print('登录操作')
    name = 'Hugo'
    return name


class TestDemo():
    def test_a(self, login):
        print(f"a  login={login} ")

    def test_b(self):
        print("b")

    def test_c(self):
        print("c")


if __name__ == '__main__':
    pytest.main(['test_a.py::TestDemo', '-v'])
