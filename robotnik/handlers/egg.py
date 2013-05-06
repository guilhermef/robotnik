#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import os
import sys
import xmlrpclib
import tornado.web
from robotnik.handlers.base import BaseHandler
from robotnik.util import string_version_compare
from tornado.process import Subprocess

REGEX = re.compile('([\w\-_]+)((?:[=><,]+[\d\w\.,]+)+) (?!\))')


class EggHandler(BaseHandler):

    def _handle_stdout(self, stdout):
        deps = {}
        result = REGEX.findall(stdout)
        client = xmlrpclib.ServerProxy('http://pypi.python.org/pypi')
        for dep in result:
            egg_name = dep[0]
            latest_version = client.package_releases(egg_name)[0]
            deps[egg_name] = string_version_compare(dep[1], latest_version)
            deps[egg_name]['current_version'] = dep[1]
            deps[egg_name]['latest_version'] = latest_version

        self.render('result.html', package_name=self.git_url.split('/')[-1], dependencies=deps)

    def _handle_pip_result(self, setup_py):
        self.sbp.stdout.read_until_close(self._handle_stdout)

    @tornado.web.asynchronous
    def post(self):
        self.git_url = self.get_argument('git_url')
        pip = self.find_pip()
        self.sbp = Subprocess([pip, 'install',  'git+%s' % self.git_url, '--no-install'],
                              io_loop=self.application.main_loop,
                              stdout=Subprocess.STREAM,
                              stderr=Subprocess.STREAM)

        self.sbp.set_exit_callback(self._handle_pip_result)

    @tornado.web.asynchronous
    def get(self):
        self.render('index.html')

    def find_pip(self):
        return os.path.sep.join(os.path.split(sys.executable)[:-1] + ('pip',))
