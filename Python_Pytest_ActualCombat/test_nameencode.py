import pytest
import yaml

with open("./third.yaml") as f:
    datas = yaml.safe_load(f)
    testids = datas.keys()
    testdatas = datas.values()


@pytest.mark.parametrize('a', datas, ids=testids)
def test_encode(a):
    print(f'{datas[a]}')
