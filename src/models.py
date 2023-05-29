from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id_user = db.Column(db.Integer(), primary_key=True, unique=True)  
    email = db.Column(db.String(250), nullable=False, unique=True)
    password = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.id

    def serialize(self):
        return {
            "id_user": self.id_user,
            "email": self.email,
            "password": self.password,
        }

class Character(db.Model):
    id_character = db.Column(db.Integer(), primary_key=True, unique=True)
    name = db.Column(db.String(250), nullable=False)
    bith_year = db.Column(db.String(250), nullable=False)
    eye_color = db.Column(db.String(250))
    gender = db.Column(db.String(250))
    hair_color = db.Column(db.String(250))
    # homeworld_id = db.Column(db.String(250), ForeingKey=("planets.id_planet"), nullable=False)
    # planets = db.relationship(Planet)
    mass = db.Column(db.String(250), nullable=False)
    skin_color = db.Column(db.String(250), nullable=False)
    species = db.Column(db.String(250), nullable=False)
    starship = db.Column(db.String(250), nullable=False)
    films = db.Column(db.String(250), nullable=False)

def __repr__(self):
        return '<Character %r>' % self.id

def serialize(self):
    return {
        "id_character": self.id_character,
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
    id_starship = db.Column(db.Integer(), primary_key=True)
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

def __repr__(self):
        return '<Starship %r>' % self.id

def serialize(self):
    return {
        "id_starship": self.id_character,
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
    __tablename__ = 'planets'
    id_planet = db.Column(db.Integer(), primary_key=True)
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

def __repr__(self):
        return '<Planet %r>' % self.id

def serialize(self):
    return {
        "id_planet": self.id_planet,
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
    id_cha_favs = db.Column(db.Integer(), primary_key=True)
    id_user = db.Column(db.Integer(), db.ForeignKey("users.id_user"), nullable=False)
    users = db.relationship(User)   

    def __repr__(self):
        return '<Cha_Favs %r>' % self.id

    def serialize(self):
        return {
            "id_cha_favs": self.id_cha_favs,
            "id_user": self.id_user,
            "users": self.users,
        }

class Pla_Favs(db.Model):
    id_pla_favs = db.Column(db.Integer(), primary_key=True)
    id_user = db.Column(db.Integer(), db.ForeignKey("users.id_user"), nullable=False)
    users = db.relationship(User)

    def __repr__(self):
            return '<Pla_Favs %r>' % self.id

    def serialize(self):
        return {
            "id_pla_favs": self.id_pla_favs,
            "id_user": self.id_user,
            "users": self.users,
        }

class Shi_Favs(db.Model):
    id_shi_favs = db.Column(db.Integer(), primary_key=True)
    id_user = db.Column(db.Integer(), db.ForeignKey("users.id_user"), nullable=False)
    users = db.relationship(User)    

    def __repr__(self):
            return '<Shi_Favs %r>' % self.id

    def serialize(self):
        return {
            "id_shi_favs": self.id_shi_favs,
            "id_user": self.id_user,
            "users": self.users,
        }
    
class Film(db.Model):
    id_films = db.Column(db.Integer(), primary_key=True)
    film_name = db.Column(db.String(250), nullable=False)
    characters = db.Column(db.String(250), db.ForeignKey("characters.name"), nullable=False)
    starships = db.Column(db.String (250), db.ForeignKey("starships.name"), nullable=False)
    planets = db.Column(db.String(250), db.ForeignKey("planets.name"), nullable=False)

    def __repr__(self):
            return '<Film_Favs %r>' % self.id

    def serialize(self):
        return {
            "id_film": self.id_film,
            "": ,
            "": ,
            "": ,
            "": ,
            "": ,
            "": ,
        }

    



# class Collaboration(Base):
#     __tablename__ = 'collaborations'
#     id_collab = db.Column(db.Integer(), primary_key=True)
#     id_films = db.Column(db.Integer(), db.ForeignKey("films.name"), nullable=False)
#     id_characters = db.Column(db.Integer(), db.ForeignKey("characters.id_character"), nullable=False)
#     id_starships = db.Column(db.String(250), db.ForeignKey("starships.name"), nullable=False)
#     id_planets = db.Column(db.String(250), db.ForeignKey("planets.name"), nullable=False)



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


