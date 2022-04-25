import pytest

from pinata_python.base import Pinata
from pinata_python.exceptions.exceptions import SetAuthenticationError


def test_empty_initialization():
    pinata = Pinata()

    assert pinata.AUTH == "keysecret"
    assert pinata.PINATA_API_KEY is None
    assert pinata.PINATA_API_SECRET is None
    assert pinata.PINATA_JWT_TOKEN is None


def test_initialize_jwt_token(auth):
    pinata = Pinata(AUTH="jwt", PINATA_JWT_TOKEN=auth[2])

    assert pinata.AUTH == "jwt"
    assert pinata.PINATA_JWT_TOKEN is not None
    assert pinata.PINATA_API_KEY is None
    assert pinata.PINATA_API_SECRET is None


def test_initialize_api(auth):
    pinata = Pinata(PINATA_API_KEY=auth[0], PINATA_API_SECRET=auth[1])
    
    assert pinata.AUTH == "keysecret"
    assert pinata.PINATA_JWT_TOKEN is None
    assert pinata.PINATA_API_KEY is not None
    assert pinata.PINATA_API_SECRET is not None


def test_full_initialization(auth):
    pinata = Pinata(PINATA_API_KEY=auth[0], PINATA_API_SECRET=auth[1], PINATA_JWT_TOKEN=auth[2])

    assert pinata.AUTH == "keysecret"
    assert pinata.PINATA_JWT_TOKEN is not None
    assert pinata.PINATA_API_KEY is not None
    assert pinata.PINATA_API_SECRET is not None


def test_api_headers(auth):
    pinata = Pinata(PINATA_API_KEY=auth[0], PINATA_API_SECRET=auth[1])

    headers = pinata.headers()

    assert headers["pinata_api_key"] == auth[0]
    assert headers["pinata_secret_api_key"] == auth[1]


def test_jwt_headers(auth):
    pinata = Pinata(AUTH="jwt", PINATA_JWT_TOKEN=auth[2])

    headers = pinata.headers()

    assert headers["Authorization"] == f"Bearer {auth[2]}"


def test_set_authentication_1(auth):
    pinata = Pinata(PINATA_API_KEY=auth[0], PINATA_API_SECRET=auth[1])
    
    options1 = {"jwt_token": "asgfaatrsjtjftjsfjfnngadhdfnsf"}
    response = pinata.set_authentication(options=options1)

    assert response == True
    assert pinata.AUTH == "jwt"
    assert pinata.PINATA_JWT_TOKEN is not None
    assert pinata.PINATA_API_KEY is not None
    assert pinata.PINATA_API_SECRET is not None


def test_set_authentication_2(auth):
    pinata = Pinata(AUTH="jwt", PINATA_JWT_TOKEN=auth[2])

    options = {"api_key": "12334566789", "api_secret": "aasgsdhsdfh"}
    response = pinata.set_authentication(options=options)

    assert response == True
    assert pinata.AUTH == "keysecret"
    assert pinata.PINATA_JWT_TOKEN is not None
    assert pinata.PINATA_API_KEY is not None
    assert pinata.PINATA_API_SECRET is not None


def test_set_authentication_error(auth):
    pinata = Pinata(AUTH="jwt", PINATA_JWT_TOKEN=auth[2])

    options = {"jwt_token": "asdgasg", "api_key": "12334566789", "api_secret": "aasgsdhsdfh"}
    
    with pytest.raises(SetAuthenticationError) as e:
        pinata.set_authentication(options=options)