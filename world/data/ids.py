from __future__ import annotations

import hashlib
import itertools
import os


class UniqueID:
    """Class for generating unique ID's"""
    used_ids: set[str] = set()

    def __init__(self):
        self._gen_uid()

    def _gen_uid(self) -> None:
        cls = self.__class__

        self._uid = hashlib.md5(os.urandom(32)).hexdigest()

        if self._uid in cls.used_ids:
            #TODO Remove recursion?
            self._uid = cls()

        cls.used_ids.add(self._uid)

    @property
    def id(self) -> str:
        return self._uid


class SequentialID:
    ids = (n for n in itertools.count())

    def __init__(self):
        self._uid = next(self.__class__.ids)

    @property
    def id(self):
        return self._uid
