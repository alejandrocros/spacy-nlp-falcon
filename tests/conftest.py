# IMPORTANT: Run 'python -m pytest tests' for testing when testing from commandline
import pytest
import spacy

from src.routes.routes import make_app
from falcon import testing

@pytest.fixture(scope='module')
def client():
    model = spacy.load('pt_core_news_sm')
    return testing.TestClient(make_app(model))
