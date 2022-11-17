FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /wishlist

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENV APP_SETTINGS="config.DevelopmentConfig"
ENV DATABASE_URL="postgres://kttoejbghptcfj:15ac4fddba6a3ce9188e7d2d843f7a97afd80dfb2fdf4e74a60e73479d3abe71@ec2-44-193-111-218.compute-1.amazonaws.com:5432/d2l93ok0mpaduh"  

EXPOSE 5000

CMD ["python","manage.py", "runserver","-h","0.0.0.0","-p","5000"] 