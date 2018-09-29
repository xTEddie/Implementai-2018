# SOEN490

## Overview

The app uses the following tools:
- [Python 3+](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Node v8.11.3](https://nodejs.org/en/)
- [React](https://reactjs.org/)

## Getting Started

Docker is used for the deployment of the software in production only.

### Setup

As a developer you will need to perform the following steps:

- Install virtualenv
```
    pip3 install virtualenv
```

- Create a venv folder where it will contain all the virtual environments
```
    mkdir venv
    cd venv
```

- Clone the git repository
```
    git clone git@github.com:SteveLocke/CapstoneReservation.git
```

- Create virtual environment
```
    virtualenv CapstoneReservation -p python3
```

- Run virtual environment
```
    source CapstoneReservation/bin/activate
```

- Go inside the the virtual environment directory and clone the project
```
    cd CapstoneReservation
    git clone git@github.com:SteveLocke/CapstoneReservation.git
```

- Go inside the repository and upgrade pip to the latest version
```
    cd CapstoneReservation
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python get-pip.py
```

- Install python dependencies
```
    pip3 install -r server/requirements/dev.txt
```

- Go to the root directory of the Django app
```
    cd server
```

-  Create migrations
```
    python3 manage.py makemigrations
```
This will basically look at the DB schema and create scripts to update it if necessary.

- Apply migration changes to the DB
```
    python3 manage.py migrate
```
This will execute the scripts generated previously from **makemigrations** and apply the new schema.

- Create super user
```
    python3 manage.py createsuperuser
```
This will create an user to access to the Django administration interface

- Start Django server
```
    python3 manage.py runserver 0.0.0.0:8000
```

- Follow the steps to install yarn on [https://yarnpkg.com/en/docs/install](https://yarnpkg.com/en/docs/install)

- Go to the root directory of the React app
```
    cd client // or cd ../client (dependending on your current directory)
```

- Install node dependencies
```
    yarn install
```
Any **yarn** (or **npm**) command has to be run on the same directory as **package.json**

- Start React app
```
    yarn start
```
The default port of the React app is **3000**


## Repository Structure

```
    server/              : Django server
    └─ apps/             : Django apps
    └─ config/           : Django configs
    │  └─ settings/      : Django settings (dev/prod)
    └─ requirements/     : Python requirements (dev/prod)
    └─ scripts/          : Utility scripts

    client/              : React app
    └─ src/              : Source code
    │  └─ assets         : Assets
    │  |  └─ img/        : media files
    │  |  └─ scss/       : .scss stylesheets (common)
    |  └─ components/    : React components
    |  └─ config/        : Configs
    └─ dist/             : Minified code for production
```

## Useful Commands

- List all Django commands
```
    python3 manage.py --help
```

- Dump DB
```
    python3 scripts/dump_database.py
```

- Deactivate virtual environment
```
    deactivate
```

## References

- [http://www.django-rest-framework.org/](http://www.django-rest-framework.org/)
- [http://www.cdrf.co/](http://www.cdrf.co/)
- [https://itnext.io/reacts-component-lifecycle-6c13e09d10ad](https://itnext.io/reacts-component-lifecycle-6c13e09d10ad)
- [https://semantic-ui.com/](https://semantic-ui.com/)
- [https://react.semantic-ui.com/](https://react.semantic-ui.com/)
- [https://github.com/headzoo/react-moment](https://github.com/headzoo/react-moment)
- [https://www.getpostman.com/](https://www.getpostman.com/)
- [https://yarnpkg.com/en/docs/install](https://yarnpkg.com/en/docs/install)
