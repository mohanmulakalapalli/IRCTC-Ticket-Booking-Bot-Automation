# IRCTC Ticket Booking Automation (Simulated)

This project provides a robust simulation of IRCTC ticket booking automation using Selenium and Python. It leverages locally hosted mock HTML pages to replicate the IRCTC website, enabling safe and controlled testing of automation scripts without interacting with the live platform.

## Project Overview

The IRCTC Ticket Booking Automation project is designed to demonstrate and test the automation of ticket booking processes in a simulated environment. By using mock HTML pages and a modular framework, it ensures scalability, maintainability, and safe experimentation.

### Key Features

- **Selenium Automation**: Automates user interactions, including login, train search, ticket booking, and payment workflows.
- **Mock HTML Pages**: Simulates IRCTC website pages locally for secure and repeatable testing.
- **Page Object Model (POM)**: Organizes code into modular, maintainable classes for each page, enhancing scalability.
- **PyTest Integration**: Provides comprehensive test suites with detailed HTML reports for validation.
- **Sanity Tests**: Includes lightweight scripts to verify core functionalities quickly.
- **Reporting Capabilities**: Generates and distributes test reports via email and Telegram for efficient monitoring.
- **Extensible Framework**: Easily adaptable for additional features, test cases, or custom workflows.

## Project Structure

- `mock_site/`: Local HTML files simulating IRCTC website pages (`login.html`, `search.html`, `booking.html`, `payment.html`).
- `pages/`: Selenium POM classes for interacting with simulated web pages.
- `tests/`: PyTest scripts for validating automation workflows.
- `sanity/`: Scripts for quick sanity checks of critical functionalities.
- `reports/`: Tools for generating and sending test reports via email and Telegram.
- `main.py`: Orchestrates the end-to-end ticket booking automation process.
- `requirements.txt`: Lists Python dependencies required for the project.

## Setup and Usage

### Prerequisites

- Python 3.8 or higher
- Google Chrome browser
- ChromeDriver compatible with the installed Chrome version
- Git (for cloning the repository)

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
   - Open the HTML files in `mock_site/` (`login.html`, `search.html`, `booking.html`, `payment.html`) using a local server or directly in Google Chrome.
   - Example: Use Python's HTTP server:
     ```bash
     python -m http.server 8000
     ```
     Access at `http://localhost:8000/mock_site/login.html`.

2. **Execute the Main Script**:
   To execute the complete ticket booking flow, run the main.py script:

   ```bash
   python3 main.py

   ```

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
python3 sanity_report_email.py.py
```

### Generating Reports

- **Email Reports**:
  - Configure email settings in `sanity_report_email.py`.
  - Run:
    ```bash
    python sanity_report_email.py
    ```

- **Telegram Reports**:
  - Set up your Telegram bot token in `telegram_bot_report.py`.
  - Run:
    ```bash
    python telegram_bot_report.py
    ```
## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For questions, feedback, or support, please reach out:

- **Author**: Mulakalapalli Mohana Krishna
- **Email**: mohanmulakalapalli@gmail.com
- **GitHub**: [mohanmulakalapalli](https://github.com/mohanmulakalapalli)

---

*This project is for educational and testing purposes only. It does not interact with the live IRCTC website and should not be used for actual ticket booking.*




