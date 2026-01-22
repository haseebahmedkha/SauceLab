# 🧪 E-Commerce QA Automation Framework (Playwright + Python)

This repository contains a **professional QA Automation Testing Framework** built using  
**Playwright with Python**.

The project focuses on **sanity, negative, boundary, functional, end-to-end (E2E), and hybrid API + UI testing**
for **Cart and Checkout flows**, following real-world QA automation practices.

---

## 🚀 Project Objectives

- Validate **critical e-commerce user journeys**
- Implement **fast sanity tests** for build verification
- Cover **positive, negative, and boundary scenarios**
- Automate **end-to-end checkout workflows**
- Perform **Hybrid API + UI testing** for reliable validation
- Enable **parallel execution** for faster test runs
- Maintain **clean, scalable, recruiter-ready framework**

---

## 🧰 Tech Stack & Tools

- **Playwright (Python)**
- **Python 3.x**
- **Pytest**
- **REST APIs** (Hybrid testing)
- **Requests library**
- **Git & GitHub**
- **CI/CD ready test design**

---

## 🧪 Test Coverage

### 1️⃣ Sanity Testing
Quick verification of core features after every build.

Examples:
- Login sanity
- Add to cart sanity
- Checkout page load
- Order confirmation page visibility

✅ *Sanity tests created and running locally*

---

### 2️⃣ Negative Sanity Testing
Validates system behavior with invalid or incorrect inputs.

Examples:
- Invalid card details
- Empty required checkout fields
- Incorrect email formats
- Invalid promo codes

✅ *Negative sanity tests implemented and passing*

---

### 3️⃣ Boundary Sanity Testing
Validates application behavior at **edge input limits**.

Examples:
- Minimum and maximum product quantity
- Maximum character limits for address fields
- ZIP / postal code boundary values
- Cart quantity upper limits

✅ *Boundary sanity tests implemented*

---

### 4️⃣ Functional Test Design (Cart & Checkout)
Validates business logic and functional behavior.

- Add/remove items from cart
- Update quantities
- Price calculation validation
- Shipping & tax checks
- Checkout form validations

---

### 5️⃣ End-to-End (E2E) User Journeys
Complete user workflows tested from start to finish.

Examples:
- Login → Add product → Checkout → Order confirmation
- Guest checkout flow
- Failed payment handling and retry scenarios

---

### 6️⃣ Hybrid API + UI Testing
Combines backend API validation with frontend UI verification.

Examples:
- Create or fetch cart/order data via API
- Validate UI reflects API response correctly
- Reduce UI dependency for faster execution

---

### 7️⃣ Parallel Execution
- Tests executed in parallel using Pytest
- Faster execution time
- Scalable test suite design

✅ *Parallel execution enabled*

---

## 📂 Project Structure


- `pages/` — Page objects for the UI (LoginPage, InventoryPage, CartPage, CheckoutPage, ...)
- `tests/`
  - `e2e/` — End-to-end test scenarios (e.g. `test_checkout_hybrid.py`)
  - other suites (smoke, regression) as needed
- `utils/` — Helpers: `config.py`, `logger.py`, fixtures, test data utilities
- `requirements.txt` — Python dependencies
- `pytest.ini` — pytest configuration (markers, reporters, options)
- `README.md`



---

---

## ⚙️ Prerequisites

- Windows OS (development environment)
- Python 3.10+ (or project target)
- WebDriver binaries for chosen browser (e.g., chromedriver) accessible in `PATH` or configured in utils
- `pip` (or pipenv/poetry)

---

## 🔧 Install

1. Create and activate a virtual environment:
   - `python -m venv .venv`
   - `.venv\Scripts\activate`

2. Install dependencies:
   - `pip install -r requirements.txt`

---

## ▶️ Run Tests

- Run all tests:
  - `pytest -q`

- Run E2E tests (marked with `@pytest.mark.e2e`):
  - `pytest -q -m e2e`

- Run hybrid tests (marked with `@pytest.mark.hybrid`):
  - `pytest -q -m hybrid`

- Run a single test file:
  - `pytest -q tests/e2e/test_checkout_hybrid.py`

- Run with HTML report:
  - `pytest -q --html=reports/report.html --self-contained-html`

- Run with increased verbosity and capture stdout:
  - `pytest -q -s`

---

## 🧭 Test Conventions

- Use Page Object Model: UI interactions belong to `pages/*` classes.
- Keep test logic minimal: tests orchestrate page calls and assertions.
- Use fixtures from `utils` for WebDriver setup/teardown (global `setup` fixture used in tests).
- Use markers for categorization: `e2e`, `hybrid`, `smoke`, `regression`.
- Hybrid tests may perform UI actions and then call backend endpoints using the `requests` library to validate backend state.

Example marker usage in tests:
```python
@pytest.mark.usefixtures("setup")
class TestCheckoutHybrid:
    @pytest.mark.e2e
    @pytest.mark.hybrid
    def test_checkout_hybrid(self, setup):
        ...

