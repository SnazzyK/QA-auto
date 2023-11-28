import pytest

@pytest.fixture()
def set_up():
    print("Start test\n------------------------------------------")
    yield
    print("Finish test\n------------------------------------------")


@pytest.fixture(scope="module")
def set_group():
    print("Enter system")
    yield
    print("Exit system")