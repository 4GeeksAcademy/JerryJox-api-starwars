"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for, json
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, Film, User, Character, Starship, Planet, Cha_Favs, Pla_Favs, Shi_Favs, Collaboration
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

# ACÁ EMPIEZAN LOS ENDPOINTS

######################################################
# endpoint para consultar todos los datos de una tabla
######################################################


@app.route('/user', methods=['GET'])
def handle_user():

    results = User.query.all()
    # users_list = list(map(lambda item: item.serialize(),results))
    data = [user.serialize() for user in results]

    response_body = {
        "msg": "Hello, this is your GET /user response ",
        "results": data
    }

    return jsonify(response_body), 200


@app.route('/character', methods=['GET'])
def handle_character():

    results = Character.query.all()
    characters_list = list(map(lambda item: item.serialize(),results))

    response_body = {
        "msg": "Hello, this is your GET /character response ",
        "results": characters_list
    }

    return jsonify(response_body), 200


@app.route('/starship', methods=['GET'])
def handle_starship():

    results = Starship.query.all()
    starships_list = list(map(lambda item: item.serialize(),results))

    response_body = {
        "msg": "Hello, this is your GET /starship response ",
        "results": starships_list
    }

    return jsonify(response_body), 200 


@app.route('/planet', methods=['GET'])
def handle_planet():

    results = Planet.query.all()
    planets_list = list(map(lambda item: item.serialize(),results))

    response_body = {
        "msg": "Hello, this is your GET /planet response ",
        "results": planets_list
    }

    return jsonify(response_body), 200


@app.route('/cha_favs', methods=['GET'])
def handle_cha_favs():

    results = Cha_Favs.query.all()
    cha_favs_list = list(map(lambda item: item.serialize(),results))

    response_body = {
        "msg": "Hello, this is your GET /cha_favs response ",
        "results": cha_favs_list
    }

    return jsonify(response_body), 200


@app.route('/shi_favs', methods=['GET'])
def handle_shi_favs():

    results = Shi_Favs.query.all()
    shi_favs_list = list(map(lambda item: item.serialize(),results))

    response_body = {
        "msg": "Hello, this is your GET /shi_favs response ",
        "results": shi_favs_list
    }

    return jsonify(response_body), 200


@app.route('/pla_favs', methods=['GET'])
def handle_pla_favs():

    results = Pla_Favs.query.all()
    pla_favs_list = list(map(lambda item: item.serialize(),results))

    response_body = {
        "msg": "Hello, this is your GET /pla_favs response ",
        "results": pla_favs_list
    }

    return jsonify(response_body), 200


@app.route('/film', methods=['GET'])
def handle_film():

    results = Film.query.all()
    films_list = list(map(lambda item: item.serialize(),results))

    response_body = {
        "msg": "Hello, this is your GET /film response ",
        "results": films_list
    }

    return jsonify(response_body), 200


@app.route('/collaboration', methods=['GET'])
def handle_collaboration():

    results = Collaboration.query.all()
    collaborations_list = list(map(lambda item: item.serialize(),results))

    response_body = {
        "msg": "Hello, this is your GET /collaboration response ",
        "results": collaborations_list
    }

    return jsonify(response_body), 200    


################################################
# endpoint para consultar un dato en una tabla #
################################################


@app.route('/user/<int:id>', methods=['GET'])
def get_user(id):
    print(id)

    user = User.query.filter_by(id=id).first()
    # user = User.query.get(id)
    print(user.serialize())
    # results = User.query.all()
    # users_list = list(map(lambda item: item.serialize(),results))


    response_body = {
        "msg": "Hello, this is your GET /user response ",
        "result": user.serialize()
    }

    return jsonify(response_body), 200


@app.route('/character/<int:id>', methods=['GET'])
def get_character(id):
    print(id)

    character = Character.query.filter_by(id=id).first()
    # user = User.query.get(id)
    print(character.serialize())
    # results = User.query.all()
    # users_list = list(map(lambda item: item.serialize(),results))


    response_body = {
        "msg": "Hello, this is your GET /character response ",
        "result": character.serialize()
    }

    return jsonify(response_body), 200


@app.route('/starship/<int:id>', methods=['GET'])
def get_starship(id):
    print(id)

    starship = Starship.query.filter_by(id=id).first()
    # user = User.query.get(id)
    print(user.serialize())
    # results = User.query.all()
    # users_list = list(map(lambda item: item.serialize(),results))


    response_body = {
        "msg": "Hello, this is your GET /starship response ",
        "result": starship.serialize()
    }

    return jsonify(response_body), 200


@app.route('/planet/<int:id>', methods=['GET'])
def get_planet(id):
    print(id)

    planet = Planet.query.filter_by(id=id).first()
    # user = User.query.get(id)
    print(planet.serialize())
    # results = User.query.all()
    # users_list = list(map(lambda item: item.serialize(),results))


    response_body = {
        "msg": "Hello, this is your GET /planet response ",
        "result": planet.serialize()
    }

    return jsonify(response_body), 200


@app.route('/cha_favs/<int:id>', methods=['GET'])
def get_cha_favs(id):
    print(id)

    cha_favs = Cha_Favs.query.filter_by(id=id).first()
    # user = User.query.get(id)
    print(cha_favs.serialize())
    # results = User.query.all()
    # users_list = list(map(lambda item: item.serialize(),results))


    response_body = {
        "msg": "Hello, this is your GET /cha_favs response ",
        "result": cha_favs.serialize()
    }

    return jsonify(response_body), 200


@app.route('/pla_favs/<int:id>', methods=['GET'])
def get_pla_favs(id):
    print(id)

    cha_favs = Pla_Favs.query.filter_by(id=id).first()
    # user = User.query.get(id)
    print(pla_favs.serialize())
    # results = User.query.all()
    # users_list = list(map(lambda item: item.serialize(),results))


    response_body = {
        "msg": "Hello, this is your GET /pla_favs response ",
        "result": pla_favs.serialize()
    }

    return jsonify(response_body), 200


@app.route('/shi_favs/<int:id>', methods=['GET'])
def get_shi_favs(id):
    print(id)

    shi_favs = Shi_Favs.query.filter_by(id=id).first()
    # user = User.query.get(id)
    print(shi_favs.serialize())
    # results = User.query.all()
    # users_list = list(map(lambda item: item.serialize(),results))


    response_body = {
        "msg": "Hello, this is your GET /shi_favs response ",
        "result": shi_favs.serialize()
    }

    return jsonify(response_body), 200


@app.route('/film/<int:id>', methods=['GET'])
def get_film(id):
    print(id)

    film = Film.query.filter_by(id=id).first()
    # user = User.query.get(id)
    print(film.serialize())
    # results = User.query.all()
    # users_list = list(map(lambda item: item.serialize(),results))


    response_body = {
        "msg": "Hello, this is your GET /film response ",
        "result": film.serialize()
    }

    return jsonify(response_body), 200


@app.route('/collaboration/<int:id>', methods=['GET'])
def get_collaboration(id):
    print(id)

    collaboration = Collaboration.query.filter_by(id=id).first()
    # user = User.query.get(id)
    print(collaboration.serialize())
    # results = User.query.all()
    # users_list = list(map(lambda item: item.serialize(),results))


    response_body = {
        "msg": "Hello, this is your GET /collaboration response ",
        "result": collaboration.serialize()
    }

    return jsonify(response_body), 200

############################################
# endpoint para crear un dato en una tabla #
############################################

@app.route('/user', methods=['POST'])
def create_user():

    body = json.loads(request.data)
    # json.loads(request.body.decode(encoding='UTF-8'))
    print(body)
    user = User(email=body["email"], password=body["password"], is_active=body["is_active"])
    db.session.add(user)
    db.session.commit()

    response_body = {
        "msg": "El usuario ha sido creado",
    }

    return jsonify(response_body), 200


@app.route('/character', methods=['POST'])
def create_character():

    body = json.loads(request.data)
    # json.loads(request.body.decode(encoding='UTF-8'))
    print(body)
    character = Character(id=body["id"], name=body["name"], birth_year=body["birth_year"], eye_color=body["eye_color"], gender=body["gender"], hair_color=body["hair_color"], mass=body["mass"], skin_color=body["skin_color"], species=["species"], starship=["starship"],films=body["films"])
    db.session.add(character)
    db.session.commit()

    response_body = {
        "msg": "El persanje ha sido creado",
    }

    return jsonify(response_body), 200


@app.route('/starship', methods=['POST'])
def create_starship():

    body = json.loads(request.data)
    # json.loads(request.body.decode(encoding='UTF-8'))
    print(body)
    starship = Starship(id=body["id"], cargo_capacity=body["cargo_capacity"], consumable=body["consumable"], cost_in_credits=body["cost_in_credits"], crew=body["crew"], hyperdrive_rating=body["hyperdrive_rating"], mglt=body["mglt"], length=body["length"], species=["species"], manufacturer=["manufacturer"], max_atmosfering_speed=body["max_atmosfering_speed"], model=body["model"], name=body["name"], passengers=body["passengers"], films=body["films"], pilots=body["pilots"], starship_class=body["starship_class"], ship_favs=body["ship_favs"])
    db.session.add(starship)
    db.session.commit()

    response_body = {
        "msg": "La nave ha sido creada",
    }

    return jsonify(response_body), 200


@app.route('/planet', methods=['POST'])
def create_planet():

    body = json.loads(request.data)
    # json.loads(request.body.decode(encoding='UTF-8'))
    print(body)
    planet = Planet(id=body["id"], climate=body["climate"], films=body["films"], gravity=body["gravity"], name=body["name"], orbital_period=body["orbital_period"], population=body["population"], residents=body["residents"], rotation_period=body["rotation_period"], surface_water=body["surface_water"], terrain=body["terrain"], pla_favs=body["pla_favs"])
    db.session.add(planet)
    db.session.commit()

    response_body = {
        "msg": "El planeta ha sido creado",
    }

    return jsonify(response_body), 200


@app.route('/cha_favs', methods=['POST'])
def create_cha_favs():

    body = json.loads(request.data)
    # json.loads(request.body.decode(encoding='UTF-8'))
    print(body)
    cha_favs = Cha_Favs(id=body["id"], id_cha_favs=body["id_cha_favs"], user_id=body["user_id"])
    db.session.add(cha_favs)
    db.session.commit()

    response_body = {
        "msg": "El favorito de personaje ha sido creado",
    }

    return jsonify(response_body), 200


@app.route('/pla_favs', methods=['POST'])
def create_pla_favs():

    body = json.loads(request.data)
    # json.loads(request.body.decode(encoding='UTF-8'))
    print(body)
    pla_favs = Pla_Favs(id=body["id"], id_pla_favs=body["id_pla_favs"], user_id=body["user_id"])
    db.session.add(pla_favs)
    db.session.commit()

    response_body = {
        "msg": "El favorito de planeta ha sido creado",
    }

    return jsonify(response_body), 200


@app.route('/shi_favs', methods=['POST'])
def create_shi_favs():

    body = json.loads(request.data)
    # json.loads(request.body.decode(encoding='UTF-8'))
    print(body)
    shi_favs = Shi_Favs(id=body["id"], id_shi_favs=body["id_shi_favs"], user_id=body["user_id"])
    db.session.add(shi_favs)
    db.session.commit()

    response_body = {
        "msg": "El favorito de nave ha sido creado",
    }

    return jsonify(response_body), 200


@app.route('/film', methods=['POST'])
def create_film():

    body = json.loads(request.data)
    # json.loads(request.body.decode(encoding='UTF-8'))
    print(body)
    film = Film(id=body["id"], film_name=body["film_name"], characters=body["characters"], starships=body["starships"], planets=body["planets"])
    db.session.add(film)
    db.session.commit()

    response_body = {
        "msg": "La película ha sido creada",
    }

    return jsonify(response_body), 200


@app.route('/collaboration', methods=['POST'])
def create_collaboration():

    body = json.loads(request.data)
    # json.loads(request.body.decode(encoding='UTF-8'))
    print(body)
    collaboration = Collaboration(id=body["id"], film_name=body["film_name"], characters=body["characters"], starships=body["starships"], planets=body["planets"])
    db.session.add(collaboration)
    db.session.commit()

    response_body = {
        "msg": "La colaboración ha sido creada",
    }

    return jsonify(response_body), 200



# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
