from example2_mock_and_fixtures.mydb import MyDB

conn = None
cur = None


# to avoid redundant coding for each test:
def setup_module(module):
    """
    will run at module start
    :param module:
    :return:
    """
    global conn
    global cur
    db = MyDB()
    conn = db.connect("sever")
    cur = conn.cursor()


def teardown_module(module):
    """
    teardown will run when execution is finished
    :param module:
    :return:
    """
    cur.close()
    conn.close()


def test_johns_id():
    # these lines can be removed
    # db = MyDB()
    # conn = db.connect("server")
    # cur = conn.cursor()
    id = cur.execute("select id from employee_db where name=John")
    assert id == 123


def test_toms_id():
    # db = MyDB()
    # conn = db.connect("server")
    # cur = conn.cursor()
    id = cur.execute("select id from employee_db where name=Tom")
    assert id == 789
