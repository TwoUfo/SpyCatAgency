# Spy Cat Agency

A Django-based web application for managing spy cats, their missions, and targets.


## Installation

1. Clone the repository:
```bash
git clone https://github.com/TwoUfo/SpyCatAgency.git
cd SpyCatAgency
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source venv/bin/activate
```

3. Install dependecies
```bash
pip isntall poetry
poetry install
```

4. Run the project
```bash
python manage.py runserver
```


## Database
I decided to use light db sqlite directly in the project, so you do not need to apply any migrations.


## Endpoints
```
https://web.postman.co/workspace/My-Workspace~5eaba7ac-057a-4e4d-89c0-29ffc2be9fe3/request/33720231-398be215-4f61-4e54-8958-c44b749869e1?action=share&source=copy-link&creator=33720231
```
Pay attention: you need to use your own object UUIDs in the requests.
