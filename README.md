# SauceDemoPlaywright

Pytest + Playwright starter structure for automating the Sauce Demo site.

Setup

1. Create and activate a virtual environment (recommended).
2. Install dependencies:

```
python -m pip install -r requirements.txt
```

3. Install Playwright browsers:

```
playwright install
```

Running tests

```
pytest
```

To generate the HTML report (already configured in pytest.ini):

```
pytest --html=reports/report.html
```

CI

A GitHub Actions workflow skeleton is included under `.github/workflows/pytest.yml` to run tests and upload the HTML report as an artifact.

