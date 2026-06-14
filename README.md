![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white)
![Allure](https://img.shields.io/badge/Allure-FF6347?style=for-the-badge&logo=target&logoColor=white)
![Pytest HTML](https://img.shields.io/badge/Pytest--HTML-FFD700?style=for-the-badge)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)
![Allure](https://img.shields.io/badge/Allure-FF6347?style=for-the-badge&logo=target&logoColor=white)
![Jenkins](https://img.shields.io/badge/Jenkins-D24939?style=for-the-badge&logo=jenkins&logoColor=white)

## Pytest Selenium Automation Framework

A scalable and maintainable UI automation framework built using **Python**, **Selenium WebDriver**, and **Pytest** for the **Smart Hospital & Research Center** application. This project was developed for learning and implementing modern test automation practices using industry-standard design patterns and tools.

## Features

- Page Object Model (POM) design pattern with a dedicated Actions layer
- Centralized configuration management using `config.ini`
- Chrome browser automation with custom download and privacy preferences
- Explicit and implicit wait strategies via a reusable `BaseAction` class
- Data-Driven Testing using Excel (`openpyxl`) and CSV data sources
- Structured logging and debugging support
- Pytest parametrization for multiple test scenarios (valid/invalid data)
- Allure Reporting integration
- Pytest HTML Reporting
- Parallel execution support using `pytest-xdist`

## Application Under Test

**Smart Hospital & Research Center**
https://demo.smart-hospital.in/site/login

## Tech Stack

| Technology | Purpose |
|---|---|
| Python 3.x | Programming Language |
| Selenium WebDriver | Browser Automation |
| Pytest | Test Framework |
| pytest-xdist | Parallel Test Execution |
| Allure Reports | Advanced Reporting |
| Pytest HTML | HTML Reporting |
| openpyxl | Excel-based Data-Driven Testing |
| selenium-page-factory | Page Object Support |
| Logging | Test Execution Logs |

## Project Structure

```
Python-Automation-SmartHospital
│
├── configurations/         # config.ini and config reader
├── data_files/              # Excel & CSV test data files
├── pages/                   # Page Object Classes
├── actions/                 # Reusable Actions (built on BaseAction)
├── tests/                   # Test Cases & conftest.py (driver setup)
├── utilities/               # Config reader, Excel/CSV readers, logger
├── requirements.txt
└── .gitignore
└── README.md
```

## Installation

Clone the repository:
```bash
git clone <repository-url>
cd Python-Automation-SmartHospital
```

Install dependencies:
```bash
pip install -r requirements.txt
```

## Configuration

Update the `configurations/config.ini` file with the application URL, browser, and test data such as ambulance details, login messages, medicine details, and income details:

```ini
[info]
url=https://demo.smart-hospital.in/site/login
browser=chrome

[login details]
validassertmess = Smart Hospital & Research Center
invalidmessage = Invalid Username or Password
emptyfielderrmessage = Username field is required
```

## Running Tests

### Run All Tests
```bash
pytest
```

### Verbose Execution
```bash
pytest -v
```

### Run a Specific Test File
```bash
pytest tests/test_login.py -v
```

### Parallel Execution
Run tests using multiple workers:
```bash
pytest -n 4
```

## Generate Reports

### Pytest HTML Report
```bash
pytest --html=reports/report.html --self-contained-html
```

### Allure Report
```bash
pytest --alluredir=allure-results
allure serve allure-results
```

## Modules Covered

- Login (valid, invalid, empty field scenarios)
- Add / Search Patient
- Add Income
- Add Item Stock
- Purchase Medicine
- Verify Medicine
- Blood Stock & Blood Issue Management
- Donor Management
- Ambulance (Add Vehicle, Add Call, Search Call List)
- Contact Us / Pharmacy Bill

## Data-Driven Testing

Test data is read from CSV and Excel files in `data_files/` using the helper utilities `csv_reader.py` and `excel_reader.py`, and fed into tests via `@pytest.mark.parametrize`.

## Contributors
-Tamilarasu
-Darshan Raj
-Balamurugan
-Janani Sri
-Harini 

## License

This project is intended for learning and educational purposes.

Built with Python, Selenium, and Pytest for modern UI test automation.

Happy Testing! 🚀
