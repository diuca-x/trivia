from flask import Blueprint
from flask_restful import Api

from api.resources.routes import SingleQuestion, ModifyOrGetQuestion

blueprint = Blueprint("api", __name__, url_prefix="/api")
api = Api(blueprint, errors=blueprint.errorhandler)

api.add_resource(SingleQuestion, "/question")
api.add_resource(ModifyOrGetQuestion, "/question/<int:question_id>")
