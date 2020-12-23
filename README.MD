# Readme
# process
pip install virtualenv
virtualenv venv --python=python3.7
# Activar ambiente en windows
venv/scripts/activate
# instalar flask
pip install flask
# Ver dependencias instaladar
pip freeze 
# Crear archivo requirements - para todas las dependencias
pip install -r requirements.txt
# Variable app Flask
set FLASK_APP=main.py
flask run
# Debug flask
set FLASK_DEBUG=1
vs Code jinja plugin
# poner flask en development
set FLASK_ENV=development