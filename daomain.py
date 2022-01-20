import requests
import sched, time
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import subprocess
from selenium.webdriver.common.by import By


s = sched.scheduler(time.time, time.sleep)
         
def wonder(sc):
        try:
            print('Starting Wonderland..')
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://app.wonderland.money/#/dashboard"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            price = soup.findAll('p', class_='card-value')[0].get_text()
            mcap = soup.findAll('p', class_='card-value')[1].get_text()
            tvl = soup.findAll('p', class_='card-value')[2].get_text()
            apy = soup.findAll('p', class_='card-value')[3].get_text()
            treasury = soup.findAll('p', class_='card-value')[5].get_text()
            backing = soup.findAll('p', class_='card-value')[6].get_text()
            
            
            driver.quit()
            print('Wonderland - $TIME', price,'\n', mcap,'\n', tvl,'\n', apy,'\n', treasury,'\n', backing)

            total = {'mcap': mcap, 'price': price, 'tvl': tvl, 'apy': apy, 'treasury': treasury, 'backing': backing}
            

            with open("/home/admin/Desktop/data/time.json", "w") as f:
                json.dump(total, f, indent=2)

            subprocess.call(['python3', '/home/admin/Desktop/Script/time.py'])

            keyboard = [
                [
                    InlineKeyboardButton("Chart", url='https://dexscreener.com/avalanche/0x4d308c46ea9f234ea515cc51f16fba776451cac8'),
                    InlineKeyboardButton("Dashboard", url='https://app.wonderland.money/#/dashboard')
                ]
            ]
             
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            print('Setting up data.')
            data = {
                    'photo': ('time.png', open('/home/admin/Desktop/ss/time.png', 'rb')),
                    'action': (None, 'send'),
                    'chat_id': (None, '-1001431327406'),
                    'caption': (None, f'\U0001F48E <b>Wonderland - $wMEMO</b> #AVAX \U0001F48E \n\n\u231B <i>@WonderlandMoney - <a href="https://discord.gg/6SvhcNHuvV">Discord</a> - <a href="https://twitter.com/Wonderland_fi">Twitter</a> - <a href="https://rebasetokens.app/f-a-q">FAQ</a></i> \u231B\n\n\U0001F4B5 <b>Market Cap:</b> {mcap}\n\U0001F4B0 <b>Price:</b> {price}\n\U0001F5D3 <b>APY:</b> {apy}\n\U0001F512 <b>TVL:</b> {tvl}\n\U0001F4AC <b>Treasury:</b> {treasury}\n\U0001F4CC <b>Backing:</b> {backing}\n\n\U0001F315 <a href="https://warp.bond/"><b>Warp.Bond</b></a> - The Next-Gen Web3 reserve currency ft. NFT Bonds & buildable starships that travel within the Staking #Metaverse\n@warpbond - <a href="https://discord.gg/warpbond">Discord</a> - <a href="https://twitter.com/warpbond">Twitter</a>\nJoin the <a href="https://warpcountdown.com/">Whitelist here!</a>  \U0001F315'),
                    "reply_markup": (None, json.dumps(reply_markup.to_dict())),
                    "parse_mode": (None, 'HTML')
            }
        
            requests.post(url='https://api.telegram.org/bot5025889373:AAEGOUROw4deWROTzTR-1v1lDddv2EJFmSQ/sendPhoto', files=data)
            print('Data sent!')

            print('Shutting off Wonderland..')
            s.enter(2, 1, hector, (s,))
            
        except Exception as errore:

            print(errore)

            data = {"chat_id": "92637783",
                    "text": f'<b>Error</b> on Wonder Main Chat\n\n {errore}' ,
                    "parse_mode": 'HTML'}

            requests.post(url='https://api.telegram.org/bot5062720103:AAHo_qpQzG5dqRteZ-VgfBYL10_EFF1h6GU/sendMessage', data=data)

            s.enter(2, 1, hector, (s,))


def hector(sc):
        try:
            print('Starting Hector..')
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://app.hectordao.com/#/dashboard"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            price = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[1].get_text()
            mcap = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[0].get_text()
            tvl = soup.findAll('h4', class_='MuiTypography-root MuiTypography-h4')[0].get_text()
            treasury = soup.findAll('h4', class_='MuiTypography-root MuiTypography-h4')[1].get_text()
            runway = soup.findAll('h4', class_='MuiTypography-root MuiTypography-h4')[5].get_text()
            
            driver.quit()
            apy = hec_api()
            
            print('HectorDAO - $HEC', price, '\n', mcap, '\n', tvl, '\n', apy, '\n', treasury, '\n' , runway)

            total = {'mcap': mcap, 'price': price, 'tvl': tvl, 'apy': apy, 'treasury': treasury,  'runway': runway}
            

            with open("/home/admin/Desktop/data/hector.json", "w") as f:
                json.dump(total, f, indent=2)

            subprocess.call(['python3', '/home/admin/Desktop/Script/hector.py'])

            keyboard = [
                [
                    InlineKeyboardButton("Chart", url='https://dexscreener.com/fantom/0xbc0eecda2d8141e3a26d2535c57cadcb1095bca9'),
                    InlineKeyboardButton("Dashboard", url='https://app.hectordao.com/#/dashboard')
                ]
            ]
             
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            print('Setting up data.')
            data = {
                    'photo': ('hector.png', open('/home/admin/Desktop/ss/hector.png', 'rb')),
                    'action': (None, 'send'),
                    'chat_id': (None, '-1001431327406'),
                    'caption': (None, f'\U0001F48E <b>HectorDAO - $HEC</b> #Fantom \U0001F48E \n\n\u231B <i>@hectorDAO - <a href="https://discord.gg/ygMfMBwkgp">Discord</a> - <a href="https://twitter.com/HectorDAO_HEC">Twitter</a> - <a href="https://rebasetokens.app/f-a-q">FAQ</a></i> \u231B\n\n\U0001F4B5 <b>Market Cap:</b> {mcap}\n\U0001F4B0 <b>Price:</b> {price}\n\U0001F5D3 <b>APY:</b> {apy}\n\U0001F512 <b>TVL:</b> {tvl}\n\U0001F4AC <b>Treasury:</b> {treasury}\n\n\U0001F315 <a href="https://warp.bond/"><b>Warp.Bond</b></a> - The Next-Gen Web3 reserve currency ft. NFT Bonds & buildable starships that travel within the Staking #Metaverse\n@warpbond - <a href="https://discord.gg/warpbond">Discord</a> - <a href="https://twitter.com/warpbond">Twitter</a>\nJoin the <a href="https://warpcountdown.com/">Whitelist here!</a> \U0001F315'),
                    "reply_markup": (None, json.dumps(reply_markup.to_dict())),
                    "parse_mode": (None, 'HTML')
            }
        
            requests.post(url='https://api.telegram.org/bot5025889373:AAEGOUROw4deWROTzTR-1v1lDddv2EJFmSQ/sendPhoto', files=data)
            print('Data sent!')

            print('Shutting off HectorDAO..')

            s.enter(2, 1, jade, (s,))

        except Exception as errore:

            print(errore)

            data = {"chat_id": "92637783",
                    "text": f'<b>Error</b> on Hector Main Chat\n\n {errore}' ,
                    "parse_mode": 'HTML'}

            requests.post(url='https://api.telegram.org/bot5062720103:AAHo_qpQzG5dqRteZ-VgfBYL10_EFF1h6GU/sendMessage', data=data)

            s.enter(2, 1, jade, (s,))


        

def hec_api():

            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)

            urltwo = "https://app.hectordao.com/#/stake"
            driver.get(urltwo)
            time.sleep(30)

            soup = BeautifulSoup(driver.page_source,'html.parser')
            apy = soup.findAll('h4', class_='MuiTypography-root MuiTypography-h4')[0].get_text()

            driver.quit()

            return apy


def jade(sc):
        try:
            print('Starting JadeProtocol..')
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
            
            urlone = "https://jadeprotocol.io/#/"
            driver.get(urlone)
            time.sleep(30)

            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            price = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[0].get_text()
            fmv = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[1].get_text()
            treasury = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[6].get_text()  
            tvl = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[4].get_text()
            backing = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[2].get_text()  
            
            
            driver.quit()

            print('JadeProtocol - $JADE', price, '\n', fmv, '\n', tvl, '\n', treasury, '\n', backing)

            total = {'price': price, 'tvl': tvl, 'fmv': fmv, 'treasury': treasury, 'backing': backing}
            

            with open("/home/admin/Desktop/data/jade.json", "w") as f:
                json.dump(total, f, indent=2)

            subprocess.call(['python3', '/home/admin/Desktop/Script/jade.py'])


            keyboard = [
                [
                    InlineKeyboardButton("Chart", url='https://dexscreener.com/bsc/0x46503d91d7a41fcbdc250e84cee9d457d082d7b4'),
                    InlineKeyboardButton("Dashboard", url='https://jadeprotocol.io/#/')
                ]
            ]
             
            reply_markup = InlineKeyboardMarkup(keyboard)

            print('Setting up data.')

            data = {
                    'photo': ('jade.png', open('/home/admin/Desktop/ss/jade.png', 'rb')),
                    'action': (None, 'send'),
                    'chat_id': (None, '-1001431327406'),
                    'caption': (None, f'\U0001F48E <b>JadeProtocol - $JADE</b> #BSC \U0001F48E \n\n\u231B <i>@jadeprotocolofficial - <a href="https://discord.gg/vm3uuJ6dWS">Discord</a> - <a href="https://twitter.com/JadeProtocol">Twitter</a> - <a href="https://rebasetokens.app/f-a-q">FAQ</a></i> \u231B\n\n\U0001F4B0 <b>Price:</b> {price}\n\U0001F5D3 <b>Fair Market Value:</b> {fmv}\n\U0001F4CC <b>Floor:</b> {backing}\n\U0001F512 <b>Backing Treasury:</b> {tvl}\n\U0001F4AC <b>Investment Treasury:</b> {treasury}\n\n\U0001F315 <a href="https://warp.bond/"><b>Warp.Bond</b></a> - The Next-Gen Web3 reserve currency ft. NFT Bonds & buildable starships that travel within the Staking #Metaverse\n@warpbond - <a href="https://discord.gg/warpbond">Discord</a> - <a href="https://twitter.com/warpbond">Twitter</a>\nJoin the <a href="https://warpcountdown.com/">Whitelist here!</a> \U0001F315'),
                    "reply_markup": (None, json.dumps(reply_markup.to_dict())),
                    "parse_mode": (None, 'HTML')
            }
        
            requests.post(url='https://api.telegram.org/bot5025889373:AAEGOUROw4deWROTzTR-1v1lDddv2EJFmSQ/sendPhoto', files=data)

            print('Data sent!')

            print('Shutting off JadeProtocol..')
            s.enter(2, 1, klima, (s,))

        except Exception as errore:

            print(errore)

            data = {"chat_id": "92637783",
                    "text": f'<b>Error</b> on Jade Main Chat\n\n {errore}' ,
                    "parse_mode": 'HTML'}

            requests.post(url='https://api.telegram.org/bot5062720103:AAHo_qpQzG5dqRteZ-VgfBYL10_EFF1h6GU/sendMessage', data=data)

            s.enter(2, 1, klima, (s,))


def klima(sc):
        try:
            print('Starting KlimaDAO..')
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
            
            urlone = "https://www.klimadao.finance/"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            apy = soup.findAll('p', class_='Home_dataCard_priceTag__LswM1 typography_h5__me6pd')[0].get_text()
            price = soup.findAll('p', class_='Home_dataCard_priceTag__LswM1 typography_h5__me6pd')[1].get_text()
            treasury = soup.find('span', class_='Home_treasuryBalance_value__q_rYL typography_h4__A__D_').get_text()
            
            
            driver.quit()

            mcap = klimamcap()

            print('KlimaDAO - $KLIMA', mcap, '\n', price, '\n', apy, '\n', treasury)

            total = {'mcap': mcap, 'price': price, 'apy': apy, 'treasury': treasury}
            

            with open("/home/admin/Desktop/data/klima.json", "w") as f:
                json.dump(total, f, indent=2)

            subprocess.call(['python3', '/home/admin/Desktop/Script/klima.py'])

            keyboard = [
                [
                    InlineKeyboardButton("Chart", url='https://dexscreener.com/polygon/0x9803c7ae526049210a1725f7487af26fe2c24614'),
                    InlineKeyboardButton("Dashboard", url='https://dapp.klimadao.finance/#/stake')
                ]
            ]
             
            reply_markup = InlineKeyboardMarkup(keyboard)

            print('Setting up data.')

            data = {
                    'photo': ('klima.png', open('/home/admin/Desktop/ss/klima.png', 'rb')),
                    'action': (None, 'send'),
                    'chat_id': (None, '-1001431327406'),
                    'caption': (None, f'\U0001F48E <b>KlimaDAO - $KLIMA</b> #Polygon \U0001F48E \n\n\u231B <i><a href="https://discord.gg/F4Ma6APYrV">Discord</a> - <a href="https://twitter.com/KlimaDAO">Twitter</a> - <a href="https://rebasetokens.app/f-a-q">FAQ</a></i> \u231B\n\n\U0001F4B5 <b>Market Cap:</b> ${mcap}\n\U0001F4B0 <b>Price:</b> {price}\n\U0001F5D3 <b>APY:</b> {apy}\n <b>Carbon in Treasury:</b> {treasury} tonnes of CO2\n\n\U0001F315 <a href="https://warp.bond/"><b>Warp.Bond</b></a> - The Next-Gen Web3 reserve currency ft. NFT Bonds & buildable starships that travel within the Staking #Metaverse\n@warpbond - <a href="https://discord.gg/warpbond">Discord</a> - <a href="https://twitter.com/warpbond">Twitter</a>\nJoin the <a href="https://warpcountdown.com/">Whitelist here!</a> \U0001F315'),
                    "reply_markup": (None, json.dumps(reply_markup.to_dict())),
                    "parse_mode": (None, 'HTML')
            }
        
            requests.post(url='https://api.telegram.org/bot5025889373:AAEGOUROw4deWROTzTR-1v1lDddv2EJFmSQ/sendPhoto', files=data)

            print('Data sent!')

            print('Shutting off KlimaDAO..')
            s.enter(2, 1, rug, (s,))

        except Exception as errore:

            print(errore)

            data = {"chat_id": "92637783",
                    "text": f'<b>Error</b> on Klima Main Chat\n\n {errore}' ,
                    "parse_mode": 'HTML'}

            requests.post(url='https://api.telegram.org/bot5062720103:AAHo_qpQzG5dqRteZ-VgfBYL10_EFF1h6GU/sendMessage', data=data)

            s.enter(2, 1, rug, (s,))


def klimamcap():
        
            options = webdriver.FirefoxOptions()
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
            driver.maximize_window()
        
            urlone = "https://dexscreener.com/polygon/0x5786b267d35f9d011c4750e0b0ba584e1fdbead1"
            driver.get(urlone)
            time.sleep(30)

            soup = BeautifulSoup(driver.page_source,'html.parser')
            mcap = soup.find_all('span', {'class' : 'chakra-text css-5sxn50', })[4].get_text()
            

            substringb = 'B'
            substringm = 'M'
            substringk = 'K'
            mcap = mcap.replace('.',',')
            mcap = mcap.replace('$','')
            countkmcap = mcap.count(substringk)
            countmmcap = mcap.count(substringm)
            countbmcap = mcap.count(substringb)
            

            if countkmcap > 0:
                mcap = mcap.replace('K','')
                mcap = mcap.replace(',','.')
                mcap = float(mcap)
                mcap = mcap * 1000
                mcap = int(mcap)
                mcap = format(mcap, ',')
                mcap = str(mcap)
                print(mcap)
            elif countmmcap > 0:
                mcap = mcap.replace('M','')
                mcap = mcap.replace(',','.')
                mcap = float(mcap)
                mcap = mcap * 1000000
                mcap = int(mcap)
                mcap = format(mcap, ',')
                mcap = str(mcap)
                print(mcap)
            elif countbmcap > 0:
                mcap = mcap.replace('B','')
                mcap = mcap.replace(',','.')
                mcap = float(mcap)
                mcap = mcap * 1000000000
                mcap = int(mcap)
                mcap = format(mcap, ',')
                mcap = str(mcap)
                print(mcap)
            else:
                print(mcap)

            driver.quit()

            return mcap


def rug(sc):
        try:
            print('Starting RUG..')
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
            
            urlone = "https://www.rug.farm/#/dashboard"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            apytag = soup.findAll('p', class_='card-value text-center')[0]
            price = soup.findAll('p', class_='card-value')[0].get_text()
            mcap = soup.findAll('p', class_='card-value')[2].get_text()
            tvl = soup.findAll('p', class_='card-value')[4].get_text()
            treasury = soup.findAll('p', class_='card-value')[7].get_text()
            apy = apytag.get('data-tip')
            runway = soup.findAll('p', class_='card-value')[9].get_text()
            backing = soup.findAll('p', class_='card-value')[8].get_text()
            
            
            driver.quit()


            print('R U Generous - $RUG', mcap, '\n', price, '\n', apy, '\n', treasury, '\n', runway, '\n', tvl, '\n', backing)

            total = {'mcap': mcap, 'price': price, 'tvl': tvl, 'apy': apy, 'treasury': treasury, 'backing': backing, 'runway': runway}
            

            with open("/home/admin/Desktop/data/rug.json", "w") as f:
                json.dump(total, f, indent=2)

            subprocess.call(['python3', '/home/admin/Desktop/Script/rug.py'])

            keyboard = [
                [
                    InlineKeyboardButton("Chart", url='https://dexscreener.com/avalanche/0x8b667c1e422c08f9874709939bc90e71c2bea167'),
                    InlineKeyboardButton("Dashboard", url='https://www.rug.farm/#/dashboard')
                ]
            ]
             
            reply_markup = InlineKeyboardMarkup(keyboard)

            print('Setting up data.')

            data = {
                    'photo': ('rug.png', open('/home/admin/Desktop/ss/rug.png', 'rb')),
                    'action': (None, 'send'),
                    'chat_id': (None, '-1001431327406'),
                    'caption': (None, f'\U0001F48E <b>R U Generous - $RUG</b> #AVAX \U0001F48E \n\n\u231B <i><a href="https://discord.gg/U6ZrH9mYdn">Discord</a> - <a href="https://twitter.com/RUGenerous">Twitter</a> - <a href="https://rebasetokens.app/f-a-q">FAQ</a></i> \u231B\n\n\U0001F4B5 <b>Market Cap:</b> {mcap}\n\U0001F4B0 <b>Price:</b> {price}\n\U0001F5D3 <b>APY:</b> {apy}\n\U0001F512 <b>TVL:</b> {tvl}\n\U0001F4AC <b>Treasury:</b> {treasury}\n\U0001F4CC <b>Backing:</b> {backing}\n\u23F0 <b>Runway:</b> {runway}\n\n\U0001F315 <a href="https://warp.bond/"><b>Warp.Bond</b></a> - The Next-Gen Web3 reserve currency ft. NFT Bonds & buildable starships that travel within the Staking #Metaverse\n@warpbond - <a href="https://discord.gg/warpbond">Discord</a> - <a href="https://twitter.com/warpbond">Twitter</a>\nJoin the <a href="https://warpcountdown.com/">Whitelist here!</a> \U0001F315'),
                    "reply_markup": (None, json.dumps(reply_markup.to_dict())),
                    "parse_mode": (None, 'HTML')
            }
        
            requests.post(url='https://api.telegram.org/bot5025889373:AAEGOUROw4deWROTzTR-1v1lDddv2EJFmSQ/sendPhoto', files=data)

            print('Data sent!')

            print('Shutting off RUG..')
            s.enter(2, 1, sparta, (s,))

        except Exception as errore:

            print(errore)

            data = {"chat_id": "92637783",
                    "text": f'<b>Error</b> on Rug Main Chat\n\n {errore}' ,
                    "parse_mode": 'HTML'}

            requests.post(url='https://api.telegram.org/bot5062720103:AAHo_qpQzG5dqRteZ-VgfBYL10_EFF1h6GU/sendMessage', data=data)

            s.enter(2, 1, sparta, (s,))



def sparta(sc):
        try:
            print('Starting Spartacus..')
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
            
            urlone = "https://app.spartacus.finance/#/dashboard"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            price = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[1].get_text()
            mcap = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[0].get_text()
            backing = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[4].get_text()
            tvl = soup.findAll('h4', class_='MuiTypography-root MuiTypography-h4')[0].get_text()
            treasury = soup.findAll('h4', class_='MuiTypography-root MuiTypography-h4')[1].get_text()
            runway = soup.findAll('h4', class_='MuiTypography-root MuiTypography-h4')[5].get_text()
            
            
            driver.quit()

            apy = spaapy()


            print('Spartacus - $SPA', mcap, '\n', price, '\n', apy, '\n', treasury, '\n', runway, '\n', tvl, '\n', backing)

            total = {'mcap': mcap, 'price': price, 'tvl': tvl, 'apy': apy, 'treasury': treasury, 'backing': backing, 'runway': runway}
            

            with open("/home/admin/Desktop/data/sparta.json", "w") as f:
                json.dump(total, f, indent=2)

            subprocess.call(['python3', '/home/admin/Desktop/Script/sparta.py'])

            keyboard = [
                [
                    InlineKeyboardButton("Chart", url='https://dexscreener.com/fantom/0xfa5a5f0bc990be1d095c5385fff6516f6e03c0a7'),
                    InlineKeyboardButton("Dashboard", url='https://app.spartacus.finance/#/dashboard')
                ]
            ]
             
            reply_markup = InlineKeyboardMarkup(keyboard)

            print('Setting up data.')

            data = {
                    'photo': ('spa.png', open('/home/admin/Desktop/ss/spa.png', 'rb')),
                    'action': (None, 'send'),
                    'chat_id': (None, '-1001431327406'),
                    'caption': (None, f'\U0001F48E <b>Spartacus - $SPA</b> #Fantom \U0001F48E \n\n\u231B <i><a href="https://discord.gg/R6ZSpWrzrb">Discord</a> - <a href="https://twitter.com/Spartacus_Fi">Twitter</a> - <a href="https://rebasetokens.app/f-a-q">FAQ</a></i> \u231B\n\n\U0001F4B5 <b>Market Cap:</b> {mcap}\n\U0001F4B0 <b>Price:</b> {price}\n\U0001F5D3 <b>APY:</b> {apy}\n\U0001F512 <b>TVL:</b> {tvl}\n\U0001F4AC <b>Treasury:</b> {treasury}\n\U0001F4CC <b>Backing:</b> {backing}\n\u23F0 <b>Runway:</b> {runway}\n\n\U0001F315 <a href="https://warp.bond/"><b>Warp.Bond</b></a> - The Next-Gen Web3 reserve currency ft. NFT Bonds & buildable starships that travel within the Staking #Metaverse\n@warpbond - <a href="https://discord.gg/warpbond">Discord</a> - <a href="https://twitter.com/warpbond">Twitter</a>\nJoin the <a href="https://warpcountdown.com/">Whitelist here!</a> \U0001F315'),
                    "reply_markup": (None, json.dumps(reply_markup.to_dict())),
                    "parse_mode": (None, 'HTML')
            }
        
            requests.post(url='https://api.telegram.org/bot5025889373:AAEGOUROw4deWROTzTR-1v1lDddv2EJFmSQ/sendPhoto', files=data)

            print('Data sent!')

            print('Shutting off Spartacus..')
            s.enter(2, 1, ohm, (s,))

        except Exception as errore:

            print(errore)

            data = {"chat_id": "92637783",
                    "text": f'<b>Error</b> on Sparta Main Chat\n\n {errore}' ,
                    "parse_mode": 'HTML'}

            requests.post(url='https://api.telegram.org/bot5062720103:AAHo_qpQzG5dqRteZ-VgfBYL10_EFF1h6GU/sendMessage', data=data)

            s.enter(2, 1, ohm, (s,))


def spaapy():
        
            options = webdriver.FirefoxOptions()
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://app.spartacus.finance/#/stake"
            driver.get(urlone)
            time.sleep(30)

            soup = BeautifulSoup(driver.page_source,'html.parser')
            apy = soup.findAll('h4', class_='MuiTypography-root MuiTypography-h4')[0].get_text()

            driver.quit()

            return apy





def ohm(sc):
        try:
            print('Starting Olympus..')
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
            
            urlone = "https://app.olympusdao.finance/#/dashboard"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            mcap = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[0].get_text()
            price = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[1].get_text()
            backing = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[4].get_text()
            tvl = soup.findAll('h4', class_='MuiTypography-root MuiTypography-h4')[0].get_text()
            treasury = soup.findAll('h4', class_='MuiTypography-root MuiTypography-h4')[1].get_text()
            runway = soup.findAll('h4', class_='MuiTypography-root MuiTypography-h4')[5].get_text()
            
            
            driver.quit()
            
            apy = ohmapy()

            print('OlympusDAO - $OHM', mcap, '\n', price, '\n', apy, '\n', treasury, '\n', runway, '\n', tvl, '\n', backing)

            total = {'mcap': mcap, 'price': price, 'tvl': tvl, 'apy': apy, 'treasury': treasury, 'backing': backing, 'runway': runway}
            

            with open("/home/admin/Desktop/data/ohm.json", "w") as f:
                json.dump(total, f, indent=2)

            subprocess.call(['python3', '/home/admin/Desktop/Script/ohm.py'])

            keyboard = [
                [
                    InlineKeyboardButton("Chart", url='https://dexscreener.com/ethereum/0x69b81152c5a8d35a67b32a4d3772795d96cae4da'),
                    InlineKeyboardButton("Dashboard", url='https://app.olympusdao.finance/#/dashboard')
                ]
            ]
             
            reply_markup = InlineKeyboardMarkup(keyboard)

            print('Setting up data.')

            data = {
                    'photo': ('ohm.png', open('/home/admin/Desktop/ss/ohm.png', 'rb')),
                    'action': (None, 'send'),
                    'chat_id': (None, '-1001431327406'),
                    'caption': (None, f'\U0001F48E <b>OlympusDAO - $OHM</b> #ETH \U0001F48E \n\n\u231B <i>@OlympusTG - <a href="https://discord.gg/P3ShgW4c28">Discord</a> - <a href="https://twitter.com/OlympusDAO">Twitter</a> - <a href="https://rebasetokens.app/f-a-q">FAQ</a></i> \u231B\n\n\U0001F4B5 <b>Market Cap:</b> {mcap}\n\U0001F4B0 <b>Price:</b> {price}\n\U0001F5D3 <b>APY:</b> {apy}\n\U0001F512 <b>TVL:</b> {tvl}\n\U0001F4AC <b>Treasury:</b> {treasury}\n\U0001F4CC <b>Backing:</b> {backing}\n\u23F0 <b>Runway:</b> {runway}\n\n\U0001F315 <a href="https://warp.bond/"><b>Warp.Bond</b></a> - The Next-Gen Web3 reserve currency ft. NFT Bonds & buildable starships that travel within the Staking #Metaverse\n@warpbond - <a href="https://discord.gg/warpbond">Discord</a> - <a href="https://twitter.com/warpbond">Twitter</a>\nJoin the <a href="https://warpcountdown.com/">Whitelist here!</a> \U0001F315'),
                    "reply_markup": (None, json.dumps(reply_markup.to_dict())),
                    "parse_mode": (None, 'HTML')
            }
        
            requests.post(url='https://api.telegram.org/bot5025889373:AAEGOUROw4deWROTzTR-1v1lDddv2EJFmSQ/sendPhoto', files=data)

            print('Data sent!')

            print('Shutting off Olympus..')
            s.enter(2, 1, ice, (s,))

        except Exception as errore:

            print(errore)

            data = {"chat_id": "92637783",
                    "text": f'<b>Error</b> on OHM Main Chat\n\n {errore}' ,
                    "parse_mode": 'HTML'}

            requests.post(url='https://api.telegram.org/bot5062720103:AAHo_qpQzG5dqRteZ-VgfBYL10_EFF1h6GU/sendMessage', data=data)

            s.enter(2, 1, ice, (s,))
        


def ohmapy():
        
            options = webdriver.FirefoxOptions()
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
            options.headless = True
            urlone = "https://app.olympusdao.finance/#/stake"
            driver.get(urlone)
            time.sleep(30)

            soup = BeautifulSoup(driver.page_source,'html.parser')
            
            apy = soup.findAll('h4', class_='MuiTypography-root MuiTypography-h4')[0].get_text()

            driver.quit()
                            
            return apy

        

def ice(sc):
        try:
            print('Starting Ice..')
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://app.icedao.finance/#/dashboard"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            price = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[0].get_text()
            apy = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[1].get_text()
            mcap = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[4].get_text()
            tvl = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[5].get_text()
            treasury = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[6].get_text()
            backing = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[11].get_text()
            runway = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[10].get_text()
            
            
            driver.quit()
            print('Ice - $ICE', price,'\n', mcap,'\n', tvl,'\n', apy,'\n', treasury,'\n', backing, '\n', runway)
            
            total = {'mcap': mcap, 'price': price, 'tvl': tvl, 'apy': apy, 'treasury': treasury, 'backing': backing, 'runway': runway}
            

            with open("/home/admin/Desktop/data/ice.json", "w") as f:
                json.dump(total, f, indent=2)

            subprocess.call(['python3', '/home/admin/Desktop/Script/ice.py'])
                
            keyboard = [
                [
                    InlineKeyboardButton("Chart", url='https://dexscreener.com/avalanche/0xfefb9b28f341d855b598e16ecc5f83b40cd827e6'),
                    InlineKeyboardButton("Dashboard", url='https://app.icedao.finance/#/dashboard')
                ]
            ]
             
            reply_markup = InlineKeyboardMarkup(keyboard)

            print('Setting up data.')

            data = {
                    'photo': ('ice.png', open('/home/admin/Desktop/ss/ice.png', 'rb')),
                    'action': (None, 'send'),
                    'chat_id': (None, '-1001431327406'),
                    'caption': (None, f'\U0001F48E <b>IceDAO - $ICY</b> #AVAX \U0001F48E \n\n\u231B <i><a href="https://discord.gg/3yThPJEN2M">Discord</a> - <a href="https://twitter.com/ICE_DAO_">Twitter</a> - <a href="https://rebasetokens.app/f-a-q">FAQ</a></i> \u231B\n\n\U0001F4B5 <b>Market Cap:</b> {mcap}\n\U0001F4B0 <b>Price:</b> {price}\n\U0001F5D3 <b>APY:</b> {apy}\n\U0001F512 <b>TVL:</b> {tvl}\n\U0001F4AC <b>Treasury:</b> {treasury}\n\U0001F4CC <b>Backing:</b> {backing}\n\u23F0 <b>Runway:</b> {runway}\n\n\U0001F315 <a href="https://warp.bond/"><b>Warp.Bond</b></a> - The Next-Gen Web3 reserve currency ft. NFT Bonds & buildable starships that travel within the Staking #Metaverse\n@warpbond - <a href="https://discord.gg/warpbond">Discord</a> - <a href="https://twitter.com/warpbond">Twitter</a>\nJoin the <a href="https://warpcountdown.com/">Whitelist here!</a> \U0001F315'),
                    "reply_markup": (None, json.dumps(reply_markup.to_dict())),
                    "parse_mode": (None, 'HTML')
            }
        
            requests.post(url='https://api.telegram.org/bot5025889373:AAEGOUROw4deWROTzTR-1v1lDddv2EJFmSQ/sendPhoto', files=data)
            
            print('Data sent!')

            print('Shutting off Ice..')
            s.enter(2, 1, hunny, (s,))

        except Exception as errore:

            print(errore)

            data = {"chat_id": "92637783",
                    "text": f'<b>Error</b> on Ice Main Chat\n\n {errore}' ,
                    "parse_mode": 'HTML'}

            requests.post(url='https://api.telegram.org/bot5062720103:AAHo_qpQzG5dqRteZ-VgfBYL10_EFF1h6GU/sendMessage', data=data)

            s.enter(2, 1, hunny, (s,))



def hunny(sc):
        try:
            print('Starting Hunny..')
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
            
            urlone = "https://dao.hunny.finance/#/dashboard"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            mcap = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[2].get_text()
            price = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[1].get_text()
            tvl = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[3].get_text()
            treasury = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[4].get_text()
            backing = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[5].get_text()
            apy = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[0].get_text()
            
            
            driver.quit()

            print('Hunny', mcap, '\n', price, '\n', apy, '\n', treasury, '\n', backing, '\n', tvl)

            total = {'mcap': mcap, 'price': price, 'tvl': tvl, 'apy': apy, 'treasury': treasury, 'backing': backing}
            

            with open("/home/admin/Desktop/data/hunny.json", "w") as f:
                json.dump(total, f, indent=2)

            subprocess.call(['python3', '/home/admin/Desktop/Script/hunny.py'])

            keyboard = [
                [
                    InlineKeyboardButton("Chart", url='https://dexscreener.com/bsc/0x9e8ae3a26536582823ef82c155b69637a4a753f8'),
                    InlineKeyboardButton("Dashboard", url='https://dao.hunny.finance/#/dashboard')
                ]
            ]
             
            reply_markup = InlineKeyboardMarkup(keyboard)

            print('Setting up data.')

            data = {
                    'photo': ('hunny.png', open('/home/admin/Desktop/ss/hunny.png', 'rb')),
                    'action': (None, 'send'),
                    'chat_id': (None, '-1001431327406'),
                    'caption': (None, f'\U0001F48E <b>HunnyDAO - $HUNNY</b> #BSC \U0001F48E \n\n\u231B <i>@HunnyFinance - <a href="https://discord.gg/d4fxKZFxPv">Discord</a> - <a href="https://twitter.com/HunnyFinance">Twitter</a> - <a href="https://rebasetokens.app/f-a-q">FAQ</a></i> \u231B\n\n\U0001F4B5 <b>Market Cap:</b> {mcap}\n\U0001F4B0 <b>Price:</b> {price}\n\U0001F5D3 <b>APY:</b> {apy}\n\U0001F512 <b>TVL:</b> {tvl}\n\U0001F4AC <b>Treasury:</b> {treasury}\n\U0001F4CC <b>Backing:</b> {backing}\n\n\U0001F315 <a href="https://warp.bond/"><b>Warp.Bond</b></a> - The Next-Gen Web3 reserve currency ft. NFT Bonds & buildable starships that travel within the Staking #Metaverse\n@warpbond - <a href="https://discord.gg/warpbond">Discord</a> - <a href="https://twitter.com/warpbond">Twitter</a>\nJoin the <a href="https://warpcountdown.com/">Whitelist here!</a> \U0001F315'),
                    "reply_markup": (None, json.dumps(reply_markup.to_dict())),
                    "parse_mode": (None, 'HTML')
            }
        
            requests.post(url='https://api.telegram.org/bot5025889373:AAEGOUROw4deWROTzTR-1v1lDddv2EJFmSQ/sendPhoto', files=data)

            print('Data sent!')

            print('Shutting off Hunny..')
            s.enter(2, 1, maxi, (s,))

        except Exception as errore:

            print(errore)

            data = {"chat_id": "92637783",
                    "text": f'<b>Error</b> on Hunny Main Chat\n\n {errore}' ,
                    "parse_mode": 'HTML'}

            requests.post(url='https://api.telegram.org/bot5062720103:AAHo_qpQzG5dqRteZ-VgfBYL10_EFF1h6GU/sendMessage', data=data)

            s.enter(2, 1, maxi, (s,))


def maxi(sc):
        try:
            print('Starting Maxi..')
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
            
            urlone = "https://app.maxixyz.com/#/dashboard"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            apy = soup.findAll('p', class_='card-value')[9].get_text()
            price = soup.findAll('p', class_='card-value')[6].get_text()
            mcap = soup.findAll('p', class_='card-value')[3].get_text()
            tvl = soup.findAll('p', class_='card-value')[4].get_text()
            treasury = soup.findAll('p', class_='card-value')[5].get_text()
            runway = soup.findAll('p', class_='card-value')[10].get_text()
            backing = soup.findAll('p', class_='card-value')[8].get_text()
            
            
            driver.quit()
            
            

            print('Maxi', mcap, '\n', price, '\n', apy, '\n', treasury, '\n', runway, '\n', tvl, '\n', backing)

            total = {'mcap': mcap, 'price': price, 'tvl': tvl, 'apy': apy, 'treasury': treasury, 'backing': backing, 'runway': runway}
            

            with open("/home/admin/Desktop/data/maxi.json", "w") as f:
                json.dump(total, f, indent=2)

            subprocess.call(['python3', '/home/admin/Desktop/Script/maxi.py'])

            keyboard = [
                [
                    InlineKeyboardButton("Chart", url='https://dexscreener.com/avalanche/0xfbdc4aa69114aa11fae65e858e92dc5d013b2ea9'),
                    InlineKeyboardButton("Dashboard", url='https://app.maxixyz.com/#/dashboard')
                ]
            ]
             
            reply_markup = InlineKeyboardMarkup(keyboard)

            print('Setting up data.')

            data = {
                    'photo': ('maxi.png', open('/home/admin/Desktop/ss/maxi.png', 'rb')),
                    'action': (None, 'send'),
                    'chat_id': (None, '-1001431327406'),
                    'caption': (None, f'\U0001F48E <b>Maximizer - $MAXI</b> #AVAX \U0001F48E \n\n\u231B <i>@maxi_xyz - <a href="https://discord.gg/J9PjgspMfd">Discord</a> - <a href="https://twitter.com/maximizer_xyz">Twitter</a> - <a href="https://rebasetokens.app/f-a-q">FAQ</a></i> \u231B\n\n\U0001F4B5 <b>Market Cap:</b> {mcap}\n\U0001F4B0 <b>Price:</b> {price}\n\U0001F5D3 <b>APY:</b> {apy}\n\U0001F512 <b>TVL:</b> {tvl}\n\U0001F4AC <b>Treasury:</b> {treasury}\n\U0001F4CC <b>Backing:</b> {backing}\n\u23F0 <b>Runway:</b> {runway}\n\n\U0001F315 <a href="https://warp.bond/"><b>Warp.Bond</b></a> - The Next-Gen Web3 reserve currency ft. NFT Bonds & buildable starships that travel within the Staking #Metaverse\n@warpbond - <a href="https://discord.gg/warpbond">Discord</a> - <a href="https://twitter.com/warpbond">Twitter</a>\nJoin the <a href="https://warpcountdown.com/">Whitelist here!</a> \U0001F315'),
                    "reply_markup": (None, json.dumps(reply_markup.to_dict())),
                    "parse_mode": (None, 'HTML')
            }
        
            requests.post(url='https://api.telegram.org/bot5025889373:AAEGOUROw4deWROTzTR-1v1lDddv2EJFmSQ/sendPhoto', files=data)

            print('Data sent!')

            print('Shutting off Maximizer..')
            s.enter(2, 1, fantohm, (s,))

        except Exception as errore:

            print(errore)

            data = {"chat_id": "92637783",
                    "text": f'<b>Error</b> on Maximizer Main Chat\n\n {errore}' ,
                    "parse_mode": 'HTML'}

            requests.post(url='https://api.telegram.org/bot5062720103:AAHo_qpQzG5dqRteZ-VgfBYL10_EFF1h6GU/sendMessage', data=data)

            s.enter(2, 1, fantohm, (s,))


def fantohm(sc):
        try:
            print('Starting FantOHM..')
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
            
            urlone = "https://app.fantohm.com/#/dashboard"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            mcap = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[1].get_text()
            price = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[0].get_text()
            tvl = soup.findAll('h4', class_='MuiTypography-root MuiTypography-h4')[0].get_text()
            apy = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[3].get_text()
            
            
            driver.quit()
            
            values = bondohm()
            treasury = values[0]
            backing = values[1]
            runway = values[2]

            print('FantOHM', mcap, '\n', price, '\n', apy, '\n', treasury, '\n', runway, '\n', tvl, '\n', backing)

            total = {'mcap': mcap, 'price': price, 'tvl': tvl, 'apy': apy, 'treasury': treasury, 'backing': backing, 'runway': runway}
            

            with open("/home/admin/Desktop/data/fantohm.json", "w") as f:
                json.dump(total, f, indent=2)

            subprocess.call(['python3', '/home/admin/Desktop/Script/fantohm.py'])

            keyboard = [
                [
                    InlineKeyboardButton("Chart", url='https://dexscreener.com/fantom/0xd77fc9c4074b56ecf80009744391942fbfddd88b'),
                    InlineKeyboardButton("Dashboard", url='https://app.fantohm.com/#/dashboard')
                ]
            ]
             
            reply_markup = InlineKeyboardMarkup(keyboard)

            print('Setting up data.')

            data = {
                    'photo': ('fant.png', open('/home/admin/Desktop/ss/fant.png', 'rb')),
                    'action': (None, 'send'),
                    'chat_id': (None, '-1001431327406'),
                    'caption': (None, f'\U0001F48E <b>FantOHM - $FHM</b> #Fantom \U0001F48E \n\n\u231B <i>@fantohm - <a href="https://discord.gg/AzAZP5VKAx">Discord</a> - <a href="https://twitter.com/FantohmDAO">Twitter</a> - <a href="https://rebasetokens.app/f-a-q">FAQ</a></i> \u231B\n\n\U0001F4B5 <b>Market Cap:</b> {mcap}\n\U0001F4B0 <b>Price:</b> {price}\n\U0001F5D3 <b>APY:</b> {apy}\n\U0001F512 <b>TVL:</b> {tvl}\n\U0001F4AC <b>Treasury:</b> {treasury}\n\U0001F4CC <b>Backing:</b> {backing}\n\u23F0 <b>Runway:</b> {runway}\n\n\U0001F315 <a href="https://warp.bond/"><b>Warp.Bond</b></a> - The Next-Gen Web3 reserve currency ft. NFT Bonds & buildable starships that travel within the Staking #Metaverse\n@warpbond - <a href="https://discord.gg/warpbond">Discord</a> - <a href="https://twitter.com/warpbond">Twitter</a>\nJoin the <a href="https://warpcountdown.com/">Whitelist here!</a> \U0001F315'),
                    "reply_markup": (None, json.dumps(reply_markup.to_dict())),
                    "parse_mode": (None, 'HTML')
            }
        
            requests.post(url='https://api.telegram.org/bot5025889373:AAEGOUROw4deWROTzTR-1v1lDddv2EJFmSQ/sendPhoto', files=data)

            print('Data sent!')

            print('Shutting off FantOHM..')
            s.enter(2, 1, templar, (s,))

        except Exception as errore:

            print(errore)

            data = {"chat_id": "92637783",
                    "text": f'<b>Error</b> on FantOHM Main Chat\n\n {errore}' ,
                    "parse_mode": 'HTML'}

            requests.post(url='https://api.telegram.org/bot5062720103:AAHo_qpQzG5dqRteZ-VgfBYL10_EFF1h6GU/sendMessage', data=data)

            s.enter(2, 1, templar, (s,))


def bondohm():
        
            options = webdriver.FirefoxOptions()
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://app.fantohm.com/#/bonds"
            driver.get(urlone)
            time.sleep(30)

            soup = BeautifulSoup(driver.page_source,'html.parser')
            
            treasury = soup.findAll('h4', class_='MuiTypography-root MuiTypography-h4')[0].get_text()
            backing = soup.findAll('h4', class_='MuiTypography-root MuiTypography-h4')[2].get_text()
            runway = soup.findAll('h4', class_='MuiTypography-root MuiTypography-h4')[3].get_text()

            driver.quit()
                            
            return treasury, backing, runway


def templar(sc):
        try:
            print('Starting Templar..')
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
            
            urlone = "https://templar.finance/"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            mcap = soup.findAll('div', class_='price')[0].get_text()
            price = soup.findAll('div', class_='price')[7].get_text()
            apy = soup.findAll('div', class_='price')[8].get_text()
            backing = soup.findAll('div', class_='price')[4].get_text()
            treasury = soup.findAll('div', class_='price')[1].get_text()
            runway = soup.findAll('div', class_='price')[5].get_text()
            
            
            driver.quit()
            
            tvl = tvltem()

            print('Templar', mcap, '\n', price, '\n', apy, '\n', treasury, '\n', runway, '\n', tvl, '\n', backing)

            total = {'mcap': mcap, 'price': price, 'tvl': tvl, 'apy': apy, 'treasury': treasury, 'backing': backing, 'runway': runway}
            

            with open("/home/admin/Desktop/data/templar.json", "w") as f:
                json.dump(total, f, indent=2)

            subprocess.call(['python3', '/home/admin/Desktop/Script/templar.py'])

            keyboard = [
                [
                    InlineKeyboardButton("Chart", url='https://dexscreener.com/bsc/0x1ede821daade714edade648f525ada0c5fe4ee3a'),
                    InlineKeyboardButton("Dashboard", url='https://templar.finance/')
                ]
            ]
             
            reply_markup = InlineKeyboardMarkup(keyboard)

            print('Setting up data.')

            data = {
                    'photo': ('temp.png', open('/home/admin/Desktop/ss/temp.png', 'rb')),
                    'action': (None, 'send'),
                    'chat_id': (None, '-1001431327406'),
                    'caption': (None, f'\U0001F48E <b>TemplarDAO - $TEM</b> #BSC \U0001F48E \n\n\u231B <i>@TemplarDAO - <a href="NAME">Twitter</a> - <a href="https://rebasetokens.app/f-a-q">FAQ</a></i> \u231B\n\n\U0001F4B5 <b>Market Cap:</b> {mcap}\n\U0001F4B0 <b>Price:</b> {price}\n\U0001F5D3 <b>APY:</b> {apy}\n\U0001F512 <b>TVL:</b> {tvl}\n\U0001F4AC <b>Treasury:</b> {treasury}\n\U0001F4CC <b>Backing:</b> {backing}\n\u23F0 <b>Runway:</b> {runway}\n\n\U0001F315 <a href="https://warp.bond/"><b>Warp.Bond</b></a> - The Next-Gen Web3 reserve currency ft. NFT Bonds & buildable starships that travel within the Staking #Metaverse\n@warpbond - <a href="https://discord.gg/warpbond">Discord</a> - <a href="https://twitter.com/warpbond">Twitter</a>\nJoin the <a href="https://warpcountdown.com/">Whitelist here!</a> \U0001F315'),
                    "reply_markup": (None, json.dumps(reply_markup.to_dict())),
                    "parse_mode": (None, 'HTML')
            }
        
            requests.post(url='https://api.telegram.org/bot5025889373:AAEGOUROw4deWROTzTR-1v1lDddv2EJFmSQ/sendPhoto', files=data)

            print('Data sent!')

            print('Shutting off Templar..')
            s.enter(2, 1, papa, (s,))

        except Exception as errore:

            print(errore)

            data = {"chat_id": "92637783",
                    "text": f'<b>Error</b> on Templar Main Chat\n\n {errore}' ,
                    "parse_mode": 'HTML'}

            requests.post(url='https://api.telegram.org/bot5062720103:AAHo_qpQzG5dqRteZ-VgfBYL10_EFF1h6GU/sendMessage', data=data)

            s.enter(2, 1, papa, (s,))


def tvltem():
        
            options = webdriver.FirefoxOptions()
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://templar.finance/#/stake"
            driver.get(urlone)
            time.sleep(30)

            soup = BeautifulSoup(driver.page_source,'html.parser')
            
            tvl = soup.findAll('div', class_='price')[1].get_text()

            driver.quit()
            
                            
            return tvl



def papa(sc):
        try:
            print('Starting PapaDAO..')
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://app.papadao.co/#/dashboard"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            mcap = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[0].get_text()
            price = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[1].get_text()
            backing = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[4].get_text()

            results = papavalue()
            apy = results[0]
            tvl = results[1]
            
            driver.quit()
            print('PapaDAO - $PAPA', price,'\n', mcap,'\n', tvl,'\n', apy,'\n', backing)
            
            total = {'mcap': mcap, 'price': price, 'tvl': tvl, 'apy': apy, 'backing': backing}
            

            with open("/home/admin/Desktop/data/papa.json", "w") as f:
                json.dump(total, f, indent=2)

            subprocess.call(['python3', '/home/admin/Desktop/Script/papa.py'])
            
            keyboard = [
                [
                    InlineKeyboardButton("Chart", url='https://dexscreener.com/avalanche/0xa03a99cd3d553fe9ebbccecabcb8c47100482f72'),
                    InlineKeyboardButton("Dashboard", url='https://www.papadao.co/#/dashboard')
                ]
            ]
             
            reply_markup = InlineKeyboardMarkup(keyboard)

            print('Setting up data.')

            data = {
                    'photo': ('papa.png', open('/home/admin/Desktop/ss/papa.png', 'rb')),
                    'action': (None, 'send'),
                    'chat_id': (None, '-1001431327406'),
                    'caption': (None, f'\U0001F48E <b>PapaDAO - $PAPA</b> #AVAX \U0001F48E \n\n\u231B <i>@papadaoofficial - <a href="https://discord.gg/9HkEHPVrFx">Discord</a> - <a href="https://twitter.com/PapaDAOofficial">Twitter</a> - <a href="https://rebasetokens.app/f-a-q">FAQ</a></i> \u231B\n\n\U0001F4B5 <b>Market Cap:</b> {mcap}\n\U0001F4B0 <b>Price:</b> {price}\n\U0001F5D3 <b>APY:</b> {apy}\n\U0001F512 <b>TVL:</b> {tvl}\n\U0001F4CC <b>Backing:</b> {backing}\n\n\U0001F315 <a href="https://warp.bond/"><b>Warp.Bond</b></a> - The Next-Gen Web3 reserve currency ft. NFT Bonds & buildable starships that travel within the Staking #Metaverse\n@warpbond - <a href="https://discord.gg/warpbond">Discord</a> - <a href="https://twitter.com/warpbond">Twitter</a>\nJoin the <a href="https://warpcountdown.com/">Whitelist here!</a> \U0001F315'),
                    "reply_markup": (None, json.dumps(reply_markup.to_dict())),
                    "parse_mode": (None, 'HTML')
            }
        
            requests.post(url='https://api.telegram.org/bot5025889373:AAEGOUROw4deWROTzTR-1v1lDddv2EJFmSQ/sendPhoto', files=data)
            
            print('Data sent!')

            print('Shutting off PapaDAO..')
            s.enter(2, 1, gg, (s,))

        except Exception as errore:

            print(errore)

            data = {"chat_id": "92637783",
                    "text": f'<b>Error</b> on PapaDAO Main Chat\n\n {errore}' ,
                    "parse_mode": 'HTML'}

            requests.post(url='https://api.telegram.org/bot5062720103:AAHo_qpQzG5dqRteZ-VgfBYL10_EFF1h6GU/sendMessage', data=data)

            s.enter(2, 1, gg, (s,))
            

def papavalue():

            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://app.papadao.co/#/stake"
            driver.get(urlone)
            time.sleep(30)
            
            soup = BeautifulSoup(driver.page_source,'html.parser')
            apy = soup.findAll('h4', class_='MuiTypography-root MuiTypography-h4')[0].get_text()
            tvl = soup.findAll('h4', class_='MuiTypography-root MuiTypography-h4')[1].get_text()

            driver.quit()

            return apy, tvl



def gg(sc):
        try:
            print('Starting GG..')
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://app.galaxygoggle.money/#/dashboard"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            price = soup.findAll('div', class_='value')[11].get_text()
            mcap = soup.findAll('div', class_='value')[14].get_text()
            tvl = soup.findAll('div', class_='value')[17].get_text()
            apy = soup.findAll('div', class_='value')[12].get_text()
            treasury = soup.findAll('div', class_='value')[16].get_text()
            backing = soup.findAll('div', class_='value')[18].get_text()
            runway = soup.findAll('div', class_='value')[19].get_text()
            
            
            driver.quit()
            print('GalaxyGoggle - $GG', price,'\n', mcap,'\n', tvl,'\n', apy,'\n', treasury,'\n', backing, '\n', runway)
            
            total = {'mcap': mcap, 'price': price, 'tvl': tvl, 'apy': apy, 'treasury': treasury, 'backing': backing, 'runway': runway}
            

            with open("/home/admin/Desktop/data/gg.json", "w") as f:
                json.dump(total, f, indent=2)

            subprocess.call(['python3', '/home/admin/Desktop/Script/gg.py'])
            
            keyboard = [
                [
                    InlineKeyboardButton("Chart", url='https://dexscreener.com/bsc/0x13cf29b3f58f777dded38278f7d938401f6b260c'),
                    InlineKeyboardButton("Dashboard", url='https://app.galaxygoggle.money/#/dashboard')
                ]
            ]
             
            reply_markup = InlineKeyboardMarkup(keyboard)

            print('Setting up data.')

            data = {
                    'photo': ('gg.png', open('/home/admin/Desktop/ss/gg.png', 'rb')),
                    'action': (None, 'send'),
                    'chat_id': (None, '-1001431327406'),
                    'caption': (None, f'\U0001F48E <b>GalaxyGoggleDAO - $GG</b> #BSC \U0001F48E \n\n\u231B <i>@ApeX_Token - <a href="https://discord.gg/fRURxgh8SP">Discord</a> - <a href="https://twitter.com/GalaxyGoggleDAO">Twitter</a> - <a href="https://rebasetokens.app/f-a-q">FAQ</a></i> \u231B\n\n\U0001F4B5 <b>Market Cap:</b> {mcap}\n\U0001F4B0 <b>Price:</b> {price}\n\U0001F5D3 <b>APY:</b> {apy}\n\U0001F512 <b>TVL:</b> {tvl}\n\U0001F4CC <b>Backing:</b> {backing}\n\n\U0001F315 <a href="https://warp.bond/"><b>Warp.Bond</b></a> - The Next-Gen Web3 reserve currency ft. NFT Bonds & buildable starships that travel within the Staking #Metaverse\n@warpbond - <a href="https://discord.gg/warpbond">Discord</a> - <a href="https://twitter.com/warpbond">Twitter</a>\nJoin the <a href="https://warpcountdown.com/">Whitelist here!</a> \U0001F315'),
                    "reply_markup": (None, json.dumps(reply_markup.to_dict())),
                    "parse_mode": (None, 'HTML')
            }
        
            requests.post(url='https://api.telegram.org/bot5025889373:AAEGOUROw4deWROTzTR-1v1lDddv2EJFmSQ/sendPhoto', files=data)
            
            print('Data sent!')

            print('Shutting off GG..')
            s.enter(2, 1, wagmi, (s,))

        except Exception as errore:

            print(errore)

            data = {"chat_id": "92637783",
                    "text": f'<b>Error</b> on GalaxyGoggle Main Chat\n\n {errore}' ,
                    "parse_mode": 'HTML'}

            requests.post(url='https://api.telegram.org/bot5062720103:AAHo_qpQzG5dqRteZ-VgfBYL10_EFF1h6GU/sendMessage', data=data)

            s.enter(2, 1, wagmi, (s,))



def wagmi(sc):
        try:
            print('Starting Wagmi..')
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://app.euphoria.money/#/dashboard"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            apy = soup.findAll('p', class_='card-value')[5].get_text()
            price = soup.findAll('p', class_='card-value')[0].get_text()
            mcap = soup.findAll('p', class_='card-value')[2].get_text()
            tvl = soup.findAll('p', class_='card-value')[4].get_text()
            treasury = soup.findAll('p', class_='card-value')[7].get_text()
            backing = soup.findAll('p', class_='card-value')[8].get_text()
            runway = soup.findAll('p', class_='card-value')[9].get_text()
            
            
            driver.quit()


            print('Euphoria - $WAGMI', mcap, '\n', price, '\n', apy, '\n', treasury, '\n', runway, '\n', tvl, '\n', backing)
            
            total = {'mcap': mcap, 'price': price, 'tvl': tvl, 'apy': apy, 'treasury': treasury, 'backing': backing, 'runway': runway}
            

            with open("/home/admin/Desktop/data/wagmi.json", "w") as f:
                json.dump(total, f, indent=2)

            subprocess.call(['python3', '/home/admin/Desktop/Script/wagmi.py'])
            
            keyboard = [
                [
                    InlineKeyboardButton("Chart", url='https://dexscreener.com/harmony/0x29c1e9fc7a4c19c8fcaf2d2b2de213ef0f323f0c'),
                    InlineKeyboardButton("Dashboard", url='https://app.euphoria.money/#/dashboard')
                ]
            ]
             
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            print('Setting up data.')
            data = {
                    'photo': ('wagmi.png', open('/home/admin/Desktop/ss/wagmi.png', 'rb')),
                    'action': (None, 'send'),
                    'chat_id': (None, '-1001431327406'),
                    'caption': (None, f'\U0001F48E <b>Euphoria - $WAGMI</b> #Harmony \U0001F48E \n\n\u231B <i>@EuphoriaWAGMI - <a href="https://discord.gg/venomdao">Discord</a> - <a href="https://twitter.com/VenomDAO">Twitter</a> - <a href="https://rebasetokens.app/f-a-q">FAQ</a></i> \u231B\n\n\U0001F4B5 <b>Market Cap:</b> {mcap}\n\U0001F4B0 <b>Price:</b> {price}\n\U0001F5D3 <b>APY:</b> {apy}\n\U0001F512 <b>TVL:</b> {tvl}\n\U0001F4AC <b>Treasury:</b> {treasury}\n\U0001F4CC <b>Backing:</b> {backing}\n\u23F0 <b>Runway:</b> {runway}\n\n\U0001F315 <a href="https://warp.bond/"><b>Warp.Bond</b></a> - The Next-Gen Web3 reserve currency ft. NFT Bonds & buildable starships that travel within the Staking #Metaverse\n@warpbond - <a href="https://discord.gg/warpbond">Discord</a> - <a href="https://twitter.com/warpbond">Twitter</a>\nJoin the <a href="https://warpcountdown.com/">Whitelist here!</a> \U0001F315'),
                    "reply_markup": (None, json.dumps(reply_markup.to_dict())),
                    "parse_mode": (None, 'HTML')
            }
        
            requests.post(url='https://api.telegram.org/bot5025889373:AAEGOUROw4deWROTzTR-1v1lDddv2EJFmSQ/sendPhoto', files=data)
            print('Data sent!')

            print('Shutting off Euphoria..')
            s.enter(2, 1, invictus, (s,))
            
        except Exception as errore:

            print(errore)

            data = {"chat_id": "92637783",
                    "text": f'<b>Error</b> on Wagmi Main Chat\n\n {errore}' ,
                    "parse_mode": 'HTML'}

            requests.post(url='https://api.telegram.org/bot5062720103:AAHo_qpQzG5dqRteZ-VgfBYL10_EFF1h6GU/sendMessage', data=data)

            s.enter(2, 1, invictus, (s,))


def invictus(sc):
        try:
            print('Starting Invictus..')
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://invictusdao.fi/#/dashboard"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            price = soup.findAll('h4', class_='MuiTypography-root MuiTypography-h4')[0].get_text()
            apy = soup.findAll('h4', class_='MuiTypography-root MuiTypography-h4')[1].get_text()
            mcap = soup.findAll('h4', class_='MuiTypography-root MuiTypography-h4')[2].get_text()
            tvl = soup.findAll('h4', class_='MuiTypography-root MuiTypography-h4')[4].get_text()
            treasury = soup.findAll('h4', class_='MuiTypography-root MuiTypography-h4')[5].get_text()
            
            
            driver.quit()
            


            print('Invictus - $IN', mcap, '\n', price, '\n', apy, '\n', treasury, '\n', tvl)

            total = {'mcap': mcap, 'price': price, 'tvl': tvl, 'apy': apy, 'treasury': treasury}
            

            with open("/home/admin/Desktop/data/invictus.json", "w") as f:
                json.dump(total, f, indent=2)

            subprocess.call(['python3', '/home/admin/Desktop/Script/invictus.py'])

            keyboard = [
                [
                    InlineKeyboardButton("Chart", url='https://nomics.com/assets/in3-invictus'),
                    InlineKeyboardButton("Dashboard", url='https://invictusdao.fi/#/dashboard')
                ]
            ]
             
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            print('Setting up data.')
            data = {
                    'photo': ('inv.png', open('/home/admin/Desktop/ss/inv.png', 'rb')),
                    'action': (None, 'send'),
                    'chat_id': (None, '-1001431327406'),
                    'caption': (None, f'\U0001F48E <b>Invictus - $IN</b> #Solana \U0001F48E \n\n\u231B <i><a href="discord.gg/invictusdao">Discord</a> - <a href="https://twitter.com/InvictusDAO">Twitter</a> - <a href="https://rebasetokens.app/f-a-q">FAQ</a></i> \u231B\n\n\U0001F4B5 <b>Market Cap:</b> {mcap}\n\U0001F4B0 <b>Price:</b> {price}\n\U0001F5D3 <b>APY:</b> {apy}\n\U0001F512 <b>TVL:</b> {tvl}\n\U0001F4AC <b>Treasury:</b> {treasury}\n\n\U0001F315 <a href="https://warp.bond/"><b>Warp.Bond</b></a> - The Next-Gen Web3 reserve currency ft. NFT Bonds & buildable starships that travel within the Staking #Metaverse\n@warpbond - <a href="https://discord.gg/warpbond">Discord</a> - <a href="https://twitter.com/warpbond">Twitter</a>\nJoin the <a href="https://warpcountdown.com/">Whitelist here!</a> \U0001F315'),
                    "reply_markup": (None, json.dumps(reply_markup.to_dict())),
                    "parse_mode": (None, 'HTML')
            }
        
            requests.post(url='https://api.telegram.org/bot5025889373:AAEGOUROw4deWROTzTR-1v1lDddv2EJFmSQ/sendPhoto', files=data)
            print('Data sent!')

            print('Shutting off Invictus..')
            s.enter(2, 1, fortress, (s,))
            
        except Exception as errore:

            print(errore)

            data = {"chat_id": "92637783",
                    "text": f'<b>Error</b> on Invictus Main Chat\n\n {errore}' ,
                    "parse_mode": 'HTML'}

            requests.post(url='https://api.telegram.org/bot5062720103:AAHo_qpQzG5dqRteZ-VgfBYL10_EFF1h6GU/sendMessage', data=data)

            s.enter(2, 1, fortress, (s,))


def fortress(sc):
        try:
            print('Starting Fortress..')
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://app.fortressdao.finance/#/dashboard"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            mcap = soup.findAll('h4', class_='MuiTypography-root MuiTypography-h4')[5].get_text()
            tvl = soup.findAll('h4', class_='MuiTypography-root MuiTypography-h4')[0].get_text()
            treasury = soup.findAll('h4', class_='MuiTypography-root MuiTypography-h4')[1].get_text()
            
            
            driver.quit()
            
            price = pri()

            print('Fortress - $FORT', mcap, '\n', price, '\n', treasury, '\n', tvl)

            total = {'mcap': mcap, 'price': price, 'tvl': tvl, 'treasury': treasury}

            subprocess.call(['python3', '/home/admin/Desktop/Script/fortress.py'])

            with open("/home/admin/Desktop/data/fortress.json", "w") as f:
                json.dump(total, f, indent=2)

            keyboard = [
                [
                    InlineKeyboardButton("Chart", url='https://dexscreener.com/avalanche/0x3e5f198b46f3de52761b02d4ac8ef4ceceac22d6'),
                    InlineKeyboardButton("Dashboard", url='https://app.fortressdao.finance/#/dashboard')
                ]
            ]
             
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            print('Setting up data.')
            data = {
                    'photo': ('fort.png', open('/home/admin/Desktop/ss/fort.png', 'rb')),
                    'action': (None, 'send'),
                    'chat_id': (None, '-1001431327406'),
                    'caption': (None, f'\U0001F48E <b>FortressDAO - $FORT</b> #AVAX \U0001F48E \n\n\u231B <i>@FortressDAO - <a href="https://discord.gg/jCEB9Wppb5">Discord</a> - <a href="https://twitter.com/FortressDAO">Twitter</a> - <a href="https://rebasetokens.app/f-a-q">FAQ</a></i> \u231B\n\n\U0001F4B5 <b>Market Cap:</b> {mcap}\n\U0001F4B0 <b>Price:</b> {price}\n\U0001F512 <b>TVL:</b> {tvl}\n\U0001F4AC <b>Treasury:</b> {treasury}\n\n\U0001F315 <a href="https://warp.bond/"><b>Warp.Bond</b></a> - The Next-Gen Web3 reserve currency ft. NFT Bonds & buildable starships that travel within the Staking #Metaverse\n@warpbond - <a href="https://discord.gg/warpbond">Discord</a> - <a href="https://twitter.com/warpbond">Twitter</a>\nJoin the <a href="https://warpcountdown.com/">Whitelist here!</a> \U0001F315'),
                    "reply_markup": (None, json.dumps(reply_markup.to_dict())),
                    "parse_mode": (None, 'HTML')
            }
        
            requests.post(url='https://api.telegram.org/bot5025889373:AAEGOUROw4deWROTzTR-1v1lDddv2EJFmSQ/sendPhoto', files=data)
            print('Data sent!')

            print('Shutting off FortressDAO..')
            s.enter(2, 1, exodia, (s,))
            
        except Exception as errore:

            print(errore)

            data = {"chat_id": "92637783",
                    "text": f'<b>Error</b> on Fortress Main Chat\n\n {errore}' ,
                    "parse_mode": 'HTML'}

            requests.post(url='https://api.telegram.org/bot5062720103:AAHo_qpQzG5dqRteZ-VgfBYL10_EFF1h6GU/sendMessage', data=data)

            s.enter(2, 1, exodia, (s,))


def pri():
        
            options = webdriver.FirefoxOptions()
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
            driver.maximize_window()
        
            urlone = "https://dexscreener.com/avalanche/0x2a91134162e2da1394df9e5e64608109d73ed3a0"
            driver.get(urlone)
            time.sleep(30)

            soup = BeautifulSoup(driver.page_source,'html.parser')
            price = soup.find_all('span', {'class' : 'chakra-text css-5sxn50', })[0].get_text()

            driver.quit()

            return price

def exodia(sc):
        try:
            print('Starting Exodia..')
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://app.exodia.fi/analytics"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            mcap = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[0].get_text()
            price = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[1].get_text()
            tvl = soup.findAll('h4', class_='MuiTypography-root MuiTypography-h4')[0].get_text()
            treasury = soup.findAll('h4', class_='MuiTypography-root MuiTypography-h4')[1].get_text()
            backing = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[4].get_text()
            runway = soup.findAll('h4', class_='MuiTypography-root MuiTypography-h4')[5].get_text()
            apy = soup.findAll('h4', class_='MuiTypography-root MuiTypography-h4')[8].get_text()
            
            
            driver.quit()

            print('Exodia - $EXOD', price,'\n', mcap,'\n', tvl,'\n', apy,'\n', treasury,'\n', backing)

            total = {'mcap': mcap, 'price': price, 'tvl': tvl, 'treasury': treasury, 'apy': apy, 'backing': backing}
            
            subprocess.call(['python3', '/home/admin/Desktop/Script/exodia.py'])

            with open("/home/admin/Desktop/data/exodia.json", "w") as f:
                json.dump(total, f, indent=2)
            
            keyboard = [
                [
                    InlineKeyboardButton("Chart", url='https://dexscreener.com/fantom/0xc0c1dff0fe24108586e11ec9e20a7cbb405cb769'),
                    InlineKeyboardButton("Dashboard", url='https://app.exodia.finance/#/dashboard')
                ]
            ]
             
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            print('Setting up data.')
            data = {
                    'photo': ('exod.png', open('/home/admin/Desktop/ss/exod.png', 'rb')),
                    'action': (None, 'send'),
                    'chat_id': (None, '-1001431327406'),
                    'caption': (None, f'\U0001F48E <b>ExodiaFinance - $EXOD</b> #FTM \U0001F48E \n\n\u231B <i><a href="https://discord.gg/XtCfmptvN6">Discord</a> - <a href="https://twitter.com/EXODIAFinance">Twitter</a> - <a href="https://rebasetokens.app/f-a-q">FAQ</a></i> \u231B\n\n\U0001F4B5 <b>Market Cap:</b> {mcap}\n\U0001F4B0 <b>Price:</b> {price}\n\U0001F5D3 <b>APY:</b> {apy}\n\U0001F512 <b>TVL:</b> {tvl}\n\U0001F4AC <b>Treasury:</b> {treasury}\n\U0001F4CC <b>Backing:</b> {backing}\n\n\U0001F315 <a href="https://warp.bond/"><b>Warp.Bond</b></a> - The Next-Gen Web3 reserve currency ft. NFT Bonds & buildable starships that travel within the Staking #Metaverse\n@warpbond - <a href="https://discord.gg/warpbond">Discord</a> - <a href="https://twitter.com/warpbond">Twitter</a>\nJoin the <a href="https://warpcountdown.com/">Whitelist here!</a> \U0001F315'),
                    "reply_markup": (None, json.dumps(reply_markup.to_dict())),
                    "parse_mode": (None, 'HTML')
            }
        
            requests.post(url='https://api.telegram.org/bot5025889373:AAEGOUROw4deWROTzTR-1v1lDddv2EJFmSQ/sendPhoto', files=data)
            print('Data sent!')

            print('Shutting off Exodia..')
            s.enter(2, 1, dios, (s,))
            
        except Exception as errore:

            print(errore)

            data = {"chat_id": "92637783",
                    "text": f'<b>Error</b> on Exodia Main Chat\n\n {errore}' ,
                    "parse_mode": 'HTML'}

            requests.post(url='https://api.telegram.org/bot5062720103:AAHo_qpQzG5dqRteZ-VgfBYL10_EFF1h6GU/sendMessage', data=data)

            s.enter(2, 1, dios, (s,))


def dios(sc):
        try:
            print('Starting Dios Finance..')
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://app.dios.finance/#/dashboard"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            price = soup.findAll('div', class_='number')[1].get_text()
            apy = soup.findAll('div', class_='number')[7].get_text()
            mcap = soup.findAll('div', class_='number')[0].get_text()
            tvl = soup.findAll('div', class_='number')[6].get_text()
            treasury = soup.findAll('div', class_='number')[5].get_text()
            backing = soup.findAll('div', class_='number')[3].get_text()
            
            
            driver.quit()
            print('DiosFinance - $DIOS', price,'\n', mcap,'\n', tvl,'\n', apy,'\n', treasury,'\n', backing)

            total = {'mcap': mcap, 'price': price, 'tvl': tvl, 'apy': apy, 'treasury': treasury, 'backing': backing}
            

            with open("/home/admin/Desktop/data/dios.json", "w") as f:
                json.dump(total, f, indent=2)

            subprocess.call(['python3', '/home/admin/Desktop/Script/dios.py'])

            keyboard = [
                [
                    InlineKeyboardButton("Chart", url='https://dexscreener.com/bsc/0x2d7a5e9d85f62adbaea9d48b11f5947f3ac57fc8'),
                    InlineKeyboardButton("Dashboard", url='https://app.dios.finance/#/dashboard')
                ]
            ]
             
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            print('Setting up data.')
            data = {
                    'photo': ('dios.png', open('/home/admin/Desktop/ss/dios.png', 'rb')),
                    'action': (None, 'send'),
                    'chat_id': (None, '-1001431327406'),
                    'caption': (None, f'\U0001F48E <b>DiosFinance - $DIOS</b> #BSC \U0001F48E \n\n\u231B <i>@dios_community - <a href="https://discord.gg/YvESZFAdjJ">Discord</a> - <a href="https://twitter.com/DiosFinance">Twitter</a> - <a href="https://rebasetokens.app/f-a-q">FAQ</a></i> \u231B\n\n\U0001F4B5 <b>Market Cap:</b> {mcap}\n\U0001F4B0 <b>Price:</b> {price}\n\U0001F5D3 <b>APY:</b> {apy}\n\U0001F512 <b>TVL:</b> {tvl}\n\U0001F4AC <b>Treasury:</b> {treasury}\n\U0001F4CC <b>Backing:</b> {backing}\n\n\U0001F315 <a href="https://warp.bond/"><b>Warp.Bond</b></a> - The Next-Gen Web3 reserve currency ft. NFT Bonds & buildable starships that travel within the Staking #Metaverse\n@warpbond - <a href="https://discord.gg/warpbond">Discord</a> - <a href="https://twitter.com/warpbond">Twitter</a>\nJoin the <a href="https://warpcountdown.com/">Whitelist here!</a> \U0001F315'),
                    "reply_markup": (None, json.dumps(reply_markup.to_dict())),
                    "parse_mode": (None, 'HTML')
            }
        
            requests.post(url='https://api.telegram.org/bot5025889373:AAEGOUROw4deWROTzTR-1v1lDddv2EJFmSQ/sendPhoto', files=data)
            print('Data sent!')

            print('Shutting off Dios..')
            s.enter(2, 1, guru, (s,))
            
        except Exception as errore:

            print(errore)

            data = {"chat_id": "92637783",
                    "text": f'<b>Error</b> on DiosFinance Main Chat\n\n {errore}' ,
                    "parse_mode": 'HTML'}

            requests.post(url='https://api.telegram.org/bot5062720103:AAHo_qpQzG5dqRteZ-VgfBYL10_EFF1h6GU/sendMessage', data=data)

            s.enter(2, 1, guru, (s,))



def guru(sc):
        try:
            print('Starting NidhiDAO..')
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://app.nidhidao.finance/#/dashboard"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            mcap = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[0].get_text()
            price = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[1].get_text()
            treasury = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[4].get_text()
            backing = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[3].get_text()

            driver.quit()

            results = guruvalue()
            apy = results[0]
            tvl = results[1]

            print('NidhiDAO - $GURU', price,'\n', mcap,'\n', tvl,'\n', apy,'\n', treasury,'\n', backing)

            total = {'mcap': mcap, 'price': price, 'tvl':tvl, 'apy':apy, 'treasury':treasury, 'backing':backing}
            

            with open("/home/admin/Desktop/data/guru.json", "w") as f:
                json.dump(total, f, indent=2)

            subprocess.call(['python3', '/home/admin/Desktop/Script/guru.py'])

            keyboard = [
                [
                    InlineKeyboardButton("Chart", url='https://dexscreener.com/polygon/0x7c9b16d845fe163f464d265193cc2b4ee3fac326'),
                    InlineKeyboardButton("Dashboard", url='https://app.nidhidao.finance/#/dashboard')
                ]
            ]
             
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            print('Setting up data.')
            data = {
                    'photo': ('guru.png', open('/home/admin/Desktop/ss/guru.png', 'rb')),
                    'action': (None, 'send'),
                    'chat_id': (None, '-1001431327406'),
                    'caption': (None, f'\U0001F48E <b>NidhiDAO - $GURU</b> #Polygon \U0001F48E \n\n\u231B <i><a href="https://discord.gg/mjXGMShDcX">Discord</a> - <a href="https://twitter.com/NidhiDAO">Twitter</a> - <a href="https://rebasetokens.app/f-a-q">FAQ</a></i> \u231B\n\n\U0001F4B5 <b>Market Cap:</b> {mcap}\n\U0001F4B0 <b>Price:</b> {price}\n\U0001F5D3 <b>APY:</b> {apy}\n\U0001F512 <b>TVL:</b> {tvl}\n\U0001F4AC <b>Treasury:</b> {treasury}\n\U0001F4CC <b>Backing:</b> {backing}\n\n\U0001F315 <a href="https://warp.bond/"><b>Warp.Bond</b></a> - The Next-Gen Web3 reserve currency ft. NFT Bonds & buildable starships that travel within the Staking #Metaverse\n@warpbond - <a href="https://discord.gg/warpbond">Discord</a> - <a href="https://twitter.com/warpbond">Twitter</a>\nJoin the <a href="https://warpcountdown.com/">Whitelist here!</a> \U0001F315'),
                    "reply_markup": (None, json.dumps(reply_markup.to_dict())),
                    "parse_mode": (None, 'HTML')
            }
        
            requests.post(url='https://api.telegram.org/bot5025889373:AAEGOUROw4deWROTzTR-1v1lDddv2EJFmSQ/sendPhoto', files=data)
            print('Data sent!')

            print('Shutting off NidhiDAO..')
            s.enter(2, 1, manifest, (s,))
            
        except Exception as errore:

            print(errore)

            data = {"chat_id": "92637783",
                    "text": f'<b>Error</b> on NidhiDAO Main Chat\n\n {errore}' ,
                    "parse_mode": 'HTML'}

            requests.post(url='https://api.telegram.org/bot5062720103:AAHo_qpQzG5dqRteZ-VgfBYL10_EFF1h6GU/sendMessage', data=data)

            s.enter(2, 1, manifest, (s,))


def guruvalue():

            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://app.nidhidao.finance/#/stake"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            apy = soup.findAll('h4', class_='MuiTypography-root MuiTypography-h4')[0].get_text()
            tvl = soup.findAll('h4', class_='MuiTypography-root MuiTypography-h4')[1].get_text()

            
            driver.quit()
            
            return apy, tvl




def manifest(sc):
        try:
            print('Starting Manifest..')
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://app.manifest.gg/#/stake"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            apy = soup.findAll('h4', class_='MuiTypography-root MuiTypography-h4')[0].get_text()
            tvl = soup.findAll('h4', class_='MuiTypography-root MuiTypography-h4')[1].get_text()

            driver.quit()
            
            results = mnfst()
            price = results[1]
            treasury = results[0]
            
            
            print('Manifest - $MNFST', price,'\n', tvl,'\n', apy,'\n', treasury)

            total = {'price': price, 'tvl': tvl, 'apy': apy, 'treasury': treasury}
            

            with open("/home/admin/Desktop/data/manifest.json", "w") as f:
                json.dump(total, f, indent=2)

            subprocess.call(['python3', '/home/admin/Desktop/Script/manifest.py'])

            keyboard = [
                [
                    InlineKeyboardButton("Chart", url='https://dexscreener.com/ethereum/0x89c4d11dfd5868d847ca26c8b1caa9c25c712cef'),
                    InlineKeyboardButton("Dashboard", url='https://app.manifest.gg/#/stake')
                ]
            ]
             
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            print('Setting up data.')
            data = {
                    'photo': ('manifest.png', open('/home/admin/Desktop/ss/manifest.png', 'rb')),
                    'action': (None, 'send'),
                    'chat_id': (None, '-1001431327406'),
                    'caption': (None, f'\U0001F48E <b>Manifest - $MNFST</b> #ETH \U0001F48E \n\n\u231B <i><a href="https://discord.gg/8UbwuybGrv">Discord</a> - <a href="https://twitter.com/manifest">Twitter</a> - <a href="https://rebasetokens.app/f-a-q">FAQ</a></i> \u231B\n\n\U0001F4B0 <b>Price:</b> {price}\n\U0001F5D3 <b>APY:</b> {apy}\n\U0001F512 <b>TVL:</b> {tvl}\n\U0001F4AC <b>Treasury:</b> {treasury}\n\n\U0001F315 <a href="https://warp.bond/"><b>Warp.Bond</b></a> - The Next-Gen Web3 reserve currency ft. NFT Bonds & buildable starships that travel within the Staking #Metaverse\n@warpbond - <a href="https://discord.gg/warpbond">Discord</a> - <a href="https://twitter.com/warpbond">Twitter</a>\nJoin the <a href="https://warpcountdown.com/">Whitelist here!</a> \U0001F315'),
                    "reply_markup": (None, json.dumps(reply_markup.to_dict())),
                    "parse_mode": (None, 'HTML')
            }
        
            requests.post(url='https://api.telegram.org/bot5025889373:AAEGOUROw4deWROTzTR-1v1lDddv2EJFmSQ/sendPhoto', files=data)
            print('Data sent!')

            print('Shutting off Manifest..')
            s.enter(2, 1, umami, (s,))
            
        except Exception as errore:

            print(errore)

            data = {"chat_id": "92637783",
                    "text": f'<b>Error</b> on Manifest Main Chat\n\n {errore}' ,
                    "parse_mode": 'HTML'}

            requests.post(url='https://api.telegram.org/bot5062720103:AAHo_qpQzG5dqRteZ-VgfBYL10_EFF1h6GU/sendMessage', data=data)

            s.enter(2, 1, umami, (s,))


def mnfst():

            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://app.manifest.gg/#/bonds"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            
            treasury = soup.findAll('h4', class_='MuiTypography-root MuiTypography-h4')[0].get_text()
            price = soup.findAll('h4', class_='MuiTypography-root MuiTypography-h4')[1].get_text()
            
         
            driver.quit()

            return treasury, price



def umami(sc):
        try:
            print('Starting Umami..')
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://app.umami.finance/#/dashboard"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            price = soup.findAll('p', class_='card-value')[0].get_text()
            mcap = soup.findAll('p', class_='card-value')[1].get_text()
            apy = soup.findAll('p', class_='card-value')[3].get_text()
            treasury = soup.findAll('p', class_='card-value')[5].get_text()
            backing = soup.findAll('p', class_='card-value')[6].get_text()
            runway = soup.findAll('p', class_='card-value')[7].get_text()
            tvl = soup.findAll('p', class_='card-value')[2].get_text()

            
            driver.quit()
            print('Umami', price,'\n', mcap,'\n', tvl,'\n', apy,'\n', treasury,'\n', backing, '\n', runway)

            total = {'mcap': mcap, 'price': price, 'tvl': tvl, 'apy': apy, 'treasury': treasury, 'backing': backing, 'runway': runway}
            

            with open("/home/admin/Desktop/data/umami.json", "w") as f:
                json.dump(total, f, indent=2)

            subprocess.call(['python3', '/home/admin/Desktop/Script/umami.py'])

            keyboard = [
                [
                    InlineKeyboardButton("Chart", url='https://dexscreener.com/arbitrum/0xce502ee9bf3ef41508a8a4a38fcf02585fcbfdf0'),
                    InlineKeyboardButton("Dashboard", url='https://app.umami.finance/#/dashboard')
                ]
            ]
             
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            print('Setting up data.')
            data = {
                    'photo': ('umami.png', open('/home/admin/Desktop/ss/umami.png', 'rb')),
                    'action': (None, 'send'),
                    'chat_id': (None, '-1001431327406'),
                    'caption': (None, f'\U0001F48E <b>Umami - $UMAMI</b> #Arbitrum \U0001F48E \n\n\u231B <i><a href="discord.gg/arbis">Discord</a> - <a href="https://twitter.com/UmamiFinance">Twitter</a> - <a href="https://rebasetokens.app/f-a-q">FAQ</a></i> \u231B\n\n\U0001F4B5 <b>Market Cap:</b> {mcap}\n\U0001F4B0 <b>Price:</b> {price}\n\U0001F5D3 <b>APY:</b> {apy}\n\U0001F512 <b>TVL:</b> {tvl}\n\U0001F4AC <b>Treasury:</b> {treasury}\n\U0001F4CC <b>Backing:</b> {backing}\n\u23F0 <b>Runway:</b> {runway}\n\n\U0001F315 <a href="https://warp.bond/"><b>Warp.Bond</b></a> - The Next-Gen Web3 reserve currency ft. NFT Bonds & buildable starships that travel within the Staking #Metaverse\n@warpbond - <a href="https://discord.gg/warpbond">Discord</a> - <a href="https://twitter.com/warpbond">Twitter</a>\nJoin the <a href="https://warpcountdown.com/">Whitelist here!</a> \U0001F315'),
                    "reply_markup": (None, json.dumps(reply_markup.to_dict())),
                    "parse_mode": (None, 'HTML')
            }
        
            requests.post(url='https://api.telegram.org/bot5025889373:AAEGOUROw4deWROTzTR-1v1lDddv2EJFmSQ/sendPhoto', files=data)
            print('Data sent!')

            print('Shutting off Umami..')
            s.enter(2, 1, rome, (s,))
            
        except Exception as errore:

            print(errore)

            data = {"chat_id": "92637783",
                    "text": f'<b>Error</b> on Umami Main Chat\n\n {errore}' ,
                    "parse_mode": 'HTML'}

            requests.post(url='https://api.telegram.org/bot5062720103:AAHo_qpQzG5dqRteZ-VgfBYL10_EFF1h6GU/sendMessage', data=data)

            s.enter(2, 1, rome, (s,))



def rome(sc):
        try:
            print('Starting Rome..')
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://romedao.finance/bond"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            treasury = soup.findAll('div', class_='mt-1 text-xl font-medium 2xl:text-3xl text-dark-600')[0].get_text()
            price = soup.findAll('div', class_='mt-1 text-xl font-medium 2xl:text-3xl text-dark-600')[1].get_text()
            
            
            driver.quit()

            results = romevalue()
            apy = results[0]
            tvl = results[1]
            
            print('RomeDAO - $ROME', price,'\n', tvl, '\n', treasury, '\n', apy)

            total = {'price': price, 'tvl': tvl, 'apy': apy, 'treasury': treasury}
            

            with open("/home/admin/Desktop/data/rome.json", "w") as f:
                json.dump(total, f, indent=2)

            subprocess.call(['python3', '/home/admin/Desktop/Script/rome.py'])

            keyboard = [
                [
                    InlineKeyboardButton("Chart", url='https://dexscreener.com/moonriver/0x069c2065100b4d3d982383f7ef3ecd1b95c05894'),
                    InlineKeyboardButton("Dashboard", url='https://romedao.finance/')
                ]
            ]
             
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            print('Setting up data.')
            data = {
                    'photo': ('rome.png', open('/home/admin/Desktop/ss/rome.png', 'rb')),
                    'action': (None, 'send'),
                    'chat_id': (None, '-1001431327406'),
                    'caption': (None, f'\U0001F48E <b>RomeDAO - $ROME</b> \U0001F48E \n\n\u231B <i><a href="http://discord.gg/romedao">Discord</a> - <a href="https://twitter.com/romedaofinance">Twitter</a> - <a href="https://rebasetokens.app/f-a-q">FAQ</a></i> \u231B\n\n\U0001F4B0 <b>Price:</b> {price}\n\U0001F5D3 <b>APY:</b> {apy}\n\U0001F512 <b>ROME Staked:</b> {tvl}\n\U0001F4AC <b>Total Value Bonded:</b> {treasury}\n\n\U0001F315 <a href="https://warp.bond/"><b>Warp.Bond</b></a> - The Next-Gen Web3 reserve currency ft. NFT Bonds & buildable starships that travel within the Staking #Metaverse\n@warpbond - <a href="https://discord.gg/warpbond">Discord</a> - <a href="https://twitter.com/warpbond">Twitter</a>\nJoin the <a href="https://warpcountdown.com/">Whitelist here!</a> \U0001F315'),
                    "reply_markup": (None, json.dumps(reply_markup.to_dict())),
                    "parse_mode": (None, 'HTML')
            }
        
            requests.post(url='https://api.telegram.org/bot5025889373:AAEGOUROw4deWROTzTR-1v1lDddv2EJFmSQ/sendPhoto', files=data)
            print('Data sent!')

            print('Shutting off RomeDAO..')
            s.enter(2, 1, squid, (s,))
            
        except Exception as errore:

            print(errore)

            data = {"chat_id": "92637783",
                    "text": f'<b>Error</b> on RomeDAO Main Chat\n\n {errore}' ,
                    "parse_mode": 'HTML'}

            requests.post(url='https://api.telegram.org/bot5062720103:AAHo_qpQzG5dqRteZ-VgfBYL10_EFF1h6GU/sendMessage', data=data)

            s.enter(2, 1, squid, (s,))


def romevalue():

            print('Starting Rome APY..')
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://romedao.finance/stake"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            apy = soup.findAll('div', class_='mt-1 text-xl font-medium 2xl:text-3xl text-dark-600')[0].get_text()
            tvl = soup.findAll('div', class_='mt-1 text-xl font-medium 2xl:text-3xl text-dark-600')[1].get_text()
            
            
            driver.quit()
            return apy, tvl


def squid(sc):
        try:
            print('Starting SquidDAO..')
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://squid.xyz/#/dashboard"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            mcap = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[1].get_text()
            tvl = soup.findAll('h4', class_='MuiTypography-root MuiTypography-h4')[0].get_text()
            treasury = soup.findAll('h4', class_='MuiTypography-root MuiTypography-h4')[1].get_text()
            backing = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[3].get_text()
            runway = soup.findAll('h4', class_='MuiTypography-root MuiTypography-h4')[6].get_text()

            apy = squidvalue()
            
            
            driver.quit()

            
            print('SquidDAO - $SQUID', mcap,'\n', tvl,'\n', apy,'\n', treasury,'\n', backing, '\n', runway)

            total = {'mcap': mcap, 'tvl': tvl, 'apy': apy, 'treasury': treasury, 'backing': backing, 'runway': runway}
            

            with open("/home/admin/Desktop/data/squid.json", "w") as f:
                json.dump(total, f, indent=2)

            subprocess.call(['python3', '/home/admin/Desktop/Script/squid.py'])

            keyboard = [
                [
                    InlineKeyboardButton("Chart", url='https://dexscreener.com/ethereum/0xfad704847967d9067df7a60910399155fca43fe8'),
                    InlineKeyboardButton("Dashboard", url='https://squid.xyz/#/dashboard')
                ]
            ]
             
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            print('Setting up data.')
            data = {
                    'photo': ('squid.png', open('/home/admin/Desktop/ss/squid.png', 'rb')),
                    'action': (None, 'send'),
                    'chat_id': (None, '-1001431327406'),
                    'caption': (None, f'\U0001F48E <b>SquidDAO - $SQUID</b> #ETH \U0001F48E \n\n\u231B <i><a href="discord.gg/squid-dao">Discord</a> - <a href="https://twitter.com/SquidDao">Twitter</a> - <a href="https://rebasetokens.app/f-a-q">FAQ</a></i> \u231B\n\n\U0001F4B5 <b>Market Cap:</b> {mcap}\n\U0001F5D3 <b>APY:</b> {apy}\n\U0001F512 <b>TVL:</b> {tvl}\n\U0001F4AC <b>Treasury:</b> {treasury}\n\U0001F4CC <b>Backing:</b> {backing}\n\u23F0 <b>Runway:</b> {runway}\n\n\U0001F315 <a href="https://warp.bond/"><b>Warp.Bond</b></a> - The Next-Gen Web3 reserve currency ft. NFT Bonds & buildable starships that travel within the Staking #Metaverse\n@warpbond - <a href="https://discord.gg/warpbond">Discord</a> - <a href="https://twitter.com/warpbond">Twitter</a>\nJoin the <a href="https://warpcountdown.com/">Whitelist here!</a> \U0001F315'),
                    "reply_markup": (None, json.dumps(reply_markup.to_dict())),
                    "parse_mode": (None, 'HTML')
            }
        
            requests.post(url='https://api.telegram.org/bot5025889373:AAEGOUROw4deWROTzTR-1v1lDddv2EJFmSQ/sendPhoto', files=data)
            print('Data sent!')

            print('Shutting off SquidDAO..')
            s.enter(2, 1, nms, (s,))
            
        except Exception as errore:

            print(errore)

            data = {"chat_id": "92637783",
                    "text": f'<b>Error</b> on Squid Main Chat\n\n {errore}' ,
                    "parse_mode": 'HTML'}

            requests.post(url='https://api.telegram.org/bot5062720103:AAHo_qpQzG5dqRteZ-VgfBYL10_EFF1h6GU/sendMessage', data=data)

            s.enter(2, 1, nms, (s,))
            

def squidvalue():

            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://squid.xyz/#/stake"
            driver.get(urlone)
            time.sleep(30)
            
            soup = BeautifulSoup(driver.page_source,'html.parser')
            apy = soup.findAll('h4', class_='MuiTypography-root MuiTypography-h4')[0].get_text()

            driver.quit()
            

            return apy


def nms(sc):
        try:
            print('Starting NemesisDAO..')
            options = webdriver.FirefoxOptions()
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://dexscreener.com/bsc/0x6b0a3e71b69ab49ddea0ed23bef48f78bf9509aa"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            price = soup.find_all('span', {'class' : 'chakra-text css-5sxn50', })[0].get_text()
            liq = soup.find_all('span', {'class' : 'chakra-text css-5sxn50', })[2].get_text()                        
            mcap = soup.find_all('span', {'class' : 'chakra-text css-5sxn50', })[4].get_text()
            vol = soup.find_all('span', {'class' : 'chakra-text css-5sxn50', })[20].get_text()
            
            
            driver.quit()
            print('NemesisDAO - $NMS', price,'\n', mcap,'\n', vol, '\n', liq)

            total = {'mcap': mcap, 'price': price, 'vol': vol, 'liquidity': liq}
            

            with open("/home/admin/Desktop/data/nms.json", "w") as f:
                json.dump(total, f, indent=2)

            subprocess.call(['python3', '/home/admin/Desktop/Script/nms.py'])

            keyboard = [
                [
                    InlineKeyboardButton("Chart", url='https://dexscreener.com/bsc/0x6b0a3e71b69ab49ddea0ed23bef48f78bf9509aa'),
                    InlineKeyboardButton("Dashboard", url='https://rising.nemesisdao.finance/')
                ]
            ]
             
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            print('Setting up data.')
            data = {
                    'photo': ('nms.png', open('/home/admin/Desktop/ss/nms.png', 'rb')),
                    'action': (None, 'send'),
                    'chat_id': (None, '-1001431327406'),
                    'caption': (None, f'\U0001F48E <b>NemesisDAO - $NMS</b> #BSC \U0001F48E \n\n\u231B <i>@nemesisdao - <a href="https://discord.gg/b8CUaukZn6">Discord</a> - <a href="https://twitter.com/nemesis_dao">Twitter</a> - <a href="https://rebasetokens.app/f-a-q">FAQ</a></i> \u231B\n\n\U0001F4B5 <b>Market Cap:</b> {mcap}\n\U0001F4B0 <b>Price:</b> {price}\n\U0001F5D3 <b>24h Volume:</b> {vol}\n\n\U0001F315 <a href="https://warp.bond/"><b>Warp.Bond</b></a> - The Next-Gen Web3 reserve currency ft. NFT Bonds & buildable starships that travel within the Staking #Metaverse\n@warpbond - <a href="https://discord.gg/warpbond">Discord</a> - <a href="https://twitter.com/warpbond">Twitter</a>\nJoin the <a href="https://warpcountdown.com/">Whitelist here!</a> \U0001F315'),
                    "reply_markup": (None, json.dumps(reply_markup.to_dict())),
                    "parse_mode": (None, 'HTML')
            }
        
            requests.post(url='https://api.telegram.org/bot5025889373:AAEGOUROw4deWROTzTR-1v1lDddv2EJFmSQ/sendPhoto', files=data)
            print('Data sent!')

            print('Shutting off NemesisDAO..')
            s.enter(2, 1, lobis, (s,))
            
        except Exception as errore:

            print(errore)

            data = {"chat_id": "92637783",
                    "text": f'<b>Error</b> on NemesisDAO Main Chat\n\n {errore}' ,
                    "parse_mode": 'HTML'}

            requests.post(url='https://api.telegram.org/bot5062720103:AAHo_qpQzG5dqRteZ-VgfBYL10_EFF1h6GU/sendMessage', data=data)

            s.enter(2, 1, lobis, (s,))


def lobis(sc):
        try:
            print('Starting Lobis..')
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://app.lobis.finance/#/dashboard"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            price = soup.findAll('p', class_='card-value')[0].get_text()
            apy = soup.findAll('p', class_='card-value')[3].get_text()
            mcap = soup.findAll('p', class_='card-value')[1].get_text()
            tvl = soup.findAll('p', class_='card-value')[2].get_text()
            treasury = soup.findAll('td', class_='MuiTableCell-root MuiTableCell-footer treasury-balance-view-card-table-title-footer MuiTableCell-alignCenter')[4].get_text()
            runway = soup.findAll('p', class_='card-value')[5].get_text()
            
            
            driver.quit()
            print('Lobis - $LOBI', price,'\n', mcap,'\n', tvl,'\n', apy,'\n', treasury, '\n', runway)

            total = {'mcap': mcap, 'price': price, 'tvl': tvl, 'apy': apy, 'treasury': treasury, 'runway': runway}
            

            with open("/home/admin/Desktop/data/lobis.json", "w") as f:
                json.dump(total, f, indent=2)

            subprocess.call(['python3', '/home/admin/Desktop/Script/lobis.py'])
            
            keyboard = [
                [
                    InlineKeyboardButton("Chart", url='https://dexscreener.com/ethereum/0x193008eaade86658df8237a436261e23e3bcbbaa'),
                    InlineKeyboardButton("Dashboard", url='https://app.lobis.finance/#/dashboard')
                ]
            ]
             
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            print('Setting up data.')
            data = {
                    'photo': ('lobis.png', open('/home/admin/Desktop/ss/lobis.png', 'rb')),
                    'action': (None, 'send'),
                    'chat_id': (None, '-1001431327406'),
                    'caption': (None, f'\U0001F48E <b>Lobis - $LOBI</b> #ETH \U0001F48E \n\n\u231B <i><a href="https://discord.gg/lobishq">Discord</a> - <a href="https://twitter.com/LobisHQ">Twitter</a> - <a href="https://rebasetokens.app/f-a-q">FAQ</a></i> \u231B\n\n\U0001F4B5 <b>Market Cap:</b> {mcap}\n\U0001F4B0 <b>Price:</b> {price}\n\U0001F5D3 <b>APY:</b> {apy}\n\U0001F512 <b>TVL:</b> {tvl}\n\U0001F4AC <b>Treasury:</b> {treasury}\n\u23F0 <b>Runway:</b> {runway}\n\n\U0001F315 <a href="https://warp.bond/"><b>Warp.Bond</b></a> - The Next-Gen Web3 reserve currency ft. NFT Bonds & buildable starships that travel within the Staking #Metaverse\n@warpbond - <a href="https://discord.gg/warpbond">Discord</a> - <a href="https://twitter.com/warpbond">Twitter</a>\nJoin the <a href="https://warpcountdown.com/">Whitelist here!</a> \U0001F315'),
                    "reply_markup": (None, json.dumps(reply_markup.to_dict())),
                    "parse_mode": (None, 'HTML')
            }
        
            requests.post(url='https://api.telegram.org/bot5025889373:AAEGOUROw4deWROTzTR-1v1lDddv2EJFmSQ/sendPhoto', files=data)
            print('Data sent!')

            print('Shutting off Lobis..')
            s.enter(2, 1, midas, (s,))
            
        except Exception as errore:

            print(errore)

            data = {"chat_id": "92637783",
                    "text": f'<b>Error</b> on Lobis Main Chat\n\n {errore}' ,
                    "parse_mode": 'HTML'}

            requests.post(url='https://api.telegram.org/bot5062720103:AAHo_qpQzG5dqRteZ-VgfBYL10_EFF1h6GU/sendMessage', data=data)

            s.enter(2, 1, midas, (s,))



def midas(sc):
        try:
            print('Starting Midas..')
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://app.midasdao.org/#/dashboard"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            price = soup.findAll('p', class_='card-value')[0].get_text()
            apy = soup.findAll('p', class_='sc-value')[1].get_text()
            mcap = soup.findAll('p', class_='sc-value')[0].get_text()
            tvl = soup.findAll('p', class_='card-value')[1].get_text()
            treasury = soup.findAll('p', class_='card-value')[2].get_text()
            backing = soup.findAll('p', class_='sc-value')[3].get_text()
            runway = soup.findAll('p', class_='sc-value')[4].get_text()
            
            
            driver.quit()
            print('Midas - $CROWN', price,'\n', mcap,'\n', tvl,'\n', apy,'\n', treasury,'\n', backing, '\n', runway)
            
            total = {'mcap': mcap, 'price': price, 'tvl': tvl, 'apy': apy, 'treasury': treasury, 'backing': backing, 'runway': runway}
            

            with open("/home/admin/Desktop/data/midas.json", "w") as f:
                json.dump(total, f, indent=2)

            subprocess.call(['python3', '/home/admin/Desktop/Script/midas.py'])

            keyboard = [
                [
                    InlineKeyboardButton("Chart", url='https://dexscreener.com/avalanche/0x3f0de4ec592e4376aa6925c3b3dc33d5ffbcdcc3'),
                    InlineKeyboardButton("Dashboard", url='https://app.midasdao.org/#/dashboard')
                ]
            ]
             
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            print('Setting up data.')
            data = {
                    'photo': ('midas.png', open('/home/admin/Desktop/ss/midas.png', 'rb')),
                    'action': (None, 'send'),
                    'chat_id': (None, '-1001431327406'),
                    'caption': (None, f'\U0001F48E <b>MidasDAO - $CROWN</b> #AVAX \U0001F48E \n\n\u231B <i><a href="http://discord.gg/midasdao">Discord</a> - <a href="https://twitter.com/Midas_DAO">Twitter</a> - <a href="https://rebasetokens.app/f-a-q">FAQ</a></i> \u231B\n\n\U0001F4B5 <b>Market Cap:</b> {mcap}\n\U0001F4B0 <b>Price:</b> {price}\n\U0001F5D3 <b>APY:</b> {apy}\n\U0001F512 <b>TVL:</b> {tvl}\n\U0001F4AC <b>Treasury:</b> {treasury}\n\U0001F4CC <b>Backing:</b> {backing}\n\u23F0 <b>Runway:</b> {runway}\n\n\U0001F315 <a href="https://warp.bond/"><b>Warp.Bond</b></a> - The Next-Gen Web3 reserve currency ft. NFT Bonds & buildable starships that travel within the Staking #Metaverse\n@warpbond - <a href="https://discord.gg/warpbond">Discord</a> - <a href="https://twitter.com/warpbond">Twitter</a>\nJoin the <a href="https://warpcountdown.com/">Whitelist here!</a> \U0001F315'),
                    "reply_markup": (None, json.dumps(reply_markup.to_dict())),
                    "parse_mode": (None, 'HTML')
            }
        
            requests.post(url='https://api.telegram.org/bot5025889373:AAEGOUROw4deWROTzTR-1v1lDddv2EJFmSQ/sendPhoto', files=data)
            print('Data sent!')

            print('Shutting off Midas..')
            s.enter(2, 1, pi, (s,))
            
        except Exception as errore:

            print(errore)

            data = {"chat_id": "92637783",
                    "text": f'<b>Error</b> on Midas Main Chat\n\n {errore}' ,
                    "parse_mode": 'HTML'}

            requests.post(url='https://api.telegram.org/bot5062720103:AAHo_qpQzG5dqRteZ-VgfBYL10_EFF1h6GU/sendMessage', data=data)

            s.enter(2, 1, pi, (s,))


        
def pi(sc):
        try:
            print('Starting Pi..')
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://dexscreener.com/bsc/0x3991e0988a69e4c8fde46c011dafe55e26fdd18d"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            price = soup.find_all('span', {'class' : 'chakra-text css-5sxn50', })[0].get_text()
            liq = soup.find_all('span', {'class' : 'chakra-text css-5sxn50', })[2].get_text()                        
            mcap = soup.find_all('span', {'class' : 'chakra-text css-5sxn50', })[4].get_text()
            vol = soup.find_all('span', {'class' : 'chakra-text css-5sxn50', })[20].get_text()
            
            
            driver.quit()
            print('Pi - $PID', price,'\n', mcap, '\n', liq, '\n', vol)

            total = {'mcap': mcap, 'price': price, 'liquidity': liq, 'vol': vol}
            

            with open("/home/admin/Desktop/data/pi.json", "w") as f:
                json.dump(total, f, indent=2)
            
            keyboard = [
                [
                    InlineKeyboardButton("Chart", url='https://dexscreener.com/bsc/0x3991e0988a69e4c8fde46c011dafe55e26fdd18d'),
                    InlineKeyboardButton("Dashboard", url='https://www.pidao.finance/dashboard')
                ]
            ]
             
            reply_markup = InlineKeyboardMarkup(keyboard)

            subprocess.call(['python3', '/home/admin/Desktop/Script/pidao.py'])
            
            print('Setting up data.')
            data = {
                    'photo': ('pi.png', open('/home/admin/Desktop/ss/pi.png', 'rb')),
                    'action': (None, 'send'),
                    'chat_id': (None, '-1001431327406'),
                    'caption': (None, f'\U0001F48E <b>Pi - $PID</b> #BSC \U0001F48E \n\n\u231B <i>@PIDAOfinance - <a href="https://discord.gg/YCC7hKkFHr">Discord</a> - <a href="https://twitter.com/PIDAOFinance">Twitter</a> - <a href="https://rebasetokens.app/f-a-q">FAQ</a></i> \u231B\n\n\U0001F4B5 <b>Market Cap:</b> {mcap}\n\U0001F4B0 <b>Price:</b> {price}\n\U0001F5D3 <b>24h Volume:</b> {vol}\n\U0001F512 <b>Liquidity:</b> {liq}\n\n\U0001F315 <a href="https://warp.bond/"><b>Warp.Bond</b></a> - The Next-Gen Web3 reserve currency ft. NFT Bonds & buildable starships that travel within the Staking #Metaverse\n@warpbond - <a href="https://discord.gg/warpbond">Discord</a> - <a href="https://twitter.com/warpbond">Twitter</a>\nJoin the <a href="https://warpcountdown.com/">Whitelist here!</a> \U0001F315'),
                    "reply_markup": (None, json.dumps(reply_markup.to_dict())),
                    "parse_mode": (None, 'HTML')
            }
        
            requests.post(url='https://api.telegram.org/bot5025889373:AAEGOUROw4deWROTzTR-1v1lDddv2EJFmSQ/sendPhoto', files=data)
            print('Data sent!')

            print('Shutting off Pi..')
            s.enter(2, 1, fortune, (s,))
            
        except Exception as errore:

            print(errore)

            data = {"chat_id": "92637783",
                    "text": f'<b>Error</b> on PiDAO Main Chat\n\n {errore}' ,
                    "parse_mode": 'HTML'}

            requests.post(url='https://api.telegram.org/bot5062720103:AAHo_qpQzG5dqRteZ-VgfBYL10_EFF1h6GU/sendMessage', data=data)

            s.enter(2, 1, fortune, (s,))



def fortune(sc):
        try:
            print('Starting FortuneDAO..')
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://app.fortunedao.com/#/dashboard"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            price = soup.findAll('p', class_='card-value')[0].get_text()
            mcap = soup.findAll('p', class_='card-value')[2].get_text()
            treasury = soup.findAll('p', class_='card-value')[6].get_text()
            backing = soup.findAll('p', class_='card-value')[4].get_text()
            
            
            driver.quit()

            apy = fortuneapy()
            
            print('FortuneDAO - $FORT', price,'\n', mcap,'\n', apy,'\n', treasury,'\n', backing)
            
            total = {'mcap': mcap, 'price': price, 'apy': apy, 'treasury': treasury, 'backing': backing}
            

            with open("/home/admin/Desktop/data/fortune.json", "w") as f:
                json.dump(total, f, indent=2)

            subprocess.call(['python3', '/home/admin/Desktop/Script/fortune.py'])
            
            keyboard = [
                [
                    InlineKeyboardButton("Chart", url='https://dexscreener.com/cronos/0x88ef5a29eec8baaab8c1111a57ad2fcec8ad6109'),
                    InlineKeyboardButton("Dashboard", url='https://www.fortunedao.com/#/dashboard')
                ]
            ]
             
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            print('Setting up data.')
            data = {
                    'photo': ('fortune.png', open('/home/admin/Desktop/ss/fortune.png', 'rb')),
                    'action': (None, 'send'),
                    'chat_id': (None, '-1001431327406'),
                    'caption': (None, f'\U0001F48E <b>FortuneDAO - $FORT</b> #Cronos \U0001F48E \n\n\u231B <i>@Fortune_Dao - <a href="https://discord.gg/U9hqMQkhZt">Discord</a> - <a href="https://twitter.com/Fortune_DAO">Twitter</a> - <a href="https://rebasetokens.app/f-a-q">FAQ</a></i> \u231B\n\n\U0001F4B5 <b>Market Cap:</b> {mcap}\n\U0001F4B0 <b>Price:</b> {price}\n\U0001F5D3 <b>APY:</b> {apy}\n\U0001F4AC <b>Treasury:</b> {treasury}\n\U0001F4CC <b>RFV per FORT:</b> {backing}\n\n\U0001F315 <a href="https://warp.bond/"><b>Warp.Bond</b></a> - The Next-Gen Web3 reserve currency ft. NFT Bonds & buildable starships that travel within the Staking #Metaverse\n@warpbond - <a href="https://discord.gg/warpbond">Discord</a> - <a href="https://twitter.com/warpbond">Twitter</a>\nJoin the <a href="https://warpcountdown.com/">Whitelist here!</a> \U0001F315'),
                    "reply_markup": (None, json.dumps(reply_markup.to_dict())),
                    "parse_mode": (None, 'HTML')
            }
        
            requests.post(url='https://api.telegram.org/bot5025889373:AAEGOUROw4deWROTzTR-1v1lDddv2EJFmSQ/sendPhoto', files=data)
            print('Data sent!')

            print('Shutting off FortuneDAO..')
            s.enter(2, 1, clam, (s,))
            
        except Exception as errore:

            print(errore)

            data = {"chat_id": "92637783",
                    "text": f'<b>Error</b> on FortuneDAO Main Chat\n\n {errore}' ,
                    "parse_mode": 'HTML'}

            requests.post(url='https://api.telegram.org/bot5062720103:AAHo_qpQzG5dqRteZ-VgfBYL10_EFF1h6GU/sendMessage', data=data)

            s.enter(2, 1, clam, (s,))


def fortuneapy():

            print('Starting FortuneDAO..')
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://app.fortunedao.com/#/stake"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            apy = soup.findAll('p', class_='stake-card-metrics-value')[0].get_text()
            
            
            driver.quit()
            
            return apy


def clam(sc):
        try:
            print('Starting OtterClam..')
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://app.otterclam.finance/#/dashboard"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            price = soup.findAll('h4', class_='MuiTypography-root MuiTypography-h4 MuiTypography-colorTextPrimary')[1].get_text()
            apy = soup.findAll('h4', class_='MuiTypography-root MuiTypography-h4')[5].get_text()
            mcap = soup.findAll('h4', class_='MuiTypography-root MuiTypography-h4 MuiTypography-colorTextPrimary')[0].get_text()
            tvl = soup.findAll('h4', class_='MuiTypography-root MuiTypography-h4')[0].get_text()
            treasury = soup.findAll('h4', class_='MuiTypography-root MuiTypography-h4')[1].get_text()
            backing = soup.findAll('h4', class_='MuiTypography-root MuiTypography-h4 MuiTypography-colorTextPrimary')[4].get_text()
            runway = soup.findAll('h4', class_='MuiTypography-root MuiTypography-h4')[6].get_text()
            
            
            driver.quit()
            print('OtterClam - $CLAM', price,'\n', mcap,'\n', tvl,'\n', apy,'\n', treasury,'\n', backing, '\n', runway)
            
            total = {'mcap': mcap, 'price': price, 'tvl': tvl, 'apy': apy, 'treasury': treasury, 'backing': backing, 'runway': runway}
            

            with open("/home/admin/Desktop/data/clam.json", "w") as f:
                json.dump(total, f, indent=2)

            subprocess.call(['python3', '/home/admin/Desktop/Script/clam.py'])

            keyboard = [
                [
                    InlineKeyboardButton("Chart", url='https://dexscreener.com/polygon/0x3fcc446c70489610462be9d61528c51151aca49f'),
                    InlineKeyboardButton("Dashboard", url='https://app.otterclam.finance/#/dashboard')
                ]
            ]
             
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            print('Setting up data.')
            data = {
                    'photo': ('clam.png', open('/home/admin/Desktop/ss/clam.png', 'rb')),
                    'action': (None, 'send'),
                    'chat_id': (None, '-1001431327406'),
                    'caption': (None, f'\U0001F48E <b>OtterClam - $CLAM</b> #Polygon \U0001F48E \n\n\u231B <i>@otterclam_official - <a href="https://discord.gg/mJc4gZvtfg">Discord</a> - <a href="https://twitter.com/OtterClam">Twitter</a> - <a href="https://rebasetokens.app/f-a-q">FAQ</a></i> \u231B\n\n\U0001F4B5 <b>Market Cap:</b> {mcap}\n\U0001F4B0 <b>Price:</b> {price}\n\U0001F5D3 <b>APY:</b> {apy}\n\U0001F512 <b>TVL:</b> {tvl}\n\U0001F4AC <b>Treasury:</b> {treasury}\n\U0001F4CC <b>Backing:</b> {backing}\n\u23F0 <b>Runway:</b> {runway}\n\n\U0001F315 <a href="https://warp.bond/"><b>Warp.Bond</b></a> - The Next-Gen Web3 reserve currency ft. NFT Bonds & buildable starships that travel within the Staking #Metaverse\n@warpbond - <a href="https://discord.gg/warpbond">Discord</a> - <a href="https://twitter.com/warpbond">Twitter</a>\nJoin the <a href="https://warpcountdown.com/">Whitelist here!</a> \U0001F315'),
                    "reply_markup": (None, json.dumps(reply_markup.to_dict())),
                    "parse_mode": (None, 'HTML')
            }
        
            requests.post(url='https://api.telegram.org/bot5025889373:AAEGOUROw4deWROTzTR-1v1lDddv2EJFmSQ/sendPhoto', files=data)
            print('Data sent!')

            print('Shutting off Clam..')
            s.enter(2, 1, mama, (s,))
            
        except Exception as errore:

            print(errore)

            data = {"chat_id": "92637783",
                    "text": f'<b>Error</b> on Clam Main Chat\n\n {errore}' ,
                    "parse_mode": 'HTML'}

            requests.post(url='https://api.telegram.org/bot5062720103:AAHo_qpQzG5dqRteZ-VgfBYL10_EFF1h6GU/sendMessage', data=data)

            s.enter(2, 1, mama, (s,))



def mama(sc):
        try:
            print('Starting Mama..')
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://app.mamadao.co/#/dashboard"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            price = driver.find_element(By.XPATH,'//*[@id="treasury-dashboard-view"]/div/div/div/div/div[2]/h5').text
            mcap = driver.find_element(By.XPATH,'//*[@id="treasury-dashboard-view"]/div/div/div/div/div[1]/div/h5').text
            backing = driver.find_element(By.XPATH,'//*[@id="treasury-dashboard-view"]/div/div/div/div/div[5]/h5').text            
            
            driver.quit()

            results = mamastake()
            apy = results[0]
            tvl = results[1]

            treasury = mamabond()
            
            print('MamaDAO - $MAMA', price,'\n', mcap,'\n', tvl,'\n', apy,'\n', treasury,'\n', backing)
            
            total = {'mcap': mcap, 'price': price, 'tvl': tvl, 'apy': apy, 'treasury': treasury, 'backing':backing}
            

            with open("/home/admin/Desktop/data/mama.json", "w") as f:
                json.dump(total, f, indent=2) 

            subprocess.call(['python3', '/home/admin/Desktop/Script/mama.py'])

            keyboard = [
                [
                    InlineKeyboardButton("Chart", url='https://dexscreener.com/polygon/0xbddb96d54e1434654f8e46dba41120cd652039bb'),
                    InlineKeyboardButton("Dashboard", url='https://app.mamadao.co/#/dashboard')
                ]
            ]
             
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            print('Setting up data.')
            data = {
                    'photo': ('mama.png', open('/home/admin/Desktop/ss/mama.png', 'rb')),
                    'action': (None, 'send'),
                    'chat_id': (None, '-1001431327406'),
                    'caption': (None, f'\U0001F48E <b>MAMADAO - $MAMA</b> #Polygon \U0001F48E \n\n\u231B <i><a href="http://discord.com/invite/CXMYD6TeYD">Discord</a> - <a href="http://twitter.com/OfficialMamaDAO">Twitter</a> - <a href="https://rebasetokens.app/f-a-q">FAQ</a></i> \u231B\n\n\U0001F4B5 <b>Market Cap:</b> {mcap}\n\U0001F4B0 <b>Price:</b> {price}\n\U0001F5D3 <b>APY:</b> {apy}\n\U0001F512 <b>TVL:</b> {tvl}\n\U0001F4AC <b>Treasury:</b> {treasury}\n\U0001F4CC <b>Backing:</b> {backing}\n\n\U0001F315 <a href="https://warp.bond/"><b>Warp.Bond</b></a> - The Next-Gen Web3 reserve currency ft. NFT Bonds & buildable starships that travel within the Staking #Metaverse\n@warpbond - <a href="https://discord.gg/warpbond">Discord</a> - <a href="https://twitter.com/warpbond">Twitter</a>\nJoin the <a href="https://warpcountdown.com/">Whitelist here!</a> \U0001F315'),
                    "reply_markup": (None, json.dumps(reply_markup.to_dict())),
                    "parse_mode": (None, 'HTML')
            }
        
            requests.post(url='https://api.telegram.org/bot5025889373:AAEGOUROw4deWROTzTR-1v1lDddv2EJFmSQ/sendPhoto', files=data)
            print('Data sent!')

            print('Shutting off MamaDAO..')
            s.enter(2, 1, unus, (s,))
            
        except Exception as errore:

            print(errore)

            data = {"chat_id": "92637783",
                    "text": f'<b>Error</b> on Mama Main Chat\n\n {errore}' ,
                    "parse_mode": 'HTML'}

            requests.post(url='https://api.telegram.org/bot5062720103:AAHo_qpQzG5dqRteZ-VgfBYL10_EFF1h6GU/sendMessage', data=data)

            s.enter(2, 1, unus, (s,))


def mamastake():
        
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://app.mamadao.co/#/stake"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            apy = driver.find_element(By.XPATH,'//*[@id="staking-card"]/div/div[2]/div/div/div[1]/div/h4').text
            tvl = driver.find_element(By.XPATH,'//*[@id="staking-card"]/div/div[2]/div/div/div[2]/div/h4').text
        
            
            driver.quit()

            return apy, tvl

def mamabond():

            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://app.mamadao.co/#/bonds"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            treasury = driver.find_element(By.XPATH,'//*[@id="choose-bond-view"]/div/div[2]/div[1]/div/h4').text

            driver.quit()

            return treasury


def unus(sc):
        try:
            print('Starting Unus..')
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://dexscreener.com/bsc/0x1f9e3432a89e53da95ac85c76ccb129841166e69"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            price = soup.find_all('span', {'class' : 'chakra-text css-5sxn50', })[0].get_text()
            liq = soup.find_all('span', {'class' : 'chakra-text css-5sxn50', })[2].get_text()                        
            mcap = soup.find_all('span', {'class' : 'chakra-text css-5sxn50', })[4].get_text()
            vol = soup.find_all('span', {'class' : 'chakra-text css-5sxn50', })[20].get_text()
            
            
            
            print('UnusDAO - $UDO', price,'\n', mcap,'\n', vol, '\n', liq)

            total = {'mcap': mcap, 'price': price, 'vol':vol, 'liquidity': liq}
            

            with open("/home/admin/Desktop/data/unus.json", "w") as f:
                json.dump(total, f, indent=2)

            subprocess.call(['python3', '/home/admin/Desktop/Script/unus.py'])
            
            keyboard = [
                [
                    InlineKeyboardButton("Chart", url='https://dexscreener.com/bsc/0x364952dc20b5720b7fd3e73141cf6a85d9af8643'),
                    InlineKeyboardButton("Dashboard", url='https://unusdao.finance/#/dashboard')
                ]
            ]
             
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            print('Setting up data.')
            data = {
                    'photo': ('unus.png', open('/home/admin/Desktop/ss/unus.png', 'rb')),
                    'action': (None, 'send'),
                    'chat_id': (None, '-1001431327406'),
                    'caption': (None, f'\U0001F48E <b>UnusDAO - $UDO</b> #BSC \U0001F48E \n\n\u231B <i>@unusdao - <a href="https://discord.gg/uhQAACcBSQ">Discord</a> - <a href="https://twitter.com/UnusDao">Twitter</a> - <a href="https://rebasetokens.app/f-a-q">FAQ</a></i> \u231B\n\n\U0001F4B5 <b>Market Cap:</b> {mcap}\n\U0001F4B0 <b>Price:</b> {price}\n\U0001F5D3 <b>24h Volume:</b> {vol}\n\U0001F5D3 <b>Liquidity:</b> {liq}\n\n\U0001F315 <a href="https://warp.bond/"><b>Warp.Bond</b></a> - The Next-Gen Web3 reserve currency ft. NFT Bonds & buildable starships that travel within the Staking #Metaverse\n@warpbond - <a href="https://discord.gg/warpbond">Discord</a> - <a href="https://twitter.com/warpbond">Twitter</a>\nJoin the <a href="https://warpcountdown.com/">Whitelist here!</a> \U0001F315'),
                    "reply_markup": (None, json.dumps(reply_markup.to_dict())),
                    "parse_mode": (None, 'HTML')
            }
        
            requests.post(url='https://api.telegram.org/bot5025889373:AAEGOUROw4deWROTzTR-1v1lDddv2EJFmSQ/sendPhoto', files=data)
            print('Data sent!')

            print('Shutting off UnusDAO..')
            s.enter(2, 1, tempo, (s,))
            
        except Exception as errore:

            print(errore)

            data = {"chat_id": "92637783",
                    "text": f'<b>Error</b> on UnusDAO Main Chat\n\n {errore}' ,
                    "parse_mode": 'HTML'}

            requests.post(url='https://api.telegram.org/bot5062720103:AAHo_qpQzG5dqRteZ-VgfBYL10_EFF1h6GU/sendMessage', data=data)

            s.enter(2, 1, tempo, (s,))



def tempo(sc):
        try:
            print('Starting TempoDAO..')
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://dexscreener.com/avalanche/0x720dd9292b3d0dd78c9afa57afd948c2ea2d50d8"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            price = soup.find_all('span', {'class' : 'chakra-text css-5sxn50', })[0].get_text()
            liquidity = soup.find_all('span', {'class' : 'chakra-text css-5sxn50', })[2].get_text()                        
            mcap = soup.find_all('span', {'class' : 'chakra-text css-5sxn50', })[4].get_text()
            vol = soup.find_all('span', {'class' : 'chakra-text css-5sxn50', })[20].get_text()
            
            
            
            driver.quit()
            print('TempoDAO - $TEMPO', price, '\n', mcap, '\n', vol, '\n', liquidity)

            total = {'mcap': mcap, 'price': price, 'vol':vol, 'liquidity': liquidity}
            

            with open("/home/admin/Desktop/data/tempo.json", "w") as f:
                json.dump(total, f, indent=2)

            subprocess.call(['python3', '/home/admin/Desktop/Script/tempo.py'])
            
            keyboard = [
                [
                    InlineKeyboardButton("Chart", url='https://dexscreener.com/avalanche/0x720dd9292b3d0dd78c9afa57afd948c2ea2d50d8'),
                    InlineKeyboardButton("Dashboard", url='https://earn.tempodao.gg/#/dashboard')
                ]
            ]
             
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            print('Setting up data.')
            data = {
                    'photo': ('tempo.png', open('/home/admin/Desktop/ss/tempo.png', 'rb')),
                    'action': (None, 'send'),
                    'chat_id': (None, '-1001431327406'),
                    'caption': (None, f'\U0001F48E <b>TempoDAO - $TEMPO</b> #AVAX \U0001F48E \n\n\u231B <i><a href="http://discord.gg/tempodao">Discord</a> - <a href="https://twitter.com/TempoDAO">Twitter</a> - <a href="https://rebasetokens.app/f-a-q">FAQ</a></i> \u231B\n\n\U0001F4B5 <b>Market Cap:</b> {mcap}\n\U0001F4B0 <b>Price:</b> {price}\n\U0001F5D3 <b>24h Volume:</b> {vol}\n\U0001F512 <b>Liquidity:</b> {liquidity}\n\n\U0001F315 <a href="https://warp.bond/"><b>Warp.Bond</b></a> - The Next-Gen Web3 reserve currency ft. NFT Bonds & buildable starships that travel within the Staking #Metaverse\n@warpbond - <a href="https://discord.gg/warpbond">Discord</a> - <a href="https://twitter.com/warpbond">Twitter</a>\nJoin the <a href="https://warpcountdown.com/">Whitelist here!</a> \U0001F315'),
                    "reply_markup": (None, json.dumps(reply_markup.to_dict())),
                    "parse_mode": (None, 'HTML')
            }
        
            requests.post(url='https://api.telegram.org/bot5025889373:AAEGOUROw4deWROTzTR-1v1lDddv2EJFmSQ/sendPhoto', files=data)
            print('Data sent!')

            print('Shutting off TempoDAO..')
            s.enter(2, 1, gyro, (s,))
            
        except Exception as errore:

            print(errore)

            data = {"chat_id": "92637783",
                    "text": f'<b>Error</b> on TempoDAO Main Chat\n\n {errore}' ,
                    "parse_mode": 'HTML'}

            requests.post(url='https://api.telegram.org/bot5062720103:AAHo_qpQzG5dqRteZ-VgfBYL10_EFF1h6GU/sendMessage', data=data)

            s.enter(2, 1, gyro, (s,))


def gyro(sc):
        try:
            print('Starting Gyro..')
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://dexscreener.com/bsc/0x5ca063a7e2bebefeb2bdea42158f5b825f0f9ffb"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            price = soup.find_all('span', {'class' : 'chakra-text css-5sxn50', })[0].get_text()
            liq = soup.find_all('span', {'class' : 'chakra-text css-5sxn50', })[2].get_text()                        
            mcap = soup.find_all('span', {'class' : 'chakra-text css-5sxn50', })[4].get_text()
            vol = soup.find_all('span', {'class' : 'chakra-text css-5sxn50', })[20].get_text()
            
            
            driver.quit()
            print('GyroDAO - $GYRO', price,'\n', mcap,'\n', vol, '\n', liq)

            total = {'mcap': mcap, 'price': price, 'vol':vol, 'liquidity': liq}
            
            with open("/home/admin/Desktop/data/gyro.json", "w") as f:
                json.dump(total, f, indent=2)

            subprocess.call(['python3', '/home/admin/Desktop/Script/gyro.py'])
            
            keyboard = [
                [
                    InlineKeyboardButton("Chart", url='https://dexscreener.com/bsc/0x5ca063a7e2bebefeb2bdea42158f5b825f0f9ffb'),
                    InlineKeyboardButton("Dashboard", url='https://gyro.money/')
                ]
            ]
             
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            print('Setting up data.')
            data = {
                    'photo': ('gyro.png', open('/home/admin/Desktop/ss/gyro.png', 'rb')),
                    'action': (None, 'send'),
                    'chat_id': (None, '-1001431327406'),
                    'caption': (None, f'\U0001F48E <b>GyroDAO - $GYRO</b> #BSC \U0001F48E \n\n\u231B <i>@GyroDAO - <a href="https://discord.gg/gyrodao">Discord</a> - <a href="https://twitter.com/GyroDAO">Twitter</a> - <a href="https://rebasetokens.app/f-a-q">FAQ</a></i> \u231B\n\n\U0001F4B5 <b>Market Cap:</b> {mcap}\n\U0001F4B0 <b>Price:</b> {price}\n\U0001F5D3 <b>24h Volume:</b> {vol}\n\U0001F512 <b>Liquidity:</b> {liq}\n\n\U0001F315 <a href="https://warp.bond/"><b>Warp.Bond</b></a> - The Next-Gen Web3 reserve currency ft. NFT Bonds & buildable starships that travel within the Staking #Metaverse\n@warpbond - <a href="https://discord.gg/warpbond">Discord</a> - <a href="https://twitter.com/warpbond">Twitter</a>\nJoin the <a href="https://warpcountdown.com/">Whitelist here!</a> \U0001F315'),
                    "reply_markup": (None, json.dumps(reply_markup.to_dict())),
                    "parse_mode": (None, 'HTML')
            }
        
            requests.post(url='https://api.telegram.org/bot5025889373:AAEGOUROw4deWROTzTR-1v1lDddv2EJFmSQ/sendPhoto', files=data)
            print('Data sent!')

            print('Shutting off Gyro..')
            s.enter(2, 1, one, (s,))
            
        except Exception as errore:

            print(errore)

            data = {"chat_id": "92637783",
                    "text": f'<b>Error</b> on Gyro Main Chat\n\n {errore}' ,
                    "parse_mode": 'HTML'}

            requests.post(url='https://api.telegram.org/bot5062720103:AAHo_qpQzG5dqRteZ-VgfBYL10_EFF1h6GU/sendMessage', data=data)

            s.enter(2, 1, one, (s,))


def one(sc):
        try:
            print('Starting OneDAO..')
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://app.onedao.finance/#/dashboard"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            price = soup.findAll('p', class_='card-value')[0].get_text()
            apy = soup.findAll('p', class_='card-value')[3].get_text()
            mcap = soup.findAll('p', class_='card-value')[1].get_text()
            tvl = soup.findAll('p', class_='card-value')[2].get_text()
            treasury = soup.findAll('p', class_='card-value')[5].get_text()
            backing = soup.findAll('p', class_='card-value')[6].get_text()
            runway = soup.findAll('p', class_='card-value')[7].get_text()
            
            
            driver.quit()
            print('OneDAO - $ODAO', price,'\n', mcap,'\n', tvl,'\n', apy,'\n', treasury,'\n', backing, '\n', runway)
            
            total = {'mcap': mcap, 'price': price, 'tvl': tvl, 'apy': apy, 'treasury': treasury, 'backing': backing, 'runway': runway}
            

            with open("/home/admin/Desktop/data/one.json", "w") as f:
                json.dump(total, f, indent=2)

            subprocess.call(['python3', '/home/admin/Desktop/Script/one.py'])

            keyboard = [
                [
                    InlineKeyboardButton("Chart", url='https://dexscreener.com/harmony/0x171ff11b53674958c273bcfccbc731aa6cae96f8'),
                    InlineKeyboardButton("Dashboard", url='https://app.onedao.finance/#/dashboard')
                ]
            ]
             
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            print('Setting up data.')
            data = {
                    'photo': ('one.png', open('/home/admin/Desktop/ss/odao.png', 'rb')),
                    'action': (None, 'send'),
                    'chat_id': (None, '-1001431327406'),
                    'caption': (None, f'\U0001F48E <b>OneDAO - $ODAO</b> #Harmony \U0001F48E \n\n\u231B <i>@onedao_finance - <a href="https://discord.gg/onedao">Discord</a> - <a href="https://twitter.com/Onedao_finance">Twitter</a> - <a href="https://rebasetokens.app/f-a-q">FAQ</a></i> \u231B\n\n\U0001F4B5 <b>Market Cap:</b> {mcap}\n\U0001F4B0 <b>Price:</b> {price}\n\U0001F5D3 <b>APY:</b> {apy}\n\U0001F512 <b>TVL:</b> {tvl}\n\U0001F4AC <b>Treasury:</b> {treasury}\n\U0001F4CC <b>Backing:</b> {backing}\n\u23F0 <b>Runway:</b> {runway}\n\n\U0001F315 <a href="https://warp.bond/"><b>Warp.Bond</b></a> - The Next-Gen Web3 reserve currency ft. NFT Bonds & buildable starships that travel within the Staking #Metaverse\n@warpbond - <a href="https://discord.gg/warpbond">Discord</a> - <a href="https://twitter.com/warpbond">Twitter</a>\nJoin the <a href="https://warpcountdown.com/">Whitelist here!</a> \U0001F315'),
                    "reply_markup": (None, json.dumps(reply_markup.to_dict())),
                    "parse_mode": (None, 'HTML')
            }
        
            requests.post(url='https://api.telegram.org/bot5025889373:AAEGOUROw4deWROTzTR-1v1lDddv2EJFmSQ/sendPhoto', files=data)
            print('Data sent!')

            print('Shutting off OneDAO..')
            s.enter(2, 1, cheez, (s,))
            
        except Exception as errore:

            print(errore)

            data = {"chat_id": "92637783",
                    "text": f'<b>Error</b> on OneDAO Main Chat\n\n {errore}' ,
                    "parse_mode": 'HTML'}

            requests.post(url='https://api.telegram.org/bot5062720103:AAHo_qpQzG5dqRteZ-VgfBYL10_EFF1h6GU/sendMessage', data=data)

            s.enter(2, 1, cheez, (s,))


def cheez(sc):
        try:
            print('Starting CheeseDAO..')
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://www.cheesedao.xyz/#/dashboard"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            price = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[1].get_text()
            apy = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[4].get_text()
            mcap = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[0].get_text()
            treasury = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[3].get_text()
            runway = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[5].get_text()
            
            
            driver.quit()

            tvl = cheezvalue()
            
            print('CheezDAO - $CHEEZ', price,'\n', mcap,'\n', tvl,'\n', apy,'\n', treasury, '\n', runway)
            
            total = {'mcap': mcap, 'price': price, 'tvl': tvl, 'apy': apy, 'treasury': treasury, 'runway': runway}
            

            with open("/home/admin/Desktop/data/cheez.json", "w") as f:
                json.dump(total, f, indent=2)

            subprocess.call(['python3', '/home/admin/Desktop/Script/cheez.py'])

            keyboard = [
                [
                    InlineKeyboardButton("Chart", url='https://dexscreener.com/harmony/0x82723f6c0b32f28ddc2006b9cdbca6cee0ad957a'),
                    InlineKeyboardButton("Dashboard", url='https://www.cheesedao.xyz/#/dashboard')
                ]
            ]
             
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            print('Setting up data.')
            data = {
                    'photo': ('cheez.png', open('/home/admin/Desktop/ss/cheez.png', 'rb')),
                    'action': (None, 'send'),
                    'chat_id': (None, '-1001431327406'),
                    'caption': (None, f'\U0001F48E <b>CheeseDAO - $CHEEZ</b> #Harmony \U0001F48E \n\n\u231B <i><a href="https://discord.gg/cheesedao">Discord</a> - <a href="https://twitter.com/CheezDAO">Twitter</a> - <a href="https://rebasetokens.app/f-a-q">FAQ</a></i> \u231B\n\n\U0001F4B5 <b>Market Cap:</b> {mcap}\n\U0001F4B0 <b>Price:</b> {price}\n\U0001F5D3 <b>APY:</b> {apy}\n\U0001F512 <b>TVL:</b> {tvl}\n\U0001F4AC <b>Treasury:</b> {treasury}\n\u23F0 <b>Runway:</b> {runway}\n\n\U0001F315 <a href="https://warp.bond/"><b>Warp.Bond</b></a> - The Next-Gen Web3 reserve currency ft. NFT Bonds & buildable starships that travel within the Staking #Metaverse\n@warpbond - <a href="https://discord.gg/warpbond">Discord</a> - <a href="https://twitter.com/warpbond">Twitter</a>\nJoin the <a href="https://warpcountdown.com/">Whitelist here!</a> \U0001F315'),
                    "reply_markup": (None, json.dumps(reply_markup.to_dict())),
                    "parse_mode": (None, 'HTML')
            }
        
            requests.post(url='https://api.telegram.org/bot5025889373:AAEGOUROw4deWROTzTR-1v1lDddv2EJFmSQ/sendPhoto', files=data)
            print('Data sent!')

            print('Shutting off CheezDAO..')
            s.enter(2, 1, luxor, (s,))
            
        except Exception as errore:

            print(errore)

            data = {"chat_id": "92637783",
                    "text": f'<b>Error</b> on CheeseDAO Main Chat\n\n {errore}' ,
                    "parse_mode": 'HTML'}

            requests.post(url='https://api.telegram.org/bot5062720103:AAHo_qpQzG5dqRteZ-VgfBYL10_EFF1h6GU/sendMessage', data=data)

            s.enter(2, 1, luxor, (s,))
            

def cheezvalue():

            options = webdriver.FirefoxOptions()
            
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://www.cheesedao.xyz/#/ageing"
            driver.get(urlone)
            time.sleep(30)
            
            soup = BeautifulSoup(driver.page_source,'html.parser')
            apy = soup.findAll('h4', class_='MuiTypography-root MuiTypography-h4')[1].get_text()

            driver.quit()
            

            return apy


def luxor(sc):
        try:
            print('Starting Luxor..')
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://app.luxor.money/#/dashboard"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            price = soup.findAll('p', class_='card-value')[0].get_text()
            apy = soup.findAll('p', class_='card-value')[8].get_text()
            mcap = soup.findAll('p', class_='card-value')[2].get_text()
            tvl = soup.findAll('p', class_='card-value')[3].get_text()
            treasury = soup.findAll('p', class_='card-value')[9].get_text()
            backing = soup.findAll('p', class_='card-value')[12].get_text()
            runway = soup.findAll('p', class_='card-value')[13].get_text()
            
            
            driver.quit()
            print('Luxor - $LUX', price,'\n', mcap,'\n', tvl,'\n', apy,'\n', treasury,'\n', backing, '\n', runway)
            
            total = {'mcap': mcap, 'price': price, 'tvl': tvl, 'apy': apy, 'treasury': treasury, 'backing': backing, 'runway': runway}
            

            with open("/home/admin/Desktop/data/luxor.json", "w") as f:
                json.dump(total, f, indent=2)

            keyboard = [
                [
                    InlineKeyboardButton("Chart", url='https://dexscreener.com/fantom/0x951bbb838e49f7081072895947735b0892cccbcd'),
                    InlineKeyboardButton("Dashboard", url='https://app.luxor.money/#/dashboard')
                ]
            ]
             
            reply_markup = InlineKeyboardMarkup(keyboard)

            subprocess.call(['python3', '/home/admin/Desktop/Script/luxor.py'])
            
            print('Setting up data.')
            data = {
                    'photo': ('luxor.png', open('/home/admin/Desktop/ss/luxor.png', 'rb')),
                    'action': (None, 'send'),
                    'chat_id': (None, '-1001431327406'),
                    'caption': (None, f'\U0001F48E <b>Luxor - $LUX</b> #Fantom \U0001F48E \n\n\u231B <i>@SoulSwapDeFi - <a href="https://discord.gg/DQjChB6Wa6">Discord</a> - <a href="https://twitter.com/LuxorMoney">Twitter</a> - <a href="https://rebasetokens.app/f-a-q">FAQ</a></i> \u231B\n\n\U0001F4B5 <b>Market Cap:</b> {mcap}\n\U0001F4B0 <b>Price:</b> {price}\n\U0001F5D3 <b>APY:</b> {apy}\n\U0001F512 <b>TVL:</b> {tvl}\n\U0001F4AC <b>Treasury:</b> {treasury}\n\U0001F4CC <b>Backing:</b> {backing}\n\u23F0 <b>Runway:</b> {runway}\n\n\U0001F315 <a href="https://warp.bond/"><b>Warp.Bond</b></a> - The Next-Gen Web3 reserve currency ft. NFT Bonds & buildable starships that travel within the Staking #Metaverse\n@warpbond - <a href="https://discord.gg/warpbond">Discord</a> - <a href="https://twitter.com/warpbond">Twitter</a>\nJoin the <a href="https://warpcountdown.com/">Whitelist here!</a> \U0001F315'),
                    "reply_markup": (None, json.dumps(reply_markup.to_dict())),
                    "parse_mode": (None, 'HTML')
            }
        
            requests.post(url='https://api.telegram.org/bot5025889373:AAEGOUROw4deWROTzTR-1v1lDddv2EJFmSQ/sendPhoto', files=data)
            print('Data sent!')

            print('Shutting off Luxor..')
            s.enter(2, 1, secure, (s,))
            
        except Exception as errore:

            print(errore)

            data = {"chat_id": "92637783",
                    "text": f'<b>Error</b> on Luxor Main Chat\n\n {errore}' ,
                    "parse_mode": 'HTML'}

            requests.post(url='https://api.telegram.org/bot5062720103:AAHo_qpQzG5dqRteZ-VgfBYL10_EFF1h6GU/sendMessage', data=data)

            s.enter(2, 1, secure, (s,))



def secure(sc):
        try:
            print('Starting SecureDAO..')
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://www.securedao.finance/#/app/dashboard"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            price = soup.findAll('p', class_='card-value')[0].get_text()
            apy = soup.findAll('p', class_='card-value')[3].get_text()
            mcap = soup.findAll('p', class_='card-value')[1].get_text()
            tvl = soup.findAll('p', class_='card-value')[2].get_text()
            treasury = soup.findAll('p', class_='card-value')[5].get_text()
            backing = soup.findAll('p', class_='card-value')[6].get_text()
            runway = soup.findAll('p', class_='card-value')[7].get_text()
            
            
            driver.quit()
            print('SecureDAO - $SCR', price,'\n', mcap,'\n', tvl,'\n', apy,'\n', treasury,'\n', backing, '\n', runway)
            
            total = {'mcap': mcap, 'price': price, 'tvl': tvl, 'apy': apy, 'treasury': treasury, 'backing': backing, 'runway': runway}
            

            with open("/home/admin/Desktop/data/secure.json", "w") as f:
                json.dump(total, f, indent=2)

            subprocess.call(['python3', '/home/admin/Desktop/Script/secure.py'])

            keyboard = [
                [
                    InlineKeyboardButton("Chart", url='https://dexscreener.com/fantom/0x468c174cc015d4a697586c0a99f95e045f7e6f91'),
                    InlineKeyboardButton("Dashboard", url='https://www.securedao.finance/#/app/dashboard')
                ]
            ]
             
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            print('Setting up data.')
            data = {
                    'photo': ('secure.png', open('/home/admin/Desktop/ss/secure.png', 'rb')),
                    'action': (None, 'send'),
                    'chat_id': (None, '-1001431327406'),
                    'caption': (None, f'\U0001F48E <b>SecureDAO - $SCR</b> #Fantom \U0001F48E \n\n\u231B <i><a href="https://discord.gg/securedao">Discord</a> - <a href="https://twitter.com/SecureDao">Twitter</a> - <a href="https://rebasetokens.app/f-a-q">FAQ</a></i> \u231B\n\n\U0001F4B5 <b>Market Cap:</b> {mcap}\n\U0001F4B0 <b>Price:</b> {price}\n\U0001F5D3 <b>APY:</b> {apy}\n\U0001F512 <b>TVL:</b> {tvl}\n\U0001F4AC <b>Treasury:</b> {treasury}\n\U0001F4CC <b>Backing:</b> {backing}\n\u23F0 <b>Runway:</b> {runway}\n\n\U0001F315 <a href="https://warp.bond/"><b>Warp.Bond</b></a> - The Next-Gen Web3 reserve currency ft. NFT Bonds & buildable starships that travel within the Staking #Metaverse\n@warpbond - <a href="https://discord.gg/warpbond">Discord</a> - <a href="https://twitter.com/warpbond">Twitter</a>\nJoin the <a href="https://warpcountdown.com/">Whitelist here!</a> \U0001F315'),
                    "reply_markup": (None, json.dumps(reply_markup.to_dict())),
                    "parse_mode": (None, 'HTML')
            }
        
            requests.post(url='https://api.telegram.org/bot5025889373:AAEGOUROw4deWROTzTR-1v1lDddv2EJFmSQ/sendPhoto', files=data)
            print('Data sent!')

            print('Shutting off Secure..')
            s.enter(2, 1, ara, (s,))
            
        except Exception as errore:

            print(errore)

            data = {"chat_id": "92637783",
                    "text": f'<b>Error</b> on Secure Main Chat\n\n {errore}' ,
                    "parse_mode": 'HTML'}

            requests.post(url='https://api.telegram.org/bot5062720103:AAHo_qpQzG5dqRteZ-VgfBYL10_EFF1h6GU/sendMessage', data=data)

            s.enter(2, 1, ara, (s,))


def ara(sc):
        try:
            print('Starting AraFinance..')
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://dexscreener.com/avalanche/0x9dd1cde570b96ba13e63d317e23637651142227c"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            price = soup.find_all('span', {'class' : 'chakra-text css-5sxn50', })[0].get_text()
            liquidity = soup.find_all('span', {'class' : 'chakra-text css-5sxn50', })[2].get_text()                        
            mcap = soup.find_all('span', {'class' : 'chakra-text css-5sxn50', })[4].get_text()
            vol = soup.find_all('span', {'class' : 'chakra-text css-5sxn50', })[20].get_text()
            
            
            
            driver.quit()
            print('AraFinance - $ARA', price, '\n', mcap, '\n', vol, '\n', liquidity)

            total = {'mcap': mcap, 'price': price, 'vol':vol, 'liquidity': liquidity}
            

            with open("/home/admin/Desktop/data/ara.json", "w") as f:
                json.dump(total, f, indent=2)

            subprocess.call(['python3', '/home/admin/Desktop/Script/ara.py'])

            keyboard = [
                [
                    InlineKeyboardButton("Chart", url='https://dexscreener.com/avalanche/0x9dd1cde570b96ba13e63d317e23637651142227c'),
                    InlineKeyboardButton("Dashboard", url='https://app.arafinance.land/')
                ]
            ]
             
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            print('Setting up data.')
            data = {
                    'photo': ('ara.png', open('/home/admin/Desktop/ss/ara.png', 'rb')),
                    'action': (None, 'send'),
                    'chat_id': (None, '-1001431327406'),
                    'caption': (None, f'\U0001F48E <b>AraFinance - $ARA</b> #AVAX \U0001F48E \n\n\u231B <i>@AraFinance - <a href="https://discord.gg/h4HrEdmrDF">Discord</a> - <a href="https://twitter.com/AraFinance">Twitter</a> - <a href="https://rebasetokens.app/f-a-q">FAQ</a></i> \u231B\n\n\U0001F4B5 <b>Market Cap:</b> {mcap}\n\U0001F4B0 <b>Price:</b> {price}\n\U0001F5D3 <b>24h Volume:</b> {vol}\n\U0001F512 <b>Liquidity:</b> {liquidity}\n\n\U0001F315 <a href="https://warp.bond/"><b>Warp.Bond</b></a> - The Next-Gen Web3 reserve currency ft. NFT Bonds & buildable starships that travel within the Staking #Metaverse\n@warpbond - <a href="https://discord.gg/warpbond">Discord</a> - <a href="https://twitter.com/warpbond">Twitter</a>\nJoin the <a href="https://warpcountdown.com/">Whitelist here!</a> \U0001F315'),
                    "reply_markup": (None, json.dumps(reply_markup.to_dict())),
                    "parse_mode": (None, 'HTML')
            }
        
            requests.post(url='https://api.telegram.org/bot5025889373:AAEGOUROw4deWROTzTR-1v1lDddv2EJFmSQ/sendPhoto', files=data)
            print('Data sent!')

            print('Shutting off AraFinance..')
            s.enter(2, 1, metareserve, (s,))
            
        except Exception as errore:

            print(errore)

            data = {"chat_id": "92637783",
                    "text": f'<b>Error</b> on AraFinance Main Chat\n\n {errore}' ,
                    "parse_mode": 'HTML'}

            requests.post(url='https://api.telegram.org/bot5062720103:AAHo_qpQzG5dqRteZ-VgfBYL10_EFF1h6GU/sendMessage', data=data)

            s.enter(2, 1, metareserve, (s,))




def metareserve(sc):
        try:
            print('Starting MetaReserve..')
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://app.metareserve.finance/#/dashboard"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            price = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[1].get_text()
            mcap = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[2].get_text()
            apy = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[0].get_text()
            backing = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[3].get_text()
            
            
            driver.quit()

            tvl = metaresvalue()
            
            print('MetaReserve - $POWER', price,'\n', mcap,'\n', apy,'\n', tvl, '\n', backing)

            total = {'mcap': mcap, 'price': price, 'tvl': tvl, 'apy': apy, 'backing': backing}
            

            with open("/home/admin/Desktop/data/power.json", "w") as f:
                json.dump(total, f, indent=2)

            subprocess.call(['python3', '/home/admin/Desktop/Script/metareserve.py'])

            keyboard = [
                [
                    InlineKeyboardButton("Chart", url='https://dexscreener.com/bsc/0xa1a64b7d85b92a19fdb628557cc44bcb40284b65'),
                    InlineKeyboardButton("Dashboard", url='https://app.metareserve.finance/#/dashboard')
                ]
            ]
             
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            print('Setting up data.')
            data = {
                    'photo': ('metareserve.png', open('/home/admin/Desktop/ss/metareserve.png', 'rb')),
                    'action': (None, 'send'),
                    'chat_id': (None, '-1001431327406'),
                    'caption': (None, f'\U0001F48E <b>MetaReserve - $POWER</b> #BSC \U0001F48E \n\n\u231B <i>@MetaReserve - <a href="https://discord.gg/metareserve">Discord</a> - <a href="https://twitter.com/MetaReserveDAO">Twitter</a> - <a href="https://rebasetokens.app/f-a-q">FAQ</a></i> \u231B\n\n\U0001F4B5 <b>Market Cap:</b> {mcap}\n\U0001F4B0 <b>Price:</b> {price}\n\U0001F5D3 <b>APY:</b> {apy}\n\U0001F512 <b>TVL:</b> {tvl}\n\U0001F4CC <b>Backing:</b> {backing}\n\n\U0001F315 <a href="https://warp.bond/"><b>Warp.Bond</b></a> - The Next-Gen Web3 reserve currency ft. NFT Bonds & buildable starships that travel within the Staking #Metaverse\n@warpbond - <a href="https://discord.gg/warpbond">Discord</a> - <a href="https://twitter.com/warpbond">Twitter</a>\nJoin the <a href="https://warpcountdown.com/">Whitelist here!</a> \U0001F315'),
                    "reply_markup": (None, json.dumps(reply_markup.to_dict())),
                    "parse_mode": (None, 'HTML')
            }
        
            requests.post(url='https://api.telegram.org/bot5025889373:AAEGOUROw4deWROTzTR-1v1lDddv2EJFmSQ/sendPhoto', files=data)
            print('Data sent!')

            print('Shutting off Traverse..')
            s.enter(2, 1, jolly, (s,))
            
        except Exception as errore:

            print(errore)

            data = {"chat_id": "92637783",
                    "text": f'<b>Error</b> on MetaReserve Main Chat\n\n {errore}' ,
                    "parse_mode": 'HTML'}

            requests.post(url='https://api.telegram.org/bot5062720103:AAHo_qpQzG5dqRteZ-VgfBYL10_EFF1h6GU/sendMessage', data=data)

            s.enter(2, 1, jolly, (s,))


def metaresvalue():

            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://app.metareserve.finance/#/stake"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            tvl = soup.findAll('h4', class_='MuiTypography-root MuiTypography-h4')[1].get_text()

            driver.quit()
            return tvl


def jolly(sc):
        try:
            print('Starting PirateDAO..')
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://app.piratedao.money/#/dashboard"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            price = soup.findAll('p', class_='card-value')[0].get_text()
            mcap = soup.findAll('p', class_='card-value')[1].get_text()
            tvl = soup.findAll('p', class_='card-value')[3].get_text()
            apy = soup.findAll('p', class_='card-value')[4].get_text()
            treasury = soup.findAll('p', class_='card-value')[6].get_text()
            backing = soup.findAll('p', class_='card-value')[7].get_text()
            runway = soup.findAll('p', class_='card-value')[8].get_text()
            
            
            driver.quit()
            print('PirateDAO - $JOLLY', price,'\n', mcap,'\n', tvl,'\n', apy,'\n', treasury,'\n', backing, '\n', runway)
            
            total = {'mcap': mcap, 'price': price, 'tvl': tvl, 'apy': apy, 'treasury': treasury, 'backing': backing, 'runway': runway}
            

            with open("/home/admin/Desktop/data/jolly.json", "w") as f:
                json.dump(total, f, indent=2)

            subprocess.call(['python3', '/home/admin/Desktop/Script/jolly.py'])
            
            keyboard = [
                [
                    InlineKeyboardButton("Chart", url='https://dexscreener.com/avalanche/0x30ff717fc266f2dcb3adc1af4043f8c517491e66'),
                    InlineKeyboardButton("Dashboard", url='https://piratedao.money/#/dashboard')
                ]
            ]
             
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            print('Setting up data.')
            data = {
                    'photo': ('jolly.png', open('/home/admin/Desktop/ss/jolly.png', 'rb')),
                    'action': (None, 'send'),
                    'chat_id': (None, '-1001431327406'),
                    'caption': (None, f'\U0001F48E <b>PirateDAO - $JOLLY</b> #AVAX \U0001F48E \n\n\u231B <i><a href="https://discord.gg/X2tcNDpjbf">Discord</a> - <a href="https://twitter.com/DAOpirate">Twitter</a> - <a href="https://rebasetokens.app/f-a-q">FAQ</a></i> \u231B\n\n\U0001F4B5 <b>Market Cap:</b> {mcap}\n\U0001F4B0 <b>Price:</b> {price}\n\U0001F5D3 <b>APY:</b> {apy}\n\U0001F512 <b>TVL:</b> {tvl}\n\U0001F4AC <b>Treasury:</b> {treasury}\n\U0001F4CC <b>Backing:</b> {backing}\n\u23F0 <b>Runway:</b> {runway}\n\n\U0001F315 <a href="https://warp.bond/"><b>Warp.Bond</b></a> - The Next-Gen Web3 reserve currency ft. NFT Bonds & buildable starships that travel within the Staking #Metaverse\n@warpbond - <a href="https://discord.gg/warpbond">Discord</a> - <a href="https://twitter.com/warpbond">Twitter</a>\nJoin the <a href="https://warpcountdown.com/">Whitelist here!</a> \U0001F315'),
                    "reply_markup": (None, json.dumps(reply_markup.to_dict())),
                    "parse_mode": (None, 'HTML')
            }
        
            requests.post(url='https://api.telegram.org/bot5025889373:AAEGOUROw4deWROTzTR-1v1lDddv2EJFmSQ/sendPhoto', files=data)
            print('Data sent!')

            print('Shutting off PirateDAO..')
            s.enter(2, 1, xenophon, (s,))
            
        except Exception as errore:

            print(errore)

            data = {"chat_id": "92637783",
                    "text": f'<b>Error</b> on PirateDAO Main Chat\n\n {errore}' ,
                    "parse_mode": 'HTML'}

            requests.post(url='https://api.telegram.org/bot5062720103:AAHo_qpQzG5dqRteZ-VgfBYL10_EFF1h6GU/sendMessage', data=data)

            s.enter(2, 1, xenophon, (s,))



def xenophon(sc):
        try:
            print('Starting Xenophon..')
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://app.xenophon.finance/#/dashboard"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            price = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[0].get_text()
            mcap = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[1].get_text()
            tvl = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[2].get_text()
            apy = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[3].get_text()
            treasury = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[5].get_text()
            backing = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[6].get_text()
            runway = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[7].get_text()
            
            
            driver.quit()
            print('Xenophon - $XPH', price,'\n', mcap,'\n', tvl,'\n', apy,'\n', treasury,'\n', backing, '\n', runway)
            
            total = {'mcap': mcap, 'price': price, 'tvl': tvl, 'apy': apy, 'treasury': treasury, 'backing': backing, 'runway': runway}
            

            with open("/home/admin/Desktop/data/xph.json", "w") as f:
                json.dump(total, f, indent=2)

            subprocess.call(['python3', '/home/admin/Desktop/Script/xenophon.py'])
            
            keyboard = [
                [
                    InlineKeyboardButton("Chart", url='https://dexscreener.com/bsc/0x5866d1032b5b6001429bf2a47b830bdc0dd138ea'),
                    InlineKeyboardButton("Dashboard", url='https://app.xenophon.finance/#/dashboard')
                ]
            ]
             
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            print('Setting up data.')
            data = {
                    'photo': ('xph.png', open('/home/admin/Desktop/ss/xph.png', 'rb')),
                    'action': (None, 'send'),
                    'chat_id': (None, '-1001431327406'),
                    'caption': (None, f'\U0001F48E <b>Xenophon - $XPH</b> #BSC \U0001F48E \n\n\u231B <i>@XenophonDAO - <a href="https://discord.gg/8tqxqVbcrk">Discord</a> - <a href="https://twitter.com/XenophonDAO">Twitter</a> - <a href="https://rebasetokens.app/f-a-q">FAQ</a></i> \u231B\n\n\U0001F4B5 <b>Market Cap:</b> {mcap}\n\U0001F4B0 <b>Price:</b> {price}\n\U0001F5D3 <b>APY:</b> {apy}\n\U0001F512 <b>TVL:</b> {tvl}\n\U0001F4AC <b>Treasury:</b> {treasury}\n\U0001F4CC <b>Backing:</b> {backing}\n\u23F0 <b>Runway:</b> {runway}\n\n\U0001F315 <a href="https://warp.bond/"><b>Warp.Bond</b></a> - The Next-Gen Web3 reserve currency ft. NFT Bonds & buildable starships that travel within the Staking #Metaverse\n@warpbond - <a href="https://discord.gg/warpbond">Discord</a> - <a href="https://twitter.com/warpbond">Twitter</a>\nJoin the <a href="https://warpcountdown.com/">Whitelist here!</a> \U0001F315'),
                    "reply_markup": (None, json.dumps(reply_markup.to_dict())),
                    "parse_mode": (None, 'HTML')
            }
        
            requests.post(url='https://api.telegram.org/bot5025889373:AAEGOUROw4deWROTzTR-1v1lDddv2EJFmSQ/sendPhoto', files=data)
            print('Data sent!')

            print('Shutting off Xenophon..')
            s.enter(2, 1, magnet, (s,))
            
        except Exception as errore:

            print(errore)

            data = {"chat_id": "92637783",
                    "text": f'<b>Error</b> on Xenophon Main Chat\n\n {errore}' ,
                    "parse_mode": 'HTML'}

            requests.post(url='https://api.telegram.org/bot5062720103:AAHo_qpQzG5dqRteZ-VgfBYL10_EFF1h6GU/sendMessage', data=data)

            s.enter(2, 1, magnet, (s,))


def magnet(sc):
        try:
            print('Starting MagnetDAO..')
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://app.magnetdao.finance/#/dashboard"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            price = soup.findAll('p', class_='card-value')[0].get_text()
            mcap = soup.findAll('p', class_='card-value')[1].get_text()
            tvl = soup.findAll('p', class_='card-value')[2].get_text()
            apy = soup.findAll('p', class_='card-value')[3].get_text()
            treasury = soup.findAll('p', class_='card-value')[7].get_text()
            backing = soup.findAll('p', class_='card-value')[4].get_text()

            
            
            driver.quit()
            print('MagnetDAO - $MAG', price,'\n', mcap,'\n', tvl, '\n', apy, '\n', treasury, '\n', backing)

            total = {'mcap': mcap, 'price': price, 'tvl':tvl, 'apy':apy, 'treasury':treasury, 'backing':backing}
            

            with open("/home/admin/Desktop/data/mag.json", "w") as f:
                json.dump(total, f, indent=2)

            subprocess.call(['python3', '/home/admin/Desktop/Script/mag.py'])

            keyboard = [
                [
                    InlineKeyboardButton("Chart", url='https://dexscreener.com/avalanche/0xd66b92fd29a6e1f9a1ccb8075a88d955fa4a409d'),
                    InlineKeyboardButton("Dashboard", url='https://app.magnetdao.finance/#/dashboard')
                ]
            ]
             
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            print('Setting up data.')
            data = {
                    'photo': ('mag.png', open('/home/admin/Desktop/ss/mag.png', 'rb')),
                    'action': (None, 'send'),
                    'chat_id': (None, '-1001431327406'),
                    'caption': (None, f'\U0001F48E <b>MagnetDAO - $MAG</b> #AVAX \U0001F48E \n\n\u231B <i>@MagnetDAO - <a href="https://discord.com/invite/magnetdao">Discord</a> - <a href="https://twitter.com/magnet_dao">Twitter</a> - <a href="https://rebasetokens.app/f-a-q">FAQ</a></i> \u231B\n\n\U0001F4B5 <b>Market Cap:</b> {mcap}\n\U0001F4B0 <b>Price:</b> {price}\n\U0001F5D3 <b>APY:</b> {apy}\n\U0001F4AC <b>Treasury:</b> {treasury}\n\U0001F512 <b>TVL:</b> {tvl}\n\U0001F4CC <b>Backing:</b> {backing}\n\n\U0001F315 <a href="https://warp.bond/"><b>Warp.Bond</b></a> - The Next-Gen Web3 reserve currency ft. NFT Bonds & buildable starships that travel within the Staking #Metaverse\n@warpbond - <a href="https://discord.gg/warpbond">Discord</a> - <a href="https://twitter.com/warpbond">Twitter</a>\nJoin the <a href="https://warpcountdown.com/">Whitelist here!</a>  \U0001F315'),
                    "reply_markup": (None, json.dumps(reply_markup.to_dict())),
                    "parse_mode": (None, 'HTML')
            }
        
            requests.post(url='https://api.telegram.org/bot5025889373:AAEGOUROw4deWROTzTR-1v1lDddv2EJFmSQ/sendPhoto', files=data)
            print('Data sent!')

            print('Shutting off MagnetDAO..')
            s.enter(2, 1, karma, (s,))
            
        except Exception as errore:

            print(errore)

            data = {"chat_id": "92637783",
                    "text": f'<b>Error</b> on Magnet Main Chat\n\n {errore}' ,
                    "parse_mode": 'HTML'}

            requests.post(url='https://api.telegram.org/bot5062720103:AAHo_qpQzG5dqRteZ-VgfBYL10_EFF1h6GU/sendMessage', data=data)

            s.enter(2, 1, karma, (s,))


def karma(sc):
        try:
            print('Starting KarmaDAO..')
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://app.karmadao.money/#/stake"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            price = soup.findAll('p', class_='MuiTypography-root colorWhite MuiTypography-body1')[0].get_text()
            mcap = soup.findAll('p', class_='MuiTypography-root MuiTypography-body1')[1].get_text()
            apy = soup.findAll('p', class_='MuiTypography-root colorWhite MuiTypography-body1')[1].get_text()
            roi = soup.findAll('p', class_='MuiTypography-root MuiTypography-body1')[11].get_text()
            
            
            driver.quit()
            print('KarmaDAO - $KARMA', price,'\n', mcap,'\n', apy,'\n', roi)

            total = {'mcap': mcap, 'price': price, 'apy': apy, 'roi': roi}
            

            with open("/home/admin/Desktop/data/karma.json", "w") as f:
                json.dump(total, f, indent=2)

            subprocess.call(['python3', '/home/admin/Desktop/Script/karma.py'])

            keyboard = [
                [
                    InlineKeyboardButton("Chart", url='https://dexscreener.com/avalanche/0xd24d364e93fcbccb3c1ea11a1ba6730f44f2b415'),
                    InlineKeyboardButton("Dashboard", url='https://app.karmadao.money/#/dashboard')
                ]
            ]
             
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            print('Setting up data.')
            data = {
                    'photo': ('karma.png', open('/home/admin/Desktop/ss/karma.png', 'rb')),
                    'action': (None, 'send'),
                    'chat_id': (None, '-1001431327406'),
                    'caption': (None, f'\U0001F48E <b>KarmaDAO - $KARMA</b> #AVAX \U0001F48E \n\n\u231B <i><a href="http://discord.gg/HfsxKMvFxX">Discord</a> - <a href="https://twitter.com/KarmaDAO_">Twitter</a> - <a href="https://rebasetokens.app/f-a-q">FAQ</a></i> \u231B\n\n\U0001F4B5 <b>Market Cap:</b> {mcap}\n\U0001F4B0 <b>Price:</b> {price}\n\U0001F5D3 <b>APY:</b> {apy}\n\U0001F4AC <b>ROI 5-Days:</b> {roi}\n\n\U0001F315 <a href="https://warp.bond/"><b>Warp.Bond</b></a> - The Next-Gen Web3 reserve currency ft. NFT Bonds & buildable starships that travel within the Staking #Metaverse\n@warpbond - <a href="https://discord.gg/warpbond">Discord</a> - <a href="https://twitter.com/warpbond">Twitter</a>\nJoin the <a href="https://warpcountdown.com/">Whitelist here!</a>  \U0001F315'),
                    "reply_markup": (None, json.dumps(reply_markup.to_dict())),
                    "parse_mode": (None, 'HTML')
            }
        
            requests.post(url='https://api.telegram.org/bot5025889373:AAEGOUROw4deWROTzTR-1v1lDddv2EJFmSQ/sendPhoto', files=data)
            print('Data sent!')

            print('Shutting off KarmaDAO..')
            s.enter(2, 1, vesq, (s,))
            
        except Exception as errore:

            print(errore)

            data = {"chat_id": "92637783",
                    "text": f'<b>Error</b> on Karma Main Chat\n\n {errore}' ,
                    "parse_mode": 'HTML'}

            requests.post(url='https://api.telegram.org/bot5062720103:AAHo_qpQzG5dqRteZ-VgfBYL10_EFF1h6GU/sendMessage', data=data)

            s.enter(2, 1, vesq, (s,))



def vesq(sc):
        try:
            print('Starting Vesq..')
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://app.vesq.io/#/dashboard"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            price = soup.findAll('h4', class_='MuiTypography-root MuiTypography-h4 MuiTypography-colorTextPrimary')[1].get_text()
            mcap = soup.findAll('h4', class_='MuiTypography-root MuiTypography-h4 MuiTypography-colorTextPrimary')[0].get_text()
            tvl = soup.findAll('h4', class_='MuiTypography-root MuiTypography-h4 MuiTypography-colorTextPrimary')[3].get_text()
            apy = soup.findAll('h4', class_='MuiTypography-root MuiTypography-h4 MuiTypography-colorTextPrimary')[4].get_text()
            treasury = soup.findAll('h4', class_='MuiTypography-root MuiTypography-h4 MuiTypography-colorTextPrimary')[2].get_text()
            backing = soup.findAll('h4', class_='MuiTypography-root MuiTypography-h4 MuiTypography-colorTextPrimary')[6].get_text()
            runway = soup.findAll('h4', class_='MuiTypography-root MuiTypography-h4 MuiTypography-colorTextPrimary')[7].get_text()
            
            
            driver.quit()
            print('Vesq - $VESQ', price,'\n', mcap,'\n', tvl,'\n', apy,'\n', treasury,'\n', backing, '\n', runway)

            total = {'mcap': mcap, 'price': price, 'tvl': tvl, 'apy': apy, 'treasury': treasury, 'backing': backing, 'runway': runway}
            

            with open("/home/admin/Desktop/data/vesq.json", "w") as f:
                json.dump(total, f, indent=2)

            subprocess.call(['python3', '/home/admin/Desktop/Script/vesq.py'])

            keyboard = [
                [
                    InlineKeyboardButton("Chart", url='https://dexscreener.com/polygon/0x5cf66ceaf7f6395642cd11b5929499229edef531'),
                    InlineKeyboardButton("Dashboard", url='https://app.vesq.io/#/dashboard')
                ]
            ]
             
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            print('Setting up data.')
            data = {
                    'photo': ('vesq.png', open('/home/admin/Desktop/ss/vesq.png', 'rb')),
                    'action': (None, 'send'),
                    'chat_id': (None, '-1001431327406'),
                    'caption': (None, f'\U0001F48E <b>Vesq - $VSQ</b> #Polygon \U0001F48E \n\n\u231B <i><a href="https://discord.gg/vesq">Discord</a> - <a href="https://twitter.com/VESQHQ">Twitter</a> - <a href="https://rebasetokens.app/f-a-q">FAQ</a></i> \u231B\n\n\U0001F4B5 <b>Market Cap:</b> {mcap}\n\U0001F4B0 <b>Price:</b> {price}\n\U0001F5D3 <b>APY:</b> {apy}\n\U0001F512 <b>TVL:</b> {tvl}\n\U0001F4AC <b>Treasury:</b> {treasury}\n\U0001F4CC <b>Backing:</b> {backing}\n\u23F0 <b>Runway:</b> {runway}\n\n\U0001F315 <a href="https://warp.bond/"><b>Warp.Bond</b></a> - The Next-Gen Web3 reserve currency ft. NFT Bonds & buildable starships that travel within the Staking #Metaverse\n@warpbond - <a href="https://discord.gg/warpbond">Discord</a> - <a href="https://twitter.com/warpbond">Twitter</a>\nJoin the <a href="https://warpcountdown.com/">Whitelist here!</a>  \U0001F315'),
                    "reply_markup": (None, json.dumps(reply_markup.to_dict())),
                    "parse_mode": (None, 'HTML')
            }
        
            requests.post(url='https://api.telegram.org/bot5025889373:AAEGOUROw4deWROTzTR-1v1lDddv2EJFmSQ/sendPhoto', files=data)
            print('Data sent!')

            print('Shutting off Vesq..')
            s.enter(2, 1, whale, (s,))
            
        except Exception as errore:

            print(errore)

            data = {"chat_id": "92637783",
                    "text": f'<b>Error</b> on Vesq Main Chat\n\n {errore}' ,
                    "parse_mode": 'HTML'}

            requests.post(url='https://api.telegram.org/bot5062720103:AAHo_qpQzG5dqRteZ-VgfBYL10_EFF1h6GU/sendMessage', data=data)

            s.enter(2, 1, whale, (s,))


def whale(sc):
        try:
            print('Starting Whale..')
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://whale.loans/dashboard"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            price = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[0].get_text()
            mcap = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[7].get_text()
            apy = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[6].get_text()
            treasury = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[4].get_text()
            backing = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[3].get_text()

            tvl = loans()
            
            driver.quit()
            print('WhaleLoans - $HUMP  ', price,'\n', mcap,'\n', tvl,'\n', apy,'\n', treasury,'\n', backing, '\n')

            total = {'mcap': mcap, 'price': price, 'tvl': tvl, 'apy': apy, 'treasury': treasury, 'backing': backing}
            

            with open("/home/admin/Desktop/data/hump.json", "w") as f:
                json.dump(total, f, indent=2)

            subprocess.call(['python3', '/home/admin/Desktop/Script/hump.py'])

            keyboard = [
                [
                    InlineKeyboardButton("Chart", url='https://dexscreener.com/bsc/0x2023ee355a2c01f084589f87b4fb9a113f940207'),
                    InlineKeyboardButton("Dashboard", url='https://whale.loans/dashboard')
                ]
            ]
             
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            print('Setting up data.')
            data = {
                    'photo': ('hump.png', open('/home/admin/Desktop/ss/hump.png', 'rb')),
                    'action': (None, 'send'),
                    'chat_id': (None, '-1001431327406'),
                    'caption': (None, f'\U0001F48E <b>WhaleLoans - $HUMP</b> #BSC \U0001F48E \n\n\u231B <i><a href="https://discord.com/invite/rFzNx4wRtK">Discord</a> - <a href="https://twitter.com/WhaleLoans">Twitter</a> - <a href="https://rebasetokens.app/f-a-q">FAQ</a></i> \u231B\n\n\U0001F4B5 <b>Market Cap:</b> {mcap}\n\U0001F4B0 <b>Price:</b> {price}\n\U0001F5D3 <b>APY:</b> {apy}\n\U0001F512 <b>TVL:</b> {tvl}\n\U0001F4AC <b>Treasury:</b> {treasury}\n\U0001F4CC <b>Backing:</b> {backing}\n\n\U0001F315 <a href="https://warp.bond/"><b>Warp.Bond</b></a> - The Next-Gen Web3 reserve currency ft. NFT Bonds & buildable starships that travel within the Staking #Metaverse\n@warpbond - <a href="https://discord.gg/warpbond">Discord</a> - <a href="https://twitter.com/warpbond">Twitter</a>\nJoin the <a href="https://warpcountdown.com/">Whitelist here!</a>  \U0001F315'),
                    "reply_markup": (None, json.dumps(reply_markup.to_dict())),
                    "parse_mode": (None, 'HTML')
            }
        
            requests.post(url='https://api.telegram.org/bot5025889373:AAEGOUROw4deWROTzTR-1v1lDddv2EJFmSQ/sendPhoto', files=data)
            print('Data sent!')

            print('Shutting off WhaleLoans..')
            s.enter(2, 1, btrfly, (s,))
            
        except Exception as errore:

            print(errore)

            data = {"chat_id": "92637783",
                    "text": f'<b>Error</b> on WhaleLoans Main Chat\n\n {errore}' ,
                    "parse_mode": 'HTML'}

            requests.post(url='https://api.telegram.org/bot5062720103:AAHo_qpQzG5dqRteZ-VgfBYL10_EFF1h6GU/sendMessage', data=data)

            s.enter(2, 1, btrfly, (s,))


def loans():

            print('Starting Whale..')
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://whale.loans/stake"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            
            tvl = soup.findAll('h4', class_='MuiTypography-root MuiTypography-h4')[1].get_text()
            
            
            driver.quit()
            
            return tvl


def btrfly(sc):
        try:
            print('Starting Redacted..')
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://dexscreener.com/ethereum/0xdf9ab3c649005ebfdf682d2302ca1f673e0d37a2"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            price = soup.find_all('span', {'class' : 'chakra-text css-5sxn50', })[0].get_text()
            liq = soup.find_all('span', {'class' : 'chakra-text css-5sxn50', })[2].get_text()                        
            mcap = soup.find_all('span', {'class' : 'chakra-text css-5sxn50', })[4].get_text()
            vol = soup.find_all('span', {'class' : 'chakra-text css-5sxn50', })[20].get_text()
            
            
            driver.quit()
            print('Redacted - $BTRFLY', price,'\n', mcap,'\n', liq, '\n', vol )

            total = {'mcap': mcap, 'price': price, 'liquidity': liq, 'vol': vol}
            

            with open("/home/admin/Desktop/data/btrfly.json", "w") as f:
                json.dump(total, f, indent=2)

            subprocess.call(['python3', '/home/admin/Desktop/Script/btrfly.py'])

            keyboard = [
                [
                    InlineKeyboardButton("Chart", url='https://dexscreener.com/ethereum/0xdf9ab3c649005ebfdf682d2302ca1f673e0d37a2'),
                    InlineKeyboardButton("Dashboard", url='https://app.redactedcartel.xyz/')
                ]
            ]
             
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            print('Setting up data.')
            data = {
                    'photo': ('btrfly.png', open('/home/admin/Desktop/ss/btrfly.png', 'rb')),
                    'action': (None, 'send'),
                    'chat_id': (None, '-1001431327406'),
                    'caption': (None, f'\U0001F48E <b>Redacted - $BTRFLY</b> #ETH \U0001F48E \n\n\u231B <i><a href="https://discord.gg/RwghRM6Shf">Discord</a> - <a href="https://twitter.com/redactedcartel">Twitter</a> - <a href="https://rebasetokens.app/f-a-q">FAQ</a></i> \u231B\n\n\U0001F4B5 <b>Market Cap:</b> {mcap}\n\U0001F4B0 <b>Price:</b> {price}\n\U0001F5D3 <b>24h Volume:</b> {vol}\n\U0001F4AC <b>Liquidity:</b> {liq}\n\n\U0001F315 <a href="https://warp.bond/"><b>Warp.Bond</b></a> - The Next-Gen Web3 reserve currency ft. NFT Bonds & buildable starships that travel within the Staking #Metaverse\n@warpbond - <a href="https://discord.gg/warpbond">Discord</a> - <a href="https://twitter.com/warpbond">Twitter</a>\nJoin the <a href="https://warpcountdown.com/">Whitelist here!</a>  \U0001F315'),
                    "reply_markup": (None, json.dumps(reply_markup.to_dict())),
                    "parse_mode": (None, 'HTML')
            }
        
            requests.post(url='https://api.telegram.org/bot5025889373:AAEGOUROw4deWROTzTR-1v1lDddv2EJFmSQ/sendPhoto', files=data)
            print('Data sent!')

            print('Shutting off Redacted..')
            s.enter(2, 1, prxy, (s,))
            
        except Exception as errore:

            print(errore)

            data = {"chat_id": "92637783",
                    "text": f'<b>Error</b> on Redacted Main Chat\n\n {errore}' ,
                    "parse_mode": 'HTML'}

            requests.post(url='https://api.telegram.org/bot5062720103:AAHo_qpQzG5dqRteZ-VgfBYL10_EFF1h6GU/sendMessage', data=data)

            s.enter(2, 1, prxy, (s,))



def prxy(sc):
        try:
            print('Starting Proxy..')
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://dexscreener.com/polygon/0x5428212fbb75046d6270c0bef4bc49882e2bb6a9"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            price = soup.find_all('span', {'class' : 'chakra-text css-5sxn50', })[0].get_text()
            liq = soup.find_all('span', {'class' : 'chakra-text css-5sxn50', })[2].get_text()                        
            mcap = soup.find_all('span', {'class' : 'chakra-text css-5sxn50', })[4].get_text()
            vol = soup.find_all('span', {'class' : 'chakra-text css-5sxn50', })[20].get_text()
            
            
            driver.quit()
            print('BTC Proxy - $PRXY', price,'\n' , mcap,'\n', liq, '\n', vol )

            total = {'mcap': mcap, 'price': price, 'liquidity': liq, 'vol': vol}
            

            with open("/home/admin/Desktop/data/prxy.json", "w") as f:
                json.dump(total, f, indent=2)

            subprocess.call(['python3', '/home/admin/Desktop/Script/prxy.py'])

            keyboard = [
                [
                    InlineKeyboardButton("Chart", url='https://dexscreener.com/polygon/0x5428212fbb75046d6270c0bef4bc49882e2bb6a9'),
                    InlineKeyboardButton("Dashboard", url='https://app.prxy.fi/#/stake')
                ]
            ]
             
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            print('Setting up data.')
            data = {
                    'photo': ('prxy.png', open('/home/admin/Desktop/ss/prxy.png', 'rb')),
                    'action': (None, 'send'),
                    'chat_id': (None, '-1001431327406'),
                    'caption': (None, f'\U0001F48E <b>BTC Proxy - $PRXY</b> #Polygon \U0001F48E \n\n\u231B <i>@BTC_Proxy_Support - <a href="https://discord.gg/JVHUbREbBU">Discord</a> - <a href="https://twitter.com/BTC_proxy">Twitter</a> - <a href="https://rebasetokens.app/f-a-q">FAQ</a></i> \u231B\n\n\U0001F4B5 <b>Market Cap:</b> {mcap}\n\U0001F4B0 <b>Price:</b> {price}\n\U0001F5D3 <b>24h Volume:</b> {vol}\n\U0001F4AC <b>Liquidity:</b> {liq}\n\n\U0001F315 <a href="https://warp.bond/"><b>Warp.Bond</b></a> - The Next-Gen Web3 reserve currency ft. NFT Bonds & buildable starships that travel within the Staking #Metaverse\n@warpbond - <a href="https://discord.gg/warpbond">Discord</a> - <a href="https://twitter.com/warpbond">Twitter</a>\nJoin the <a href="https://warpcountdown.com/">Whitelist here!</a>  \U0001F315'),
                    "reply_markup": (None, json.dumps(reply_markup.to_dict())),
                    "parse_mode": (None, 'HTML')
            }
        
            requests.post(url='https://api.telegram.org/bot5025889373:AAEGOUROw4deWROTzTR-1v1lDddv2EJFmSQ/sendPhoto', files=data)
            print('Data sent!')

            print('Shutting off Proxy..')
            s.enter(2, 1, sierra, (s,))
            
        except Exception as errore:

            print(errore)

            data = {"chat_id": "92637783",
                    "text": f'<b>Error</b> on Proxy Main Chat\n\n {errore}' ,
                    "parse_mode": 'HTML'}

            requests.post(url='https://api.telegram.org/bot5062720103:AAHo_qpQzG5dqRteZ-VgfBYL10_EFF1h6GU/sendMessage', data=data)

            s.enter(2, 1, sierra, (s,))



def sierra(sc):
        try:
            print('Starting SierraDAO..')
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://app.sierra.money/#/dashboard"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            price = soup.findAll('p', class_='card-value')[1].get_text()
            mcap = soup.findAll('p', class_='card-value')[2].get_text()
            tvl = soup.findAll('p', class_='card-value')[3].get_text()
            apy = soup.findAll('p', class_='card-value')[4].get_text()
            treasury = soup.findAll('p', class_='card-value')[6].get_text()
            
            
            
            driver.quit()
            print('SierraDAO - $SRA', price,'\n', mcap,'\n', tvl,'\n', apy,'\n', treasury,'\n')

            total = {'mcap': mcap, 'price': price, 'tvl': tvl, 'apy': apy, 'treasury': treasury}
            

            with open("/home/admin/Desktop/data/sierra.json", "w") as f:
                json.dump(total, f, indent=2)

            subprocess.call(['python3', '/home/admin/Desktop/Script/sierra.py'])

            keyboard = [
                [
                    InlineKeyboardButton("Chart", url='https://dexscreener.com/avalanche/0xcac0101426fdbfcfe7baff17ddc6652d92540480'),
                    InlineKeyboardButton("Dashboard", url='https://app.sierra.money/#/dashboard')
                ]
            ]
             
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            print('Setting up data.')
            data = {
                    'photo': ('sierra.png', open('/home/admin/Desktop/ss/sierra.png', 'rb')),
                    'action': (None, 'send'),
                    'chat_id': (None, '-1001431327406'),
                    'caption': (None, f'\U0001F48E <b>SierraDAO - $SRA</b> #AVAX \U0001F48E \n\n\u231B <i>@sierradao - <a href="https://discord.gg/sierradao">Discord</a> - <a href="https://twitter.com/SierraDAO">Twitter</a> - <a href="https://rebasetokens.app/f-a-q">FAQ</a></i> \u231B\n\n\U0001F4B5 <b>Market Cap:</b> {mcap}\n\U0001F4B0 <b>Price:</b> {price}\n\U0001F5D3 <b>APY:</b> {apy}\n\U0001F512 <b>TVL:</b> {tvl}\n\U0001F4AC <b>Treasury:</b> {treasury}\n\n\U0001F315 <a href="https://warp.bond/"><b>Warp.Bond</b></a> - The Next-Gen Web3 reserve currency ft. NFT Bonds & buildable starships that travel within the Staking #Metaverse\n@warpbond - <a href="https://discord.gg/warpbond">Discord</a> - <a href="https://twitter.com/warpbond">Twitter</a>\nJoin the <a href="https://warpcountdown.com/">Whitelist here!</a>  \U0001F315'),
                    "reply_markup": (None, json.dumps(reply_markup.to_dict())),
                    "parse_mode": (None, 'HTML')
            }
        
            requests.post(url='https://api.telegram.org/bot5025889373:AAEGOUROw4deWROTzTR-1v1lDddv2EJFmSQ/sendPhoto', files=data)
            print('Data sent!')

            print('Shutting off Sierra..')
            s.enter(2, 1, pegasus, (s,))
            
        except Exception as errore:

            print(errore)

            data = {"chat_id": "92637783",
                    "text": f'<b>Error</b> on Sierra Main Chat\n\n {errore}' ,
                    "parse_mode": 'HTML'}

            requests.post(url='https://api.telegram.org/bot5062720103:AAHo_qpQzG5dqRteZ-VgfBYL10_EFF1h6GU/sendMessage', data=data)

            s.enter(2, 1, pegasus, (s,))



def pegasus(sc):
        try:
            print('Starting Pegasus..')
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://dexscreener.com/cronos/0x4ac7fc24eb8cecce40289ac6f2f514cec4af58ef"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            price = soup.find_all('span', {'class' : 'chakra-text css-5sxn50', })[0].get_text()
            liq = soup.find_all('span', {'class' : 'chakra-text css-5sxn50', })[2].get_text()                        
            mcap = soup.find_all('span', {'class' : 'chakra-text css-5sxn50', })[4].get_text()
            vol = soup.find_all('span', {'class' : 'chakra-text css-5sxn50', })[20].get_text()
            
            
            
            driver.quit()
            print('PegasusDAO - $SUS', price,'\n', mcap,'\n', vol, '\n', liq)

            total = {'mcap': mcap, 'price': price, 'vol': vol, 'liq': liq}
            

            with open("/home/admin/Desktop/data/pegasus.json", "w") as f:
                json.dump(total, f, indent=2)

            subprocess.call(['python3', '/home/admin/Desktop/Script/pegasus.py'])

            keyboard = [
                [
                    InlineKeyboardButton("Chart", url='https://dexscreener.com/cronos/0x4ac7fc24eb8cecce40289ac6f2f514cec4af58ef'),
                    InlineKeyboardButton("Dashboard", url='https://app.pegasusdao.finance/#/dashboard')
                ]
            ]
             
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            print('Setting up data.')
            data = {
                    'photo': ('pegasus.png', open('/home/admin/Desktop/ss/pegasus.png', 'rb')),
                    'action': (None, 'send'),
                    'chat_id': (None, '-1001431327406'),
                    'caption': (None, f'\U0001F48E <b>PegasusDAO - $SUS</b> #Cronos \U0001F48E \n\n\u231B <i>@pegasusdaodiscussion - <a href="https://discord.gg/pegasusdao">Discord</a> - <a href="https://twitter.com/pegasusdaofi">Twitter</a> - <a href="https://rebasetokens.app/f-a-q">FAQ</a></i> \u231B\n\n\U0001F4B5 <b>Market Cap:</b> {mcap}\n\U0001F4B0 <b>Price:</b> {price}\n\U0001F5D3 <b>24h Volume:</b> {vol}\n\U0001F512 <b>Liquidity:</b> {liq}\n\n\U0001F315 <a href="https://warp.bond/"><b>Warp.Bond</b></a> - The Next-Gen Web3 reserve currency ft. NFT Bonds & buildable starships that travel within the Staking #Metaverse\n@warpbond - <a href="https://discord.gg/warpbond">Discord</a> - <a href="https://twitter.com/warpbond">Twitter</a>\nJoin the <a href="https://warpcountdown.com/">Whitelist here!</a>  \U0001F315'),
                    "reply_markup": (None, json.dumps(reply_markup.to_dict())),
                    "parse_mode": (None, 'HTML')
            }
        
            requests.post(url='https://api.telegram.org/bot5025889373:AAEGOUROw4deWROTzTR-1v1lDddv2EJFmSQ/sendPhoto', files=data)
            print('Data sent!')

            print('Shutting off Pegasus..')
            s.enter(2, 1, snowbank, (s,))
            
        except Exception as errore:

            print(errore)

            data = {"chat_id": "92637783",
                    "text": f'<b>Error</b> on Pegasus Main Chat\n\n {errore}' ,
                    "parse_mode": 'HTML'}

            requests.post(url='https://api.telegram.org/bot5062720103:AAHo_qpQzG5dqRteZ-VgfBYL10_EFF1h6GU/sendMessage', data=data)

            s.enter(2, 1, snowbank, (s,))



def snowbank(sc):
        try:
            print('Starting Snowbank..')
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://dapp.snowbank.finance/#/dashboard"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            price = soup.findAll('p', class_='card-value')[2].get_text()
            mcap = soup.findAll('p', class_='card-value')[4].get_text()
            tvl = soup.findAll('p', class_='card-value')[5].get_text()
            apy = soup.findAll('p', class_='card-value')[6].get_text()
            treasury = soup.findAll('p', class_='card-value')[8].get_text()
            runway = soup.findAll('p', class_='card-value')[9].get_text()
            
            
            driver.quit()
            print('SnowbankDAO - $SB', price,'\n', mcap,'\n', tvl,'\n', apy,'\n', treasury, '\n', runway)

            total = {'mcap': mcap, 'price': price, 'tvl': tvl, 'apy': apy, 'treasury': treasury, 'runway': runway}
            

            with open("/home/admin/Desktop/data/snowbank.json", "w") as f:
                json.dump(total, f, indent=2)

            subprocess.call(['python3', '/home/admin/Desktop/Script/snowbank.py'])

            keyboard = [
                [
                    InlineKeyboardButton("Chart", url='https://dexscreener.com/avalanche/0x425c45adfb53861e5db8f17d9b072ab60d4404d8'),
                    InlineKeyboardButton("Dashboard", url='https://dapp.snowbank.finance/#/dashboard')
                ]
            ]
             
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            print('Setting up data.')
            data = {
                    'photo': ('time.png', open('/home/admin/Desktop/ss/snowbank.png', 'rb')),
                    'action': (None, 'send'),
                    'chat_id': (None, '-1001431327406'),
                    'caption': (None, f'\U0001F48E <b>SnowbankDAO - $SB</b> #AVAX \U0001F48E \n\n\u231B <i><a href="https://t.me/joinchat/rlVyL0qVGcI5NWZk">Telegram</a> - <a href="https://discord.gg/MCzhPPFXqG">Discord</a> - <a href="https://twitter.com/SnowbankDAO">Twitter</a> - <a href="https://rebasetokens.app/f-a-q">FAQ</a></i> \u231B\n\n\U0001F4B5 <b>Market Cap:</b> {mcap}\n\U0001F4B0 <b>Price:</b> {price}\n\U0001F5D3 <b>APY:</b> {apy}\n\U0001F512 <b>TVL:</b> {tvl}\n\U0001F4AC <b>Treasury:</b> {treasury}\n\u23F0 <b>Runway:</b> {runway}\n\n\U0001F315 <a href="https://warp.bond/"><b>Warp.Bond</b></a> - The Next-Gen Web3 reserve currency ft. NFT Bonds & buildable starships that travel within the Staking #Metaverse\n@warpbond - <a href="https://discord.gg/warpbond">Discord</a> - <a href="https://twitter.com/warpbond">Twitter</a>\nJoin the <a href="https://warpcountdown.com/">Whitelist here!</a>  \U0001F315'),
                    "reply_markup": (None, json.dumps(reply_markup.to_dict())),
                    "parse_mode": (None, 'HTML')
            }
        
            requests.post(url='https://api.telegram.org/bot5025889373:AAEGOUROw4deWROTzTR-1v1lDddv2EJFmSQ/sendPhoto', files=data)
            print('Data sent!')

            print('Shutting off Wonderland..')
            s.enter(2, 1, titano, (s,))
            
        except Exception as errore:

            print(errore)

            data = {"chat_id": "92637783",
                    "text": f'<b>Error</b> on Snowbank Main Chat\n\n {errore}' ,
                    "parse_mode": 'HTML'}

            requests.post(url='https://api.telegram.org/bot5062720103:AAHo_qpQzG5dqRteZ-VgfBYL10_EFF1h6GU/sendMessage', data=data)

            s.enter(2, 1, titano, (s,))


def titano(sc):
        try:
            print('Starting Titano..')
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://app.titano.finance/"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            mcap = soup.find('div', class_='bx').get_text()
            price = soup.find('div', class_='info').get_text()
            apy = soup.find('div', class_='bx rate').get_text()
            
            results = titvalues()
            liq = results[0]
            vol = results[1]

            
            driver.quit()
            print('Titano - $TITANO', price,'\n', mcap, '\n', apy,'\n', liq, '\n', vol)

            total = {'mcap': mcap, 'price': price, 'apy': apy, 'liq': liq, 'vol': vol}
            

            with open("/home/admin/Desktop/data/titano.json", "w") as f:
                json.dump(total, f, indent=2)

            subprocess.call(['python3', '/home/admin/Desktop/Script/titano.py'])

            keyboard = [
                [
                    InlineKeyboardButton("Chart", url='https://dexscreener.com/bsc/0x44f382cec44c33067cb12fcfc08457eb6734be02'),
                    InlineKeyboardButton("Dashboard", url='https://app.titano.finance/')
                ]
            ]
             
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            print('Setting up data.')
            data = {
                    'photo': ('titano.png', open('/home/admin/Desktop/ss/titano.png', 'rb')),
                    'action': (None, 'send'),
                    'chat_id': (None, '-1001431327406'),
                    'caption': (None, f'\U0001F48E <b>Titano Finance - $TITANO</b> #BSC \U0001F48E \n\n\u231B <i>@titano_finance - <a href="https://discord.gg/xxdS792B7q">Discord</a> - <a href="https://twitter.com/TitanoFinance">Twitter</a> - <a href="https://rebasetokens.app/f-a-q">FAQ</a></i> \u231B\n\n\U0001F4B5 <b>Market Cap:</b> {mcap}\n\U0001F4B0 <b>Price:</b> {price}\n\U0001F5D3 <b>APY:</b> {apy}\n\U0001F512 <b>Liquidity:</b> {liq}\n\U0001F4AC <b>24h Volume:</b> {vol}\n\n\U0001F315 <a href="https://warp.bond/"><b>Warp.Bond</b></a> - The Next-Gen Web3 reserve currency ft. NFT Bonds & buildable starships that travel within the Staking #Metaverse\n@warpbond - <a href="https://discord.gg/warpbond">Discord</a> - <a href="https://twitter.com/warpbond">Twitter</a>\nJoin the <a href="https://warpcountdown.com/">Whitelist here!</a>  \U0001F315'),
                    "reply_markup": (None, json.dumps(reply_markup.to_dict())),
                    "parse_mode": (None, 'HTML')
            }
        
            requests.post(url='https://api.telegram.org/bot5025889373:AAEGOUROw4deWROTzTR-1v1lDddv2EJFmSQ/sendPhoto', files=data)
            print('Data sent!')

            print('Shutting off Titano..')
            s.enter(2, 1, empyr, (s,))
            
        except Exception as errore:

            print(errore)

            data = {"chat_id": "92637783",
                    "text": f'<b>Error</b> on Titano Main Chat\n\n {errore}' ,
                    "parse_mode": 'HTML'}

            requests.post(url='https://api.telegram.org/bot5062720103:AAHo_qpQzG5dqRteZ-VgfBYL10_EFF1h6GU/sendMessage', data=data)

            s.enter(2, 1, empyr, (s,))



def titvalues():

            print('Starting Titano..')
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://dexscreener.com/bsc/0x44f382cec44c33067cb12fcfc08457eb6734be02"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            liq = soup.find_all('span', {'class' : 'chakra-text css-5sxn50', })[2].get_text()                        
            vol = soup.find_all('span', {'class' : 'chakra-text css-5sxn50', })[20].get_text()
            
            
            driver.quit()
            
            return liq, vol



def empyr(sc):
        try:
            print('Starting Empyrean..')
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://dexscreener.com/aurora/0x6e46c69fe35ef5bb78d7f35d92645c74245a6567"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            price = soup.find_all('span', {'class' : 'chakra-text css-5sxn50', })[0].get_text()
            liq = soup.find_all('span', {'class' : 'chakra-text css-5sxn50', })[2].get_text()                        
            mcap = soup.find_all('span', {'class' : 'chakra-text css-5sxn50', })[4].get_text()
            vol = soup.find_all('span', {'class' : 'chakra-text css-5sxn50', })[20].get_text()
            
            
            
            driver.quit()
            print('Empyrean - $EMPYR', price,'\n', mcap,'\n', liq, '\n', vol)

            total = {'mcap': mcap, 'price': price, 'liq': liq, 'vol': vol}
            

            with open("/home/admin/Desktop/data/empyr.json", "w") as f:
                json.dump(total, f, indent=2)

            subprocess.call(['python3', '/home/admin/Desktop/Script/empyr.py'])

            keyboard = [
                [
                    InlineKeyboardButton("Chart", url='https://dexscreener.com/avalanche/0x113f413371fc4cc4c9d6416cf1de9dfd7bf747df'),
                    InlineKeyboardButton("Dashboard", url='https://app.empyrean.fi/#/dashboard')
                ]
            ]
             
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            print('Setting up data.')
            data = {
                    'photo': ('empyr.png', open('/home/admin/Desktop/ss/empyr.png', 'rb')),
                    'action': (None, 'send'),
                    'chat_id': (None, '-1001431327406'),
                    'caption': (None, f'\U0001F48E <b>EmpyreanDAO - $EMPYR</b> #Aurora \U0001F48E \n\n\u231B <i><a href="https://discord.gg/empyreandao">Discord</a> - <a href="https://twitter.com/empyreanfi">Twitter</a> - <a href="https://rebasetokens.app/f-a-q">FAQ</a></i> \u231B\n\n\U0001F4B5 <b>Market Cap:</b> {mcap}\n\U0001F4B0 <b>Price:</b> {price}\n\U0001F512 <b>Liquidity:</b> {liq}\n\U0001F4AC <b>24h Volume:</b> {vol}\n\n\U0001F315 <a href="https://warp.bond/"><b>Warp.Bond</b></a> - The Next-Gen Web3 reserve currency ft. NFT Bonds & buildable starships that travel within the Staking #Metaverse\n@warpbond - <a href="https://discord.gg/warpbond">Discord</a> - <a href="https://twitter.com/warpbond">Twitter</a>\nJoin the <a href="https://warpcountdown.com/">Whitelist here!</a>  \U0001F315'),
                    "reply_markup": (None, json.dumps(reply_markup.to_dict())),
                    "parse_mode": (None, 'HTML')
            }
        
            requests.post(url='https://api.telegram.org/bot5025889373:AAEGOUROw4deWROTzTR-1v1lDddv2EJFmSQ/sendPhoto', files=data)
            print('Data sent!')

            print('Shutting off Empyrean..')
            s.enter(2, 1, minotaur, (s,))
            
        except Exception as errore:

            print(errore)

            data = {"chat_id": "92637783",
                    "text": f'<b>Error</b> on Wonder Main Chat\n\n {errore}' ,
                    "parse_mode": 'HTML'}

            requests.post(url='https://api.telegram.org/bot5062720103:AAHo_qpQzG5dqRteZ-VgfBYL10_EFF1h6GU/sendMessage', data=data)

            s.enter(2, 1, minotaur, (s,))



def minotaur(sc):
        try:
            print('Starting Minotaur..')
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://minotaur.money/#/dashboard"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            price = soup.findAll('p', class_='card-value')[0].get_text()
            mcap = soup.findAll('p', class_='card-value')[1].get_text()
            tvl = soup.findAll('p', class_='card-value')[2].get_text()
            apy = soup.findAll('p', class_='card-value')[3].get_text()
            treasury = soup.findAll('p', class_='card-value')[5].get_text()
            backing = soup.findAll('p', class_='card-value')[6].get_text()
            runway = soup.findAll('p', class_='card-value')[7].get_text()
            
            
            driver.quit()
            print('Minotaur - $MINO', price,'\n', mcap,'\n', tvl,'\n', apy,'\n', treasury,'\n', backing, '\n', runway)

            total = {'mcap': mcap, 'price': price, 'tvl': tvl, 'apy': apy, 'treasury': treasury, 'backing': backing, 'runway': runway}
            

            with open("/home/admin/Desktop/data/mino.json", "w") as f:
                json.dump(total, f, indent=2)

            subprocess.call(['python3', '/home/admin/Desktop/Script/mino.py'])

            keyboard = [
                [
                    InlineKeyboardButton("Chart", url='https://dexscreener.com/cronos/0xf5a5f547612e95c688971fb68334a80ceb3c542b'),
                    InlineKeyboardButton("Dashboard", url='https://minotaur.money/#/dashboard')
                ]
            ]
             
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            print('Setting up data.')
            data = {
                    'photo': ('mino.png', open('/home/admin/Desktop/ss/mino.png', 'rb')),
                    'action': (None, 'send'),
                    'chat_id': (None, '-1001431327406'),
                    'caption': (None, f'\U0001F48E <b>Minotaur Money - $MINO</b> #Cronos \U0001F48E \n\n\u231B <i>@MinotaurMoney - <a href="https://discord.gg/cQSNDEFC3T">Discord</a> - <a href="https://twitter.com/Minotaur_Money">Twitter</a> - <a href="https://rebasetokens.app/f-a-q">FAQ</a></i> \u231B\n\n\U0001F4B5 <b>Market Cap:</b> {mcap}\n\U0001F4B0 <b>Price:</b> {price}\n\U0001F5D3 <b>APY:</b> {apy}\n\U0001F512 <b>TVL:</b> {tvl}\n\U0001F4AC <b>Treasury:</b> {treasury}\n\U0001F4CC <b>Backing:</b> {backing}\n\u23F0 <b>Runway:</b> {runway}\n\n\U0001F315 <a href="https://warp.bond/"><b>Warp.Bond</b></a> - The Next-Gen Web3 reserve currency ft. NFT Bonds & buildable starships that travel within the Staking #Metaverse\n@warpbond - <a href="https://discord.gg/warpbond">Discord</a> - <a href="https://twitter.com/warpbond">Twitter</a>\nJoin the <a href="https://warpcountdown.com/">Whitelist here!</a>  \U0001F315'),
                    "reply_markup": (None, json.dumps(reply_markup.to_dict())),
                    "parse_mode": (None, 'HTML')
            }
        
            requests.post(url='https://api.telegram.org/bot5025889373:AAEGOUROw4deWROTzTR-1v1lDddv2EJFmSQ/sendPhoto', files=data)
            print('Data sent!')

            print('Shutting off Minotaur..')
            s.enter(2, 1, samo, (s,))
            
        except Exception as errore:

            print(errore)

            data = {"chat_id": "92637783",
                    "text": f'<b>Error</b> on Minotaur Main Chat\n\n {errore}' ,
                    "parse_mode": 'HTML'}

            requests.post(url='https://api.telegram.org/bot5062720103:AAHo_qpQzG5dqRteZ-VgfBYL10_EFF1h6GU/sendMessage', data=data)

            s.enter(2, 1, samo, (s,))


def samo(sc):
        try:
            print('Starting samoDAO..')
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://www.samodao.finance/dashboard"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            price = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[0].get_text()
            mcap = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[7].get_text()
            apy = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[6].get_text()
            treasury = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[4].get_text()
            backing = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[3].get_text()

            
            
            driver.quit()
            print('SamoDAO - $samoDAO', price,'\n', mcap,'\n', apy,'\n', treasury,'\n', backing, '\n')

            total = {'mcap': mcap, 'price': price, 'apy': apy, 'treasury': treasury, 'backing': backing}
            

            with open("/home/admin/Desktop/data/samo.json", "w") as f:
                json.dump(total, f, indent=2)

            subprocess.call(['python3', '/home/admin/Desktop/Script/samo.py'])

            keyboard = [
                [
                    InlineKeyboardButton("Chart", url='https://dexscreener.com/bsc/0x4a49858b15f934306725b32582ffa55f95d9f90a'),
                    InlineKeyboardButton("Dashboard", url='https://www.samodao.finance/dashboard')
                ]
            ]
             
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            print('Setting up data.')
            data = {
                    'photo': ('samo.png', open('/home/admin/Desktop/ss/samo.png', 'rb')),
                    'action': (None, 'send'),
                    'chat_id': (None, '-1001431327406'),
                    'caption': (None, f'\U0001F48E <b>samoDAO - $samoDAO</b> #BSC \U0001F48E \n\n\u231B <i>@SamoDAO_Chat - <a href="https://discord.gg/brMvUvb8pY">Discord</a> - <a href="https://twitter.com/samoDAO_finance">Twitter</a> - <a href="https://rebasetokens.app/f-a-q">FAQ</a></i> \u231B\n\n\U0001F4B5 <b>Market Cap:</b> {mcap}\n\U0001F4B0 <b>Price:</b> {price}\n\U0001F5D3 <b>APY:</b> {apy}\n\U0001F4AC <b>Treasury:</b> {treasury}\n\U0001F4CC <b>Backing:</b> {backing}\n\n\U0001F315 <a href="https://warp.bond/"><b>Warp.Bond</b></a> - The Next-Gen Web3 reserve currency ft. NFT Bonds & buildable starships that travel within the Staking #Metaverse\n@warpbond - <a href="https://discord.gg/warpbond">Discord</a> - <a href="https://twitter.com/warpbond">Twitter</a>\nJoin the <a href="https://warpcountdown.com/">Whitelist here!</a>  \U0001F315'),
                    "reply_markup": (None, json.dumps(reply_markup.to_dict())),
                    "parse_mode": (None, 'HTML')
            }
        
            requests.post(url='https://api.telegram.org/bot5025889373:AAEGOUROw4deWROTzTR-1v1lDddv2EJFmSQ/sendPhoto', files=data)
            print('Data sent!')

            print('Shutting off samoDAO..')
            s.enter(2, 1, cleo, (s,))
            
        except Exception as errore:

            print(errore)

            data = {"chat_id": "92637783",
                    "text": f'<b>Error</b> on samoDAO Main Chat\n\n {errore}' ,
                    "parse_mode": 'HTML'}

            requests.post(url='https://api.telegram.org/bot5062720103:AAHo_qpQzG5dqRteZ-VgfBYL10_EFF1h6GU/sendMessage', data=data)

            s.enter(2, 1, cleo, (s,))




def cleo(sc):
        try:
            print('Starting Cleopatra..')
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://www.cleopatra-dao.xyz/#/dashboard"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            price = soup.find('p', class_='headerMarketprice').get_text()
            price = price.replace('Current Marketprice CAT-token: ','')
            mcap = soup.findAll('p', class_='dash-value')[0].get_text()
            apy = soup.findAll('p', class_='dash-value')[3].get_text()
            treasury = soup.findAll('p', class_='dash-value')[5].get_text()
            backing = soup.findAll('p', class_='dash-value')[6].get_text()
            tvl = soup.findAll('p', class_='dash-value')[2].get_text()
            runway = soup.findAll('p', class_='dash-value')[7].get_text()

            
            
            driver.quit()
            print('Cleopatra-DAO - $CAT', price,'\n', mcap,'\n', apy,'\n', treasury,'\n', backing, '\n', runway, '\n', tvl)
            
            
            total = {'mcap': mcap, 'price': price, 'apy': apy, 'treasury': treasury, 'backing': backing, 'runway':runway, 'tvl':tvl}
            

            with open("/home/admin/Desktop/data/cleo.json", "w") as f:
                json.dump(total, f, indent=2)

            subprocess.call(['python3', '/home/admin/Desktop/Script/cleo.py'])

            keyboard = [
                [
                    InlineKeyboardButton("Chart", url='https://dexscreener.com/avalanche/0x6a71044647c960afb6bbe758cc444dedfa9349f7'),
                    InlineKeyboardButton("Dashboard", url='https://www.cleopatra-dao.xyz/#/dashboard')
                ]
            ]
             
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            print('Setting up data.')
            data = {
                    'photo': ('cleo.png', open('/home/admin/Desktop/ss/cleo.png', 'rb')),
                    'action': (None, 'send'),
                    'chat_id': (None, '-1001431327406'),
                    'caption': (None, f'\U0001F48E <b>Cleopatra-DAO - $CAT</b> #AVAX \U0001F48E \n\n\u231B <i><a href="https://discord.gg/XR2Pgfc3C4">Discord</a> - <a href="https://twitter.com/Cleopatra_DAO">Twitter</a> - <a href="https://rebasetokens.app/f-a-q">FAQ</a></i> \u231B\n\n\U0001F4B5 <b>Market Cap:</b> {mcap}\n\U0001F4B0 <b>Price:</b> {price}\n\U0001F5D3 <b>APY:</b> {apy}\n\U0001F4AC <b>Treasury:</b> {treasury}\n\U0001F512 <b>TVL:</b> {tvl}\n\U0001F4CC <b>Backing:</b> {backing}\n\u23F0 <b>Runway:</b> {runway}\n\n\U0001F315 <a href="https://warp.bond/"><b>Warp.Bond</b></a> - The Next-Gen Web3 reserve currency ft. NFT Bonds & buildable starships that travel within the Staking #Metaverse\n@warpbond - <a href="https://discord.gg/warpbond">Discord</a> - <a href="https://twitter.com/warpbond">Twitter</a>\nJoin the <a href="https://warpcountdown.com/">Whitelist here!</a>  \U0001F315'),
                    "reply_markup": (None, json.dumps(reply_markup.to_dict())),
                    "parse_mode": (None, 'HTML')
            }
        
            requests.post(url='https://api.telegram.org/bot5025889373:AAEGOUROw4deWROTzTR-1v1lDddv2EJFmSQ/sendPhoto', files=data)
            print('Data sent!')

            print('Shutting off Cleopatra..')
            s.enter(2, 1, volt, (s,))

        except Exception as errore:

            print(errore)

            data = {"chat_id": "92637783",
                    "text": f'<b>Error</b> on Cleopatra Twitter\n\n {errore}' ,
                    "parse_mode": 'HTML'}

            requests.post(url='https://api.telegram.org/bot5062720103:AAHo_qpQzG5dqRteZ-VgfBYL10_EFF1h6GU/sendMessage', data=data)

            s.enter(2, 1, volt, (s,))



def volt(sc):
        try:
            print('Starting Volt..')
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://dexscreener.com/avalanche/0x0d8b232373e0a0ce741d376d42e425e83ea87375"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            price = soup.find_all('span', {'class' : 'chakra-text css-5sxn50', })[0].get_text()
            liq = soup.find_all('span', {'class' : 'chakra-text css-5sxn50', })[2].get_text()                        
            mcap = soup.find_all('span', {'class' : 'chakra-text css-5sxn50', })[4].get_text()
            vol = soup.find_all('span', {'class' : 'chakra-text css-5sxn50', })[20].get_text()
            
            driver.quit()

            results = voltapy()
            apy = results[0]
            tvl = results[1]
            
            print('Asgard Defi - $VOLT', price,'\n', mcap,'\n', apy,'\n', tvl, '\n', liq, '\n', vol)
            
            
            total = {'mcap': mcap, 'price': price, 'apy': apy, 'tvl':tvl, 'liq':liq, 'vol':vol}
            

            with open("/home/admin/Desktop/data/volt.json", "w") as f:
                json.dump(total, f, indent=2)

            subprocess.call(['python3', '/home/admin/Desktop/Script/volt.py'])

            keyboard = [
                [
                    InlineKeyboardButton("Chart", url='https://dexscreener.com/avalanche/0x0d8b232373e0a0ce741d376d42e425e83ea87375'),
                    InlineKeyboardButton("Dashboard", url='https://app.asgarddao.fi/#/odinsvault')
                ]
            ]
             
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            print('Setting up data.')
            data = {
                    'photo': ('volt.png', open('/home/admin/Desktop/ss/volt.png', 'rb')),
                    'action': (None, 'send'),
                    'chat_id': (None, '-1001431327406'),
                    'caption': (None, f'\U0001F48E <b>Asgard Defi - $VOLT</b> #AVAX \U0001F48E \n\n\u231B <i>@asgardsquare - <a href="https://discord.gg/ZdmrAaUG3v">Discord</a> - <a href="https://twitter.com/AsgardDefi">Twitter</a> - <a href="https://rebasetokens.app/f-a-q">FAQ</a></i> \u231B\n\n\U0001F4B5 <b>Market Cap:</b> {mcap}\n\U0001F4B0 <b>Price:</b> {price}\n\U0001F5D3 <b>APY:</b> {apy}\n\U0001F4AC <b>24h Volume:</b> {vol}\n\U0001F512 <b>TVL:</b> {tvl}\n\U0001F4CC <b>Liquidity:</b> {liq}\n\n\U0001F315 <a href="https://warp.bond/"><b>Warp.Bond</b></a> - The Next-Gen Web3 reserve currency ft. NFT Bonds & buildable starships that travel within the Staking #Metaverse\n@warpbond - <a href="https://discord.gg/warpbond">Discord</a> - <a href="https://twitter.com/warpbond">Twitter</a>\nJoin the <a href="https://warpcountdown.com/">Whitelist here!</a>  \U0001F315'),
                    "reply_markup": (None, json.dumps(reply_markup.to_dict())),
                    "parse_mode": (None, 'HTML')
            }
        
            requests.post(url='https://api.telegram.org/bot5025889373:AAEGOUROw4deWROTzTR-1v1lDddv2EJFmSQ/sendPhoto', files=data)
            print('Data sent!')

            print('Shutting off Volt..')
            s.enter(2, 1, glbd, (s,))

        except Exception as errore:

            print(errore)

            data = {"chat_id": "92637783",
                    "text": f'<b>Error</b> on Volt Twitter\n\n {errore}' ,
                    "parse_mode": 'HTML'}

            requests.post(url='https://api.telegram.org/bot5062720103:AAHo_qpQzG5dqRteZ-VgfBYL10_EFF1h6GU/sendMessage', data=data)

            s.enter(2, 1, glbd, (s,))


def voltapy():

            print('Starting Volt..')
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://app.asgarddao.fi/#/forge"
            driver.get(urlone)
            time.sleep(30)
        
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            apy = soup.find_all('p', {'class' : 'stake-card-metrics-value', })[0].get_text()
            tvl = soup.find_all('p', {'class' : 'stake-card-metrics-value', })[1].get_text()                        

            
            driver.quit()
            return apy, tvl  


def glbd(sc):
        try:
            print('Starting BeGlobalDAO..')
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://beglobaldao.finance/#/stake"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            apy = soup.find_all('h4', {'class' : 'MuiTypography-root MuiTypography-h4', })[0].get_text()
            tvl = soup.find_all('h4', {'class' : 'MuiTypography-root MuiTypography-h4', })[1].get_text()                        
            
            
            driver.quit()

            results = beglapy()
            treasury = results[0]
            price = results[1]

           
            print('BeGlobalDAO - $GLBD', price, '\n', apy,'\n', tvl, '\n', treasury)
            
            
            total = {'price': price, 'tvl': tvl, 'apy': apy, 'treasury': treasury}
            

            with open("/home/admin/Desktop/data/glbd.json", "w") as f:
                json.dump(total, f, indent=2)

            subprocess.call(['python3', '/home/admin/Desktop/Script/glbd.py'])

            keyboard = [
                [
                    InlineKeyboardButton("Chart", url='https://dexscreener.com/bsc/0x1df0b759ee5b144852eeb571bba9cca2aec66b35'),
                    InlineKeyboardButton("Dashboard", url='https://beglobaldao.finance/#/stake')
                ]
            ]
             
            reply_markup = InlineKeyboardMarkup(keyboard)

            print('Setting up data.')

            data = {
                    'photo': ('glbd.png', open('/home/admin/Desktop/ss/glbd.png', 'rb')),
                    'action': (None, 'send'),
                    'chat_id': (None, '-1001431327406'),
                    'caption': (None, f'\U0001F48E <b>BeGlobalDAO - $GLBD</b> #BSC \U0001F48E \n\n\u231B <i><a href="https://discord.gg/nHgGKsrk">Discord</a> - <a href="https://twitter.com/Beglobaldefi">Twitter</a> - <a href="https://rebasetokens.app/f-a-q">FAQ</a></i> \u231B\n\n\U0001F4B0 <b>Price:</b> {price}\n\U0001F5D3 <b>APY:</b> {apy}\n\U0001F512 <b>TVL:</b> {tvl}\n\U0001F4AC <b>Treasury:</b> {treasury}\n\n\U0001F315 <a href="https://warp.bond/"><b>Warp.Bond</b></a> - The Next-Gen Web3 reserve currency ft. NFT Bonds & buildable starships that travel within the Staking #Metaverse\n@warpbond - <a href="https://discord.gg/warpbond">Discord</a> - <a href="https://twitter.com/warpbond">Twitter</a>\nJoin the <a href="https://warpcountdown.com/">Whitelist here!</a> \U0001F315'),
                    "reply_markup": (None, json.dumps(reply_markup.to_dict())),
                    "parse_mode": (None, 'HTML')
            }
        
            requests.post(url='https://api.telegram.org/bot5025889373:AAEGOUROw4deWROTzTR-1v1lDddv2EJFmSQ/sendPhoto', files=data)
            
            print('Data sent!')

            print('Shutting off BeGlobalDAO..')
            s.enter(2, 1, immo, (s,))

        except Exception as errore:

            print(errore)

            data = {"chat_id": "92637783",
                    "text": f'<b>Error</b> on BeGlobalDAO Main Chat\n\n {errore}' ,
                    "parse_mode": 'HTML'}

            requests.post(url='https://api.telegram.org/bot5062720103:AAHo_qpQzG5dqRteZ-VgfBYL10_EFF1h6GU/sendMessage', data=data)

            s.enter(2, 1, immo, (s,))    



def beglapy():

            print('Starting BeGlobalDAO..')
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://beglobaldao.finance/#/bonds"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
                             
            treasury = soup.find_all('h4', {'class' : 'MuiTypography-root MuiTypography-h4', })[0].get_text()
            price = soup.find_all('h4', {'class' : 'MuiTypography-root MuiTypography-h4', })[1].get_text()
            
            driver.quit()

            return treasury, price


def immo(sc):
        try:
            print('Starting Immortal..')
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://www.immortaldao.finance/#/dashboard"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            price = soup.findAll('p', class_='card-value')[0].get_text()
            mcap = soup.findAll('p', class_='card-value')[1].get_text()
            tvl = soup.findAll('p', class_='card-value')[4].get_text()
            apy = soup.findAll('p', class_='card-value')[2].get_text()
            treasury = soup.findAll('p', class_='card-value')[6].get_text()
            backing = soup.findAll('p', class_='card-value')[8].get_text()
            runway = soup.findAll('p', class_='card-value')[11].get_text()
            
            
            driver.quit()
            print('ImmortalDAO - $IMMO', price,'\n', mcap,'\n', tvl,'\n', apy,'\n', treasury,'\n', backing, '\n', runway)
            
            
            total = {'mcap': mcap, 'price': price, 'tvl': tvl, 'apy': apy, 'treasury': treasury, 'backing': backing, 'runway': runway}
            

            with open("/home/admin/Desktop/data/immo.json", "w") as f:
                json.dump(total, f, indent=2)

            subprocess.call(['python3', '/home/admin/Desktop/Script/immo.py'])

            keyboard = [
                [
                    InlineKeyboardButton("Chart", url='https://dexscreener.com/celo/0x7d63809ebf83ef54c7ce8ded3591d4e8fc2102ee'),
                    InlineKeyboardButton("Dashboard", url='https://www.immortaldao.finance/#/dashboard')
                ]
            ]
             
            reply_markup = InlineKeyboardMarkup(keyboard)

            print('Setting up data.')

            data = {
                    'photo': ('immortal.png', open('/home/admin/Desktop/ss/immortal.png', 'rb')),
                    'action': (None, 'send'),
                    'chat_id': (None, '-1001431327406'),
                    'caption': (None, f'\U0001F48E <b>ImmortalDAO - $IMMO</b> #CELO \U0001F48E \n\n\u231B <i><a href="https://discord.gg/immortaldao">Discord</a> - <a href="https://twitter.com/ImmortalDAO_Fi">Twitter</a> - <a href="https://rebasetokens.app/f-a-q">FAQ</a></i> \u231B\n\n\U0001F4B5 <b>Market Cap:</b> {mcap}\n\U0001F4B0 <b>Price:</b> {price}\n\U0001F5D3 <b>APY:</b> {apy}\n\U0001F512 <b>TVL:</b> {tvl}\n\U0001F4AC <b>Treasury:</b> {treasury}\n\U0001F4CC <b>Backing:</b> {backing}\n\u23F0 <b>Runway:</b> {runway}\n\n\U0001F315 <a href="https://warp.bond/"><b>Warp.Bond</b></a> - The Next-Gen Web3 reserve currency ft. NFT Bonds & buildable starships that travel within the Staking #Metaverse\n@warpbond - <a href="https://discord.gg/warpbond">Discord</a> - <a href="https://twitter.com/warpbond">Twitter</a>\nJoin the <a href="https://warpcountdown.com/">Whitelist here!</a> \U0001F315'),
                    "reply_markup": (None, json.dumps(reply_markup.to_dict())),
                    "parse_mode": (None, 'HTML')
            }
        
            requests.post(url='https://api.telegram.org/bot5025889373:AAEGOUROw4deWROTzTR-1v1lDddv2EJFmSQ/sendPhoto', files=data)
            
            print('Data sent!')

            print('Shutting off ImmortalDAO..')
            s.enter(2, 1, atlas, (s,))

        except Exception as errore:

            print(errore)

            data = {"chat_id": "92637783",
                    "text": f'<b>Error</b> on Immortal Main Chat\n\n {errore}' ,
                    "parse_mode": 'HTML'}

            requests.post(url='https://api.telegram.org/bot5062720103:AAHo_qpQzG5dqRteZ-VgfBYL10_EFF1h6GU/sendMessage', data=data)

            s.enter(2, 1, atlas, (s,))


def atlas(sc):
        try:
            print('Starting Atlas..')
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://atlantis.autoshark.finance/"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            price = soup.findAll('div', class_='text-sm font-semibold text-white')[0].get_text()
            mcap = soup.findAll('div', class_='text-sm font-semibold text-white')[5].get_text()
            tvl = soup.findAll('div', class_='text-sm font-semibold text-white')[3].get_text()
            treasury = soup.findAll('div', class_='text-sm font-semibold text-white')[6].get_text()
            backing = soup.findAll('div', class_='text-sm font-semibold text-white')[2].get_text()
            
            
            driver.quit()
            print('Atlantis - $ATLAS', price,'\n', mcap,'\n', tvl, '\n', treasury,'\n', backing)
            
            
            total = {'mcap': mcap, 'price': price, 'tvl': tvl, 'treasury': treasury, 'backing': backing}
            

            with open("/home/admin/Desktop/data/atlas.json", "w") as f:
                json.dump(total, f, indent=2)

            subprocess.call(['python3', '/home/admin/Desktop/Script/atlas.py'])

            keyboard = [
                [
                    InlineKeyboardButton("Chart", url='https://dexscreener.com/bsc/0x8ec2dcc0b88ef879c885b0b31e87aba14543a8cd'),
                    InlineKeyboardButton("Dashboard", url='https://atlantis.autoshark.finance/')
                ]
            ]
             
            reply_markup = InlineKeyboardMarkup(keyboard)

            print('Setting up data.')

            data = {
                    'photo': ('atlas.png', open('/home/admin/Desktop/ss/atlas.png', 'rb')),
                    'action': (None, 'send'),
                    'chat_id': (None, '-1001431327406'),
                    'caption': (None, f'\U0001F48E <b>AutoSharkFinance Atlantis - $ATLAS</b> #BSC \U0001F48E \n\n\u231B <i>@AutoSharkFinance - <a href="https://twitter.com/AutoSharkFin">Twitter</a> - <a href="https://rebasetokens.app/f-a-q">FAQ</a></i> \u231B\n\n\U0001F4B5 <b>Market Cap:</b> {mcap}\n\U0001F4B0 <b>Price:</b> {price}\n\U0001F512 <b>TVL:</b> {tvl}\n\U0001F4AC <b>Treasury:</b> {treasury}\n\U0001F4CC <b>Backing:</b> {backing}\n\n\U0001F315 <a href="https://warp.bond/"><b>Warp.Bond</b></a> - The Next-Gen Web3 reserve currency ft. NFT Bonds & buildable starships that travel within the Staking #Metaverse\n@warpbond - <a href="https://discord.gg/warpbond">Discord</a> - <a href="https://twitter.com/warpbond">Twitter</a>\nJoin the <a href="https://warpcountdown.com/">Whitelist here!</a> \U0001F315'),
                    "reply_markup": (None, json.dumps(reply_markup.to_dict())),
                    "parse_mode": (None, 'HTML')
            }
        
            requests.post(url='https://api.telegram.org/bot5025889373:AAEGOUROw4deWROTzTR-1v1lDddv2EJFmSQ/sendPhoto', files=data)
            
            print('Data sent!')

            print('Shutting off Atlas..')
            s.enter(2, 1, asgard, (s,))

        except Exception as errore:

            print(errore)

            data = {"chat_id": "92637783",
                    "text": f'<b>Error</b> on Atlas Main Chat\n\n {errore}' ,
                    "parse_mode": 'HTML'}

            requests.post(url='https://api.telegram.org/bot5062720103:AAHo_qpQzG5dqRteZ-VgfBYL10_EFF1h6GU/sendMessage', data=data)

            s.enter(2, 1, asgard, (s,)) 



def asgard(sc):
        try:
            print('Starting Asgard..')
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://app.asgarddao.live/#/dashboard"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            price = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[1].get_text()
            mcap = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[0].get_text()
            backing = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[4].get_text()
            runway = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[7].get_text()
            
            
            driver.quit()

            results = asgardapy()
            apy = results[0]
            tvl = results[1]

            treasury = asgardtreas()

            print('AsgardDAO - $ASGARD', price,'\n', mcap,'\n', tvl,'\n', apy,'\n', treasury,'\n', backing, '\n', runway)

            
            total = {'mcap': mcap, 'price': price, 'tvl': tvl, 'apy': apy, 'treasury': treasury, 'backing': backing, 'runway': runway}
            

            with open("/home/admin/Desktop/data/asgard.json", "w") as f:
                json.dump(total, f, indent=2)

            subprocess.call(['python3', '/home/admin/Desktop/Script/asgard.py'])

            keyboard = [
                [
                    InlineKeyboardButton("Chart", url='https://dexscreener.com/bsc/0x11ceddd7a64ec79212d8ae9c8b46d23b8b750db0'),
                    InlineKeyboardButton("Dashboard", url='https://app.asgarddao.live/#/dashboard')
                ]
            ]
             
            reply_markup = InlineKeyboardMarkup(keyboard)

            print('Setting up data.')

            data = {
                    'photo': ('asgard.png', open('/home/admin/Desktop/ss/asgard.png', 'rb')),
                    'action': (None, 'send'),
                    'chat_id': (None, '-1001431327406'),
                    'caption': (None, f'\U0001F48E <b>AsgardDAO - $ASGARD</b> #BSC \U0001F48E \n\n\u231B <i>@Asgard_dao - <a href="https://discord.gg/gXevKQJTAx">Discord</a> - <a href="https://twitter.com/asgarddao_">Twitter</a> - <a href="https://rebasetokens.app/f-a-q">FAQ</a></i> \u231B\n\n\U0001F4B5 <b>Market Cap:</b> {mcap}\n\U0001F4B0 <b>Price:</b> {price}\n\U0001F5D3 <b>APY:</b> {apy}\n\U0001F512 <b>TVL:</b> {tvl}\n\U0001F4AC <b>Treasury:</b> {treasury}\n\U0001F4CC <b>Backing:</b> {backing}\n\u23F0 <b>Runway:</b> {runway}\n\n\U0001F315 <a href="https://warp.bond/"><b>Warp.Bond</b></a> - The Next-Gen Web3 reserve currency ft. NFT Bonds & buildable starships that travel within the Staking #Metaverse\n@warpbond - <a href="https://discord.gg/warpbond">Discord</a> - <a href="https://twitter.com/warpbond">Twitter</a>\nJoin the <a href="https://warpcountdown.com/">Whitelist here!</a> \U0001F315'),
                    "reply_markup": (None, json.dumps(reply_markup.to_dict())),
                    "parse_mode": (None, 'HTML')
            }
        
            requests.post(url='https://api.telegram.org/bot5025889373:AAEGOUROw4deWROTzTR-1v1lDddv2EJFmSQ/sendPhoto', files=data)
            
            print('Data sent!')

            print('Shutting off Asgard..')
            s.enter(2, 1, pal, (s,))

        except Exception as errore:

            print(errore)

            data = {"chat_id": "92637783",
                    "text": f'<b>Error</b> on Asgard Main Chat\n\n {errore}' ,
                    "parse_mode": 'HTML'}

            requests.post(url='https://api.telegram.org/bot5062720103:AAHo_qpQzG5dqRteZ-VgfBYL10_EFF1h6GU/sendMessage', data=data)

            s.enter(2, 1, pal, (s,))   



def asgardapy():

            print('Starting Asgard..')
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://app.asgarddao.live/#/stake"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            apy = soup.findAll('h4', class_='MuiTypography-root MuiTypography-h4')[0].get_text()
            tvl = soup.findAll('h4', class_='MuiTypography-root MuiTypography-h4')[1].get_text()

            driver.quit()

            return apy, tvl



def asgardtreas():

            print('Starting Asgard..')
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://app.asgarddao.live/#/bonds"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            treasury = soup.findAll('h4', class_='MuiTypography-root MuiTypography-h4')[0].get_text()

            driver.quit()

            return treasury       



def pal(sc):
        try:
            print('Starting Paladin..')
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://dapp.paladindao.com/#/dashboard"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            price = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[1].get_text()
            mcap = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[0].get_text()
            backing = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[4].get_text()
            
            driver.quit()

            results = palapy()
            apy = results[0]
            tvl = results[1]

            treasury = paltreas()

            print('PaladinDAO - $PAL', price,'\n', mcap,'\n', tvl,'\n', apy,'\n', treasury,'\n', backing)
            
            
            total = {'mcap': mcap, 'price': price, 'tvl': tvl, 'apy': apy, 'treasury': treasury, 'backing': backing}
            

            with open("/home/admin/Desktop/data/pal.json", "w") as f:
                json.dump(total, f, indent=2)

            subprocess.call(['python3', '/home/admin/Desktop/Script/pal.py'])
                
            keyboard = [
                [
                    InlineKeyboardButton("Chart", url='https://dexscreener.com/bsc/0x103900036e483c85ea4748b6733f621b8df21e2d'),
                    InlineKeyboardButton("Dashboard", url='https://dapp.paladindao.com/#/dashboard')
                ]
            ]
             
            reply_markup = InlineKeyboardMarkup(keyboard)

            print('Setting up data.')

            data = {
                    'photo': ('pal.png', open('/home/admin/Desktop/ss/pal.png', 'rb')),
                    'action': (None, 'send'),
                    'chat_id': (None, '-1001431327406'),
                    'caption': (None, f'\U0001F48E <b>PaladinDAO - $PAL</b> #BSC \U0001F48E \n\n\u231B <i><a href="https://discord.gg/paladindao">Discord</a> - <a href="https://twitter.com/DaoPaladin">Twitter</a> - <a href="https://rebasetokens.app/f-a-q">FAQ</a></i> \u231B\n\n\U0001F4B5 <b>Market Cap:</b> {mcap}\n\U0001F4B0 <b>Price:</b> {price}\n\U0001F5D3 <b>APY:</b> {apy}\n\U0001F512 <b>TVL:</b> {tvl}\n\U0001F4AC <b>Treasury:</b> {treasury}\n\U0001F4CC <b>Backing:</b> {backing}\n\n\U0001F315 <a href="https://warp.bond/"><b>Warp.Bond</b></a> - The Next-Gen Web3 reserve currency ft. NFT Bonds & buildable starships that travel within the Staking #Metaverse\n@warpbond - <a href="https://discord.gg/warpbond">Discord</a> - <a href="https://twitter.com/warpbond">Twitter</a>\nJoin the <a href="https://warpcountdown.com/">Whitelist here!</a> \U0001F315'),
                    "reply_markup": (None, json.dumps(reply_markup.to_dict())),
                    "parse_mode": (None, 'HTML')
            }
        
            requests.post(url='https://api.telegram.org/bot5025889373:AAEGOUROw4deWROTzTR-1v1lDddv2EJFmSQ/sendPhoto', files=data)
            
            print('Data sent!')

            print('Shutting off Paladin..')
            s.enter(2, 1, index, (s,))

        except Exception as errore:

            print(errore)

            data = {"chat_id": "92637783",
                    "text": f'<b>Error</b> on Paladin Main Chat\n\n {errore}' ,
                    "parse_mode": 'HTML'}

            requests.post(url='https://api.telegram.org/bot5062720103:AAHo_qpQzG5dqRteZ-VgfBYL10_EFF1h6GU/sendMessage', data=data)

            s.enter(2, 1, index, (s,))


def palapy():
            
            print('Starting Paladin..')
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://dapp.paladindao.com/#/stake"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            
            apy = soup.findAll('h4', class_='MuiTypography-root MuiTypography-h4')[0].get_text()
            tvl = soup.findAll('h4', class_='MuiTypography-root MuiTypography-h4')[1].get_text()
            
            
            driver.quit()
            
            return apy, tvl


def paltreas():
            
            print('Starting Paladin..')
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://dapp.paladindao.com/#/bonds"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            
            treasury = soup.findAll('h4', class_='MuiTypography-root MuiTypography-h4')[0].get_text()
            
            
            driver.quit()
            
            return treasury



def index(sc):
        try:
            print('Starting Index..')
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://app.indexdao.finance/#/dashboard"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            price = soup.findAll('p', class_='card-value')[0].get_text()
            mcap = soup.findAll('p', class_='card-value')[1].get_text()
            tvl = soup.findAll('p', class_='card-value')[3].get_text()
            apy = soup.findAll('p', class_='card-value')[4].get_text()
            treasury = soup.findAll('p', class_='card-value')[6].get_text()
            backing = soup.findAll('p', class_='card-value')[7].get_text()
            runway = soup.findAll('p', class_='card-value')[8].get_text()
            
            
            driver.quit()
            print('IndexDAO - $INDEX', price,'\n', mcap,'\n', tvl,'\n', apy,'\n', treasury,'\n', backing, '\n', runway)
            
            
            total = {'mcap': mcap, 'price': price, 'tvl': tvl, 'apy': apy, 'treasury': treasury, 'backing': backing, 'runway': runway}
            

            with open("/home/admin/Desktop/data/index.json", "w") as f:
                json.dump(total, f, indent=2)

            subprocess.call(['python3', '/home/admin/Desktop/Script/index.py'])
                
            keyboard = [
                [
                    InlineKeyboardButton("Chart", url='https://dexscreener.com/avalanche/0xd7babf820ba35e9dfb59b830292417ec53fbd8c1'),
                    InlineKeyboardButton("Dashboard", url='https://app.indexdao.finance/#/dashboard')
                ]
            ]
             
            reply_markup = InlineKeyboardMarkup(keyboard)

            print('Setting up data.')

            data = {
                    'photo': ('index.png', open('/home/admin/Desktop/ss/index.png', 'rb')),
                    'action': (None, 'send'),
                    'chat_id': (None, '-1001431327406'),
                    'caption': (None, f'\U0001F48E <b>IndexDAO - $INDEX</b> #AVAX \U0001F48E \n\n\u231B <i><a href="https://discord.gg/indexdao">Discord</a> - <a href="https://twitter.com/Index_DAO">Twitter</a> - <a href="https://rebasetokens.app/f-a-q">FAQ</a></i> \u231B\n\n\U0001F4B5 <b>Market Cap:</b> {mcap}\n\U0001F4B0 <b>Price:</b> {price}\n\U0001F5D3 <b>APY:</b> {apy}\n\U0001F512 <b>TVL:</b> {tvl}\n\U0001F4AC <b>Treasury:</b> {treasury}\n\U0001F4CC <b>Backing:</b> {backing}\n\u23F0 <b>Runway:</b> {runway}\n\n\U0001F315 <a href="https://warp.bond/"><b>Warp.Bond</b></a> - The Next-Gen Web3 reserve currency ft. NFT Bonds & buildable starships that travel within the Staking #Metaverse\n@warpbond - <a href="https://discord.gg/warpbond">Discord</a> - <a href="https://twitter.com/warpbond">Twitter</a>\nJoin the <a href="https://warpcountdown.com/">Whitelist here!</a> \U0001F315'),
                    "reply_markup": (None, json.dumps(reply_markup.to_dict())),
                    "parse_mode": (None, 'HTML')
            }
        
            requests.post(url='https://api.telegram.org/bot5025889373:AAEGOUROw4deWROTzTR-1v1lDddv2EJFmSQ/sendPhoto', files=data)
            
            print('Data sent!')

            print('Shutting off Index..')
            s.enter(2, 1, god, (s,))

        except Exception as errore:

            print(errore)

            data = {"chat_id": "92637783",
                    "text": f'<b>Error</b> on Index Main Chat\n\n {errore}' ,
                    "parse_mode": 'HTML'}

            requests.post(url='https://api.telegram.org/bot5062720103:AAHo_qpQzG5dqRteZ-VgfBYL10_EFF1h6GU/sendMessage', data=data)

            s.enter(2, 1, god, (s,))



def god(sc):
        try:
            print('Starting God..')
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://www.gods.so/"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            price = soup.findAll('div', class_='mantine-w5sg59 mantine-Text-root')[0].get_text()
            apy = soup.findAll('div', class_='mantine-w5sg59 mantine-Text-root')[1].get_text()
            mcap = soup.findAll('div', class_='mantine-w5sg59 mantine-Text-root')[2].get_text()
            tvl = soup.findAll('div', class_='mantine-1f6ovmy mantine-Text-root')[0].get_text()
            treasury = soup.findAll('div', class_='mantine-w5sg59 mantine-Text-root')[4].get_text()
            
            
            driver.quit()
            print('GodDAO - $GOD', price,'\n', mcap,'\n', tvl,'\n', apy,'\n', treasury)
            
            
            total = {'mcap': mcap, 'price': price, 'tvl': tvl, 'apy': apy, 'treasury': treasury}
            

            with open("/home/admin/Desktop/data/god.json", "w") as f:
                json.dump(total, f, indent=2)

            subprocess.call(['python3', '/home/admin/Desktop/Script/god.py'])
                
            keyboard = [
                [
                    InlineKeyboardButton("Chart", url='https://birdeye.so/token/9kt93AW5QMjFL6ZxomnSq3FbWiU5ibNeTSgBz9UDFSB6'),
                    InlineKeyboardButton("Dashboard", url='https://www.gods.so/')
                ]
            ]
             
            reply_markup = InlineKeyboardMarkup(keyboard)

            print('Setting up data.')

            data = {
                    'photo': ('god.png', open('/home/admin/Desktop/ss/god.png', 'rb')),
                    'action': (None, 'send'),
                    'chat_id': (None, '-1001431327406'),
                    'caption': (None, f'\U0001F48E <b>GodDAO - $GOD</b> #Solana \U0001F48E \n\n\u231B <i><a href="https://discord.gg/2pvHDdZ5Ue">Discord</a> - <a href="https://twitter.com/gods_sol">Twitter</a> - <a href="https://rebasetokens.app/f-a-q">FAQ</a></i> \u231B\n\n\U0001F4B5 <b>Market Cap:</b> {mcap}\n\U0001F4B0 <b>Price:</b> {price}\n\U0001F5D3 <b>APY:</b> {apy}\n\U0001F512 <b>TVL:</b> {tvl}\n\U0001F4AC <b>Treasury:</b> {treasury}\n\n\U0001F315 <a href="https://warp.bond/"><b>Warp.Bond</b></a> - The Next-Gen Web3 reserve currency ft. NFT Bonds & buildable starships that travel within the Staking #Metaverse\n@warpbond - <a href="https://discord.gg/warpbond">Discord</a> - <a href="https://twitter.com/warpbond">Twitter</a>\nJoin the <a href="https://warpcountdown.com/">Whitelist here!</a> \U0001F315'),
                    "reply_markup": (None, json.dumps(reply_markup.to_dict())),
                    "parse_mode": (None, 'HTML')
            }
        
            requests.post(url='https://api.telegram.org/bot5025889373:AAEGOUROw4deWROTzTR-1v1lDddv2EJFmSQ/sendPhoto', files=data)
            
            print('Data sent!')

            print('Shutting off God..')
            s.enter(2, 1, noah, (s,))

        except Exception as errore:

            print(errore)

            data = {"chat_id": "92637783",
                    "text": f'<b>Error</b> on God Main Chat\n\n {errore}' ,
                    "parse_mode": 'HTML'}

            requests.post(url='https://api.telegram.org/bot5062720103:AAHo_qpQzG5dqRteZ-VgfBYL10_EFF1h6GU/sendMessage', data=data)

            s.enter(2, 1, noah, (s,))



def noah(sc):
        try:
            print('Starting NoahArkDAO..')
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "http://noahark.money/#/app/dashboard"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            price = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[1].get_text()
            apy = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[2].get_text()
            mcap = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[0].get_text()
            tvl = soup.findAll('h4', class_='MuiTypography-root MuiTypography-h4')[0].get_text()
            treasury = soup.findAll('h4', class_='MuiTypography-root MuiTypography-h4')[1].get_text()
            backing = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[4].get_text()
            runway = soup.findAll('h4', class_='MuiTypography-root MuiTypography-h4')[5].get_text()
            
            
            driver.quit()
            print('NoahArkDAO - $NRK', price, '\n', tvl,'\n', apy, '\n', mcap, '\n', treasury,'\n', backing, '\n', runway)
            
            
            total = {'mcap': mcap, 'price': price, 'tvl': tvl, 'apy': apy, 'treasury': treasury, 'backing': backing, 'runway': runway}
            

            with open("/home/admin/Desktop/data/noah.json", "w") as f:
                json.dump(total, f, indent=2)

            subprocess.call(['python3', '/home/admin/Desktop/Script/noah.py'])
                
            keyboard = [
                [
                    InlineKeyboardButton("Chart", url='https://dexscreener.com/avalanche/0x790c840b774d8f02ebdad9ddb74331614b535cef'),
                    InlineKeyboardButton("Dashboard", url='http://noahark.money/#/app/dashboard')
                ]
            ]
             
            reply_markup = InlineKeyboardMarkup(keyboard)

            print('Setting up data.')

            data = {
                    'photo': ('noah.png', open('/home/admin/Desktop/ss/noah.png', 'rb')),
                    'action': (None, 'send'),
                    'chat_id': (None, '-1001431327406'),
                    'caption': (None, f'\U0001F48E <b>NoahArkDAO - $NRK</b> #AVAX \U0001F48E \n\n\u231B <i><a href="https://discord.gg/KaTFSdmj9f">Discord</a> - <a href="https://twitter.com/NoahArkDAO">Twitter</a> - <a href="https://rebasetokens.app/f-a-q">FAQ</a></i> \u231B\n\n\U0001F4B5 <b>Market Cap:</b> {mcap}\n\U0001F4B0 <b>Price:</b> {price}\n\U0001F5D3 <b>APY:</b> {apy}\n\U0001F512 <b>TVL:</b> {tvl}\n\U0001F4AC <b>Treasury:</b> {treasury}\n\U0001F4CC <b>Backing:</b> {backing}\n\u23F0 <b>Runway:</b> {runway}\n\n\U0001F315 <a href="https://warp.bond/"><b>Warp.Bond</b></a> - The Next-Gen Web3 reserve currency ft. NFT Bonds & buildable starships that travel within the Staking #Metaverse\n@warpbond - <a href="https://discord.gg/warpbond">Discord</a> - <a href="https://twitter.com/warpbond">Twitter</a>\nJoin the <a href="https://warpcountdown.com/">Whitelist here!</a> \U0001F315'),
                    "reply_markup": (None, json.dumps(reply_markup.to_dict())),
                    "parse_mode": (None, 'HTML')
            }
        
            requests.post(url='https://api.telegram.org/bot5025889373:AAEGOUROw4deWROTzTR-1v1lDddv2EJFmSQ/sendPhoto', files=data)
            
            print('Data sent!')

            print('Shutting off NoahArkDAO..')
            s.enter(2, 1, usv, (s,))

        except Exception as errore:

            print(errore)

            data = {"chat_id": "92637783",
                    "text": f'<b>Error</b> on NoahArk Main Chat\n\n {errore}' ,
                    "parse_mode": 'HTML'}

            requests.post(url='https://api.telegram.org/bot5062720103:AAHo_qpQzG5dqRteZ-VgfBYL10_EFF1h6GU/sendMessage', data=data)

            s.enter(2, 1, usv, (s,))



def usv(sc):
        try:
            print('Starting AtlasUSV..')
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://app.atlasusv.com/#/dashboard"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            price = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[1].get_text()
            mcap = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[0].get_text()
            
            
            driver.quit()

            results = usvapy()

            apy = results[0]
            tvl = results[1]


            print('AtlasUSV - $USV', price,'\n', mcap,'\n', tvl,'\n', apy)
            
            
            total = {'mcap': mcap, 'price': price, 'tvl': tvl, 'apy': apy}
            

            with open("/home/admin/Desktop/data/usv.json", "w") as f:
                json.dump(total, f, indent=2)

            subprocess.call(['python3', '/home/admin/Desktop/Script/usv.py'])
                
            keyboard = [
                [
                    InlineKeyboardButton("Chart", url='https://dexscreener.com/polygon/0xc16e382aa7353aad0f598856afd9a93513542970'),
                    InlineKeyboardButton("Dashboard", url='https://app.atlasusv.com/#/dashboard')
                ]
            ]
             
            reply_markup = InlineKeyboardMarkup(keyboard)

            print('Setting up data.')

            subprocess.call(['python3', '/home/admin/Desktop/data/auto.sh'])

            data = {
                    'photo': ('usv.png', open('/home/admin/Desktop/ss/usv.png', 'rb')),
                    'action': (None, 'send'),
                    'chat_id': (None, '-1001431327406'),
                    'caption': (None, f'\U0001F48E <b>AtlasUSV - $USV</b> #Polygon \U0001F48E \n\n\u231B <i><a href="https://discord.gg/kfhjcGmu5h">Discord</a> - <a href="https://twitter.com/AtlasUSV">Twitter</a> - <a href="https://rebasetokens.app/f-a-q">FAQ</a></i> \u231B\n\n\U0001F4B5 <b>Market Cap:</b> {mcap}\n\U0001F4B0 <b>Price:</b> {price}\n\U0001F5D3 <b>APY:</b> {apy}\n\U0001F512 <b>TVL:</b> {tvl}\n\n\U0001F315 <a href="https://warp.bond/"><b>Warp.Bond</b></a> - The Next-Gen Web3 reserve currency ft. NFT Bonds & buildable starships that travel within the Staking #Metaverse\n@warpbond - <a href="https://discord.gg/warpbond">Discord</a> - <a href="https://twitter.com/warpbond">Twitter</a>\nJoin the <a href="https://warpcountdown.com/">Whitelist here!</a> \U0001F315'),
                    "reply_markup": (None, json.dumps(reply_markup.to_dict())),
                    "parse_mode": (None, 'HTML')
            }
        
            requests.post(url='https://api.telegram.org/bot5025889373:AAEGOUROw4deWROTzTR-1v1lDddv2EJFmSQ/sendPhoto', files=data)

            print('Shutting off AtlasUSV..')
            s.enter(2, 1, fidl, (s,))

        except Exception as errore:

            print(errore)

            data = {"chat_id": "92637783",
                    "text": f'<b>Error</b> on AtlasUSV Twitter\n\n {errore}' ,
                    "parse_mode": 'HTML'}

            requests.post(url='https://api.telegram.org/bot5062720103:AAHo_qpQzG5dqRteZ-VgfBYL10_EFF1h6GU/sendMessage', data=data)

            s.enter(2, 1, fidl, (s,))


def usvapy():

            print('Starting AtlasUSV..')
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://app.atlasusv.com/#/stake"
            driver.get(urlone)
            time.sleep(40)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')

            apy = soup.findAll('h4', class_='MuiTypography-root MuiTypography-h4')[0].get_text()
            tvl = soup.findAll('h4', class_='MuiTypography-root MuiTypography-h4')[1].get_text()
            
            
            driver.quit()
            
            return apy, tvl



def fidl(sc):
        try:
            print('Starting Fidl..')
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://app.trapeza.finance/dashboard/"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            price = soup.findAll('p', class_='Typography__DefaultParagraph-sc-17bu997-0 Typography__XLParagraph-sc-17bu997-5 fUdTVp jRMJXQ Metric__Value-sc-1u25ofm-2 gJQoMe')[2].get_text()
            apy = soup.findAll('p', class_='Typography__DefaultParagraph-sc-17bu997-0 Typography__XLParagraph-sc-17bu997-5 fUdTVp jRMJXQ Metric__Value-sc-1u25ofm-2 gJQoMe')[4].get_text()
            mcap = soup.findAll('p', class_='Typography__DefaultParagraph-sc-17bu997-0 Typography__XLParagraph-sc-17bu997-5 fUdTVp jRMJXQ Metric__Value-sc-1u25ofm-2 gJQoMe')[1].get_text()
            tvl = soup.findAll('p', class_='Typography__DefaultParagraph-sc-17bu997-0 Typography__XL1Paragraph-sc-17bu997-6 fUdTVp doGqTA rechart__HeaderSubData-sc-1j13ymb-2 loajmK')[0].get_text()
            treasury = soup.findAll('p', class_='Typography__DefaultParagraph-sc-17bu997-0 Typography__XL1Paragraph-sc-17bu997-6 fUdTVp doGqTA rechart__HeaderSubData-sc-1j13ymb-2 loajmK')[1].get_text()
            backing = soup.findAll('p', class_='Typography__DefaultParagraph-sc-17bu997-0 Typography__XLParagraph-sc-17bu997-5 fUdTVp jRMJXQ Metric__Value-sc-1u25ofm-2 gJQoMe')[3].get_text()
            runway = soup.findAll('p', class_='Typography__DefaultParagraph-sc-17bu997-0 Typography__XL1Paragraph-sc-17bu997-6 fUdTVp doGqTA rechart__HeaderSubData-sc-1j13ymb-2 loajmK')[2].get_text()
            
            
            driver.quit()
            print('TrapezaProtocol - $FIDL', price,'\n', mcap,'\n', tvl,'\n', apy,'\n', treasury,'\n', backing, '\n', runway)
            
            
            total = {'mcap': mcap, 'price': price, 'tvl': tvl, 'apy': apy, 'treasury': treasury, 'backing': backing, 'runway': runway}
            

            with open("/home/admin/Desktop/data/fidl.json", "w") as f:
                json.dump(total, f, indent=2)

            subprocess.call(['python3', '/home/admin/Desktop/Script/fidl.py'])
                
            keyboard = [
                [
                    InlineKeyboardButton("Chart", url='https://dexscreener.com/bsc/0x08dbefd8f7aca80729267a84df012ea0f203cfa8'),
                    InlineKeyboardButton("Dashboard", url='https://app.trapeza.finance/dashboard/')
                ]
            ]
             
            reply_markup = InlineKeyboardMarkup(keyboard)

            print('Setting up data.')

            data = {
                    'photo': ('fidl.png', open('/home/admin/Desktop/ss/fidl.png', 'rb')),
                    'action': (None, 'send'),
                    'chat_id': (None, '-1001431327406'),
                    'caption': (None, f'\U0001F48E <b>TrapezaProtocol - $FIDL</b> #BSC \U0001F48E \n\n\u231B <i><a href="https://t.me/+s_axHYExmDM2YzNl">Telegram</a> - <a href="https://discord.gg/CbPbR9SXNA">Discord</a> - <a href="https://twitter.com/TrapezaProtocol">Twitter</a> - <a href="https://rebasetokens.app/f-a-q">FAQ</a></i> \u231B\n\n\U0001F4B5 <b>Market Cap:</b> {mcap}\n\U0001F4B0 <b>Price:</b> {price}\n\U0001F5D3 <b>APY:</b> {apy}\n\U0001F512 <b>TVL:</b> {tvl}\n\U0001F4AC <b>Treasury:</b> {treasury}\n\U0001F4CC <b>Backing:</b> {backing}\n\u23F0 <b>Runway:</b> {runway}\n\n\U0001F315 <a href="https://warp.bond/"><b>Warp.Bond</b></a> - The Next-Gen Web3 reserve currency ft. NFT Bonds & buildable starships that travel within the Staking #Metaverse\n@warpbond - <a href="https://discord.gg/warpbond">Discord</a> - <a href="https://twitter.com/warpbond">Twitter</a>\nJoin the <a href="https://warpcountdown.com/">Whitelist here!</a> \U0001F315'),
                    "reply_markup": (None, json.dumps(reply_markup.to_dict())),
                    "parse_mode": (None, 'HTML')
            }
        
            requests.post(url='https://api.telegram.org/bot5025889373:AAEGOUROw4deWROTzTR-1v1lDddv2EJFmSQ/sendPhoto', files=data)
            
            print('Data sent!')

            print('Shutting off Trapeza..')
            s.enter(2, 1, redpill, (s,))

        except Exception as errore:

            print(errore)

            data = {"chat_id": "92637783",
                    "text": f'<b>Error</b> on Trapeza Main Chat\n\n {errore}' ,
                    "parse_mode": 'HTML'}

            requests.post(url='https://api.telegram.org/bot5062720103:AAHo_qpQzG5dqRteZ-VgfBYL10_EFF1h6GU/sendMessage', data=data)

            s.enter(2, 1, redpill, (s,))



def redpill(sc):
        try:
            print('Starting TheRedPill..')
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://app.theredpilldao.com/#/dashboard"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            price = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[1].get_text()
            mcap = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[0].get_text()
            backing = soup.findAll('h5', class_='MuiTypography-root MuiTypography-h5')[4].get_text()
            
            
            driver.quit()

            treasury = redtreas()
            results = redapy()
            apy = results[0]
            tvl = results[1]


            print('The Red Pill DAO - $TRP', price,'\n', mcap,'\n', tvl,'\n', apy,'\n', treasury,'\n', backing)
            
            
            total = {'mcap': mcap, 'price': price, 'tvl': tvl, 'apy': apy, 'treasury': treasury, 'backing': backing}
            

            with open("/home/admin/Desktop/data/trp.json", "w") as f:
                json.dump(total, f, indent=2)

            subprocess.call(['python3', '/home/admin/Desktop/Script/trp.py'])
                
            keyboard = [
                [
                    InlineKeyboardButton("Chart", url='https://dexscreener.com/bsc/0x4c2de88e92456a00bb012bb8d653da7995cd62b5'),
                    InlineKeyboardButton("Dashboard", url='https://app.theredpilldao.com/#/dashboard')
                ]
            ]
             
            reply_markup = InlineKeyboardMarkup(keyboard)

            print('Setting up data.')

            data = {
                    'photo': ('trp.png', open('/home/admin/Desktop/ss/trp.png', 'rb')),
                    'action': (None, 'send'),
                    'chat_id': (None, '-1001431327406'),
                    'caption': (None, f'\U0001F48E <b>The Red Pill DAO - $TRP</b> #BSC \U0001F48E \n\n\u231B <i>@theredpilldao - <a href="https://twitter.com/TheRedPillDAO">Twitter</a> - <a href="https://rebasetokens.app/f-a-q">FAQ</a></i> \u231B\n\n\U0001F4B5 <b>Market Cap:</b> {mcap}\n\U0001F4B0 <b>Price:</b> {price}\n\U0001F5D3 <b>APY:</b> {apy}\n\U0001F512 <b>TVL:</b> {tvl}\n\U0001F4AC <b>Treasury:</b> {treasury}\n\U0001F4CC <b>Backing:</b> {backing}\n\n\U0001F315 <a href="https://warp.bond/"><b>Warp.Bond</b></a> - The Next-Gen Web3 reserve currency ft. NFT Bonds & buildable starships that travel within the Staking #Metaverse\n@warpbond - <a href="https://discord.gg/warpbond">Discord</a> - <a href="https://twitter.com/warpbond">Twitter</a>\nJoin the <a href="https://warpcountdown.com/">Whitelist here!</a> \U0001F315'),
                    "reply_markup": (None, json.dumps(reply_markup.to_dict())),
                    "parse_mode": (None, 'HTML')
            }
        
            requests.post(url='https://api.telegram.org/bot5025889373:AAEGOUROw4deWROTzTR-1v1lDddv2EJFmSQ/sendPhoto', files=data)
            
            print('Data sent!')

            print('Shutting off TheRedPill..')
            s.enter(2, 1, cleaner, (s,))

        except Exception as errore:

            print(errore)

            data = {"chat_id": "92637783",
                    "text": f'<b>Error</b> on RedPill Main Chat\n\n {errore}' ,
                    "parse_mode": 'HTML'}

            requests.post(url='https://api.telegram.org/bot5062720103:AAHo_qpQzG5dqRteZ-VgfBYL10_EFF1h6GU/sendMessage', data=data)

            s.enter(2, 1, cleaner, (s,))


def redapy():

            print('Starting RedPill..')
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://app.theredpilldao.com/#/stake"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            
            apy = soup.findAll('h4', class_='MuiTypography-root MuiTypography-h4')[0].get_text()
            tvl = soup.findAll('h4', class_='MuiTypography-root MuiTypography-h4')[1].get_text()
            

            driver.quit()

            return apy, tvl


def redtreas():

            print('Starting RedPill..')
            options = webdriver.FirefoxOptions()
            options.headless = True
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(options=options, service=service)
        
            urlone = "https://app.theredpilldao.com/#/bonds"
            driver.get(urlone)
            time.sleep(30)
            
            print('Scraping..')
            soup = BeautifulSoup(driver.page_source,'html.parser')
            
            treasury = soup.findAll('h4', class_='MuiTypography-root MuiTypography-h4')[0].get_text()
            

            driver.quit()

            return treasury


def cleaner(sc):
        try:
            print('Cleaner')
            subprocess.call(['/home/admin/Desktop/Main/cleaner.sh'])
  
            s.enter(5, 1, wonder, (s,))
            
        except Exception as errore:

            print(errore)

            data = {"chat_id": "92637783",
                    "text": f'<b>Error</b> on Cleaner Main Chat\n\n {errore}' ,
                    "parse_mode": 'HTML'}

            requests.post(url='https://api.telegram.org/bot5062720103:AAHo_qpQzG5dqRteZ-VgfBYL10_EFF1h6GU/sendMessage', data=data)

            s.enter(2, 1, wonder, (s,))




            
        
s.enter(5, 1, usv, (s,))
s.run()
