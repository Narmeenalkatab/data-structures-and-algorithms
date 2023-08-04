import pytest
from scripts.hashtable import Hashtable

def test_set_and_get():
    hashtable = Hashtable()
    hashtable.set('name', 'John')
    assert hashtable.get('name') == 'John'

def test_non_existent_key():
    hashtable = Hashtable()
    assert hashtable.get('age') is None

def test_has_existing_key():
    hashtable = Hashtable()
    hashtable.set('age', 30)
    assert hashtable.has('age') is True

def test_has_non_existent_key():
    hashtable = Hashtable()
    assert hashtable.has('name') is False

def test_keys():
    hashtable = Hashtable()
    hashtable.set('name', 'John')
    hashtable.set('age', 30)
    hashtable.set('country', 'USA')
    assert set(hashtable.keys()) == {'name', 'age', 'country'}

def test_find_common_values():
    hashtable1 = Hashtable()
    hashtable1.set('name', 'John')
    hashtable1.set('age', 30)
    hashtable1.set('country', 'USA')

    hashtable2 = Hashtable()
    hashtable2.set('name', 'John')
    hashtable2.set('age', 25)
    hashtable2.set('city', 'New York')

    common_values = hashtable1.find_common_values(hashtable2)
    assert common_values == {'John'}

    hashtable2.set('country', 'USA')
    common_values = hashtable1.find_common_values(hashtable2)
    assert common_values == {'John', 'USA'}

    hashtable2.set('age', 30)
    common_values = hashtable1.find_common_values(hashtable2)
    assert common_values == {'John', 'USA', 30}
