from flask import Flask,render_template
from flask_migrate import Migrate
from rest.ormdb import db
from flask_marshmallow import Marshmallow
from rest.userApp.userInfo import UserInfo






app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
db.init_app(app)
app.app_context().push()
db.create_all()
migrate = Migrate(app, db)



app.add_url_rule("/", view_func=UserInfo.as_view("userinfo"),methods=["GET","POST"])
app.add_url_rule("/<user_id>", view_func=UserInfo.as_view("userinfo_delete"),methods=["DELETE"])



