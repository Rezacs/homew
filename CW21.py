import redis
# apt list --installed
# pip freeze


r = redis.Redis(host='localhost', port=6379, db=0 , charset="utf-8", decode_responses=True)
r.set('foo', 'bar')
print(r.get('foo'))


p2 = r.pubsub()
p2.subscribe('my-first-channel')

p = r.pubsub()
p.subscribe('my-first-channel', 'my-second-channel')


r.publish('my-first-channel', 'some data salam')
r.publish('my-first-channel', 'awesome data')
r.publish('my-first-channel', 'gggggggg')




# print('dovvomi' ,  p.get_message())
# message = p.get_message()
def my_handler(message):
    print('MY HANDLER: ', message['data'])


# listen to all channels
# print(r.pubsub_channels())
# for i in p.listen() :
#     print(i)

#listen to only one channel
# print(r.pubsub_channels())
# for i in p2.listen() :
#     print(i)

print(r.pubsub_channels())
for i in p2.listen() :
    my_handler(i)

