from movdata.companyList import save_companies

def test_save_companies():
    r = save_companies(sleep_time=0.1)
    assert r
