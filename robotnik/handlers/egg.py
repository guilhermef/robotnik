#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import os
import sys
import tornado.web
from robotnik.handlers.base import BaseHandler
from tornado.process import Subprocess

REGEX = re.compile('([\w\-_]+)((?:[=><,]+[\d\w\.,]+)+) (?!\))')


class EggHandler(BaseHandler):

    def _handle_stdout(self, stdout):
        deps = {}
        result = REGEX.findall(stdout)
        for dep in result:
            deps[dep[0]] = dep[1]
        self.write(deps)
        self.finish()

    def _handle_pip_result(self, setup_py):
        self.sbp.stdout.read_until_close(self._handle_stdout)

    @tornado.web.asynchronous
    def get(self):
        pip = self.find_pip()
        self.sbp = Subprocess([pip, 'install',  'git+https://github.com/globocom/thumbor', '--no-install'],
                              io_loop=self.application.main_loop,
                              stdout=Subprocess.STREAM,
                              stderr=Subprocess.STREAM)

        self.sbp.set_exit_callback(self._handle_pip_result)

    def find_pip(self):
        return os.path.sep.join(os.path.split(sys.executable)[:-1] + ('pip',))
