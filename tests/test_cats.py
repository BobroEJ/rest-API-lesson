import requests
from pytest_voluptuous import S
from voluptuous import Schema, Any, PREVENT_EXTRA

from schemas.facts import fact, facts

from utils.sessions import cats


def test_facts_count():
    """
    1. https://catfact.ninja/facts?limit=2
    2. asserts
    """
    limit = 2

    response = requests.get('https://catfact.ninja/facts', params={'limit': limit})

    assert len(response.json()['data']) == limit


def test_facts_count_v2():
    """
    1. https://catfact.ninja/facts?limit=2
    2. asserts
    """
    limit = 2

    # response = cats().request('GET', '/facts', params={'limit': limit})
    response = cats().get('/facts', params={'limit': limit})

    assert len(response.json()['data']) == limit


def test_facts_status_code():
    limit = 2
    response = requests.get('https://catfact.ninja/facts', params={'limit': limit})

    assert response.status_code == 200
    assert S(facts) == response.json()


def test_fact_fields_validation():
    response = requests.get('https://catfact.ninja/fact')

    assert isinstance(response.json()['fact'], str)
    assert isinstance(response.json()['length'], int)


def test_fact_schema_validation():
    response = requests.get('https://catfact.ninja/fact')

    assert S(fact) == response.json()
    # assert isinstance(response.json()['length'], int)
