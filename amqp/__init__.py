# -*- coding: utf-8 -*-
"""AMQP settings."""
import app_settings


class settings(object):
    """
    If you want redefine any amqp settings use settings_local.py file
    constat_prefix is ``AMQP_`` for example::

      AMQP_TIMEOUT = 3
    """
    TIMEOUT = None

