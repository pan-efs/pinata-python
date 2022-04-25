import pytest

from pinata_python.pinning import Pinning


@pytest.mark.skip(reason='Provide your filepath.')
def test_pin_file_to_ipfs(auth):
    pinata = Pinning(AUTH="jwt", PINATA_JWT_TOKEN=auth[2])
    filepath = '' # filepath here
    
    response = pinata.pin_file_to_ipfs(filepath)

    assert len(response) == 3 or len(response) == 4

    assert type(response['IpfsHash']) == str
    assert type(response['PinSize']) == int
    assert type(response['Timestamp']) == str


def test_pin_json_to_ipfs(auth):
    pinata = Pinning(AUTH="jwt", PINATA_JWT_TOKEN=auth[2])

    j = {'name': 'george', 'surname': 'geo'}
    options = {
        'pinataMetadata': {
            'name': 'bob',
            'keyvalues': {
                'power': 10,
                'stamina': 'high',
                'job': 'warrior'
            }  
        }
    }

    response = pinata.pin_json_to_ipfs(j, options)

    assert len(response) == 3 or len(response) == 4

    assert type(response['IpfsHash']) == str
    assert type(response['PinSize']) == int
    assert type(response['Timestamp']) == str


@pytest.mark.skip(reason='Provide your hashstring.')
def test_pin_by_hash(auth):
    pinata = Pinning(AUTH="jwt", PINATA_JWT_TOKEN=auth[2])
    
    options = {
        'pinataMetadata': {
            'name': 'alice',
            'keyvalues': {
                'power': 100,
                'stamina': 'high',
                'job': 'queen'
            }  
        }
    }
    hashstring = '' #hashstring here

    response = pinata.pin_by_hash(hashstring, options)

    assert len(response) == 4
    
    assert type(response['id']) == str
    assert type(response['IpfsHash']) == str
    assert type(response['PinSize']) == int
    assert type(response['Timestamp']) == str


@pytest.mark.skip(reason='Provide your CID.')
def test_unpin(auth):
    pinata = Pinning(AUTH="jwt", PINATA_JWT_TOKEN=auth[2])
    cid = '' # cid here

    response = pinata.unpin(cid)

    assert response == 200


@pytest.mark.skip(reason='Provide your CID.')
def test_hash_metadata(auth):
    pinata = Pinning(AUTH="jwt", PINATA_JWT_TOKEN=auth[2])
    cid = '' # cid here
    options = {
            'name': 'alice',
            'keyvalues': {
                'power': 100,
                'stamina': 'high',
                'job': 'queen'
            } 
    }

    response = pinata.hash_metadata(cid, options)

    assert response == 200


@pytest.mark.skip(reason='Provide your CID.')
def test_hash_pin_policy(auth):
    pinata = Pinning(AUTH="jwt", PINATA_JWT_TOKEN=auth[2])
    cid = '' # cid here
    new_pin_policy = {
            'regions': [
                {
                    'id': 'FRA1',
                    'desiredReplicationCount': 1
                }
            ]
        }
    
    response = pinata.hash_pin_policy(cid, new_pin_policy)

    assert response == 200


@pytest.mark.skip(reason='No reason. Unmark it if you wish.')
def test_global_pin_policy(auth):
    pinata = Pinning(AUTH="jwt", PINATA_JWT_TOKEN=auth[2])
    new_pin_policy = {
            'regions': [
                {
                    'id': 'FRA1',
                    'desiredReplicationCount': 1
                }
            ]
        }
    
    response = pinata.global_pin_policy(new_pin_policy, migrate_previous_pins=True)

    assert response == 200


def test_pin_jobs(auth):
    pinata = Pinning(AUTH="jwt", PINATA_JWT_TOKEN=auth[2])
    options = {
        'sort': 'ASC',
        'status': 'prechecking',
        'limit': 3
    }

    response = pinata.pin_jobs(options)

    assert response == {'count': 0, 'rows': []}