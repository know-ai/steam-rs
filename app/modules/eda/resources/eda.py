from flask_restx import Namespace, Resource
from app.extensions.api import api


ns = Namespace('EDA', description='Exploratory Data Analysis API')

@ns.route('/')
class EDA(Resource):
    
    @api.doc()
    def get(self):
        
        return { 'success': True, 'message': "healthy" }