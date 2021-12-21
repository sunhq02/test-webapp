from orm import Model, StringField, IntegerField
import orm
import asyncio
import aiomysql


class User(Model):
    __table__ = 'user'

    id = IntegerField(primary_key=True)
    name = StringField()


async def test():
    await orm.create_pool(user='root', password='admin', db='test')
    # rs = await orm.select('select * from user')
    user = User(id=13, name='Peppa')
    await user.update()
    users = await User.findAll()
    for u in users:
        print(u.id, u.name)
    # print(rs)

loop = asyncio.get_event_loop()
loop.run_until_complete(test())
# asyncio.run(test())
