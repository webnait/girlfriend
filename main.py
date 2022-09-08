from datetime import date, datetime
import datetime
import time
import math
from wechatpy import WeChatClient
from wechatpy.client.api import WeChatMessage, WeChatTemplate
import requests
import os
import random

nowtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
# today = datetime.now()
start_date = os.environ['START_DATE']
city = os.environ['CITY']
birthday = os.environ['BIRTHDAY']
app_id = os.environ["APP_ID"]
app_secret = os.environ["APP_SECRET"]

user_id = os.environ["USER_ID"]
template_id = os.environ["TEMPLATE_ID"]
birthday_B = "12-01"
o_w ='又是想你的一天'
# o_w = "关于你的一切我想要比谁都懂"
# o_w2 ='此刻我没有勇气放下身边关于你的anything'
O_W = 'I found actually I didn’t like the wrong person.'
O_W2 = 'Just didn’t have enough time to love you deeply.'
O_W3 = 'Trying to say good night, I found myself trapped in sadness.'
O_W4 = 'Until missing you has also bred into a hobby.'
cz = "橙子"
# say_my ='想你'
# say_my = '''每到晚上，总会想起很多很多，总感觉来的是那么突然，却好像又在意料之中。但又不是所想象的那个结局，直到现在，内心还有点小小的期待...
# 脑袋里总不停的闪过跟你的每分每秒，可惜还没等缓过来，进度条就已经被拉到了最后，像是追剧一样，总是对下一集怀着满满的憧憬...
# 每次犯了错，总是少不了的一句理由就是“因为爱你...因为喜欢你...”一直把这些理由挂在嘴边，却忽略了你的感受，把“喜欢”当做了筹码，最后把这仅有的筹码给输的干净，你的好感也一点点减少...
# 总想从你的每句话中猜测你的心情和想法，想逗你开心，无奈等级太低，总是给自己找来一些虚无的小情绪，因为这些小情绪，对你的热情无意间显得好像有些敷衍，有些冷淡、差感觉...
# 也因为这样，很喜欢跟你打电话，你的声音总是能给我带来开心，而我不擅长的言语一直有点儿尴尬。当与一个人用声音交流的时候，这个时候的感受是确切的，还会减少很多用键盘可以打出来却无法说出口的话，增加的是内心的交流...
# 你还是第一个让我对大学有目标的人，在这之前，从来都没有过这些想法...
# 想说早安晚安，却发现除了你，竟找不到可以让我按下Enter键的人，每次为你按下之前，感觉有些空泛，不知道是不是该好好的想一想，但我还是决定按下，因为我不想留下任何一件让我为你后悔的事儿。然后陪着我的就是“安静”，直到听到那一声特别关心的提示音响，才终于深呼一口气，“呼～”...
# 总是在想你，想你此刻会在做什么，夜深失眠，想会不会在另一个地方有一个你也正难眠...
# 看着身边关于你的所有，小皮筋、手机壳、为你敲的每一行代码，都不舍得去变动，到现在，甚至没有勇气从手腕上摘下那个小皮筋，就好像一旦摘下来，离你就更远了...
# 放学回家，本应该激动的向你分享身边发生的事，但迎来的是“冷漠”的空气，“空荡的”卧室，没有一点儿变动的消息框...
# 想如果时间能倒流，我能不能把握的住，心情好复杂，没有了你一切都变得空虚了...还依旧有一个声音浮现，“不要放弃，你再也找不到她这样的女孩了...”可是我该怎么办呢，试着改变难以改变的嘛
# 真的好想去改变，好想你...
# 2022.9.6晚'''
zy = '你一直都是最重要的.'

url_wb = 'http://api.tianapi.com/weibohot/?key=ea30182362d9b0fab6480f883319f68b'
res_wb = requests.get(url_wb).json()['newslist']
wb =[]
for itemwb in res_wb:
    hotword= itemwb['hotword']
    wb.append(hotword)
wb=wb[0:5]
wb1 = wb[0]
wb2 = wb[1]
wb3 = wb[2]
wb4 = wb[3]
wb5 = wb[4]


def get_weather():
  url = "http://autodev.openspeech.cn/csp/api/v2.1/weather?openId=aiuicus&clientType=android&sign=android&city=" + city
  res = requests.get(url).json()
  weather = res['data']['list'][0]
  return weather['weather'], math.floor(weather['temp'])

def get_weather2():
  url = "http://autodev.openspeech.cn/csp/api/v2.1/weather?openId=aiuicus&clientType=android&sign=android&city=" + city
  res = requests.get(url).json()
  weather = res['data']['list'][0]
  return math.floor(weather['low']),math.floor(weather['high']),str(weather['date']),str(weather['wind']),str(weather['humidity'])

# def get_count():
#   delta = nowtime - datetime.strptime(start_date, "%Y-%m-%d")
#   return delta.days
def get_count():
  d1 = datetime.date.today()
  y = int(f'{d1.year}')
  m = int(f'{d1.month}')
  d = int(f'{d1.day}')

  date1=datetime.date(2022,8,6)#这里面year,month,day是代表年，月，日，年必须写成2021这种格式，都必须写成数字
  date2=datetime.date(y,m,d)#同上，这个是第二个日期（后面的），上面的是第一个日期（前面的）
  delta=date2-date1#这是两个日期相减，是一个时间差对象
  diffdays=int(delta.total_seconds()//86400)#差的秒数除以86400即可
  return diffdays+1

# def get_birthday():
#   next = datetime.strptime(str(date.today().year) + "-" + birthday, "%Y-%m-%d")
#   if next < datetime.now():
#     next = next.replace(year=next.year + 1)
#   return (next - today).days

# def get_birthday2():
#   next2 = datetime.strptime(str(date.today().year) + "-" + birthday_B, "%Y-%m-%d")
#   if next2 < datetime.now():
#     next2 = next2.replace(year=next2.year + 1)
#   return (next2 - today).days

def get_words():
  words = requests.get("https://api.shadiao.pro/chp")
  if words.status_code != 200:
    return get_words()
  return words.json()['data']['text']
def tips():
  tips = requests.get("https://api.tianapi.com/healthtip/?key=ea30182362d9b0fab6480f883319f68b")
  if tips.status_code != 200:
    return tips()
  return tips.json()["newslist"][0]['content']

def get_random_color():
  return "#%06x" % random.randint(0, 0xFFFFFF)
def birthday(uyear,umon,uday):
    # 获取当前年月日(单个)
    toyear = time.strftime('%Y', time.localtime(time.time()))  # "%Y"将被无世纪的年份锁代替
    tomon = time.strftime('%m', time.localtime(time.time()))
    today = time.strftime('%d', time.localtime(time.time()))
    toyear = int(toyear)
    tomon = int(tomon)
    today = int(today)
    # 将年月日连接起来，使其成为完整的时间(例：2022 - 03 -27)
    todaynow = time.strftime("%Y-%m-%d", time.localtime())
    todaynow_mon_day = time.strftime("%m-%d", time.localtime())
    # 获取年
    def insert_year():
        # 润年2月29天，平年28天
        flag = True
        while flag:
            input_year = uyear
            input_year = int(input_year)
            # 今年之前出生的
            if input_year <= toyear:
                return input_year
                flag = False
    # 获取月
    def insert_mon():
        flag = True
        while flag:
            input_mon = umon
            input_mon = int(input_mon)
            return input_mon
            flag = False
    # 获取日
    def insert_day():
        flag = True
        while flag:
            input_day = uday
            input_day = int(input_day)
            if input_day > today:
                if input_day > 31 or input_day < 1:
                    continue
                elif input_day == today:
                    flag = False
                    return input_day
                else:
                    return input_day
                    flag = False
            else:
                return input_day
                flag = False
    # 计算还有多少天生日(生日\今天\生日月\生日天)
    def how_long(todaynow, mon, day):
        # 明年的今天
        next_year = int(toyear) + 1
        str3 = str(next_year) + "-" + str(mon) + "-" + str(day)
        str4 = str(int(toyear)) + "-" + str(mon) + "-" + str(day)
        date2 = datetime.datetime.strptime(todaynow[0:10], "%Y-%m-%d")  # 今天
        date3 = datetime.datetime.strptime(str3[0:10], "%Y-%m-%d")  # 明年生日=今年年份+1 +生日的月日
        date4 = datetime.datetime.strptime(str4[0:10], "%Y-%m-%d")  # 今年的年+生日的月日
        num = 0
        # 明年
        # 今天过生日:月日相等
        if mon == tomon:
            if day == today:
                num = 0
            if day > today:
                num = (date4 - date2).days
            if day < today:
                num = (date3 - date2).days
        # 已经过了的生日:明年生日-今天
        elif mon < tomon:
            num = (date3 - date2).days
        # 还没过生日:今年的年+生日的月日 - 今天的年月日
        else:
            num = (date4 - date2).days  # 返回的全部是非0的整数
        return num
    year = insert_year()
    mon = insert_mon()
    day = insert_day()
    num = how_long(todaynow, mon, day)
    return num

client = WeChatClient(app_id, app_secret)

wm = WeChatMessage(client)
wea, temperature= get_weather()
low,high,date_t,wind,humidity= get_weather2()
#data = {"open_word":{"value":o_w,"color":get_random_color()},"today":{"value":date_t,"color":get_random_color()},"city":{"value":city,"color":get_random_color()},"weather":{"value":wea,"color":get_random_color()},"temperature":{"value":temperature,"color":get_random_color()},"low":{"value":low,"color":get_random_color()},"high":{"value":high,"color":get_random_color()},"wind":{"value":wind,"color":get_random_color()},"humidity":{"value":humidity,"color":get_random_color()},"love_days":{"value":get_count(),"color":get_random_color()},"birthday_left":{"value":birthday('2004','1','26'),"color":get_random_color()},"birthday_left2":{"value":birthday('2004','12','1'),"color":get_random_color()},"tips":{"value":tips(), "color":get_random_color()},"words":{"value":get_words(), "color":get_random_color()},"wb1":{"value":wb1, "color":get_random_color()},"wb2":{"value":wb2, "color":get_random_color()},"wb3":{"value":wb3, "color":get_random_color()},"wb4":{"value":wb4, "color":get_random_color()},"wb5":{"value":wb5, "color":get_random_color()},"chengzi":{"value":cz,"color":get_random_color()}}
data = {"dy":{"value":dy,"color":get_random_color()}}
res = wm.send_template(user_id, template_id, data)
print(res)
