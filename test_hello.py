from hello import toyou, add, subtract


def setup_function(function):
    print(f" Running Setup: {function.__name__}")
    function.me = 10


def teardown_function(function):
    print(f" Running Teardown: {function.__name__}")
    del function.me


### Run to see failed test
#def test_hello_add():
#    assert add(test_hello_add.x) == 12

def test_hello_subtract():
    assert subtract(test_hello_subtract.me) == 9