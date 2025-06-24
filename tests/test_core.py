import pytest
from crawlquest import json, html


def test_json_get():
    res = json("https://httpbin.org/get")
    assert isinstance(res, dict)
    assert res["url"] == "https://httpbin.org/get"


def test_json_post():
    payload = {"hello": "world"}
    res = json("https://httpbin.org/post", payload=payload)
    assert res["json"] == payload


def test_html_get():
    res = html("https://example.com")
    assert "<html" in res.lower()


def test_bad_url():
    with pytest.raises(RuntimeError):
        json("https://example.com/api")
