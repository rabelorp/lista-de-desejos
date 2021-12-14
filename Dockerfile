FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /wishlist

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENV APP_SETTINGS="config.DevelopmentConfig"
ENV DATABASE_URL="postgresql://postgres:postgres@localhost/wishlist"  

EXPOSE 5000

CMD ["python","manage.py", "runserver","-h","0.0.0.0","-p","5000"] 