#!/usr/bin/env python3
"""
REGEX-ING
"""

import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """ returns obfuscated values of fields """
    for item in fields:
        message = re.sub(r'{}=.*?{}'.format(item, separator),
                         item + "=" + redaction + separator, message)
    return message
