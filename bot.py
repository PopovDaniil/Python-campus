import vk_api, math, datetime, random
import requests
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

kbfile = open("keyboard.json",'r',encoding="UTF-8")
keyboard = kbfile.read()

vk_session = vk_api.VkApi(token="878fce9d7476eb28d019f8aa393e2a720030c1350acb857e3cbe4150c96fc6981de6417ae556611573220")
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, "187553815")
att = ''

for event in longpoll.listen(): 
    if event.type == VkBotEventType.MESSAGE_NEW:
        if event.obj.text != '': 
            if event.from_user:
                text = event.obj.text.lower()
                text = text.split(' ')
                if (len (text) == 2 )and(text[0] == 'погода'):
                    now = datetime.datetime.now()
                    city = text[1]
                    res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                    params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': 'ff804351b97f7a93823cbf829df18b62'})
                    data = res.json()
                    print(data)
                    if data['cod'] == '404':
                        reply = "Такого города не существует"
                        att = 'photo-187553815_457239027'
                    else:
                        descr = data['weather'][0]['description'].title()
                        reply = "Погодные условия: " + descr + '\n'
                        if descr == "Ясно":
                            if now.hour > 21:
                                att = 'photo-187553815_457239021'
                            elif now.strftime('%a') == "Sun":
                                att = random.choice(['photo-187553815_457239022','photo-187553815_457239023'])
                            else:
                                att = 'photo-187553815_457239018'
                        elif ((descr == "Пасмурно") or (descr == 'Слегка Облачно')):
                            if (now.hour > 16) and (now.hour < 20): 
                                att = 'photo-187553815_457239020'
                            else:
                                att = 'photo-187553815_457239019'
                        elif ((descr == "Дождь") or (descr == 'Легкий Дождь')):
                            if (now.hour > 8) and (now.hour < 18): 
                                att = 'photo-187553815_457239017'
                            else:
                                att = 'photo-187553815_457239026'
                        else:
                            att = ''
                        
                        if data['main']['temp'] > 0:
                            sign = '+'
                        else:
                            sign = '-'
                            
                        reply += "Температура: " + sign + str(round(data['main']['temp']))+ '\n'
                        reply += "Влажность: " + str(data['main']['humidity']) + '%\n'
                        reply += "Атмосферное давление " + str(round(data['main']['pressure']*0.750063755419211)) + ' мм. рт. ст.'        
                else:
                    reply='Неверная команда'
                    att = 'photo-187553815_457239024'
                vk.messages.send(
                        user_id=event.obj.from_id,
                        random_id=get_random_id(),
                        message=reply,
                        keyboard=keyboard,
                        attachment=att)