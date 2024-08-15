from movdata.movieInfo import save_movieInfo

def test_save_movieInfo():
    for y in range(2015, 2022):
        r = save_movieInfo(year=y, sleep_time=0.1)
    assert r
