from test_package.lib import try_me

def test_try_me():
    assert len(try_me()) >= 0
    assert type(try_me()) == str
