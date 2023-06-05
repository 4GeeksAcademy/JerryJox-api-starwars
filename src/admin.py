import os
from flask_admin import Admin
from models import db, Film, User, Character, Starship, Planet, Cha_Favs, Pla_Favs, Shi_Favs, Collaboration
from flask_admin.contrib.sqla import ModelView

def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin = Admin(app, name='4Geeks Admin', template_mode='bootstrap3')


# mostra id 1 de 2
# class CharacterAdmin(ModelView):
#     column_list = ("id", "name", "birth_year", "eye_color", "gender", "hair_color", "height", "films", "homeworld_id", "mass", "skin_color", "species", "starships_id", "url", "vehicles")
#     form_columns = ("name", "birth_year", "eye_color", "gender", "hair_color", "height", "films", "homeworld_id", "mass", "skin_color", "species", "starships_id", "url", "vehicles")
#     column_hide_backrefs = False
    
    # Add your models here, for example this is how we add a the User model to the admin
    admin.add_view(ModelView(User, db.session))
    # admin.add_view(ModelView(Address, db.session))

    # You can duplicate that line to add mew models
    # admin.add_view(ModelView(YourModelName, db.session))
    admin.add_view(ModelView(Film, db.session))
    admin.add_view(ModelView(Character, db.session))
    admin.add_view(ModelView(Planet, db.session))
    admin.add_view(ModelView(Starship, db.session))
    admin.add_view(ModelView(Cha_Favs, db.session))
    admin.add_view(ModelView(Pla_Favs, db.session))
    admin.add_view(ModelView(Shi_Favs, db.session))    
    admin.add_view(ModelView(Collaboration, db.session))

# mostra id 2 de 2
# admin.add_view(CharacterAdmin(Character, db.session))
    