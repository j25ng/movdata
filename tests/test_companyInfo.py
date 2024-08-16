from movdata.companyInfo import save_companyInfo

def test_save_companyInfo():
    r = save_companyInfo(sleep_time=0.1)
    assert r
