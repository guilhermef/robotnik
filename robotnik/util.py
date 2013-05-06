import re
import operator
from distutils.version import LooseVersion

COMPARE = {'>=': operator.ge,
           '>': operator.gt,
           '<=': operator.le,
           '<': operator.lt,
           '==': operator.eq}


def string_version_compare(version_string, last_version):
    if ',' in version_string:
        version_string = version_string.split(',')[1]

    comp, version = re.match('([<>=]+)([\w\.]+)', version_string).groups()

    parsed_last_verion, parsed_current_version = LooseVersion(last_version), LooseVersion(version)

    if COMPARE[comp](parsed_last_verion, parsed_current_version):
        result = {'status': True, 'type': 'updated'}
    else:
        result = {'status': False}
        if not parsed_last_verion.version[0] == parsed_current_version.version[0]:
            result['type'] = 'major_outdated'
        else:
            result['type'] = 'minor_outdated'

    return result
