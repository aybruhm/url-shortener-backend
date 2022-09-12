# URL Shortener
Build and protect your brand using powerful, recognizable short links. It is built with Python and Django Rest Framework.

## Docs
![api_docs_screenshot](https://user-images.githubusercontent.com/55067204/189690612-bb68ef04-f8d0-464b-aae8-7420434f82f7.png)


## Frontend
Link to [repository](https://github.com/israelabraham/url-shortener-frontend)

## Features

- Keeps count of how many times each URL is followed.
- Random and String Modules were implemented to generate the token for the original URL.
- URL Length: Shortened URL are combination of numbers(0-9) and characters(a-Z) of length 5.
- Stats of URLs that have been shortened

## Installation


To get it running on your local machine, follow the steps below:

1. Run the commands below in your terminal:

```
git clone git@github.com:israelabraham/url-shortener-backend.git
```

2. Change directory to url-shortener-backend:

```
cd url-shortener-backend
```

3. Install the requirements with the command below:

```
pipenv install -r requirements.txt
```

4. Run the development server with

```
python manage.py runserver
```

5. Launch your browser and navigate to:

```
http://127.0.0.1:8000
```