from setuptools import setup

setup(
	name='striper',
	version='0.1',
	packages=['striper'],
	author='dialupfloppy',
	include_package_data=True,
	description='Stripe processing engine with database record keeping and dynamically generated invoices',
	install_requires=[
		'flask',
		'flask-sqlalchemy',
		'stripe'
	],
)
