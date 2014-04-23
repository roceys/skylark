from models import User
from CURD import fn, sql

# create data..
User.create(name='jack')
User.create(name='jack')
User.create(name='foo')

# select count(user.id) as count_id, user.name from user group by user.name having count_id >= '2'
query = User.groupby(User.name).having(
    sql('count_id') >= 2
).select(fn.count(User.id).alias('count_id'), User.name)
result = query.execute()
user, func = result.one()  # user.name, func.count_id
