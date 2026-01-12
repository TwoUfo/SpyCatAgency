# Spy Cat Agency

A Django-based web application for managing spy cats, their missions, and targets.


## Requirements
Python version >=3.12

## Installation

1. Clone the repository:
```bash
git clone https://github.com/TwoUfo/SpyCatAgency.git
cd SpyCatAgency
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate
```

3. Install dependecies
```bash
pip install poetry
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
https://www.postman.com/security-cosmonaut-36081406/workspace/publicworkspace/request/33720231-ca6745ed-4038-4e4f-a7fa-5fe73db5a8c6?action=share&source=copy-link&creator=33720231
```
Pay attention: you need to use your own object UUIDs in the requests.
