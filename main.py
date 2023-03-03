import os
import time
from info import create_driver
import traceback
from selenium.webdriver.common.by import By
from sms_activate import get_sms
from sms_activate import get_code
from info import create_profile
from info import update_profile_proxy
import re
from selenium.webdriver.support.relative_locator import locate_with
from info import update_profile_geo
import random
from info import parse_gmail
from info import parse_line
from geo_randomizer_polygon import get_points
import shutil
from info import parse_photos
from selenium.webdriver.support.ui import Select
from sms_activate import get_sms
from sms_activate import get_code
from selenium.webdriver.remote.file_detector import UselessFileDetector



russian_female_names = ['Anastasia', 'Maria', 'Daria', 'Yulia', 'Anna', 'Ekaterina', 'Olga', 'Natalia', 'Elena', 'Irina', 'Alexandra', 'Polina', 'Ksenia', 'Kristina', 'Vera', 'Tatiana', 'Sofiya', 'Alina', 'Arina', 'Svetlana', 'Nadezhda', 'Galina', 'Margarita', 'Yana', 'Taisiya', 'Lyudmila', 'Zoya', 'Valentina', 'Elizaveta', 'Ulyana', 'Lidiya', 'Viktoriya', 'Yaroslava', 'Yekaterina', 'Mariya', 'Yelena', 'Zinaida', 'Raisa', 'Marina', 'Tamara', 'Margarita', 'Inna', 'Alla', 'Sofiya', 'Anastasiya', 'Evgeniya', 'Ekaterina', 'Lyubov', 'Irina', 'Angelina', 'Lyudmila', 'Nina', 'Alena', 'Tatyana', 'Natalya', 'Anna', 'Kristina', 'Svetlana', 'Darya', 'Sofia', 'Valeriya', 'Valentina', 'Kira', 'Marianna', 'Galina', 'Veronika', 'Roza', 'Lubov', 'Anastasia', 'Margarita', 'Diana', 'Ekaterina', 'Yevgeniya', 'Yuliya', 'Olga', 'Sofiya', 'Inna', 'Natalia', 'Svetlana', 'Angelina', 'Irina', 'Taisiya', 'Anna', 'Yana', 'Elizaveta', 'Polina', 'Kseniya', 'Aleksandra', 'Yaroslava', 'Mariya', 'Ulyana', 'Zoya', 'Lidiya', 'Alina', 'Raisa', 'Tamara', 'Viktoriya', 'Yekaterina', 'Lyubov']


def google_auth(driver, email, password, reserve):
    """Logining in google account"""
    driver.get(r'https://accounts.google.com/signin/v2/identifier?continue=' + \
               'https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1' + \
               '&flowName=GlifWebSignIn&flowEntry = ServiceLogin')
    #driver.implicitly_wait(15)

    loginBox = driver.find_element(By.XPATH, '//*[@id ="identifierId"]')
    loginBox.send_keys(email)

    time.sleep(3)

    nextButton = driver.find_elements(By.XPATH, '//*[@id ="identifierNext"]')
    nextButton[0].click()

    time.sleep(5)

    passWordBox = driver.find_element(By.XPATH,
        '//*[@id ="password"]/div[1]/div / div[1]/input')
    passWordBox.send_keys(password)

    time.sleep(3)

    nextButton = driver.find_elements(By.XPATH, '//*[@id ="passwordNext"]')
    nextButton[0].click()

    time.sleep(3)

    try:
        driver.find_element(By.XPATH, "(//div[contains(@role,'link')])[4]").click()
        time.sleep(3)
        reserve_email = driver.find_element(By.XPATH, "//input[@id='knowledge-preregistered-email-response']")
        reserve_email.send_keys(reserve)
        time.sleep(3)
        next = locate_with(By.TAG_NAME, "button").near(reserve_email)
        time.sleep(3)
        next_elem = driver.find_element(next)
        time.sleep(3)
        next_elem.click()
    except:
        traceback.print_exc()
        pass


def input_dialog(func, text, *args):
    """User interface"""
    h = input(text)
    match h:
        case "re":
            func(*args)
        case "skip":
            continue_var = True
            return continue_var
        case "next":
            pass
        case _:
            print("Wrong input, try again")
            input_dialog(func, *args)


def new_session(session_name, proxy_host, proxy_port, proxy_type, proxy_username, proxy_password, latitude, longitude, port, city):
    """Creating new session"""
    profile_id = create_profile(session_name=session_name, port=port)
    time.sleep(2)
    update_profile_proxy(profile_id=str(profile_id), proxy_port=proxy_port, proxy_username=proxy_username,
                         proxy_host=proxy_host,
                         proxy_password=proxy_password, proxy_type=proxy_type, port=str(port))
    latitude, longitude = get_points(city)
    update_profile_geo(profile_id, latitude, longitude, port)
    time.sleep(2)
    driver = create_driver(profile_id, port)
    return driver

def start_session(port, city):
    """Starting session"""
    email, password, reserve = parse_gmail("res/gmail.xlsx")
    photos_folder = parse_photos()
    latitude, longitude = get_points(city)
    session_name = parse_line("res/session_names")
    proxy_host = "proxy.soax.com"
    proxy_type = "SOCKS"
    proxy_username = "rUfgRb6QMNgjiLYv"
    proxy_password = "wifi;ru;;moscow;moscow"
    ports = ["9250", "9251", "9252", "9253", "9254", "9255", "9256", "9257", "9258", "9259", "9260", "9261", "9262", "9263", "9264", "9265", "9266", "9267", "9268", "9269", "9270", "9271", "9272", "9273", "9274", "9275", "9276", "9277", "9278", "9279", "9280", "9281", "9282", "9283", "9284", "9285", "9286", "9287", "9288", "9289", "9290", "9291", "9292", "9293", "9294", "9295", "9296", "9297", "9298", "9299", "9300", "9301", "9302", "9303", "9304", "9305", "9306", "9307", "9308", "9309", "9310", "9311", "9312", "9313", "9314", "9315", "9316", "9317", "9318", "9319", "9320", "9321", "9322", "9323", "9324", "9325", "9326", "9327", "9328", "9329", "9330", "9331", "9332", "9333", "9334", "9335", "9336", "9337", "9338", "9339", "9340", "9341", "9342", "9343", "9344", "9345", "9346", "9347", "9348", "9349"]
    proxy_port = ports[random.randint(0,99)]
    driver = new_session(session_name, proxy_host, proxy_port, proxy_type, proxy_username, proxy_password, latitude,
                         longitude, port, city)
    return email, password, reserve, driver, photos_folder

def reg(port, city):
    for i in range(1000):
        try:
            print(f"ITERATION NUMBER: {i}")
            """Parsing account reinformation and creating session"""
            try:
                email, password, reserve, driver, photos_folder = start_session(port, city)
            except:
                continue
            """Log in into your google account"""
            try:
                google_auth(driver, email, password, reserve)
            except:
                traceback.print_exc()
                continue_var = input_dialog(google_auth, "Ошибка при входе в гугл аккаунт", driver, email, password, reserve)
                if continue_var:
                    continue

            driver.get("https://mamba.ru")
            time.sleep(15)
            driver.find_element(By.XPATH, "(//button[contains(text(),'Женщина')])[1]").click()
            time.sleep(2)
            driver.find_element(By.XPATH, "//button[contains(text(),'С мужчинами')]").click()
            time.sleep(2)
            driver.find_element(By.XPATH, "//button[contains(text(),'Встреча, свидание')]").click()
            time.sleep(2)
            driver.find_element(By.XPATH, "//button[contains(text(),'Любого')]").click()
            time.sleep(2)
            driver.find_element(By.XPATH, "//button[contains(text(),'Любого')]").click()
            time.sleep(2)
            driver.find_element(By.XPATH, "//input[@placeholder='Ваше имя']").send_keys("Вика")
            time.sleep(2)
            driver.find_element(By.XPATH, "//input[@value='Далее']").click()
            time.sleep(2)
            day_box = driver.find_element(By.XPATH, "//select[@name='day']")
            time.sleep(2)
            select = Select(day_box)
            time.sleep(2)
            select.select_by_visible_text("1")
            time.sleep(2)
            month_box = driver.find_element(By.XPATH, "//select[@name='month']")
            time.sleep(2)
            select = Select(month_box)
            time.sleep(2)
            select.select_by_visible_text("январь")
            time.sleep(2)
            year_box = driver.find_element(By.XPATH, "//select[@name='year']")
            time.sleep(2)
            select = Select(year_box)
            time.sleep(2)
            select.select_by_visible_text("2000")
            time.sleep(2)
            driver.find_element(By.XPATH, "//input[@value='Далее']").click()
            time.sleep(2)
            driver.find_element(By.XPATH, "//input[@placeholder='Электронная почта']").send_keys(email)
            time.sleep(2)
            driver.find_element(By.XPATH, "//button[contains(text(),'Регистрация с почтой')]").click()
            time.sleep(5)
            driver.find_element(By.XPATH, "//a[@data-name='by-phone-action']").click()
            time.sleep(2)
            country, phone_number, id = get_sms("United Kingdom", "Lithuania", "Sweden", 0, 0, 0, 1, 1, 1)
            driver.find_element(By.XPATH, "//input[@placeholder='Номер телефона']").send_keys(phone_number)
            time.sleep(2)
            driver.find_element(By.XPATH, "//input[@value='Получить код подтверждения']").click()
            time.sleep(2)
            try:
                driver.find_element(By.XPATH, "//input[@placeholder='Код подтверждения']").click()
            except:
                country, phone_number, id = get_sms("United Kingdom", "Lithuania", "Sweden", 0, 0, 0, 1, 1, 1)
                driver.find_element(By.XPATH, "//input[@placeholder='Номер телефона']").send_keys(phone_number)
                time.sleep(2)
                driver.find_element(By.XPATH, "//input[@value='Получить код подтверждения']").click()
                try:
                    driver.find_element(By.XPATH, "//input[@placeholder='Код подтверждения']").click()
                except:
                    continue

            time.sleep(65)
            sms = get_code(id)
            if sms["status"] == "STATUS_WAIT_CODE":
                driver.find_element(By.XPATH, "//button[contains(text(),'Попробовать снова')]").click()
                time.sleep(65)
                sms = get_code(id)
                driver.find_element(By.XPATH, "//input[@placeholder='Код подтверждения']").send_keys(sms)
            else:
                driver.find_element(By.XPATH, "//input[@placeholder='Код подтверждения']").send_keys(sms)
            driver.find_element(By.XPATH, "//button[contains(text(),'Понятно')]").click()
            time.sleep(5)
            driver.find_element(By.XPATH, "//label[@for='input-file-upload']").send_keys("")




        except Exception:
            traceback.print_exc()
            continue
        finally:
            shutil.rmtree(photos_folder)
            try:
                driver.quit()
            except:
                traceback.print_exc()
                h = input("Close Driver and press enter")


reg(35000, "msk")
