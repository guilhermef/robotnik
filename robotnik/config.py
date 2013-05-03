#!/usr/bin/python
# -*- coding: utf-8 -*-

from derpconf.config import Config, generate_config

Config.define('HEALTHCHECK_TEXT', 'WORKING', 'Healcheck text duhh', 'General')

if __name__ == '__main__':
    generate_config()
