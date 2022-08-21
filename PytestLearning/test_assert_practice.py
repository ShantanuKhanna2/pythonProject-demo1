import pytest


# def test_function():
#     expected_result = "Gmail.com"
#     actual_result = "Google.com"
#     title = "yeh hai Gmail ki site"
#
#     # if actual_result == expected_result:
#     #     print("Test pass")
#     # else:
#     #     print("test fail")
#
#     assert actual_result == expected_result, "test not passed"
#     assert "Gmails" in title

import pytest


def get_data():
    return [

        ("trainer@way2automation.com", "kjsdfbksdf"),
        ("java@way2automation.com", "sdf"),
        ("info@way2automation.com", "sdfsdf")

    ]


@pytest.mark.parametrize("username,password", get_data())
def test_dologin(username, password):
    print(username, "---", password)
