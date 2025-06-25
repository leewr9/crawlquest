import requests
import json as jsonlib
from typing import Optional, Dict, Any, Union


def _fetch(
    url: str,
    payload: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    timeout: float = 10.0,
    session: Optional[requests.Session] = None,
) -> requests.Response:
    """
    Sends a GET or POST request using a session (optional).

    Raises:
        RuntimeError: If the HTTP request fails.
    """
    sess = session or requests.Session()
    try:
        if payload is not None:
            response = sess.post(url, data=payload, headers=headers, timeout=timeout)
        else:
            response = sess.get(url, headers=headers, timeout=timeout)
        response.raise_for_status()
        return response
    except requests.RequestException as e:
        raise RuntimeError(f"HTTP request failed: {e}") from e


def json(
    url: str,
    payload: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    timeout: float = 10.0,
    session: Optional[requests.Session] = None,
) -> Optional[Union[Dict[str, Any], list]]:
    response = _fetch(url, payload, headers, timeout, session)
    try:
        return response.json()
    except (jsonlib.JSONDecodeError, ValueError):
        return None


def raw(
    url: str,
    payload: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    timeout: float = 10.0,
    session: Optional[requests.Session] = None,
) -> bytes:
    response = _fetch(url, payload, headers, timeout, session)
    return response.content


def html(
    url: str,
    payload: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    timeout: float = 10.0,
    session: Optional[requests.Session] = None,
) -> str:
    response = _fetch(url, payload, headers, timeout, session)
    response.encoding = response.apparent_encoding
    return response.text
