import pytest
from  user_registration import *


def test_validate_first_name_valid():
    assert UserValidator.validate_first_name("Aniket") == True


def test_validate_first_name_too_short():
    assert UserValidator.validate_first_name("An") == False


def test_validate_first_name_not_title_case():
    assert UserValidator.validate_first_name("aniket") == False


def test_validate_first_name_with_space():
    assert UserValidator.validate_first_name("Aniket Kumar") == False


# Last Name validation tests
def test_validate_last_name_valid():
    assert UserValidator.validate_last_name("Wagh") == True


def test_validate_last_name_too_short():
    assert UserValidator.validate_last_name("Wa") == False


def test_validate_last_name_not_title_case():
    assert UserValidator.validate_last_name("wagh") == False


def test_validate_last_name_with_space():
    assert UserValidator.validate_last_name("Wagh Singh") == False


# Email validation tests
def test_validate_email_valid():
    assert UserValidator.validate_email("abc.xyz@bl.co.in") == True


def test_validate_email_invalid_format():
    assert UserValidator.validate_email("abc@xyz") == False


def test_validate_email_missing_domain():
    assert UserValidator.validate_email("abc.xyz@") == False


def test_validate_email_missing_username():
    assert UserValidator.validate_email("@bl.co.in") == False


# Mobile Number validation tests
def test_validate_mobile_number_valid_indian_format():
    assert UserValidator.validate_mobile_number("91 9919819801") == True


def test_validate_mobile_number_valid_international_format():
    assert UserValidator.validate_mobile_number("1234567890") == True


def test_validate_mobile_number_invalid_format():
    assert UserValidator.validate_mobile_number("12345") == False


def test_validate_mobile_number_missing_country_code():
    assert UserValidator.validate_mobile_number("9919819801") == False


# Password validation tests
def test_validate_password_valid():
    assert UserValidator.validate_password("Password1@") == True


def test_validate_password_too_short():
    assert UserValidator.validate_password("Pass1@") == False


def test_validate_password_no_uppercase():
    assert UserValidator.validate_password("password1@") == False


def test_validate_password_no_digit():
    assert UserValidator.validate_password("Password@") == False


def test_validate_password_no_special_character():
    assert UserValidator.validate_password("Password1") == False


def test_validate_password_multiple_special_characters():
    assert UserValidator.validate_password("Password1@@") == False


if __name__ == "__main__":
    pytest.main()
