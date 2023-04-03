def swap_bytes(num):
    byte1 = num & 0xFF
    byte2 = (num >> 8) & 0xFF 
    return (byte1 << 8) | byte2


def test_swap_bytes():
    assert swap_bytes(0x1234) == 0x3412
    assert swap_bytes(0x5678) == 0x7856
    assert swap_bytes(0xABCD) == 0xCDAB
    assert swap_bytes(0xEF01) == 0x01EF
    assert swap_bytes(0x0000) == 0x0000
    assert swap_bytes(0xFFFF) == 0xFFFF
