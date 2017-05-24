from channels.channel import Group
import django.dispatch
import json

pizza_done = django.dispatch.Signal(providing_args=["toppings", "size"])

def callback(sender,**kwargs):
    toppings = kwargs['toppings']
    jo = json.loads(toppings)
    data = jo['data']
    for item in data:
        item_id = item['itemid']
        if item_id == 23314:
            print(item)
        Group(str(item_id)).send({'text':json.dumps(item)})

pizza_done.connect(callback)

def ws_connect(message):
    message.reply_channel.send({'accept':True})
    item_id = message.content['path'].strip("/")
    Group(str(item_id)).add(message.reply_channel)

def ws_receive(message):
    item_id = message.content['path'].strip("/")
    #Group(str(item_id)).send({'text':'--------'})

def ws_disconnect(message):
    item_id = message.content['path'].strip("/")
    Group(str(item_id)).discard(message.reply_channel)