# aiu_booking

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

### List of services: ###

* Dev server: [https://api.aiu_booking.com/](https://api.aiu_booking.com/)

### Documentation: ###

* [Architecture overview](docs/architecture_overview.md)
* [Backend: Routine tasks](docs/commands.md)
* [Backend: Pre-commit hook](docs/pre_commit_hook.md)

### API documentation: ###

* ReDoc web UI: [https://api.aiu_booking.com/_platform/docs/v1/redoc/](https://api.aiu_booking.com/_platform/docs/v1/redoc/)
* Swagger web UI: [https://api.aiu_booking.com/_platform/docs/v1/swagger/](https://api.aiu_booking.com/_platform/docs/v1/swagger/)
* Swagger JSON: [https://api.aiu_booking.com/_platform/docs/v1/swagger.json](https://api.aiu_booking.com/_platform/docs/v1/swagger.json)
* Swagger YAML: [https://api.aiu_booking.com/_platform/docs/v1/swagger.yaml](https://api.aiu_booking.com/_platform/docs/v1/swagger.yaml)

### First run: ###

Install Python 3.9.9 & setup virtual environment. We recommend to use [pyenv](https://github.com/pyenv/pyenv) & [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv):

```bash
pyenv install 3.9.9
pyenv virtualenv 3.9.9 aiu_booking
pyenv activate aiu_booking
```

Update `pip` & `setuptools`, install `fabric`, `invoke` & `pip-tools`:

```bash
pip install -U fabric invoke pip pip-tools setuptools
```

Install Python requirements:

```bash
fab pip.sync
```

Copy initial settings for Django project:

```bash
cp ./app/.env.example ./app/.env
```

Generate `SECRET_KEY`:

```bash
./app/manage.py generate_secret_key
```

and write it to `./api/.env`:

```
AIU_BOOKING_SECRET_KEY=<your-generated-key>
```

Run backing services (require Docker):

```bash
fab compose.up -d
```

Run migrations:

```bash
./app/manage.py migrate
```

Run Django server:

```bash
fab run
```
