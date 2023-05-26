from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# CÓDIGO DE 
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password = db.Column(db.String(80), unique=False, nullable=False)
#     is_active = db.Column(db.Boolean(), unique=False, nullable=False)

#     def __repr__(self):
#         return '<User %r>' % self.id

class Films(db.Model):
    id_films = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    characters = db.Column(db.String(120), unique=True, nullable=False)
    starships = db.Column(db.String(120), unique=True, nullable=False)
    planets = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<Films %r>' % self.id

# <User 1> => {
        #     "id": self.id,
        #     "email": self.email,
        #     # do not serialize the password, its a security breach
        # }
    def serialize(self):
        return {
            "id_films": self.id,
            "name": self.email,
            "character": self.character,
            "starships": self.starships,
            "planets": self.planets,
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