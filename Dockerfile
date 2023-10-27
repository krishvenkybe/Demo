FROM python:latest

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "/usr/local/bin/gunicorn", "0.0.0.0:8000", "site.wsgi:application"]

