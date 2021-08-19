from PageActions.commonfunctions import Automation_texting
from PageObjects.automation_obj import Automation
import time
import yaml

with open('../TestData/create.yaml', 'r') as file:
    create = yaml.full_load(file)

cfuntion = Automation_texting()
g_objects = Automation

cfuntion.open_url('https://testautomationpractice.blogspot.com/?m=1')
time.sleep(2)
cfuntion.click_on_inputs_send_keys(g_objects.searchinput_xpath, create['search_input'])
cfuntion.click_on_elements(g_objects.searchbutton)
cfuntion.click_on_elements(g_objects.clcik)
cfuntion.arlts()
cfuntion.click_on_elements(g_objects.datepicker)

cfuntion.click_on_inputs_send_keys(g_objects.select_a_speed, create['speed'])
cfuntion.click_on_inputs_send_keys(g_objects.select_a_fils, create['fil'])
cfuntion.click_on_inputs_send_keys(g_objects.select_a_number, create['number'])
cfuntion.click_on_inputs_send_keys(g_objects.select_a_products, create['product'])
cfuntion.click_on_inputs_send_keys(g_objects.select_a_animals, create['animal'])
cfuntion.switch_to_frame(g_objects.main_section)
cfuntion.click_on_inputs_send_keys(g_objects.first_name, create['firstname'])
cfuntion.click_on_inputs_send_keys(g_objects.last_name, create['lastname'])
cfuntion.click_on_inputs_send_keys(g_objects.phone_number, create['mobileno'])
cfuntion.click_on_inputs_send_keys(g_objects.country,create['Country'])
cfuntion.click_on_inputs_send_keys(g_objects.city,create['city'])
cfuntion.click_on_inputs_send_keys(g_objects.email_enter, create['Email Address'])
cfuntion.click_on_elements(g_objects.gender)
cfuntion.click_on_elements(g_objects.best_day)
cfuntion.click_on_elements(g_objects.best_time)
time.sleep(5)
# cfuntion.switch_to_frame(g_objects.rightside_xpath)

