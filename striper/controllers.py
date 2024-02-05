import os
#import logging
from flask import Flask, render_template, request, redirect, session
import stripe
from striper import app, db
from striper.models import Product, Client, Sale

stripe_keys = {
'secret_key': os.environ['SECRET_KEY'],
'publishable_key': os.environ['PUBLISHABLE_KEY']
}

stripe.api_key = stripe_keys['secret_key']

#charge = Blueprint('charge', __name__)
#app = Flask(__name__)

@app.route('/')
def result():
	return render_template('index.html')

@app.route('/support')
#get help now
def support():
	return render_template('support.html')

@app.route('/connect', methods=['POST', 'GET'])
def connect():
	#if method == 'POST':
		#validate email input
		#email = request.form.get('email')
		#client = Client.query.filter_by(email=email).last_or_404()
		#sale = Sale.query.filter_by(client_id=client.id, paid=True).first_or_404()
	if method == 'GET':
	#validate input
		var = request.args.get('id')
		sale = Sale.query.filter_by(uuid=id, paid=True).last_or_404()
	if sale.remain > 0:
		sale.remain -= 1
		#generated or constant support code
		code='value'
		#db session update?
		db.session.commit()
		#email connection html
		return render_template('connect.html', connect_string=code)
	else:
		return render_template('depleted.html')

@app.route('/product', methods=['POST', 'GET'])
def button():
	if method == 'POST':
		id=request.form.get('id')
	else method =='GET':
		id=request.args.get('id')

	product=Product.get_or_404(id)
	return render_template('buy.html', description=product.description, amount=product.amount, id=product.id, key=stripe_keys['publishable_key'])

@app.route('/charge', methods = ['POST'])
def create():
	#if method == 'POST':
	product_id = request.form.get_or_404('product_id')
	email = request.form.get('stripeEmail')
	token = request.form.get('stripeToken')
	#sale = Sale.query.filter_by(product_id=product.id, client_id=current.id, paid=False).first()
	product = Product.query.get_or_404(product_id)
	current = Client.query.filter_by(email=email).first()
	if current:
		token = current.customer_id
	else:
		createCustomer = stripe.Customer.create(
			email=email,
			source=token)
		token = createCustomer.id
		current=(Client(email=email, customer_id=token))
		db.session.add(current)

	uuid=str(uuid.uuid4())
	remain = 1
	#if product.subscription = False:
	#remain = 1
	#if product.id == 2:
		#remain = 2
	#elif product.id = 3:
		#remain == 3
	try:
		charge = stripe.Charge.create(
			customer = token,
			amount = product.amount,
			currency="usd",
			description=product.description
			#statement_descriptor="Custom descriptor",
			#metadata={'uuid': uuid}
		)
	except stripe.CardError, e:
		return render_template('fail.html')

	#sale.paid = True
	#else:
	#not subscription

	#if product_id ==  8:
		#setup_fee = '5500'
	#else:
		#setup_fee = '0'
	#try:
	#subscribe = stripe.Subscription.create(
		#customer=token,
		#account_balance=setup_fee,
		#items=[{"plan": "monthlySupport",},]
		#)

	#email UUID and/or receipt
	#beatrix.io/connect?id=uuid

	sale = Sale(product_id=product.id, paid=True, remain=remain, uuid=uuid, client_id=current.id)
	db.session.add(sale)
	db.session.commit()
	return render_template('result.html', email=email, product=product.description, amount=int(product.amount / 100))

@app.route('/invoice', methods=['POST'])
def invoice():
	if method == 'POST':
		#if request.form.get('form_id') == "whiskerbisker:"
		id = request.form.get('id')
		description = request.form.get('description')
		#email = request.form.get('email')
		subscription = request.form.get('subscription')
		amount = request.form.get('amount')
		#name = request.form.get('name')
		query=Product.get(id)
		if query:
			query.amount=amount
			db.session.commit()
			return render_teplate ('success.html')
		else:
			product = Product(description=description, subscription=subscription, amount=amount, name=name)
			db.session.add(product)
			db.session.commit()

	#check with stripe plan for consistency
	#generate invoice
	#email (bcc to notify) html link to product?product=product.id route

	return render_template('product_add.html', id=product.id, name=product.name, subscription=product.subscripition, product=product.description, amount=int(product.amount / 100))

#@app.route('/<uuid>/')
# methods=['POST'])
#def pull_invoice(uuid):

	#query from database
	#Product.query.filter_by(Invoice.uuid.any(address=address))

	#charges = Invoice.query(uuid).order_by(desc(Invoice.date)).all()
	#invoice = tuple(charges)

	#invoices = [for charge in Invoice.query(uuid).order_by(desc(Invoice.date)).all()]
	#invoices = []
	#for charge in charges:
		#invoices.append(dict(charge))

#for charge in charges:
	#	print dict(charge.description(),charge.amount())
	#if no uuid - 404
#	return render_template('invoice.html', key=stripe_keys['publishable_key'], description=newCharge.description, amount=newCharge.amount)
	#add form variable to discner dymanically created invoices and regular charges - update DB
	#delete uuid in form.
