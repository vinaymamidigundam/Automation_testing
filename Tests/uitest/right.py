from PageActions.commonfunctions import Automation_texting
from PageObjects.automation_obj import Automation
import time
import yaml
from selenium.webdriver.common.by import By

with open('../TestData/create.yaml', 'r') as file:
    create = yaml.full_load(file)


cfuntion = Automation_texting()
g_objects = Automation

cfuntion.open_url('https://testautomationpractice.blogspot.com/?m=1')
time.sleep(2)
cfuntion.click_on_elements(g_objects.rightside_xpath)
# cfuntion.click_on_pro(g_objects.right_inner)
cfuntion.browser.find_element(By.XPATH, g_objects.field).clear()
cfuntion.click_on_inputs_send_keys(g_objects.field, create['field1'])
txt_box = cfuntion.browser.find_element(By.XPATH, g_objects.double_cleck)
cfuntion.double_click(txt_box)

source_drag = cfuntion.browser.find_element(By.XPATH, g_objects.drag)
target_drop = cfuntion.browser.find_element(By.XPATH, g_objects.drop)
cfuntion.click_hold_move(source_drag, target_drop)

source_img = cfuntion.browser.find_element(By.XPATH, g_objects.mary)
target_img = cfuntion.browser.find_element(By.XPATH, g_objects.Trash)
cfuntion.drag_and_drop(source_img, target_img)

slider_ele = cfuntion.browser.find_element(By.XPATH, g_objects.slider)
cfuntion.slider_element(slider_ele, 120, 0)
resizeable_ele = cfuntion.browser.find_element(By.XPATH, g_objects.resizable)
cfuntion.scrollDown()
cfuntion.scrollDown()
cfuntion.move_element(resizeable_ele, 50, 5)
cfuntion.click_on_inputs_send_keys(g_objects.age, create['age'])
cfuntion.browser.close()