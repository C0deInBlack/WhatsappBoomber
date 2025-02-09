#!/usr/bin/python 

import sys, signal, time, getpass, os, asyncio
# import cv2
# sys.path.append('libs/lib/python3.13/site-packages')
from playwright.async_api import async_playwright

def sig_handler(sig, frame) -> None: os.remove(os.path.join(os.getcwd(), 'qr.png')); sys.exit(0)

signal.signal(signal.SIGINT, sig_handler)

url: str = "https://web.whatsapp.com/send?phone=" 

async def main() -> None:
    start_time = time.time()
    if len(sys.argv) != 4: print("\t[?] usage:\n\t\t%s <phone number with country code> <number of messages> <message>" % (sys.argv[0])); sys.exit(1)

    async with async_playwright() as p:
        # browser = await p.firefox.launch(headless=False, slow_mo=50)
        browser = await p.firefox.launch()
        context = await browser.new_context()
        
        page = await context.new_page(); await page.goto("%s%d" % (url, int(sys.argv[1])))
       
        await page.wait_for_timeout(5000)
        await page.screenshot(path="qr.png")
        # cv2.imshow('QR', (cv2.imread('qr.png', cv2.IMREAD_ANYCOLOR)))
        os.system('kitten icat qr.png')
        a = getpass.getpass(prompt="\n[*] Type any key after scan the QR: ")
        
        print("\n[*] Starting attack\n")
        
        for i in range(int(sys.argv[2])):
            await page.fill('div.lexical-rich-text-input:nth-child(2) > div:nth-child(1) > p:nth-child(1)', str(sys.argv[3]))
            await page.click('button.x1c4vz4f')
 
        await context.close(); await browser.close()
        os.remove(os.path.join(os.getcwd(), 'qr.png'))
        end_time = time.time()
        print("\n[*] Process finished in: %d s\n" % ((end_time - start_time)))

if __name__ == '__main__': asyncio.run(main())

