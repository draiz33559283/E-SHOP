from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from routes import main as routes

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('PROD_DATABASE_URI', 'postgresql://user:password@localhost/dbname')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

app.register_blueprint(routes)

if __name__ == '__main__':
    app.run(debug=False)
