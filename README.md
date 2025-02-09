# WhatsappBoomber
A Python script that sends bulk messages to a WhatsApp number using two different methods: Selenium and Playwright.

## Installation

```bash
python -m venv libs
source libs/bin/activate
pip install selenium
pip install playwright
playwright install
```
I'm using kitty terminal, and the command ```kitten icat``` to display th QR code, you can use any other image viewer or command if you want.

## Usage

```bash
        [?] usage:
                main_playwright.py <phone number with country code> <number of messages> <message>
```

## Note

If there is an error, probably need to update the selector of the textbox, because whatsappp web is constantly updating.
In general Playwright version is faster at handling when an element is available, and Selenium send the keys faster than Playwright.
There is a difference between 10 seconds, being Playwright faster in general, I prefer the Playwright version because automatically manages the times.
These test were tested on my machine, maybe on yours the behavior of the script is a little different and depending on your network connection.
