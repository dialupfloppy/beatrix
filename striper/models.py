from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from striper import db
import sys
import os
import datetime

class Product(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(30))
	subscription = db.Column(db.Boolean, default=0)
	description = db.Column(db.String(160))
	amount = db.Column(db.Integer)
	def __init__(self, description, amount, name, subscription):
		self.description = description
		self.amount = amount
		self.name = name
		self.subscription = subscription
	def __repr__(self):
		return self.description, self.amount, self.name, self.subscription

class Client(db.Model):
	# __tablename__ = 'client'
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(120))
	customer_id = db.Column(db.String(40), unique=True)
	def __init__(self, email, customer_id):
		self.customer_id = customer_id
		self.email = email
	def __repr__(self):
		return self.customer_id, self.email

class Sale(db.Model):
	#__tablename__ = 'invoice'
	id = db.Column(db.Integer, primary_key=True)
	#order_id = db.Column(db.Integer, unique=True)
	#db.sequence('orderid_seq'),
	uuid = db.Column(db.String(64), unique=True, nullable=True)
	#description = db.Column(db.String(160))
	#price = db.Column(db.Float)
	paid = db.Column(db.Boolean)
	remain = db.Column(db.Integer, nullable=True)
	created = db.Column(db.DateTime, nullable=False,  default=datetime.datetime.utcnow(),
		onupdate=datetime.datetime.utcnow()
	)
	client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
	client = db.relationship(Client)
	product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
	product = db.relationship(Product)

	def __init__(self, paid, uuid, remain, client_id, product_id):
		self.paid = paid
		self.uuid = uuid
		self.remain = remain
		self.client_id = client_id
		self.product_id = product_id
	def __repr__(self):
		return self.description, self.price, self.paid, self.remain, self.client_id, self.client_id
