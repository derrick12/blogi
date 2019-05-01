from flask import Blueprint
main = Blueprint('main',__name__)  # The name of the blueprint and the __name__ variable to find the location of the blueprint.
from . import views
