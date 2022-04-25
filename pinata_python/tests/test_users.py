from pinata_python.users import Users


def test_generate_keys(auth):
    pinata = Users(AUTH="jwt", PINATA_JWT_TOKEN=auth[2])
    
    response = pinata.generate_keys()
    
    assert len(response) == 3

    assert type(response['JWT']) == str
    assert type(response['pinata_api_key']) == str
    assert type(response['pinata_api_secret']) == str
    
    assert len(response['pinata_api_key']) == 20
    assert len(response['pinata_api_secret']) == 64


def test_revoke_key(auth):
    pinata = Users(AUTH="jwt", PINATA_JWT_TOKEN=auth[2])
    
    # Given a fake key, still revokes it
    response = pinata.revoke_key('asgagdfhdfh4jislpR0Q')
    
    assert response == 'Revoked'