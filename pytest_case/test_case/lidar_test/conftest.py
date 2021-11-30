import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--tester", action="store", default="lidar", help="my option: type1 or type2"
    )
    parser.addoption(
        "--thresh", action="store", default=0.01, help="my option: type1 or type2"
    )
# @pytest.fixture
# def tester(request):
#     return request.config.getoption("--tester")
# @pytest.fixture(scope='session')
# def get_name(request):
#     return request.config.getoption("--name")


# def pytest_generate_tests(metafunc):
#     if "get_name" in metafunc.fixturenames:
#         if metafunc.config.getoption("name"):
#             param = str(metafunc.config.getoption("name"))
#         else:
#             param = "default"
#         metafunc.parametrize("get_name", [param])


# def pytest_collection_modifyitems(items):
#     for item in items:
#         # check that we are altering a test named `test_run_name`
#         # and it accepts the `get_name` arg
#         if item.originalname == 'test_run_name' and 'get_name' in item.fixturenames:
#             item._nodeid = item.nodeid.replace(']', '').replace('run_name[', '')