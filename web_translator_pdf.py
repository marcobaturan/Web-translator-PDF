# libraries
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyautogui
import json
import time


def main():
    """Web translator and PDF

        @author: Marco Baturan
        @date: 15-12-2022
        @license: None
        
        It's a program for search, translation and print PDF
        of the page.
        
        Args:
            param1: URL or set of URLS in a list.
            
        Returns:
            Generate a PDF in Downloads folder.
            
        TESTED ON:
            Distributor ID: Ubuntu
            Description: Ubuntu 22.04.1 LTS
            Release: 22.04
            Codename: jammy
            Python3.10.6
            Framework: Thonny 3.3.14
            Browser: Chrome Versión 107.0.5304.110 (Build oficial) (64 bits)
            Hardware: Lenovo Thinkpad Ideapad 100-15IBD
            
        Installation and use:
        
            1. virtualenv venv --python=python3.10.6
            2. pip install -r requirements.txt
            3. python web_translator_pdf.py
            4. Write the url: http://example.com/
            4. Get PDF from Downloads folder.
            
    """
    # ask the url
    url = input('Write the url: ')
    # options for print pdf from page
    options = webdriver.ChromeOptions()
    settings = {
           "recentDestinations": [{
                "id": "Save as PDF",
                "origin": "local",
                "account": "",
            }],
            "selectedDestinationId": "Save as PDF",
            "version": 2
        }
    prefs = {'printing.print_preview_sticky_settings.appState': json.dumps(settings)}
    options.add_experimental_option('prefs', prefs)
    options.add_argument('--kiosk-printing')

    # brose to web and point to body
    driver = webdriver.Chrome(chrome_options=options)
    driver.maximize_window()
    
    # Uncomment this section and tab the code below to print a set of pages
    #URL_list = []
    #for ul in URL_list:
    #    driver. get()
    driver.get(url)
    source = driver.find_element(By.XPATH,"//body")
    time.sleep(1)

    # right click and translate
    action = ActionChains(driver)
    action.context_click(source).perform()
    for i in range(7):
        pyautogui.press('down')
    pyautogui.press('enter')
    time.sleep(1)

    # point and click and print PDF to Donwloads folder
    action.context_click(source).perform()
    for i in range(4):
        pyautogui.press('down')
    pyautogui.press('enter')
    time.sleep(1)
    driver.quit()    

if __name__ == "__main__":
    main()