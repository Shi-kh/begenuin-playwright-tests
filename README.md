# Playwright Test Automation – BeGenuin Project

This repository contains automated end-to-end UI test cases for the BeGenuin web application using [Playwright](https://playwright.dev/) and `pytest`.

---

## Project Setup

### Prerequisites

- Python 3.8 or above installed
- Git installed
- VS Code (optional but recommended)

---

### Install Dependencies

1. Clone the repository:

```bash
git clone https://github.com/yourusername/begenuin-playwright-tests.git
cd begenuin-playwright-tests

# Windows
python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
pip install pytest playwright pytest-playwright

playwright install

#Run All Test Cases:
pytest

#Run Specific Test File:
pytest tests/test_login.py





