from flask import Blueprint, Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from .config import Config


app = Flask(__name__)
CORS(app)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from .api import HelpFinanciallyResource, HelpWithActivityResource, NeedHelpResource, FacultyResource,\
    ActivityResource, SkillResource

api = Blueprint('api', __name__)
api.add_url_rule('/help-financially', view_func=HelpFinanciallyResource.as_view('help-financially'))
api.add_url_rule('/help-with-activity', view_func=HelpWithActivityResource.as_view('help-with-activity'))
api.add_url_rule('/need-help', view_func=NeedHelpResource.as_view('need-help'))
api.add_url_rule('/faculties', view_func=FacultyResource.as_view('faculties'))
api.add_url_rule('/activities', view_func=ActivityResource.as_view('activities'))
api.add_url_rule('/skills', view_func=SkillResource.as_view('skills'))

app.register_blueprint(api, url_prefix='/api/v1')
