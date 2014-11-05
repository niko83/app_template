#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import json


class JSONRequest(object):
    def __init__(self, json_str):
        self.json_str = json_str
        self.filtred_data = {}
        self.warnings = []

    @property
    def json(self):
        return json.loads(self.json_str)

    def getWarnings(self):
        return self.warnings

    def setToKey(self, keys, obj):
        tmp_data = self.filtred_data
        for key in keys[:-1]:
            try:
                tmp_data = tmp_data[key]
            except KeyError:
                tmp_data[key] = {}
                tmp_data = tmp_data[key]

        tmp_data[keys[-1]] = obj

    def getPosInt(self, keys, interval=None, default=None):
        self.getInt(keys, interval=[1, sys.maxint], default=default)

    def getInt(self, keys, interval=None, default=None):
        try:
            val = int(self._get_by_keys(keys))
        except (ValueError, TypeError, KeyError):
            self.warnings.append('msg')
            if default:
                self.warnings.append(' not found %s, use default %s' % (keys, default))
                self.setToKey(keys, default)
            raise Exception('incorrect')

        if interval:
            if interval[0] <= val <= interval[1]:
                self.setToKey(keys, val)
            else:
                raise Exception('interval %s %s', interval)
        else:
            self.setToKey(keys, val)

    def getBool(self, keys, default=None):
        try:
            self.setToKey(keys, bool(self._get_by_keys(keys)))
        except (ValueError, TypeError, KeyError):
            self.warnings.append('msg')
            if default:
                self.warnings.append(' not found %s, use default %s' % (keys, default))
                self.setToKey(keys, default)
            raise Exception('incorrect')

    def getStr(self, keys, interval=None, default=None):
        try:
            return unicode(self._get_by_keys(keys))
        except (ValueError, TypeError, KeyError):
            self.warnings.append('Bad value %s' % (keys))
            if default:
                self.warnings.append(' not found %s, use default %s' % (keys, default))
                self.setToKey(keys, default)
            raise Exception('incorrect')

    def getEnum(self, keys, enum=None, default=None):
        enum = enum or []
        try:
            val = self._get_by_keys(keys)
        except KeyError:
            if default:
                self.warnings.append(' not found %s, use default %s' % (keys, default))
                self.setToKey(keys, default)
                return
            raise Exception('not foud key')
        else:
            if val in enum:
                return val

    def getObj(self, keys, default=None):
        try:
            return self._get_by_keys(keys)
        except KeyError:

            if default:
                self.warnings.append(' not found %s, use default %s' % (keys, default))
                self.setToKey(keys, default)
            else:
                raise Exception('not foud key %s' % keys)

    def getList(self, keys, default=None, parser=None, count=None):

        try:
            val = self._get_by_keys(keys)
        except KeyError:
            if default:
                self.warnings.append(' not found %s, use default %s' % (keys, default))
                self.setToKey(keys, default)
            else:
                raise Exception('not foud key')
        else:
            if parser:
                parsed_val = []
                for item in val:
                    parsed_val.append(parser(item))
                val = parsed_val

            if count and len(val) != count:
                raise Exception('length of list is not valid %s, %s', len(val), count)

            self.setToKey(keys, val)

    def _get_by_keys(self, keys):
        tmp_data = self.json
        for key in keys:
            tmp_data = tmp_data[key]

        return tmp_data
