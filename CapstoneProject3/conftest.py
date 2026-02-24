import pytest
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests on: chrome | firefox | edge"
    )


def pytest_configure(config):
    # Generate unique report name with timestamp for every run
    timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    report_dir = "reports"
    os.makedirs(report_dir, exist_ok=True)
    report_path = os.path.join(report_dir, f"report_{timestamp}.html")
    config.option.htmlpath = report_path


def get_driver(browser_name):
    browser_name = browser_name.lower()

    if browser_name == "chrome":
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-popup-blocking")
        service = ChromeService(ChromeDriverManager().install())
        return webdriver.Chrome(service=service, options=options)

    elif browser_name == "firefox":
        options = FirefoxOptions()
        options.add_argument("--start-maximized")
        geckodriver_path = os.path.expanduser(
            r"~\.wdm\drivers\geckodriver\win64\v0.36.0\geckodriver.exe"
        )
        service = FirefoxService(executable_path=geckodriver_path)
        driver = webdriver.Firefox(service=service, options=options)
        driver.maximize_window()
        return driver

    elif browser_name == "edge":
        options = EdgeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-popup-blocking")
        service = EdgeService(EdgeChromiumDriverManager().install())
        return webdriver.Edge(service=service, options=options)

    else:
        raise ValueError(f"Unsupported browser: '{browser_name}'. Choose from: chrome, firefox, edge")


@pytest.fixture(scope="function")
def browser_name(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="function")
def driver(request, browser_name):
    drv = get_driver(browser_name)
    request.node._browser_name = browser_name
    yield drv
    drv.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        drv = item.funcargs.get("driver")
        if drv:
            screenshots_dir = "screenshots"
            os.makedirs(screenshots_dir, exist_ok=True)
            browser = getattr(item, "_browser_name", "unknown")
            file_name = os.path.join(screenshots_dir, f"{item.name}_{browser}.png")
            drv.save_screenshot(file_name)