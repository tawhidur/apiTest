# REST API Test Suite 🔴

> **Lightweight Python test scripts for validating REST APIs — GET, POST, and PUT operations with assertion-based verification.**

[![Python](https://img.shields.io/badge/Python-3.8%2B-dc143c?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Requests](https://img.shields.io/badge/Requests-Library-111111?style=for-the-badge&logo=python&logoColor=white)](https://requests.readthedocs.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-dc143c?style=for-the-badge)](LICENSE)
[![Portfolio](https://img.shields.io/badge/Portfolio-tawhidur.github.io-111111?style=for-the-badge&logo=github&logoColor=white)](https://tawhidur.github.io/)

---

## Overview

This project provides a set of focused Python scripts for testing RESTful API endpoints across the most common HTTP methods. Each script demonstrates a distinct request type — **GET**, **POST**, and **PUT** — complete with response validation and status assertion.

Built as part of a broader QA automation portfolio to demonstrate API-level test coverage using Python's `requests` library, without relying on heavyweight test frameworks.

---

## Features

- ✅ **GET request** with header configuration and JSON response validation
- ✅ **POST request** with payload construction and response assertion
- ✅ **PUT request** with body update and status code verification
- ✅ Clear, readable script-per-method structure for easy extension
- ✅ Assertion-based validation on HTTP status codes and response bodies

---

## Tech Stack

[![Python](https://img.shields.io/badge/Python-3.8+-dc143c?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Requests](https://img.shields.io/badge/Requests-2.x-111111?style=for-the-badge)](https://requests.readthedocs.io/)
[![REST API](https://img.shields.io/badge/Protocol-REST-dc143c?style=for-the-badge)](https://restfulapi.net/)

---

## Project Structure

```
apiTest/
├── getapicall.py       # GET request with response validation
├── postRequest.py      # POST request with payload and assertion
├── putRequest.py       # PUT request with body update
├── requirements.txt    # Python dependencies
└── README.md
```

---

## Prerequisites

- Python 3.8 or higher
- pip

---

## Installation

```bash
# Clone the repository
git clone https://github.com/tawhidur/apiTest.git
cd apiTest

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

---

## Usage

Run each script individually to test the corresponding HTTP method:

```bash
# Test GET endpoint
python getapicall.py

# Test POST endpoint
python postRequest.py

# Test PUT endpoint
python putRequest.py
```

**Example output:**

```
200
{'id': 3, 'title': 'Activity 3', 'dueDate': '...', 'completed': False}
✔ Assertion passed: status 200
```

---

## Configuration

The target API base URL and endpoint IDs are configurable via environment variables:

```bash
export API_BASE_URL="https://fakerestapi.azurewebsites.net"
export ACTIVITY_ID=3
```

Or copy `.env.example` to `.env` and fill in your values:

```env
API_BASE_URL=https://fakerestapi.azurewebsites.net
ACTIVITY_ID=3
```

> ⚠️ **Never commit `.env` files.** The `.gitignore` excludes them by default.

---

## Roadmap

- [ ] Add pytest integration for structured test reporting
- [ ] Add DELETE method coverage
- [ ] Parameterize all test inputs via `pytest.mark.parametrize`
- [ ] Integrate with GitHub Actions for CI on every push
- [ ] Generate HTML/Allure test reports

---

## Contributing

This is a personal portfolio project. Issues and suggestions are welcome via GitHub Issues, but pull requests are not actively reviewed.

---

## License

Distributed under the MIT License. See [LICENSE](LICENSE) for details.

---

## Contact

**Tawhidur Rahman** — Senior SQA Lead | CSM  
🌐 [Portfolio](https://tawhidur.github.io/) · 💼 [LinkedIn](https://www.linkedin.com/in/tawhid1/) · 🐦 [@Tawhid_CSE](https://twitter.com/Tawhid_CSE) · ✉️ tawhid.cse@gmail.com

---

*Built by [Tawhidur Rahman](https://tawhidur.github.io/) — 14+ years in SQA | Samsung Research · Progoti Systems*
