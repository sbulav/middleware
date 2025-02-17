# -*- coding=utf-8 -*-
import contextlib

from middlewared.test.integration.utils import call

__all__ = ["api_key"]


@contextlib.contextmanager
def api_key(allowlist):
    key = call("api_key.create", {"name": "Test API KEY", "allowlist": allowlist})
    try:
        yield key["key"]
    finally:
        call("api_key.delete", key["id"])
