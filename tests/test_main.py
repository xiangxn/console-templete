from console.main import *

class TestMain(object):
    logfile = open("./log/test.log", 'a')

    def test_the_function(self):
        output = 2
        assert output == 2, "Doh! Got %s instead" % (output)
