import pytest

from utils import get_next_url
from utils import get_prev_url


@pytest.mark.parametrize("url, len_data, page, page_size, expected",
                         [("url", 1, 1, 2, None),
                          ("url", 1, 1, 1, "url?page=2"),
                          ("url?q=hola", 1, 1, 1, "url?q=hola&page=2"),
                          ("url?q=hola&page_size=1", 1, 1, 1, "url?q=hola&page_size=1&page=2"),
                          ("url?q=hola&page=3", 1, 3, 1, "url?q=hola&page=4"),
                          ("url?q=hola&page=3&page_size=1", 1, 3, 1, "url?q=hola&page=4&page_size=1")])
def test_get_next_url(
    url: str,
    len_data: int,
    page: int,
    page_size: int,
    expected: str,
) -> None:
    assert get_next_url(url=url, len_data=len_data, page=page, page_size=page_size) == expected


@pytest.mark.parametrize("url, page, expected",
                         [("url", 1, None),
                          ("url", 3, "url?page=2"),
                          ("url?q=hola", 3, "url?q=hola&page=2"),
                          ("url?q=hola&page_size=1", 3, "url?q=hola&page_size=1&page=2"),
                          ("url?q=hola&page=3", 3, "url?q=hola&page=2"),
                          ("url?q=hola&page=3&page_size=1", 3, "url?q=hola&page=2&page_size=1")])
def test_get_prev_url(
    url: str,
    page: int,
    expected: str,
) -> None:
    assert get_prev_url(url=url, page=page) == expected
