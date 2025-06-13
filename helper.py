from faker import Faker
from random import randint

fake = Faker()


def generate_registration_data():
    name = fake.name()
    email = fake.email()
    password = fake.password(length=randint(6, 15))
    return name, email, password


def generate_registration_data_incorrect_password():
    name = fake.name()
    email = fake.email()
    password = fake.password(length=5)
    return name, email, password
