#!/usr/bin/env python3
"""
Function to filter the message
"""

import re


def filter_datum(fields, redaction, message, separator):
    """
    Filter the datum
    """
    escape_filter = [
        re.escape(f) + r'=[^' + re.escape(separator) + r']*' for f in fields
    ]
    filter = f"({'|'.join(escape_filter)})"
    return re.sub(filter, lambda match: match.group(0)
                  .split('=')[0] + f"={redaction}", message)
