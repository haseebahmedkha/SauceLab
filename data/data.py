# This file contains test data for various test scenarios.
# -----------------------
#         if expected_result == "Pass":
#             assert admin_page.is_success_message_displayed(), "Success message not displayed!"
#         else:
#             assert not admin_page.is_success_message_displayed(), "Unexpected success message!"

checkout_test_data = [("john", "doe", "54321"),
             ("haseeb", "khan", "12345"),
             ("alice", "smith", "67890")]

test_data_for_login = [("standard_user", "secret_sauce"),
                       ("performance_glitch_user", "secret_sauce"),
                       ("problem_user", "secret_sauce"),
                        ("locked_out_user", "secret_asauce")]

negative_login_data = [("invalid_user", "wrong_password"),
                       ("Haseeb", "12345"),
                       ("",""),("standard_user",""),("","secret")]


