from app.SRC.sort_list import sort_value
test_dict={'a':1, 'b':2,'c':3}
def test_sort_value():
    assert sort_value(test_dict)=={'a':1, 'b':2,'c':3}

