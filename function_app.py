import azure.functions as func
import datetime
import json
import logging
from playwright.sync_api import sync_playwright

app = func.FunctionApp()

def run(playwright):
    browser = playwright.chromium.launch()
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.google.com/")
    page.screenshot(path="example.png")
    browser.close()

@app.timer_trigger(schedule="0 */5 * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False) 
def PlayWrightFunction(myTimer: func.TimerRequest) -> None:
    
    if myTimer.past_due:
        logging.info('The timer is past due!')

    with sync_playwright() as playwright:
        run(playwright)