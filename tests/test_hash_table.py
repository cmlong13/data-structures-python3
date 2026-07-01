import sys
from pathlib import Path

import pytest


ROOT_DIR = Path(__file__).resolve().parents[1]
SRC_DIR = ROOT_DIR / "src"

if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from HashTable.HashTable import HashTable


class CollidingKey:
    def __init__(self, value):
        self.value = value

    def __hash__(self):
        return 42

    def __eq__(self, other):
        return isinstance(other, CollidingKey) and self.value == other.value


def test_new_hash_table_is_empty():
    table = HashTable()

    assert table.is_empty()
    assert table.size() == 0
    assert table.keys() == []
    assert table.values() == []
    assert table.items() == []


def test_set_adds_key_value_pairs():
    table = HashTable()

    table.set("name", "Ada")
    table.set("language", "Python")

    assert not table.is_empty()
    assert table.size() == 2
    assert table.get("name") == "Ada"
    assert table.get("language") == "Python"
    assert "name" in table


def test_set_updates_existing_key_without_growing_size():
    table = HashTable()

    table.set("name", "Ada")
    table.set("name", "Grace")

    assert table.size() == 1
    assert table.get("name") == "Grace"


def test_remove_returns_value_and_deletes_key():
    table = HashTable()
    table.set("name", "Ada")
    table.set("language", "Python")

    removed = table.remove("name")

    assert removed == "Ada"
    assert table.size() == 1
    assert not table.contains("name")
    assert table.get("language") == "Python"


def test_dictionary_style_access():
    table = HashTable()

    table["topic"] = "data structures"

    assert table["topic"] == "data structures"

    del table["topic"]

    assert table.is_empty()


def test_keys_values_and_items_return_all_entries():
    table = HashTable()
    table.set("first", 1)
    table.set("second", 2)

    assert set(table.keys()) == {"first", "second"}
    assert set(table.values()) == {1, 2}
    assert set(table.items()) == {("first", 1), ("second", 2)}


def test_clear_removes_all_entries():
    table = HashTable()
    table.set("first", 1)
    table.set("second", 2)

    table.clear()

    assert table.is_empty()
    assert table.size() == 0
    assert table.keys() == []


def test_missing_key_operations_raise_key_error():
    table = HashTable()

    with pytest.raises(KeyError):
        table.get("missing")

    with pytest.raises(KeyError):
        table.remove("missing")


def test_capacity_must_be_positive():
    with pytest.raises(ValueError):
        HashTable(0)


def test_hash_collisions_keep_keys_separate():
    table = HashTable(capacity=2)
    first = CollidingKey("first")
    second = CollidingKey("second")

    table.set(first, "one")
    table.set(second, "two")

    assert table.size() == 2
    assert table.get(first) == "one"
    assert table.get(second) == "two"

    table.set(first, "updated")

    assert table.size() == 2
    assert table.get(first) == "updated"
    assert table.get(second) == "two"
