from pprint import pprint
import json

from jsfuzz.inspector import load, search


def test_load():
    original_object = {
        "key": "value",
        "array_key": ["a", "b", "c"],
        "float_key": 0.1,
        "int_key": 29,
    }

    js_obj = json.dumps(original_object)

    loaded_object = load(js_obj)

    assert loaded_object["key"] == original_object["key"]
    assert loaded_object["float_key"] == original_object["float_key"]
    assert len(loaded_object["array_key"]) == len(original_object["array_key"])
    assert sorted(loaded_object["array_key"]) == sorted(original_object["array_key"])


def test_search():
    original_object = {
        "key": "value",
        "array_key": ["a", "b", "c"],
        "float_key": 0.1
    }

    js_obj = json.dumps(original_object)

    candidate = search(js_obj, "value")

    print()
    pprint(candidate)
    assert len(candidate) > 0


def test_search_with_payload():
    with open("resources/test_payload.json") as f:
        original_object = json.load(f)

    js_obj = json.dumps(original_object)

    candidate = search(js_obj, "brand")

    print()
    pprint(candidate)
    assert len(candidate) > 0


def test_search_with_value():
    with open("resources/test_payload.json") as f:
        original_object = json.load(f)

    js_obj = json.dumps(original_object)

    candidate = search(js_obj, "65", top_k=10)

    assert len(candidate) <= 10

