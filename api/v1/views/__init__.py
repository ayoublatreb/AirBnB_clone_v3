#!/usr/bin/python3
<<<<<<< HEAD
"""Definition of main blueprint"""


from flask import Blueprint


app_views = Blueprint('api', __name__, url_prefix='/api/v1')


from api.v1.views.amenities import *
from api.v1.views.cities import *
from api.v1.views.index import *
from api.v1.views.places.amenities import *
from api.v1.views.places_reviews import *
from api.v1.views.places import *
from api.v1.views.states import *
from api.v1.views.users import *
=======
"""sharing app_views Blueprint"""

from flask import Blueprint
app_views = Blueprint('app_views', __name__)
from api.v1.views.index import *
from api.v1.views.states import *
>>>>>>> 2684add9eb218d614a3068833b3937865f07d15a
