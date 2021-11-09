from typing import Optional


def get_next_url(
    url: str,
    len_data: int,
    page: int,
    page_size: int,
) -> Optional[str]:
    next_url = None
    if len_data == page_size:
        url_has_page = (url.find(f"page={page}") != -1)
        url_has_params = (url.find("?") != -1)

        if url_has_page:
            next_url = url.replace(f"page={page}", f"page={page + 1}")
        elif url_has_params:
            next_url = f"{url}&page={page + 1}"
        else:
            next_url = f"{url}?page={page + 1}"

    return next_url


def get_prev_url(
    url: str,
    page: int,
) -> Optional[str]:
    prev_url = None
    if page > 1:
        url_has_page = (url.find(f"page={page}") != -1)
        url_has_params = (url.find("?") != -1)

        if url_has_page:
            prev_url = url.replace(f"page={page}", f"page={page - 1}")
        elif url_has_params:
            prev_url = f"{url}&page={page - 1}"
        else:
            prev_url = f"{url}?page={page - 1}"

    return prev_url
