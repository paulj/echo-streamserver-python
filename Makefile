init:
	virtualenv env
	env/bin/python setup.py develop
	env/bin/pip install -r requirements.txt

test:
	env/bin/nosetests ./tests/*.py

doc:
	(cd docs; make html)