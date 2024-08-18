from movdata.peopleInfo import save_peopleInfo

def test_save_peopleInfo():
    r = save_peopleInfo(sleep_time=0.1)
    assert r
