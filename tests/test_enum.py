import test_enum_ext as t
import pytest

def test01_unsigned_enum():
    assert repr(t.Enum.A) == 'Enum.A'
    assert repr(t.Enum.B) == 'Enum.B'
    assert repr(t.Enum.C) == 'Enum.C'
    assert t.Enum.A.__name__ == 'A'
    assert t.Enum.B.__name__ == 'B'
    assert t.Enum.C.__name__ == 'C'
    assert t.Enum.A.__doc__ == 'Value A'
    assert t.Enum.B.__doc__ == 'Value B'
    assert t.Enum.C.__doc__ == 'Value C'
    assert int(t.Enum.A) == 0
    assert int(t.Enum.B) == 1
    assert int(t.Enum.C) == 0xffffffff
    assert t.Enum(0) is t.Enum.A
    assert t.Enum(1) is t.Enum.B
    assert t.Enum(0xffffffff) is t.Enum.C
    assert t.Enum(t.Enum.A) is t.Enum.A
    assert t.Enum(t.Enum.B) is t.Enum.B
    assert t.Enum(t.Enum.C) == t.Enum.C
    assert t.from_enum(t.Enum.A) == 0
    assert t.from_enum(t.Enum.B) == 1
    assert t.from_enum(t.Enum.C) == 0xffffffff
    assert t.to_enum(0).__name__ == 'A'
    assert t.to_enum(0) == t.Enum.A
    assert t.to_enum(1) == t.Enum.B
    assert t.to_enum(0xffffffff) == t.Enum.C

    with pytest.raises(RuntimeError) as excinfo:
        t.to_enum(5).__name__
        assert t.test_bad_tuple()
    assert 'nb_enum: could not find entry!' in str(excinfo.value)


def test02_signed_enum():
  assert repr(t.SEnum.A) == 'SEnum.A'
  assert repr(t.SEnum.B) == 'SEnum.B'
  assert repr(t.SEnum.C) == 'SEnum.C'
  assert int(t.SEnum.A) == 0
  assert int(t.SEnum.B) == 1
  assert int(t.SEnum.C) == -1
  assert t.SEnum(0) is t.SEnum.A
  assert t.SEnum(1) is t.SEnum.B
  assert t.SEnum(-1) is t.SEnum.C
  assert t.from_enum(t.SEnum.A) == 0
  assert t.from_enum(t.SEnum.B) == 1
  assert t.from_enum(t.SEnum.C) == -1


def test03_enum_arithmetic():
    assert t.SEnum.B + 2 == 3
    assert 2 + t.SEnum.B == 3
    assert t.SEnum.B >> t.SEnum.B == 0
    assert t.SEnum.B << t.SEnum.B == 2
    assert -t.SEnum.B == -1 and -t.SEnum.C == 1
    assert t.SEnum.B & t.SEnum.B == 1
    assert t.SEnum.B & ~t.SEnum.B == 0

    with pytest.raises(TypeError) as excinfo:
        assert t.Enum.B + 2 == 3
    assert 'unsupported operand type' in str(excinfo.value)
