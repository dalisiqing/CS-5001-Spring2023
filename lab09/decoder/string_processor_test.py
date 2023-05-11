from string_processor import StringProcessor


def test_process_string():
    """Test for process_string function"""
    # Include the following cases
    # "ab" should yield "" as ouptut
    # "ab*" should yield "b" as output
    # "ab^" should yield "ba" as output
    # "^" should yield "" as output

    t1 = StringProcessor("ab")
    assert t1.process_string() == ''
    t2 = StringProcessor("ab*")
    assert t2.process_string() == 'b'
    t3 = StringProcessor("ab^")
    assert t3.process_string() == 'ba'
    t4 = StringProcessor("^")
    assert t4.process_string() == ''
    t5 = StringProcessor("b-5es^m9c*u?er^xl0t*a")
    assert t5.process_string() == 'secret'
    t6 = StringProcessor("na0s*9-o*veXul^z-2it^,no^pr8")
    assert t6.process_string() == 'solution'
    t7 = StringProcessor("zeM^un-e*0 t^a*l t^75*4a1:^s35*A,P ^2NM* ,^Mc.+GcO^ t^3*,0^2 ^5m0*x22^")
    assert t7.process_string() == 'Meet at 5:15 PM, Oct 30, 2022'
    t8 = StringProcessor("1^*")
    assert t8.process_string() == ''
    t9 = StringProcessor("1^2^")
    assert t9.process_string() == ''
