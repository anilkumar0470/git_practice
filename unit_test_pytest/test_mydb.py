from mydb import MyDB
import pytest

@pytest.fixture()
def cur():
    db = MyDB()
    conn = db.connect("server")
    cur = conn.cursor()
    return cur


def test_johns_id(cur):
    id = cur.execute("select id from employee_db where name=John")
    assert id ==123


def test_toms_id(cur):
    id = cur.execute("select id from employee_db where name=Tom")
    assert id == 789