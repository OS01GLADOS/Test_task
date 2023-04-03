def find_fake_basket(N, w, d, P):
    total_weight = (N * (N + 1) // 2 - P) * w
    fake_weight = w - d
    fake_basket = int(total_weight / fake_weight)
    return fake_basket


def test_find_fake_basket():
    assert find_fake_basket(N=1, w=10, d=2, P=0) == 1
    assert find_fake_basket(N=1, w=10, d=2, P=45) == 1
    assert find_fake_basket(N=2, w=10, d=2, P=0) == 1
    assert find_fake_basket(N=2, w=10, d=2, P=55) == 2
    assert find_fake_basket(N=5, w=10, d=2, P=15) == 3
    assert find_fake_basket(N=5, w=10, d=2, P=10) == 1
    assert find_fake_basket(N=5, w=10, d=2, P=40) == 5
