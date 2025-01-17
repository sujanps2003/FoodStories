# FoodStories

FoodStories is a web application developed using Django and Bootstrap. The project aims to provide a platform for users to share and discover food-related stories, recipes, and experiences.

## Features

- User registration and authentication.
- Create, edit, and delete food stories.
- Browse and search for stories by category or tags.
- Responsive design powered by Bootstrap.

## Technologies Used

- **Backend:** Django
- **Frontend:** Bootstrap, HTML, CSS
- **Database:** SQLite3
- **Deployment:** Compatible with local and production environments

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x
- pip (Python package installer)
- Virtualenv (optional but recommended)

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/sujanps2003/FoodStories.git
   cd FoodStories
   ```

## Create a virtual environment

```bash
python3 -m venv venv
```

## Install the required packages and Apply migrations

```bash
pip install -r requirements.txt

python manage.py migrate

```

## Run the development server

```bash
python manage.py runserver
```
