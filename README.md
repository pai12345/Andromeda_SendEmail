Andromeda Send Email

# Introduction

Andromeda server for sending email to Customers.

## Prerequisites

- python version 3 or above.
- pip latest version.

## Installation

### On-Premise

- Clone the repository from GitHub.
  `git clone <address>`
- Install the dependencies.
  `pip install requirements.txt`

### Container Environment - Docker

- Clone the repository from GitHub using
  `git clone <address>`
- Build the image
  `docker build -t <name> --compress .`

## Execution

### On-Premise

- Execute the application using python command.
  `python index.py`

### Container Environment - Docker

- Execute the application using docker run command.
  `docker run -p 5001:5001 <name>`
