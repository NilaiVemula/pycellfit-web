# pycellfit-web
A web-app implementation of [pycellfit](https://github.com/NilaiVemula/pycellfit) built using [Django](https://www.djangoproject.com/) and deployed with [Heroku](heroku.com). A live-version of the website is available [here](https://pycellfit-web.herokuapp.com/).

## Getting Started

Starting server:
```bash
    cd pycellfitweb
    python manage.py runserver
```

## Technical Overview

- No database models are being used. Files are uploaded using a form, processed using `pycellfit`, and outputs are generated using `plotly`.
- UI is created using Bootstrap 4 CSS.
