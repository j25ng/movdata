from movdata.peopleList import save_people

def test_save_people():
    r = save_people(sleep_time=0.1)
    assert r
