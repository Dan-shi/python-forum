import asyncio

import www.orm as orm

from www.model.model import User, Blog, Comment
async def test(loop):
    await orm.create_pool(loop, user='root', password='root', db='pythonForum')
    # u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')
    userList=[]
    userList = await User.findAll()
    for u in userList:
        print(u)
    #print(u for u in userList)

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))