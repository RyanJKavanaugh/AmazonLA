import unittest
#import HTMLTestRunner
import os
from LAVerifyMenuOptions import Verify_LA_Menu_Options
from LAVerifyHeaderLinks import Verify_Links
from LAVerifyCreateAndDeleteRoute import Verify_Login_And_Saving_Routes
from LAVerifyFDandTextSizes import Verify_Future_Dates_And_Text_Sizes
from LAVerifyUserLogin import Verify_Login
from LAVerifyMapLayers import Verify_Map_Layers


# get all tests from SearchText and HomePageTest class
#   1
left_hand_menu = unittest.TestLoader().loadTestsFromTestCase(Verify_LA_Menu_Options)
#   2
header_links = unittest.TestLoader().loadTestsFromTestCase(Verify_Links)
#   3
future_dates_and_text_sizes = unittest.TestLoader().loadTestsFromTestCase(Verify_Future_Dates_And_Text_Sizes)
#   4
user_login = unittest.TestLoader().loadTestsFromTestCase(Verify_Login)
#   5
map_layers = unittest.TestLoader().loadTestsFromTestCase(Verify_Map_Layers)

#   6
create_and_delete_route = unittest.TestLoader().loadTestsFromTestCase(Verify_Login_And_Saving_Routes)

# create a test suite combining search_text and home_page_test
test_suite = unittest.TestSuite([left_hand_menu, header_links, future_dates_and_text_sizes, user_login, map_layers])

# run the suite
unittest.TextTestRunner(verbosity=2).run(test_suite)