import os
import base64
import json

from typing import Union


def is_base64(value: Union[bytes, str]) -> bool:
    try:
        if isinstance(value, str):
            value = value.encode("utf-8")
        return base64.b64encode(base64.b64decode(value)) == value
    except (Exception,):
        return False


if __name__ == '__main__':
    auth_token = os.getenv('MOMENTO_AUTH_TOKEN')

    if is_base64(auth_token):
        print("decode")
        decode_b64_token = base64.b64decode(auth_token).decode('utf-8')
        decode_info = json.loads(decode_b64_token)

        print(decode_info)
