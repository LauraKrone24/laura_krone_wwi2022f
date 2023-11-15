#Laden des aktuellsten Python Images
FROM python:latest

#Ändern des Arbeitsverzeichnises zu /app
WORKDIR /app

#Alle Inhalte werden des Ordners my_micro_service werden nach /app kopiert
COPY . /app

#Es werden alle benötigten Anforderungen installiert
RUN pip install -r requirements.txt

#Der Python Micorservice wird für localhost gestartet
CMD [ "python", "app.py", "--host=0.0.0.0"]


