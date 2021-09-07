from BinaryChop import chop


class TestBinaryChop:
    def test_should_return_minus_1_for_empty_list(self):
        assert chop(3, []) == -1

    def test_should_return_minus_1_when_element_not_in_array(self):
        assert chop(3, [1]) == -1
        assert chop(0, [1, 3, 5]) == -1
        assert chop(2, [1, 3, 5]) == -1
        assert chop(4, [1, 3, 5]) == -1
        assert chop(6, [1, 3, 5]) == -1
        assert chop(0, [1, 3, 5, 7]) == -1
        assert chop(2, [1, 3, 5, 7]) == -1
        assert chop(4, [1, 3, 5, 7]) == -1
        assert chop(6, [1, 3, 5, 7]) == -1
        assert chop(8, [1, 3, 5, 7]) == -1

    def test_should_return_0_if_searched_num_is_first_element_of_array(self):
        assert chop(1, [1]) == 0
        assert chop(1, [1, 3, 5]) == 0
        assert chop(1, [1, 3, 5, 7]) == 0

    def test_should_return_index_of_element_from_array(self):
        assert chop(3, [1, 3, 5]) == 1
        assert chop(5, [1, 3, 5]) == 2
        assert chop(3, [1, 3, 5, 7]) == 1
        assert chop(5, [1, 3, 5, 7]) == 2
        assert chop(7, [1, 3, 5, 7]) == 3
        assert chop(2500, [x for x in range(10000)]) == 2500