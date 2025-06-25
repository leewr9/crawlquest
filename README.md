# CrawlQuest
[![Test Status](https://github.com/leewr9/crawlquest/actions/workflows/test.yml/badge.svg)](https://github.com/leewr9/crawlquest/actions/workflows/test.yml)
[![Publish Status](https://github.com/leewr9/crawlquest/actions/workflows/publish.yml/badge.svg)](https://github.com/leewr9/crawlquest/actions/workflows/publish.yml)


Lightweight wrapper around Python `requests` that automatically chooses between `GET` and `POST` based on the presence of a payload.  
Perfect for **web scraping**, **automation**, and **crawling tools** where fast and adaptive request behavior is needed.

## Features

- Automatically uses `GET` if no payload, `POST` if payload is present
- Supports returning **JSON**, **HTML**, **raw bytes**
- Optional `requests.Session` injection for cookie/session reuse
- Simple API with built-in error handling
- Customizable timeout and headers

## Installation

```bash
pip install crawlquest
```

### Alternatively, install manually

```bash
git clone https://github.com/leewr9/crawlquest.git
cd crawlquest
pip install .
```

## Usage

```python
from crawlquest import json, html, raw

# Automatically POSTs (since payload exists)
res = json("https://httpbin.org/post", payload={"key": "value"})

# Automatically GETs (no payload)
html_content = html("https://example.com")

# Raw bytes (e.g., image or file)
binary = raw("https://httpbin.org/image/png")
```

### Using a persistent session (cookie reuse)

```python
import requests
from crawlquest import json

session = requests.Session()
json("https://httpbin.org/cookies/set?mycookie=value", session=session)
res = json("https://httpbin.org/cookies", session=session)

print(res)
# Output: {'cookies': {'mycookie': 'value'}}
```

## API Reference

### `json(url, payload=None, headers=None, timeout=10.0, session=None) -> dict | None`

- Automatically parses JSON response.
- Returns `None` if decoding fails.

### `html(url, ...) -> str`

- Returns the text (HTML) of the response.
- Automatically applies `apparent_encoding` if needed.

### `raw(url, ...) -> bytes`

- Returns the raw byte content (e.g., for images or binary files).

## Error Handling

All internal HTTP calls raise `RuntimeError` with context on failure

```python
try:
    data = json("https://example.com/api")
except RuntimeError as e:
    print(f"Request failed: {e}")
```

## License  
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.  
