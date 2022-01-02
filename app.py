from flask import Flask


 # ,render_template,request,redirect
# from interact_with_DB import interact_db
###### App setup
app = Flask(__name__)
app.config.from_pyfile('settings.py')

###### Pages
## Homepage
from pages.homepage.homepage import homepage
app.register_blueprint(homepage)

## About
from pages.about.about import about
app.register_blueprint(about)

## Assignment10
from pages.Assignment10.Assignment10 import assignment10
app.register_blueprint(assignment10)

## Catalog
from pages.catalog.catalog import catalog
app.register_blueprint(catalog)



###### Components
## Main menu
from components.main_menu.main_menu import main_menu
app.register_blueprint(main_menu)




