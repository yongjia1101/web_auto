import allure
import pytest
from pytest import assume


def test_x():
    with allure.step("步骤1"):
        # pytest.assume(1 == 1)
        print("1")
        with assume: assert 1 == 1

    with allure.step("步骤2"):
        # pytest.assume(2 == 2)
        print("2")
        with assume: assert 2 == 2

    with allure.step("步骤3"):
        # pytest.assume(3 ==3)
        print("3")
        with assume: assert 3 == 3

