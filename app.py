"""
Main app function
"""
import logging
import spacy

from src.routes.routes import make_app
from utils.constants import DICTIONARY_OF_MODELS

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('model_loader')

def load_model(language):
    """
    This function loads the model assigned for the specific language,
    defined in utils.constants.DICTIONARY_OF_MODELS
    """
    return spacy.load(DICTIONARY_OF_MODELS[language])

def main(language):
    model = load_model(language)
    logger.info('Model Loaded!')
    app = make_app(model)
    return app
