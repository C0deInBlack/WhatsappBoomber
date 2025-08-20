# WhatsappBoomber
A Python script that sends bulk messages to a WhatsApp number.

## Installation

```bash
python -m venv libs
source libs/bin/activate
pip install -r requirements.txt
playwright install
```
I'm using kitty terminal, and the command ```kitten icat``` to display th QR code, you can use any other image viewer or command if you want.

For example in the page [example](https://www.delftstack.com/howto/python/python-display-image/) show how to open the image with the default image viewer in your system
```python
from PIL import Image

img = Image.open('path_to_your_image.jpg')
img.show()
```
But it's weird, I just prefer to see the image in the terminal with kitty.

## Usage

```bash
./boomber.py
usage: boomber.py [-h] [-p PHONE] [-t TARGET] [-n NUMBER] [-m MESSAGE] [-qr QR] [-c CODE]

Whatsapp Boomber

options:
  -h, --help            show this help message and exit
  -p, --phone PHONE     Your phone number with country code
  -t, --target TARGET   Target phone with country code
  -n, --number NUMBER   Number of messages
  -m, --message MESSAGE
                        Message to send
  -qr, --qr QR          Login using QR [true/false, Default false]
  -c, --code CODE       Login using Code [true/false, Default false]
```

You can use QR or a code to login your account.


Using QR
```bash
./boomber.py -p $NUMBER -t $NUMBER -n 30 -m 'python boomber' -qr true
```

In your terminal should apper the QR to scan 

![img](https://github.com/C0deInBlack/WhatsappBoomber/blob/main/images/qr.cleaned.png)

Using code
```bash
./boomber.py -p $NUMBER -t $NUMBER -n 30 -m 'python boomber' -c true
```

You will receive a message in your phone, then enter the code showed in the terminal 

![img](https://github.com/C0deInBlack/WhatsappBoomber/blob/main/images/code.cleaned.png)

Obviously that's not my phone, it's from some African guy who tried to scam me, so I don't care.

In both cases, the boomber will the effective 

![img](https://github.com/C0deInBlack/WhatsappBoomber/blob/main/images/boomber.cleaned.png)

## Note

If there is an error, probably need to update the selector of the textbox, because whatsappp web is constantly updating. 
