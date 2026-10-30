from carrinho import total_com_desconto

def test_carrinho():
    assert total_com_desconto([10, 20, 30, 40, 50]) == 141.0
    
    assert total_com_desconto([]) == 0.0
    assert total_com_desconto([10, 20, 30]) == 60.0
    assert total_com_desconto([10.111]) == 10.11