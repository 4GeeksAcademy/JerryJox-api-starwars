from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True, unique=True)
    user_name = db.Column(db.String(), nullable=False, unique=True)  
    email = db.Column(db.String(250), nullable=False, unique=True)
    password = db.Column(db.String(250), nullable=False)
    cha_favs = db.relationship("Cha_Favs", backref="user", lazy=True)   
    pla_favs = db.relationship("Pla_Favs", backref="user", lazy=True)
    shi_favs = db.relationship("Shi_Favs", backref="user", lazy=True)

    def __repr__(self):
        return '<User %r>' % self.id

    def serialize(self):
        return {
            "user_name": self.user_name,
            "email": self.email,
            # "password": self.password,
        }

class Character(db.Model):
    id = db.Column(db.Integer(), primary_key=True, unique=True)
    name = db.Column(db.String(250), nullable=False, unique=True)
    birth_year = db.Column(db.String(250), nullable=False)
    eye_color = db.Column(db.String(250))
    gender = db.Column(db.String(250))
    hair_color = db.Column(db.String(250))
    # homeworld_id = db.Column(db.Integer(), db.ForeignKey("planet.id_planet"), nullable=False)
    # planets = db.relationship("Planet")
    mass = db.Column(db.String(250), nullable=False)
    skin_color = db.Column(db.String(250), nullable=False)
    species = db.Column(db.String(250), nullable=False)
    starship = db.Column(db.String(250), nullable=False)
    films = db.Column(db.String(250), nullable=False)
    cha_favs = db.relationship("Cha_Favs", backref="character", lazy=True)

    def __repr__(self):
        return '<Character %r>' % self.id
        
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "birth_year": self.birth_year,
            "eye_color": self.eye_color,
            "gender": self.gender,
            "hair_color": self.hair_color,
            "mass": self.mass,
            "skin_color": self.skin_color,
            "species": self.species,
            "starship": self.starship,
            "films": self.films,     
        }

class Starship(db.Model):
    id = db.Column(db.Integer(), primary_key=True, unique=True)
    cargo_capacity = db.Column(db.Integer(), nullable=False)
    consumable = db.Column(db.String(250), nullable=False)
    cost_in_credits = db.Column(db.Integer(), nullable=False)
    crew = db.Column(db.String(250), nullable=False)
    hyperdrive_rating = db.Column(db.Integer(), nullable=False)
    mglt = db.Column(db.String(250), nullable=False)
    length = db.Column(db.Integer(), nullable=False)
    manufacturer = db.Column(db.String(250), nullable=False)
    max_atmosfering_speed = db.Column(db.String(250), nullable=False)
    model = db.Column(db.String(250), nullable=False)
    name = db.Column(db.String(250), nullable=False)
    passengers = db.Column(db.Integer(), nullable=False)
    films = db.Column(db.String(250), nullable=False)
    pilots = db.Column(db.String(250), nullable=False)
    starship_class = db.Column(db.String(250), nullable=False)
    ship_favs = db.relationship("Shi_Favs", backref="starship", lazy=True)

    def __repr__(self):
        return '<Starship %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "cargo_capacity": self.cargo_capacity,
            "consumable": self.consumable,
            "cost_in_credits": self.cost_in_credits,
            "crew": self.crew,
            "hyperdrive_rating": self.hyperdrive_rating,
            "mglt": self.mglt,
            "length": self.length,
            "manufacturer": self.manufacturer,
            "max_atmosfering_speed": self.max_atmosfering_speed,
            "model": self.model,
            "name": self.name,
            "passenger": self.passenger,
            "films": self.films,
            "pilots": self.pilots,
            "starship_class": self.starship_class,
        }

class Planet(db.Model):
    id = db.Column(db.Integer(), primary_key=True, unique=True)
    climate = db.Column(db.String(250), nullable=False)
    films = db.Column(db.Integer(), primary_key=True)
    gravity = db.Column(db.String(250), nullable=False)
    name = db.Column(db.String(250), nullable=False)
    orbital_period = db.Column(db.String(250), nullable=False)
    population = db.Column(db.String(250), nullable=False)
    residents = db.Column(db.String(250), nullable=False)
    rotation_period = db.Column(db.String(250), nullable=False)
    surface_water = db.Column(db.String(250), nullable=False)
    terrain = db.Column(db.String(250), nullable=False)
    pla_favs = db.relationship("Pla_Favs", backref="planet", lazy=True)

    def __repr__(self):
        return '<Planet %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "climate": self.climate,
            "films": self.films,
            "gravity": self.gravity,
            "name": self.name,
            "orbital_period": self.orbital_period,
            "population": self.population,
            "residents": self.residents,
            "rotation_period": self.rotation_period,
            "surface_water": self.surface_water,
            "terrain": self.terrain,
        }

class Cha_Favs(db.Model):
    id = db.Column(db.Integer(), primary_key=True, unique=True)
    id_cha_favs = db.Column(db.Integer(), db.ForeignKey("character.id"), nullable=True)
    user_id = db.Column(db.Integer(), db.ForeignKey("user.id"), nullable=False)
    
    def __repr__(self):
        return '<Cha_Favs %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "id_cha_favs": self.id_cha_favs,
            "id_user": self.id_user,
        }

class Pla_Favs(db.Model):
    id = db.Column(db.Integer(), primary_key=True, unique=True)
    id_pla_favs = db.Column(db.Integer(), db.ForeignKey("planet.id"), nullable=True)
    id_user = db.Column(db.Integer(), db.ForeignKey("user.id"), nullable=False)

    def __repr__(self):
        return '<Pla_Favs %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "id_user": self.id_user,
            "users": self.users,
        }

class Shi_Favs(db.Model):
    id = db.Column(db.Integer(), primary_key=True, unique=True)
    id_shi_favs = db.Column(db.Integer(), db.ForeignKey("starship.id"), nullable=True)
    id_user = db.Column(db.Integer(), db.ForeignKey("user.id"), nullable=False)
   
    def __repr__(self):
        return '<Shi_Favs %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "id_user": self.id_user,
            "users": self.users,
        }
    
class Film(db.Model):
    id = db.Column(db.Integer(), primary_key=True, unique=True)
    film_name = db.Column(db.String(250), nullable=False)
    characters = db.Column(db.Integer(), db.ForeignKey("character.id"), nullable=False)
    starships = db.Column(db.Integer(), db.ForeignKey("starship.id"), nullable=False)
    planets = db.Column(db.Integer(), db.ForeignKey("planet.id"), nullable=False)

    def __repr__(self):
        return '<Film_Favs %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "film_name": self.film_name,
            "characters": self.characters,
            "starships": self.starships,           
            "planets": self.planets,
        }

class Collaboration(db.Model):
    id = db.Column(db.Integer(), primary_key=True, unique=True)
    id_films = db.Column(db.Integer(), db.ForeignKey("film.id"), nullable=False)
    characters = db.Column(db.Integer(), db.ForeignKey("character.id"), nullable=False)
    id_starships = db.Column(db.Integer(), db.ForeignKey("starship.id"), nullable=False)
    id_planets = db.Column(db.Integer(), db.ForeignKey("planet.id"), nullable=False)

    def __repr__(self):
        return '<Collaboration %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "id_films": self.id_films,
            "characters": self.characters,
            "id_starships": self.id_starships,           
            "id_planets": self.id_planets,
        }



# class Address(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     calle = db.Column(db.String(120), unique=True, nullable=False)
#     numero = db.Column(db.String(80), unique=False, nullable=False)


#     def __repr__(self):
#         return '<Address %r>' % self.id

#     def serialize(self):
#         return {
#             "id": self.id,
#             "calle": self.calle,
#             "numero": self.numero
#             # do not serialize the password, its a security breach
#         }


