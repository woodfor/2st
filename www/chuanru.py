import orm,asyncio
from models import User, Blog, Comment

async def test(loop):

    await orm.create_pool(loop=loop,user='www-data', password='www-data', database='awesome')
    u = User(name='jxk', email='jxk@example.com', passwd='0987654321', image='about:blank')
    await u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()
