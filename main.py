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
o_w = "又是爱你的一天 宝贝"
cz = "橙子"

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
data = {"open_word":{"value":o_w,"color":get_random_color()},"today":{"value":date_t,"color":get_random_color()},"city":{"value":city,"color":get_random_color()},"weather":{"value":wea,"color":get_random_color()},"temperature":{"value":temperature,"color":get_random_color()},"low":{"value":low,"color":get_random_color()},"high":{"value":high,"color":get_random_color()},"wind":{"value":wind,"color":get_random_color()},"humidity":{"value":humidity,"color":get_random_color()},"love_days":{"value":get_count(),"color":get_random_color()},"birthday_left":{"value":birthday('2004','1','26'),"color":get_random_color()},"birthday_left2":{"value":birthday('2004','12','1'),"color":get_random_color()},"tips":{"value":tips(), "color":get_random_color()},"words":{"value":get_words(), "color":get_random_color()},"chengzi":{"value":cz,"color":get_random_color()}}
res = wm.send_template(user_id, template_id, data)
print(res)
