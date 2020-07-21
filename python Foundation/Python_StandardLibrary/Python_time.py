"""
time 模块
time.time()时间戳
timesleep()等待
timelocaltime0时间戳转成时间元组
time.strftime()将当前的时间戳转成带格式的时间
格式：timestrftime(“％Y-％m-％d%H-%M-%S",time.localtime())

"""
import time

# print(time.asctime())
# print(time.time())
# print(time.localtime())
# print(time.strftime("%Y{y}%m{m}%d{d} %H:%M:%S", time.localtime()).format(y='年', m='月', d='日'))
# print(time.strftime('%Y{y}%m{m}%d{d} %H:%M:%S').format(y='年', m='月', d='日', h='时', f='分', s='秒'))

# 获取三天后的时间
now_timetamp = time.time()
three_day_after = now_timetamp + 60 * 60 * 24 * 3
time_tuple=time.localtime(three_day_after)
print(time.strftime("%Y{y}%m{m}%d{d} %H:%M:%S", time_tuple).format(y='年', m='月', d='日'))
