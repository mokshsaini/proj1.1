
# Proj1.1 (A Fast API Application)

A tool to create and fetch user's records from database



## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [Configuration](#configuration)
## Prerequisites
Before you begin, ensure you have met the following requirements:
- You have installed Python 3.7 or higher.
- You have installed [Pipenv](https://pipenv.pypa.io/en/latest/).
## Installation
1. Clone the repository:

  ```bash
  git clone https://github.com/yourusername/yourproject.git cd yourproject
  ```

2. Install the dependencies and set up the virtual environment using Pipenv:

```bash
pipenv install --dev
  ```
        


## Usage
Activate the virtual environment created by Pipenv:

```bash
pipenv shell
  ```
## Running the Application
To run the FastAPI application, use the following command:

```bash
uvicorn main:app --reload
  ```

- 'main' is the name of your main Python file (e.g., main.py).

- 'app' is the name of the FastAPI instance.

- '--reload' enables auto-reloading for development


## Configuration
Make sure to configure your environment variables or settings according to your needs. For example, you might need to set up your MongoDB connection string in an environment variable or a configuration file.