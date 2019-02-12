import json
import logging
import falcon
from src.use_cases.spacy_ops.pos_tagging import pos_tagger

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)

class TagController(object):

    def __init__(self, model):
        """
        Initializes and assigns model
        """
        self.model = model

    def on_post(self, req, resp):
        """
        Handles the `POST` requests.

        Returns a JSON with two fields:
            - 'result' contains the tagged text
            - 'status' for checking performance (OK if status == 1)

        Catches Different Exceptions with different status (all negative)
        """

        try:
            jason = json.load(req.stream)
            tagged_text = pos_tagger(self.model, jason['text'])
            tagged_json = {'result': tagged_text, 'status': 1}
            resp.status = falcon.HTTP_200 # '200 OK'
        except json.JSONDecodeError as e:
            logger.error(' JSON Encoding Error')
            resp.status = falcon.HTTP_400 # '400 Bad Request'
            tagged_json = {'result': 'JSON Encoding Error', 'status': -1}
        except KeyError as e:
            logger.error(' text Key Not Found')
            resp.status = falcon.HTTP_400 # '400 Bad Request'
            tagged_json = {'result': 'Key Error', 'status': -2}
        except Exception as e:
            logger.error(' Unknown Error')
            resp.status = falcon.HTTP_400 # '400 Bad Request'
            tagged_json = {'result': 'UNKNOWN', 'status': -9}
        finally:
            resp.body = json.dumps(tagged_json)

