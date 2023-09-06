from flask_restx import Namespace, Resource
from app.extensions.api import api


ns = Namespace('MLO', description='Machine Learning Operations API')

@ns.route('/')
class MLO(Resource):
    
    @api.doc()
    def get(self):
        
        return { 'success': True, 'message': "healthy" }