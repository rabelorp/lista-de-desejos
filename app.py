import os
from flask import Flask, request, jsonify, render_template, Response
from flask_sqlalchemy import SQLAlchemy
import json 

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Wishlist 

@app.route("/getall")
def get_all():
    try:
        wishlists = Wishlist.query.all()
        return jsonify([e.serialize() for e in wishlists]), 200
    except Exception as e:
        return Response(str(e), status=500, mimetype='application/json')


@app.route("/get/<id_>", methods=["GET"])
def get_by_id(id_):
    try:
        wishlist = Wishlist.query.filter_by(id=id_).first()  
        return jsonify(wishlist.serialize()), 200
    except Exception as e:
        return Response(str(e), status=500, mimetype='application/json')

@app.route("/add", methods=['POST'])
def add_wishlist():
    body = request.get_json()  
    try:
        wishlist = Wishlist(
            title = body["title"],
            description = body["description"],
            link = body["link"],
            photo = body["photo"]
        )
        db.session.add(wishlist)
        db.session.commit()  
        return jsonify(wishlist.serialize()), 201
    except Exception as e:
        return Response(str(e), status=500, mimetype='application/json') 
 

@app.route("/update/<id_>", methods=['PUT'])
def update_by_id(id_):
    wishlist = Wishlist.query.filter_by(id=id_).first() 
    body = request.get_json()  
    try: 
        wishlist.title = body["title"]
        wishlist.description = body["description"]
        wishlist.link = body["link"]
        wishlist.photo = body["photo"]
        
        db.session.commit()   
        return jsonify(wishlist.serialize()), 200
    except Exception as e:
        return Response(str(e), status=500, mimetype='application/json')  


@app.route("/delete/<id_>", methods=['DELETE'])
def delete_by_id(id_):
    wishlist = Wishlist.query.filter_by(id=id_).first()
    try:  
        db.session.delete(wishlist)
        db.session.commit()   
        return jsonify(), 200
    except Exception as e:
        return Response(str(e), status=500, mimetype='application/json')  


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
