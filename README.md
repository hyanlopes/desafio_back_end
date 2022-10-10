# To-Do API


An api that you can upload and translate your cnab file.

## Functionalities

- Upload your file cnab
- Organizate each transactions by store
- Sub_total expacted by store


## Api link

[API](https://desafio-back-hyan.herokuapp.com/)

## Routes

Upload for your file (in the browser)
```bash
  method: POST
  https://desafio-back-hyan.herokuapp.com/api/upload/
```

View all store registered
```bash
method: GET
  https://desafio-back-hyan.herokuapp.com/api/store/
```

View all transactions of a store
```bash
method: GET
  https://desafio-back-hyan.herokuapp.com/api/store/<store_name>/
```


## Running locally

Clone the project

```bash
  git clone git@github.com:hyanlopes/desafio_back_end.git
```

Enter the project directory

```bash
  cd desafio_back_end
```

Create your virtual enviroment

```bash
  python -m venv nameOfYourVirtualEnvironment
```

Activate your virtual environment

```bash
  source nameOfYourVirtualEnvironment/bin/activate
```

Install the dependencies

```bash
  pip install -r requirements.txt
```

Config your database settings with postgres: Open the file .env.example to see more details.

Run the migrations

```bash
  ./manage.py makemigrations
```

```bash
  ./manage.py migrate
```

Start the server

```bash
  ./manage.py runserver
```

## Stack used

**Back-end:** Python, Django-rest-framework


## My contacts


- [github](https://github.com/hyanlopes)
- [portifolio](https://hyan-portifolio.vercel.app/)
- [linkedin](https://www.linkedin.com/in/hyanlopes/)
