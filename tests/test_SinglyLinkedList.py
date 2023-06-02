from DataTypes.SinglyLinkedList import SinglyLinkedList as sll
from tests.jsons_t.json_attrs import get_attr_sll_TEST as func_json

sll_Test = sll('TEST', 1, True, "", "True", [], {})


def test_init():
    sll1 = sll("ssl1")

    assert sll1.head is None
    assert sll1.tail is None
    assert sll1.name == "ssl1"


def test_len():
    assert len(sll_Test) == 6


def test_append():
    test_len()
    sll_Test.append(3)

    assert len(sll_Test) == 7


def test_attrs():
    test_len()

    for i in range(len(sll_Test)):
        attrs = func_json()
        assert type(sll_Test[i]) == type(attrs[i])
        assert sll_Test[i] == attrs[i]

    assert sll_Test[2] == ""


def test_remove():
    test_len()

    assert sll_Test[0] == 1

    del sll_Test[0]

    assert sll_Test[0] == True

    del sll_Test[2]

    assert sll_Test[2] == []

    del sll_Test[3]

    assert sll_Test[2] == []
