import requests


def make_request(method, url, **kwargs):
    method = method.lower()

    if method == 'get':
        response = requests.get(url, **kwargs)

    elif method == 'post':
        response = requests.post(url, **kwargs)

    elif method == 'patch':
        response = requests.patch(url, **kwargs)

    elif method == 'put':
        response = requests.put(url, **kwargs)

    elif method == 'delete':
        response = requests.delete(url, **kwargs)

    else:
        raise ValueError(f"HTTP method '{method}' not supported.")

    return response
