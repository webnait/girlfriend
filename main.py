from datetime import date, datetime
import math
from wechatpy import WeChatClient
from wechatpy.client.api import WeChatMessage, WeChatTemplate
import requests
import os
import random

today = datetime.now()
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

def get_count():
  delta = today - datetime.strptime(start_date, "%Y-%m-%d")
  return delta.days

def get_birthday():
  next = datetime.strptime(str(date.today().year) + "-" + birthday, "%Y-%m-%d")
  if next < datetime.now():
    next = next.replace(year=next.year + 1)
  return (next - today).days

def get_birthday2():
  next2 = datetime.strptime(str(date.today().year) + "-" + birthday_B, "%Y-%m-%d")
  if next2 < datetime.now():
    next2 = next2.replace(year=next2.year + 1)
  return (next2 - today).days

def get_words():
  words = requests.get("https://api.shadiao.pro/chp")
  if words.status_code != 200:
    return get_words()
  return words.json()['data']['text']
def tips():
  tips = requests.get("http://api.tianapi.com/healthtip/index?key=9253f567ff2efb17d32ca831ed327983&")
  if tips.status_code != 200:
    return tips()
  return tips.json()["newslist"][0]['content']

def get_random_color():
  return "#%06x" % random.randint(0, 0xFFFFFF)


client = WeChatClient(app_id, app_secret)

wm = WeChatMessage(client)
wea, temperature= get_weather()
low,high,date_t,wind,humidity= get_weather2()
data = {"open_word":{"value":o_w,"color":get_random_color()},"today":{"value":date_t,"color":get_random_color()},"city":{"value":city,"color":get_random_color()},"weather":{"value":wea,"color":get_random_color()},"temperature":{"value":temperature,"color":get_random_color()},"low":{"value":low,"color":get_random_color()},"high":{"value":high,"color":get_random_color()},"wind":{"value":wind,"color":get_random_color()},"humidity":{"value":humidity,"color":get_random_color()},"love_days":{"value":get_count(),"color":get_random_color()},"birthday_left":{"value":get_birthday(),"color":get_random_color()},"birthday_left2":{"value":get_birthday2(),"color":get_random_color()},"tips":{"value":tips(), "color":get_random_color()},"words":{"value":get_words(), "color":get_random_color()},"chengzi":{"value":cz,"color":get_random_color()}}
res = wm.send_template(user_id, template_id, data)
print(res)
