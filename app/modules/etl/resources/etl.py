from flask_restx import Namespace, Resource
from app.extensions.api import api


ns = Namespace('ETL', description='Extraction Transform and Load API')

@ns.route('/')
class ETL(Resource):
    
    @api.doc()
    def get(self):
        
        return { 'success': True, 'message': "healthy" }