# Makefile für Sprachwerkstatt

# Variablen
default: run

# Installiere notwendige Python-Pakete
install:
	pip install -r requirements.txt

# Starte die Streamlit-App
run:
	streamlit run app.py
