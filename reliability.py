# 분야별로 신뢰도 가중치를 작성

class Reliability:
    def __init__(self):
        """생성자"""
        do = 0
        min = 0
        dong = 0
        ji = 0

    def business(self):
        do = 3
        min = 1.5
        go = 1

    def design(self):
        do = 1
        min = 3
        go = 3

    def web_develop(self):
        do = 2
        min = 0.5
        go = 2

    def algorithm(self):
        do = 3
        min = 2
        go = 2

    def marketing(self):
        do = 1
        min = 2
        go = 1.9
