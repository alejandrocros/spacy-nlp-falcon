# spacy-nlp

This repo hosts a project for building a Docker container that performs text POS-Tagging using Spacy Python library and falcon FrameWork. Firstly thought for pt-br but with available models for other languages (see Spacy Doc). 

## TO-DO

- [ ] Improve testing
- [ ] Implement other languages and compare performance with Stanford-Core-NLP
- [X] Compare performance with Tornado

## Testing

Some performance tests are located in `./tests/endpoint_tests`, with a config file `./tests/conftest.py`. In order to run them from terminal, change to parent directory and run the following command:

```python -m pytest tests```