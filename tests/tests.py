from textwrap import dedent

import pytest

from src.heroku_config_vars_formatter.formatting import format_text


def test_format_text__encoding():
    text = dedent(
        """
        SECRET_KEY
        124981u209,c0#14124!ä214ö1l2ü12ü&M5
        Edit Delete
    """
    )
    res = format_text(text)

    expected = "export SECRET_KEY=124981u209,c0#14124\\!ä214ö1l2ü12ü\\&M5\n"
    assert res == expected


def test_format_text__with_start_and_end():
    text = dedent(
        """
        Config Vars
        EMAIL_BACKEND
        post_office.EmailBackend
        Edit Delete
        KEY
        VALUE
        Add
    """
    )
    res = format_text(text)

    expected = "export EMAIL_BACKEND=post_office.EmailBackend\n"
    assert res == expected


def test_format_text__with_start():
    text = dedent(
        """
        Config Vars
        EMAIL_BACKEND
        post_office.EmailBackend
        Edit Delete
    """
    )
    res = format_text(text)

    expected = "export EMAIL_BACKEND=post_office.EmailBackend\n"
    assert res == expected


def test_format_text__with_end():
    text = dedent(
        """
        EMAIL_BACKEND
        post_office.EmailBackend
        Edit Delete
        KEY
        VALUE
        Add
    """
    )
    res = format_text(text)

    expected = "export EMAIL_BACKEND=post_office.EmailBackend\n"
    assert res == expected


def test_format_text__just_values():
    text = dedent(
        """
        EMAIL_BACKEND
        post_office.EmailBackend
    """
    )
    res = format_text(text)

    expected = "export EMAIL_BACKEND=post_office.EmailBackend\n"
    assert res == expected


def test_invalid_input():
    text = dedent("""ASDLKJASKL""")

    msg = (
        "The contents of your cache couldn't be formatted."
        " Please make sure you copied the contents of your Heroku config."
    )
    with pytest.raises(ValueError, match=msg):
        format_text(text)
