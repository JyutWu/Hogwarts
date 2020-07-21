import pytest
import yaml


class TestData:

    @pytest.mark.parametrize('a,b', yaml.safe_load(open('./data.yaml')))
    def test_add(self, a, b):
        print(a + b)
