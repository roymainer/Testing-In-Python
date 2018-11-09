"""
Fixtures leverage a concecpt of dependancy injection

the tests are have a dependancy with the argument cur so we are injecting it using a fixture
"""

from example2_mock_and_fixtures.mydb import MyDB
import pytest



@pytest.fixture(scope="module")
def cur():
    """
    scope="module" : do this once at the module level, not once for each test
    yield curs : when finished with cur, do this:... (teardown method)
    :return:
    """
    print("\nSetting up")
    db = MyDB()
    conn = db.connect("sever")
    _cur = conn.cursor()
    yield _cur
    print("\nTearing down")
    _cur.close()
    conn.close()


def test_johns_id(cur):
    # these lines can be removed
    # db = MyDB()
    # conn = db.connect("server")
    # cur = conn.cursor()
    id = cur.execute("select id from employee_db where name=John")
    assert id == 123


def test_toms_id(cur):
    # db = MyDB()
    # conn = db.connect("server")
    # cur = conn.cursor()
    id = cur.execute("select id from employee_db where name=Tom")
    assert id == 789
