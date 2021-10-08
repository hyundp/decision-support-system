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
        dong = 1
        ji = 1

    def design(self):
        do = 1
        min = 3
        dong = 1
        ji = 1.5

    def develop(self):
        do = 2
        min = 1
        dong = 1.5
        ji = 3

    def algorithm(self):
        do = 2
        dong = 3
        min = 1
        ji = 1.5

    def marketing(self):
        do = 1
        dong = 1
        ji = 1
        min = 2
