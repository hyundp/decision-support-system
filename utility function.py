from cmath import exp, log, sqrt


class UtilityFunction:
    def __init__(self, _R):
        self.R = _R

    def averse_function1(self, monetary):
        return 1-(exp(-monetary/self.R))

    def averse_function2(self, monetary):
        return log(monetary)

    def averse_funtion3(self, monetary):
        return sqrt(monetary)

