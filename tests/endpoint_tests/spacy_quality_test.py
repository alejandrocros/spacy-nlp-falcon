"""
Some basic tests are defined here. Run them with 'python -m pytest tests' command
"""
EXPECTED_RESULT = [
    ["tempo", "NOUN"],
    ["atrás", "ADV"],
    ["era", "VERB"],
    ["possível", "ADJ"],
    ["distinguir", "VERB"],
    ["loja", "NOUN"],
    ["cidade", "NOUN"],
    ["Nova", "PNOUN"],
    ["York", "PNOUN"],
    ["operação", "NOUN"],
    ["era", "VERB"],
    ["totalmente", "ADV"],
    ["online", "NOUN"],
    ["mais", "ADV"],
    ["tradicionais", "ADJ"]
    ]
# Original text
TEXT = "Até pouco tempo atrás, era possível distinguir uma loja da cidade de Nova York cuja operação era totalmente online de outras mais tradicionais"

def test_spacy_performance(client):
    """
    This test checks if the basic result defined above is properly obtained
    """
    response = client.simulate_post('/tag', json={'text': TEXT})
    assert response.json['result'] == EXPECTED_RESULT


def test_bad_encoding_request(client):
    """
    JSON Encoding Error test
    """
    response = client.simulate_post('/tag', json=None)
    result = response.json['result']
    status = response.json['status']
    error_message = response.status
    assert (result, status, error_message) == ('JSON Encoding Error', -1, '400 Bad Request')


def test_bad_key_request(client):
    """
    Key Error test
    """
    response = client.simulate_post('/tag', json={'badkey': 'foo'})
    result = response.json['result']
    status = response.json['status']
    error_message = response.status
    assert (result, status, error_message) == ('Key Error', -2, '400 Bad Request')
