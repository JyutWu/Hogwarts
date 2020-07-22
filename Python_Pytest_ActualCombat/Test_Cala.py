import pytest
import yaml

from Cacl import Calculator


# 参数化与fixture结合使用
# 情况一：传入值和数据
# 情况二：传入一个fixture方法，将数据传入到fixture方法中
#       fixture方法使用ruquest参数来接受这组数据，在方法体里使用request.param来使用这组数据

# @pytest.mark.parametrize('a,b,result', [
#     (1, 2, 3),
#     (200, 300, 700),
#     (0.1, 0.1, 0.2),
#     (-1, -2, -3),
#     ('a','b','c')
# ], ids=['int1', 'bigdata', 'float', 'minus','str'])

fnum= yaml.safe_load(open('./first.yaml'))
snum= yaml.safe_load(open('./second.yaml'))


@pytest.mark.parametrize('a', fnum,ids=[f'{fnum[i][0]}' for i in range(len(fnum))])
@pytest.mark.parametrize('b', snum,ids=[f'{snum[i][0]}' for i in range(len(snum))])
# def test_yaml(a,b):
#     result = a[1] + b[1]
#     print(result)

# 加法
def test_add(a, b, Tips):
    cal = Calculator()
    result = a[1] + b[1]
    assert result == cal.add(a[1], b[1])


@pytest.mark.parametrize('a', fnum,ids=[f'{fnum[i][0]}' for i in range(len(fnum))])
@pytest.mark.parametrize('b', snum,ids=[f'{snum[i][0]}' for i in range(len(snum))])
# 减法
def test_sub(a, b, Tips):
    cal = Calculator()
    result = a[1] - b[1]
    assert result == cal.sub(a[1], b[1])


@pytest.mark.parametrize('a', fnum,ids=[f'{fnum[i][0]}' for i in range(len(fnum))])
@pytest.mark.parametrize('b', snum,ids=[f'{snum[i][0]}' for i in range(len(snum))])
# 除法
def test_div(a, b, Tips):
    cal = Calculator()
    result = a[1] / b[1]
    assert result == cal.div(a[1], b[1])


@pytest.mark.parametrize('a', fnum,ids=[f'{fnum[i][0]}' for i in range(len(fnum))])
@pytest.mark.parametrize('b', snum,ids=[f'{snum[i][0]}' for i in range(len(snum))])
# 乘法
def test_mul(a, b, Tips):
    cal = Calculator()
    result = a[1] * b[1]
    assert result == cal.mul(a[1], b[1])
