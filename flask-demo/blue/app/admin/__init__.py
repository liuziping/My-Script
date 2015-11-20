from flask import Blueprint

users=Blueprint('users',__name__,
				template_folder='template',
				static_folder='static')
import views,managers
