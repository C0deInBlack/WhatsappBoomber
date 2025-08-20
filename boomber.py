#!/usr/bin/python 

import sys, signal, time, asyncio, getpass, os, argparse
sys.path.append('libs/lib/python3.13/site-packages')
from playwright.async_api import async_playwright
from termcolor import colored

def sig_handler(sig, frame) -> None:
    if os.path.exists(os.path.join(os.getcwd(), 'qr.png')): os.remove(os.path.join(os.getcwd(), 'qr.png'))
    if os.path.exists(os.path.join(os.getcwd(), 'code.png')): os.remove(os.path.join(os.getcwd(), 'code.png'))
    print(colored("\n\n[!] Exiting\n\n", "red"));
    sys.exit(0)

signal.signal(signal.SIGINT, sig_handler)

url: str = "https://web.whatsapp.com/send?phone=" 

async def main() -> None:
    parser = argparse.ArgumentParser(description='Whatsapp Boomber')
    parser.add_argument('-p', '--phone', type=str, default='', help='Your phone number with country code')
    parser.add_argument('-t', '--target', type=str, default='', help='Target phone with country code')
    parser.add_argument('-n', '--number', type=str, default='', help='Number of messages')
    parser.add_argument('-m', '--message', type=str, default='', help='Message to send')
    parser.add_argument('-qr', '--qr', type=bool, default=False, help='Login using QR [true/false, Default false]' )
    parser.add_argument('-c', '--code', type=bool, default=False, help='Login using Code [true/false, Default false]' )
    args = parser.parse_args()

    start_time = time.time()
    if len(sys.argv) != 11: parser.print_help(); sys.exit(1)
    elif not args.qr and not args.code: print(colored("[!] Specify the login method, 'qr' or 'code'", "red")); parser.print_help(); sys.exit(1)
    elif args.qr and args.code: parser.print_help(); sys.exit(1)

    async with async_playwright() as p:
        # browser = await p.firefox.launch(headless=False, slow_mo=50)
        browser = await p.firefox.launch()
        context = await browser.new_context()
        
        page = await context.new_page()
        await page.goto(f"{url}{args.target}&text={args.message}")
   
        if args.code:
            await page.wait_for_timeout(5000)
            await page.click('.x1iorvi4 > div:nth-child(1)')
            await page.wait_for_timeout(5000)
            await page.fill('.selectable-text', args.phone)
            await page.click('.x1v8p93f')
            await page.wait_for_timeout(5000)
            await page.screenshot(path="code.png")
            os.system('kitten icat code.png')
            a = getpass.getpass(prompt=colored("\n[*] Type any key after linking the device: ", "blue"))
        elif args.qr:
            await page.wait_for_timeout(5000)
            await page.screenshot(path="qr.png")
            os.system('kitten icat qr.png')
            a = getpass.getpass(prompt=colored("\n[*] Type any key after linking the device: ", "blue"))

        time.sleep(10)

        await page.click('button.x889kno')
        await page.wait_for_timeout(5000)

        attack_page = await context.new_page()
        await attack_page.goto(f"{url}{args.target}&text={args.message}")

        # await page.wait_for_timeout(5000)

        print(colored("\n[*] Starting attack\n", "magenta"))

        for i in range(int(args.number)):
            await attack_page.fill('div.lexical-rich-text-input:nth-child(3) > div:nth-child(1) > p:nth-child(1)', args.message)
            await attack_page.click('button.x1c4vz4f')
 
        await context.close(); await browser.close()
        
        if os.path.exists(os.path.join(os.getcwd(), 'qr.png')): os.remove(os.path.join(os.getcwd(), 'qr.png'))
        if os.path.exists(os.path.join(os.getcwd(), 'code.png')): os.remove(os.path.join(os.getcwd(), 'code.png'))

        end_time = time.time()
        print(colored("\n[*] Process finished in: %d s\n" % ((end_time - start_time)), "yellow"))

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except Exception as e:
        print(colored(e, "red"))
        if os.path.exists(os.path.join(os.getcwd(), 'qr.png')): os.remove(os.path.join(os.getcwd(), 'qr.png'))
        if os.path.exists(os.path.join(os.getcwd(), 'code.png')): os.remove(os.path.join(os.getcwd(), 'code.png'))

