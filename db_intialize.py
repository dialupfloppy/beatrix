from striper import db
from striper.models import Product, Client, Sale


db.create_all()

#match product db to stripe plans
#item = []
#for x in 1,2,3,4,5,6,7,8:
#	item.add=Product.query.get(x)

item1=Product(subscription=False, description='1 Remote Support Session', amount='5000', name='oneRemote')
item2=Product(subscription=False, description='2 Remote Support Sessions', amount='9000', name='twoRemote')
item3=Product(subscription=False, description='3 Remote Support Sessions', amount='13000', name='threeRemote')
item4=Product(subscription=True, description='Monthly Computer Check-up', amount='10000', name='monthlySupport')
item5=Product(subscription=True, description='Weekly Computer Check-up', amount='25000', name='weeklySupport')
item6=Product(subscription=True, description='On-Call Computer Support', amount='35000', name='oncallSupport')
#db.session.add(Product(description='Adblocking Service Setup', amount='5500'))
item7=Product(subscription=True, description='Adblocking Service', amount='500', name='adblock')
item8=Product(subscription=True, description='Cloud Phone Service', amount='4000', name='basicPhone')

db.session.add(item1)
db.session.add(item2)
db.session.add(item3)
db.session.add(item4)
db.session.add(item5)
db.session.add(item6)
db.session.add(item7)
db.session.add(item8)

#firstsale = Sales(order_id='1000')
#alter table for auto increment
#engine = db.engine
#connection = engine.connect()

#firstsale = connection.execute("ALTER TABLE sale MODIFY COLUMN id INT auto_increment = 1")
#firstsale = connection.execute("ALTER TABLE sale AUTO_INCREMENT = 10000")
db.engine.execute("ALTER TABLE sale AUTO_INCREMENT=10000")

#db.session.add(product1, product2, product3, product4, product5, product6, product7, product8, product9)
db.session.commit()
