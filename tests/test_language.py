from pages.demo_uptr_dev import DemoUpTr
import time
import pytest


@pytest.mark.English
def test_language_english(browser):
    page = DemoUpTr(browser)
    page.visit()
    time.sleep(3)
    assert page.language.get_text() == 'English'
    assert page.sign_in.get_text() == 'Sign in'
    assert page.register.get_text() == 'Register'


@pytest.mark.Russian
def test_language_russian(browser):
    page = DemoUpTr(browser)
    page.visit()
    time.sleep(3)
    assert page.language.get_text() == 'русский'
    assert page.sign_in.get_text() == 'Войти'
    assert page.register.get_text() == 'Регистрация'


@pytest.mark.France
def test_language_france(browser):
    page = DemoUpTr(browser)
    page.visit()
    time.sleep(3)
    assert page.language.get_text() == 'français'
    assert page.sign_in.get_text() == 'Sign in'
    assert page.register.get_text() == 'Inscrivez-vous'
