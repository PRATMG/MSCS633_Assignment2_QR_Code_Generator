# QR Code Generator (Biox Systems)

This simple Python tool generates a QR code PNG for any URL you enter.  
By default it uses the Biox Systems website (`https://www.bioxsystems.com`).

## Quick Start

```bash
# 1) Create and activate a virtual environment (recommended)
python -m venv .venv

# Windows:
.venv\Scripts\activate

# macOS/Linux:
source .venv/bin/activate

# 2) Install dependencies
pip install -r requirements.txt

# 3) Run
python main.py
# Press Enter to accept the default, or paste another URL.

# 4) Output
# A PNG is saved to ./output/ e.g., output/qr_20250921-2145.png
```

Notes:

* Uses high error correction (`H`) to improve readability.
* `img.show()` tries to open your default image viewer for an immediate preview.

---

## How to run (step-by-step)

1. **Install Python** (3.9+ recommended).
2. **Create a virtual environment**
   - Windows (PowerShell):

     ```
     python -m venv .venv
     .venv\Scripts\Activate
     ```

   - macOS/Linux:

     ```
     python3 -m venv .venv
     source .venv/bin/activate
     ```
3. **Install the library**

   ```
   pip install -r requirements.txt
   ```

4. **Run the program**

   ```
   python main.py
   ```

   Press **Enter** to use the default `https://www.bioxsystems.com`, or paste another URL.

5. A PNG file appears in `./output/` and a preview window pops up.

