from pinata_python.data import Data


def test_pin_list(auth):
    pinata = Data(AUTH="jwt", PINATA_JWT_TOKEN=auth[2])

    options = {
        'pinStart': '2022-04-16T00:00:00.000Z',
        'pinEnd': '2022-04-19T00:00:00.000Z',
        'status': 'pinned',
        'pageLimit': 1,
        'nameContains': 'oleoleole'
    }

    response = pinata.pin_list(options=options)

    assert response == {'count': 0, 'rows': []}


def test_user_pinned_data_total(auth):
    pinata = Data(AUTH="jwt", PINATA_JWT_TOKEN=auth[2])

    response = pinata.user_pinned_data_total()

    assert len(response) == 3

    assert type(response['pin_count']) == int
    assert type(response['pin_size_total']) == str
    assert type(response['pin_size_with_replications_total']) == str