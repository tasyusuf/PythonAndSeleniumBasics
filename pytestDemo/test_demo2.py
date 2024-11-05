#any pytest file should start with test_
#pytest method ames should start with test
#method names should have sense
# -k stand for names execution, -s logs in output -v stands for more info metadata
#you can run spesific file with py.test <filename>
#you can mark (tag) tests @pytest.mark.smoke and then run with -m
#fixtures are used as setup and tear down methods for test cases
#conftest file to generalize fixture and make at available for all test cases


import pytest


@pytest.mark.smoke
#@pytest.mark.skip
def test_firstProgram():
    msg = "Hello"
    assert msg == "Hi", "Test failed because strings does not match"

@pytest.mark.xfail
def test_secondCreditCard():
    a = 4
    b = 6
    assert a+2 == 6, "Addition does not match"

@pytest.fixture()
def setup2():
    print("I will be executing first.")

def test_fixtureDemo(setup2):
    print("I will execute steps in fixtureDemo method")