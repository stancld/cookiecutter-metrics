PHONY: clean

clean:
	rm metrics/nlp/automatic.py
	rm metrics/functional/nlp/automatic.py
	git restore metrics/nlp/__init__.py
	git restore metrics/functional/nlp/__init__.py