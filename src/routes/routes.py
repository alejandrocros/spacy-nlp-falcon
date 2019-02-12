import falcon
from src.controllers.tag_controller import TagController

def make_app(spacy_model):
    app = falcon.API()
    add_routes(app, spacy_model)
    return app

def add_routes(falcon_api, spacy_model):
    falcon_api.add_route('/tag', TagController(spacy_model))
