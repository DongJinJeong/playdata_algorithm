# 2016년
import datetime
def solution(a, b):
    answer = {0 : "MON", 1 : "TUE", 2 : "WED", 3 : "THU", 4 : "FRI", 5 : "SAT", 6 : "SUN"}
    dt = datetime.datetime(2016, a, b)
    return answer[dt.weekday()]