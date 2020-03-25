
run:
	python devine.py

pytest:
	pytest -v --doctest-modules --cov=devine --cov-report=term-missing .

test:
	python test_devine.py


