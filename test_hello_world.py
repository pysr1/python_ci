from duckdb import sql

def hello_world():
    return 'hello world'


def test_hello_world():
    output = hello_world()
    assert output == 'hello world'

def test_duckdb_query():
    sql('SELECT 42'