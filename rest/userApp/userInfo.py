from flask.views import MethodView
from .models import User
from .userschema import UserSchema
from flask.json import jsonify
from flask import request
from rest.ormdb import db

class UserInfo(MethodView):
    def get(self):
        user_info = User.query.all()
        users_schema = UserSchema(many=True)
        results = users_schema.dump(user_info)
        return jsonify(results.data)
    
    def post(self):
        user_info = UserSchema()
        user_info.validate(request.json)
        user_data = request.json
        save_data = User(username=user_data["username"],email = user_data["email"])
        db.session.add(save_data)
        db.session.commit()
        return jsonify({"success":True})
    
    def delete(self,user_id):
        user_info = UserSchema()
        user_details = User.query.get(user_id)
        user_info.validate(user_details)
        db.session.delete(user_details)
        db.session.commit()
        return jsonify({"success":True})
        