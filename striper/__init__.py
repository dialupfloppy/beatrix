from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
#app.register_blueprint('charge')
app.config.from_object('config')
db = SQLAlchemy(app)

toolbar = DebugToolbarExtension(app)

import controllers, models


if __name__ == '__main__':
        app.run(debug = True)


#from models import Invoice, Client
#from controllers import charge

#app.register_blueprint(invoice, url_prefix='/invoice')
#app.config.from_object('config')
#db = SQLAlchemy(app)

#import app.views
#from striper.app.views import charge
#invoice
