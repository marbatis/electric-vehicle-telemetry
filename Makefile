.PHONY: setup nb-01 nb-02 nb-03 clean

setup:
	python -m pip install --upgrade pip
	python -m pip install -r requirements.txt

nb-01:
	jupyter notebook notebooks/01_clean_eda.ipynb

nb-02:
	jupyter notebook notebooks/02_models_cv.ipynb

nb-03:
	jupyter notebook notebooks/03_report.ipynb

clean:
	rm -rf __pycache__ */__pycache__ notebooks/.ipynb_checkpoints
