# Utiliser une image Python comme base
FROM  python:3


# Définir le répertoire de travail
WORKDIR /app

# Copier le fichier requirements.txt et installer les dépendances
COPY requirements.txt /app/
    
RUN pip install --no-cache-dir -r requirements.txt

RUN pip install setuptools

RUN python -m venv env

# Copier le contenu de l'application dans le conteneur
COPY . /app

# Exposer le port sur lequel Django est exécuté (par défaut 8000)
EXPOSE 8000

# Lancer le serveur Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]