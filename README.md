# IRCTC Ticket Booking Automation (Simulated)
![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Selenium](https://img.shields.io/badge/Selenium-Automation-green)
![pytest](https://img.shields.io/badge/Pytest-8.3.1-blue)
![Html](https://img.shields.io/badge/HTML-Report-orange)
![HTML Report](https://img.shields.io/badge/HTML--Report-orange)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow)

This project provides a robust simulation of IRCTC ticket booking automation using Selenium and Python. It leverages locally hosted mock HTML pages to replicate the IRCTC website, enabling safe and controlled testing of automation scripts without interacting with the live platform.

## Project Overview

The IRCTC Ticket Booking Automation project is designed to demonstrate and test the automation of ticket booking processes in a simulated environment. By using mock HTML pages and a modular framework, it ensures scalability, maintainability, and safe experimentation.

### Key Features

- **Selenium Automation**: Automates user interactions for login, train search, ticket booking, and payment workflows using the Page Object Model.
- **Mock HTML Pages**: Simulates IRCTC website pages locally (`mock_site/`) for safe, repeatable testing.
- **Cross-Browser Support**: Easily run tests on Chrome, Firefox, or Edge using the `--browser` option.
- **PyTest Integration**: Comprehensive test suites with detailed HTML reports for validation.
- **Sanity & E2E Tests**: Includes both quick sanity scripts and full end-to-end automation flows.
- **Logging**: Centralized logging of automation and test runs in the `logs/` directory.
- **Reporting Capabilities**: Generates and distributes test reports via email and Telegram.
- **Extensible Framework**: Modular structure for adding new features, test cases, or workflows.
- **Configuration Management**: Centralized test data and configuration in the `configurations/` directory.

## Project Structure

- [`mock_site/`](mock_site/): Local HTML files simulating IRCTC website pages ([`login.html`](mock_site/login.html), [`search.html`](mock_site/search.html), [`booking.html`](mock_site/booking.html), [`payment.html`](mock_site/payment.html)).
- [`pages/`](pages/): Selenium POM classes for interacting with simulated web pages.
- [`tests/`](tests/): PyTest scripts for validating automation workflows.
- [`configurations/`](configurations/): Test data and configuration scripts.
- `sanity/`: Scripts for quick sanity checks of critical functionalities.
- [`report/`](report/): Tools for generating and sending test reports via email and Telegram.
- [`logs/`](logs/): Log files for automation and sanity test runs.
- [`main.py`](main.py): Orchestrates the end-to-end ticket booking automation process.
- [`requirements.txt`](requirements.txt): Lists Python dependencies required for the project.
- [`utilities/`](utilities/): Utility scripts and helpers.

## Setup and Usage

### Prerequisites

- ![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python) Python 3.8 or higher
- ![Google Chrome](https://img.shields.io/badge/Chrome-Browser-green?logo=googlechrome) Google Chrome browser
- ![ChromeDriver](https://img.shields.io/badge/ChromeDriver-Compatible-blue?logo=googlechrome) ChromeDriver compatible with the installed Chrome version
- ![Mozilla Firefox](https://img.shields.io/badge/Firefox-Browser-orange?logo=firefox-browser) Mozilla Firefox browser
- ![GeckoDriver](https://img.shields.io/badge/GeckoDriver-Compatible-orange?logo=firefox-browser) GeckoDriver compatible with the installed Firefox version
- ![Microsoft Edge](https://img.shields.io/badge/Edge-Browser-blue?logo=microsoftedge) Microsoft Edge browser
- ![EdgeDriver](https://img.shields.io/badge/EdgeDriver-Compatible-blue?logo=microsoftedge) EdgeDriver compatible with the installed Edge version
- ![Git](https://img.shields.io/badge/Git-VersionControl-red?logo=git) Git (for cloning the repository)

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/mohanmulakalapalli/IRCTC-Ticket-Booking-Bot-Automation.git
   cd IRCTC-Ticket-Booking-Bot-Automation
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Automation

1. **Launch the Mock Website**:
   - Open the HTML files in [`mock_site/`](mock_site/) ([`login.html`](mock_site/login.html), [`search.html`](mock_site/search.html), [`booking.html`](mock_site/booking.html), [`payment.html`](mock_site/payment.html)) using a local server or directly in Google Chrome.
   - Example: Use Python's HTTP server:
     ```bash
     python -m http.server 8000
     ```
     Access at [http://localhost:8000/mock_site/login.html](http://localhost:8000/mock_site/login.html).

2. **Execute the Main Script**:
   To execute the complete ticket booking flow, run the [`main.py`](main.py) script:

   ```bash
   python3 main.py
   ```

### Cross-Browser Testing

This framework supports Chrome, Firefox, and Edge browsers.  
To run tests on a specific browser, use the `--browser` option:

```bash
# For Chrome (default)
pytest tests/

# For Firefox
pytest tests/ --browser=firefox

# For Edge
pytest tests/ --browser=edge
```

Make sure the corresponding driver (ChromeDriver, GeckoDriver, or EdgeDriver) is installed and available at the specified path in [`tests/conftest.py`](tests/conftest.py).

### Running Tests

Run test suites using PyTest with HTML reporting:

```bash
pytest tests/ --html=report/all_tests.html
```

Individual test cases:
```bash
pytest tests/test_login.py --html=report/test_report_login.html
pytest tests/test_search.py --html=report/test_report_search.html
pytest tests/test_booking.py --html=report/test_report_booking.html
pytest tests/test_L_S_B_P.py --html=report/test_report_L_S_B_P.html
pytest tests/test_e2e.py --html=report/test_report_e2e.html
```

### Running Sanity Tests

Execute sanity tests for rapid validation:
```bash
python3 sanity_report_email.py
```

### Generating Reports

- **Email Reports**:
  - Configure email settings in [`sanity_report_email.py`](sanity_report_email.py).
  - Run:
    ```bash
    python sanity_report_email.py
    ```

- **Telegram Reports**:
  - Set up your Telegram bot token in [`telegram_bot_report.py`](telegram_bot_report.py).
  - Run:
    ```bash
    python telegram_bot_report.py
    ```

- **HTML Reports (Interactive):**
  - PyTest generates interactive HTML reports for each test suite.
  - These reports allow you to:
    - Filter results by status (Passed, Failed, Skipped, etc.)
    - Expand/collapse test details and logs
    - View attached screenshots or media for failed steps
    - Sort tests by result, name, or duration
  - Example command:
    ```bash
    pytest tests/ --html=report/all_tests.html
    ```
  - Example reports:
    - [report/test_report_login.html](report/test_report_login.html)
    - [report/test_report_search.html](report/test_report_search.html)
    - [report/test_report_booking.html](report/test_report_booking.html)
    - [report/test_report_L_S_B_P.html](report/test_report_L_S_B_P.html)
    - [report/test_report_e2e.html](report/test_report_e2e.html)
    -[report/all_tests.html](report/all_tests.html)

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For questions, feedback, or support, please reach out:

- **Author**: Mulakalapalli Mohana Krishna
- **Email**: mohanmulakalapalli@gmail.com
- **GitHub**: [mohanmulakalapalli](https://github.com/mohanmulakalapalli)

---

*This project is for educational and testing purposes only. It does not interact with the live IRCTC website and should not be used for actual ticket booking.*




