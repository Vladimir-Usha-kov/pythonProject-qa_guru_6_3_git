import pytest
from selene import browser
from selene.support.conditions import have, be


@pytest.fixture(scope='session', autouse=True)
def size_window():
    browser.config.window_width = 900
    browser.config.window_height = 1920


def test_positive():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_negative():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('dfhgydfhrfgh').press_enter()
    browser.element('[id="result-stats"]').should(have.text('Результатов: примерно 0'))