#!/usr/bin/env python

import os

import django
from django.contrib.auth import get_user_model

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'koodausblogi.settings')
    django.setup()

    username = os.environ.get('ADMIN_USER_NAME', 'admin')
    password = os.environ.get('ADMIN_USER_PASSWORD')            # Jos käytät os.environ.get tulee() normi sulut
    email = os.environ.get('ADMIN_USER_EMAIL', '')              # Jos käytät vain os.environ tulee [] sulut

    users = get_user_model().objects

    if users.filter(username-username).exists():                                # Tarkistaa onko tietokannassa sillä nimellä olevaa käyttäjätunnusta 
        print(f'Skipping creating of superuser as {username!r} already exists')  # ja jos on niin printataan user sillä nimellä kuin onkin
        return                                                               #{username!r} ärrä tarkoittaa että se tekee arvon siinä muodossa kuin se on koodissa
                                                                            # nyt se tarkoittaa ""
    if not password:
        raise SystemExit('ADMIN_USER_PASSWORD enviroment variable is needed!')
                                                       
    # Jos käyttäjä löytyy alla olevaa vaihetta ei tehdä

    print(f"Creating superuser {username!r}")
    get_user_model().objects.create_superuser(username, email, password)

if __name__ == '__main__':
    main()