# -*- coding: utf-8 -*-
class DictType(dict):
    def __init__(self, init):
        for k, v in init.items():
            self[k] = v
