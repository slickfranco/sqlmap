#!/usr/bin/env python

"""
Copyright (c) 2006-2013 sqlmap developers (http://sqlmap.org/)
See the file 'doc/COPYING' for copying permission
"""

import re

from lib.core.enums import HTTPHEADER
from lib.core.settings import WAF_ATTACK_VECTORS

__product__ = "Teros/Citrix Application Firewall Enterprise (Teros/Citrix Systems)"

def detect(get_page):
    retval = False

    for vector in WAF_ATTACK_VECTORS:
        page, headers, code = get_page(get=vector)
        retval = re.search(r"\Ast8(id|_wat|_wlf)", headers.get(HTTPHEADER.SET_COOKIE, ""), re.I) is not None
        if retval:
            break

    return retval
