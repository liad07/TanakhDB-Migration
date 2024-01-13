בס"ד
# Tanakh Text Migration

## Overview

This repository contains a Python script designed to process Tanakh (תנ"ך) text from HTML files obtained from the Mechon Mamre website and populate a Microsoft Access database.

## Getting Started

### Prerequisites

- Python 3.x
- Microsoft Access
- Required Python libraries (install using `pip install -r requirements.txt`):
  - beautifulsoup4
  - chardet
  - pyodbc

### Download Tanakh HTML Files

Download the Tanakh HTML files from the Mechon Mamre website using the following link: [Tanakh HTML Files (t002.zip)](https://mechon-mamre.org/htmlzips/t002.zip)

### Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/liad07/tanakh-text-migration.git
   ```

2. Install required Python libraries:

   ```bash
   pip install -r requirements.txt
   ```

3. Extract the downloaded Tanakh HTML files (t002.zip) into the root of the cloned repository.

4. Run the script:

   ```bash
   python main.py
   ```

## File Structure

- **`main.py`**: The main Python script for processing Tanakh HTML files.
- **`Tanakh.accdb`**: Microsoft Access database for storing Tanakh data.
- **`done/`**: Directory to store processed HTML files.

## Contributing

Contributions are welcome! If you have any improvements or suggestions, feel free to open an issue or submit a pull request.

