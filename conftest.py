# conftest.py
import time
import pytest
import yaml
from pathlib import Path
from playwright.sync_api import sync_playwright
import os
from pytest_bdd import scenarios


CONFIG_PATH = Path(__file__).parent / "configs" / "config.yaml"

@pytest.fixture(scope="session")
def config():
    with open(CONFIG_PATH, "r") as f:
        data = yaml.safe_load(f)
    return data

# Automatically discover and load all feature files
FEATURE_DIR = os.path.join(os.path.dirname(__file__), "features")

for filename in os.listdir(FEATURE_DIR):
    if filename.endswith(".feature"):
        feature_path = os.path.join(FEATURE_DIR, filename)
        scenarios(feature_path)

@pytest.fixture(scope="session")
def browser_instance(config):
    """Start playwright and browser for the test session."""
    playwright = sync_playwright().start()
    browser_name = config.get("browser", "chromium")
    headless = config.get("headless", True)
    browser = getattr(playwright, browser_name).launch(headless=headless)
    yield browser
    browser.close()
    playwright.stop()

@pytest.fixture
def page(browser_instance, config):
    """Create a fresh context + page for each test to isolate sessions."""
    viewport = config.get("viewport", {"width": 1280, "height": 720})
    context = browser_instance.new_context(
        viewport=viewport
    )
    page = context.new_page()
    # set default timeout (ms)
    page.set_default_timeout(config.get("timeout", 10000))
    yield page
    context.close()

def pytest_bdd_before_scenario(request, feature, scenario):
    """Print the scenario name before its steps."""
    print(f"\nScenario: {scenario.name}")

def pytest_bdd_before_step(request, feature, scenario, step, step_func):
    """Print each Gherkin step as it runs."""
    print(f"{step.keyword} {step.name}")
