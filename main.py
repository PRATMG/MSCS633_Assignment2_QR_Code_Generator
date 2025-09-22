#!/usr/bin/env python3
"""
QR Code Generator for Biox Systems (or any URL)

- Prompts for a URL (defaults to https://www.bioxsystems.com).
- Validates the URL format.
- Generates a high-quality PNG QR code to the ./output/ folder.
- Displays the image after saving.

Author: Prakash Tamang
Course: MSCS 633 – Advanced Artificial Intelligence
"""

from __future__ import annotations

import sys
import os
from datetime import datetime
from urllib.parse import urlparse

import qrcode
from qrcode.constants import ERROR_CORRECT_H

# Where generated QR images will be stored
OUTPUT_DIR = "output"


def is_valid_url(url: str) -> bool:
    """
    Basic URL validation using urllib.parse.
    Accepts http/https schemes with a netloc.

    :param url: The URL string to validate.
    :return: True if the URL is valid, False otherwise.
    """
    try:
        # Parse the URL and check scheme and network location
        parsed = urlparse(url.strip())
        return parsed.scheme in {"http", "https"} and bool(parsed.netloc)
    except Exception:
        # If parsing fails, it's not a valid URL
        return False


def build_qr(url: str, box_size: int = 10, border: int = 4):
    """
    Create a QRCode object configured for robust error correction and clean edges.

    :param url: The URL data to encode into the QR code.
    :param box_size: Size of each box in pixels; larger values produce bigger QR codes.
    :param border: Width of the white border around the QR code, measured in boxes.
    :return: A PIL image object representing the generated QR code.
    """
    # Initialize QRCode with high error correction
    qr = qrcode.QRCode(
        version=None,                  # let the library pick the best version
        error_correction=ERROR_CORRECT_H,  # ~30% error correction
        box_size=box_size,             # pixel size of each box
        border=border                  # white border around the QR
    )
    qr.add_data(url)
    qr.make(fit=True)
    return qr.make_image(fill_color="black", back_color="white")


def ensure_output_dir(path: str = OUTPUT_DIR) -> None:
    """
    Ensure that the output directory exists. If not, create it.

    :param path: Directory path to check or create.
    """
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)


def main() -> int:
    """
    Entry point for the QR generator. Prompts the user for a URL,
    validates the input, generates a QR code, saves it to disk,
    and attempts to display it using the default image viewer.

    :return: Exit code (0 for success, non-zero for errors).
    """
    print("=== QR Code Generator ===")
    default_url = "https://www.bioxsystems.com"
    # Prompt user for input, using default if empty
    user_input = input(f"Enter a URL [{default_url}]: ").strip() or default_url

    # Validate the URL format
    if not is_valid_url(user_input):
        print("Error: Please enter a valid http(s) URL, e.g., https://example.com")
        return 1

    # Ensure output directory exists
    ensure_output_dir()

    # Use timestamp to create a unique filename
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = f"qr_{timestamp}.png"
    filepath = os.path.join(OUTPUT_DIR, filename)

    # Generate QR image and save
    img = build_qr(user_input)
    img.save(filepath)

    print(f"Saved QR code to: {filepath}")

    # Attempt to open the image in default viewer for preview
    try:
        img.show(title="QR Code")
    except Exception:
        # Not fatal if viewer isn't available
        pass

    return 0


if __name__ == "__main__":
    sys.exit(main())