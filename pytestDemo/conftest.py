import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executing first.")
    yield
    print("I will be executed last")

@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["Yusuf", "Tas", "ytas@abc.com"]

@pytest.fixture(params=["chrome","edge"])
def crossBrowser(request):
    return request.param