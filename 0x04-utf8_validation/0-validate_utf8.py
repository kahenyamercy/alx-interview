#!/usr/bin/python3
"""UTF-8 Validation"""

import sys
from collections import deque


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding"""

    # Count of remaining bytes expected in the current sequence
    remaining_bytes = 0

    for num in data:
        # Check if this is the start of a new character sequence
        if remaining_bytes == 0:
            if num >> 7 == 0b0:
                # Single-byte character
                continue
            elif num >> 5 == 0b110:
                # Two-byte character
                remaining_bytes = 1
            elif num >> 4 == 0b1110:
                # Three-byte character
                remaining_bytes = 2
            elif num >> 3 == 0b11110:
                # Four-byte character
                remaining_bytes = 3
            else:
                # Invalid start of a sequence
                return False
        else:
            # Check if the current byte is following the format 10xxxxxx
            if num >> 6 != 0b10:
                return False
            remaining_bytes -= 1

    # Check if all bytes were used in character sequences
    return remaining_bytes == 0
