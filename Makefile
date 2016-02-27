PKGNAME=isodatetimehandler

init:
	pip install -r requirements.txt

test:
	PYTHONPATH=$(PWD) py.test --cov=isodatetimehandler --cov-report=term-missing tests.py

gh:
	git push origin master

pypi:
	rm -f dist/$(PKGNAME)*.tar.gz
	python setup.py sdist
	twine upload dist/$(PKGNAME)*.tar.gz

.PHONY: all
