# TravelVerse E2E Automation Framework

End-to-end test automation for the TravelVerse travel booking platform built with Selenium WebDriver and Python using the Page Object Model design pattern.

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.14 | Programming Language |
| Selenium WebDriver | Browser Automation |
| Pytest | Test Framework |
| WebDriver Manager | Auto ChromeDriver Management |
| Allure | Test Reporting |
| Page Object Model | Design Pattern |

---

## Modules Covered

| Module | Test File | Status |
|--------|-----------|--------|
| Login | test_login.py | Done |
| Flights | test_flights.py | Done |
| Trains | test_trains.py | Done |
| Bus | test_bus.py | Done |
| Movies | test_movies.py | Done |
| Events | test_events.py | Done |
| Sports | test_sports.py | Done |
| Activities | test_activities.py | Done |
| Hotels | test_hotels.py | Done |
| Logout | test_logout.py | Done |

---

## Project Structure

```
TRAVELVERSE_E2E/
│
├── base/
│   └── base_page.py          # Reusable Selenium methods
│
├── pages/
│   ├── login_page.py         # Login page locators and actions
│   ├── flights_page.py       # Flights module
│   ├── trains_page.py        # Trains module
│   ├── bus_page.py           # Bus module
│   ├── movies_page.py        # Movies module
│   ├── events_page.py        # Events module
│   ├── sports_page.py        # Sports module
│   ├── activities_page.py    # Activities module
│   └── hotels_page.py        # Hotels module
│
├── tests/
│   ├── test_login.py
│   ├── test_flights.py
│   ├── test_trains.py
│   ├── test_bus.py
│   ├── test_movies.py
│   ├── test_events.py
│   ├── test_sports.py
│   ├── test_activities.py
│   ├── test_hotels.py
│   └── test_logout.py
│
├── utils/
│   └── test_data.py          # Test credentials and data
│
├── screenshots/              # Auto-generated after each test run
├── conftest.py               # Driver setup and teardown
├── requirements.txt          # Project dependencies
├── .gitignore
└── README.md
```

---

## Setup and Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Padmashree-2709/TRAVELVERSE_E2E.git
cd TRAVELVERSE_E2E
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## How to Run Tests

### Run All Tests
```bash
pytest -v -s
```

### Run a Specific Module
```bash
pytest tests/test_login.py -v -s
pytest tests/test_flights.py -v -s
pytest tests/test_trains.py -v -s
pytest tests/test_bus.py -v -s
pytest tests/test_movies.py -v -s
pytest tests/test_events.py -v -s
pytest tests/test_sports.py -v -s
pytest tests/test_activities.py -v -s
pytest tests/test_logout.py -v -s
