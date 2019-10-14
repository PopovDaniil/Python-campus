import vk_api
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

vk_session = vk_api.VkApi(token="878fce9d7476eb28d019f8aa393e2a720030c1350acb857e3cbe4150c96fc6981de6417ae556611573220")
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, "187553815")

for event in longpoll.listen(): 
    if event.type == VkBotEventType.MESSAGE_NEW:
        if event.obj.text != '': 
            if event.from_user:
                if event.obj.text == "secret":
                    reply = ":)"
                else:
                    reply = "))))"
                vk.messages.send(
                        user_id=event.obj.from_id,
                        random_id=get_random_id(),
                        message=reply)