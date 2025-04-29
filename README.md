# IRCTC Ticket Booking Automation (Simulated)

This project demonstrates the automation of IRCTC ticket booking using **Selenium** and **Python**. It uses locally hosted **mock HTML pages** to simulate the IRCTC website for testing and experimentation purposes.

## Project Structure

- **`mock_site/`**: Contains local HTML files that mimic IRCTC's website for simulation purposes.
- **`pages/`**: Implements the Selenium Page Object Model (POM) for the application's web pages.
- **`tests/`**: Includes test scripts written with PyTest to validate various automation scenarios.
- **`main.py`**: Orchestrates the complete ticket booking process.
- **`requirements.txt`**: Lists the Python dependencies needed for the project.

## Setup and Usage

Follow these steps to set up and run the project:

### 1. Install Dependencies 

Ensure Python is installed on your system, then install the required dependencies:
```bash
pip install -r requirements.txt

### 2. Launch the Mock Website

Open the login page of the simulated IRCTC website in your browser:

mock_site/login.html
mock_site/search.html
mock_site/booking.html
mock_site/payment.html

### 3. Run the Automation Script

To execute the complete ticket booking flow, run the main.py script:

python3 main.py

### 4. Execute Tests

Run the test cases using PyTest to validate the automation flow:

pytest tests  --html=report/all_tests.html
pytest tests/test_login.py --html=report/test_report_login.html
pytest tests/test_search.py --html=report/test_report_search.html
pytest tests/test_booking.py --html=report/test_report_booking.html
pytest tests/test_L_S_B_P.py  --html=report/test_report_L_S_B_P.html
pytest tests/test_e2e.py --html=report/test_report_e2e.html

## Key Features

Selenium Automation: Automates user interactions on the simulated IRCTC website.
Mock HTML Pages: Provides a safe and controlled environment for testing.
Page Object Model (POM): Ensures modular and maintainable test scripts.
PyTest Integration: Enables robust testing and validation of the automation flow.


