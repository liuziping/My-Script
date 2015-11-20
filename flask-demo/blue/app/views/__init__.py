from flask import Blueprint

asset=Blueprint('asset',__name__,
				template_folder='template',
				static_folder='static')
import hosts,servers
