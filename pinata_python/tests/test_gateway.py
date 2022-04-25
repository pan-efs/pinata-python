import pytest

from pinata_python.gateway import PublicGateway

@pytest.mark.skip(reason='Provide your CID and save_to path.')
def test_retrieve_content_text_file(auth):
    pinata = PublicGateway(AUTH="jwt", PINATA_JWT_TOKEN=auth[2])
    cid = '' # cid here
    save_to = '' # save_to path here

    response = pinata.retrieve_content(cid, save_to)

    assert response == 200

@pytest.mark.skip(reason='Provide your CID and save_to path.')
def test_retrieve_content_img_file(auth):
    pinata = PublicGateway(AUTH="jwt", PINATA_JWT_TOKEN=auth[2])
    cid = '' # cid here
    save_to = '' # save_to path here

    response = pinata.retrieve_content(cid, save_to)

    assert response == 200