import vk_api
import requests
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

vk_session = vk_api.VkApi(token="878fce9d7476eb28d019f8aa393e2a720030c1350acb857e3cbe4150c96fc6981de6417ae556611573220")
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, "187553815")

for event in longpoll.listen(): 
    if event.type == VkBotEventType.MESSAGE_NEW:
        if event.obj.text != '': 
            if event.from_user:
                str = event.obj.text.split(' ')
                if str[0] == 'погода':
                    city = input('Введите город:')
                    res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                    params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': 'ff804351b97f7a93823cbf829df18b62'})
                    data = res.json()
                    reply += "conditions:" + data['weather'][0]['description']
                    reply +="temp:", data['main']['temp']
                    reply +="temp_min:", data['main']['temp_min']
                    reply +="temp_max:", data['main']['temp_max']
                vk.messages.send(
                        user_id=event.obj.from_id,
                        random_id=get_random_id(),
                        message=reply)