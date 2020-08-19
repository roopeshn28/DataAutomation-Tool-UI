# import Tkinter as tk     # python 2
# import tkFont as tkfont  # python 2
import tkinter as tk  # python 3
from tkinter import font as tkfont  # python 3
from tkinter.filedialog import askopenfile
from tkinter.ttk import *
from tkinter import ttk
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as soup
import requests
import re
import os
import pandas as pd
from requests.compat import quote_plus
from urllib.error import HTTPError
from urllib.error import URLError
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from pandas import DataFrame
import time
from PIL import Image
import pytesseract
import argparse
import cv2
import os
import unicodedata
import re
import inflect
from pandas import read_csv
import pandas as pd
import os
import PyPDF2
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import csv as my_csv
from textblob import TextBlob
global title,  price, image , year, month, day, entry1, variable


pytesseract.pytesseract.tesseract_cmd= "C:/Program Files/Tesseract-OCR/tesseract.exe"
lanlist=["Afrikaans", "Amharic", "Arabic", "Assamese", "Azerbaijani", "Belarusian", "Bengali", "Tibetan",
                      "Bosnian", "Bulgarian", "Catalan", "Valencian", "Cebuano", "Czech",
                      "Chinese-Simplified ", "Chinese-Traditional ", "Cherokee", "Welsh", "Danish",
                      "Dzongkha", "English", "Esperanto", "Estonian", "Basque", "Persian", "Finnish", "French", "German Fraktur",
                      "Irish", "Galician", "Greek", "Gujarati",  "German","Greek","Haitian", "Haitian Creole", "Hebrew", "Hindi",
                      "Croatian", "Hungarian", "Inuktitut", "Indonesian", "Icelandic", "Italian", "Italian - Old",
                      "Javanese", "Japanese", "Kannada", "Georgian", "Georgian - Old", "Kazakh", "Central Khmer",
                      "Kirghiz", "Kyrgyz", "Korean", "Kurdish", "Lao", "Latin", "Latvian", "Lithuanian", "Malayalam",
                      "Marathi", "Macedonian", "Maltese", "Malay", "Burmese", "Nepali", "Dutch", "Flemish", "Norwegian",
                      "Oriya", "Panjabi", "Punjabi", "Polish", "Portuguese", "Pushto", "Pashto", "Romanian",
                      "Moldavian","Moldovan", "Russian", "Sanskrit", "Sinhala", "Sinhalese", "Slovak", "Slovenian", "Spanish",
                      "Castilian", "Castilian - Old", "Albanian", "Serbian", "Serbian - Latin", "Swahili", "Swedish", "Syriac",
                      "Tamil","Telugu", "Tajik", "Tagalog", "Thai", "Tigrinya", "Turkish", "Uighur", "Uyghur", "Ukrainian",
                      "Urdu","Uzbek", "Uzbek - Cyrillic", "Vietnamese", "Yiddish"]

teslanguages = {"Afrikaans": "afr", "Amharic": "amh", "Arabic": "ara", "Assamese": "asm", "Azerbaijani": "aze",
                    "Belarusian": "bel", "Bengali": "ben", "Tibetan": "bod",
                    "Bosnian": "bos", "Bulgarian": "bul", "Catalan": "cat", "Valencian": "cat", "Cebuano": "ceb",
                    "Czech": "ces", "Chinese-Simplified ": "chi_sim",
                    "Chinese-Traditional ": "chi_tra", "Cherokee": "chr", "Welsh": "cym", "Danish": "dan",
                    "German": "deu", "Dzongkha": "dzo", "Greek": "ell",
                    "English": "eng", "Esperanto": "epo", "Estonian": "est", "Basque": "eus", "Persian": "fas",
                    "Finnish": "fin", "French": "fra", "German Fraktur": "frk",
                    "Irish": "gle", "Galician": "glg", "Greek": "grc", "Gujarati": "guj", "Haitian": "hat",
                    "Haitian Creole": "hat", "Hebrew": "heb", "Hindi": "hin",
                    "Croatian": "hrv", "Hungarian": "hun", "Inuktitut": "iku", "Indonesian": "ind", "Icelandic": "isl",
                    "Italian": "ita", "Italian - Old": "ita_old",
                    "Javanese": "jav", "Japanese": "jpn", "Kannada": "kan", "Georgian": "kat",
                    "Georgian - Old": "kat_old", "Kazakh": "kaz", "Central Khmer": "khm",
                    "Kirghiz": "kir", "Kyrgyz": "kir", "Korean": "kor", "Kurdish": "kur", "Lao": "lao", "Latin": "lat",
                    "Latvian": "lav", "Lithuanian": "lit", "Malayalam": "mal",
                    "Marathi": "mar", "Macedonian": "mkd", "Maltese": "mlt", "Malay": "msa", "Burmese": "mya",
                    "Nepali": "nep", "Dutch": "nld", "Flemish": "nld", "Norwegian": "nor",
                    "Oriya": "ori", "Panjabi": "pan", "Punjabi": "pan", "Polish": "pol", "Portuguese": "por",
                    "Pushto": "pus", "Pashto": "pus", "Romanian": "ron", "Moldavian": "ron",
                    "Moldovan": "ron", "Russian": "rus", "Sanskrit": "san", "Sinhala": "sin", "Sinhalese": "sin",
                    "Slovak": "slk", "Slovenian": "slv", "Spanish": "spa", "Castilian": "spa",
                    "Castilian - Old": "spa_old", "Albanian": "sqi", "Serbian": "srp", "Serbian - Latin": "srp_latn",
                    "Swahili": "swa", "Swedish": "swe", "Syriac": "syr", "Tamil": "tam",
                    "Telugu": "tel", "Tajik": "tgk", "Tagalog": "tgl", "Thai": "tha", "Tigrinya": "tir",
                    "Turkish": "tur", "Uighur": "uig", "Uyghur": "uig", "Ukrainian": "ukr", "Urdu": "urd",
                    "Uzbek": "uzb", "Uzbek - Cyrillic": "uzb_cyrl", "Vietnamese": "vie", "Yiddish": "yid"}

driver = 'C:\windows\geckodriver'
#path="D:/"
#file="{}".format(os.getpid())
#filename=os.path.join(path,file)
home_path="E:/"
original_scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
                  "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

url = 'https://docs.google.com/spreadsheets/d/17dp3qr--cUlNRYoIB7Ur1Gao6NdMVv__YsIFGihkul4'

spreadsheet_name = 'CSV-to-Google-Sheet'

credential_file = 'client_secret.json'

#Calling a function to run the Translation
def performtranslation(lan1,lan2,file):
    print("Lan1",lan1)
    print("Lan2",lan2)
    selected_lang1 = teslanguages.get(lan1)
    selected_lang2 = teslanguages.get(lan2)
    print("File is selected")
    image = cv2.imread(file.name)
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Gets the image and translates it to Czech. You can specify own lang if you want.
    options = "-l {}".format(selected_lang1)
    text = pytesseract.image_to_string(rgb, config=options)
    print(text)
    tb = TextBlob(text)
    print("Running translation")
    translated = tb.translate(to=selected_lang2)
    target_folder = os.path.join(home_path, '_'.join("Language Translation".lower().split(' ')))
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)  # make dir if not present
    files = "{}".format(os.getpid())
    storagename = files + "_" + lang
    filename = os.path.join(target_folder, storagename)
    file1 = open(filename + ".txt", "w", encoding="utf8")  # writing the text to the file with the pid as the file name
    # \n is placed to indicate EOL (End of Line)
    file1.writelines(text)
    file1.close()  # to change file access modes

    # Finally, print the translated image's text and print it.
    print(translated)
    print("Task Completed")


def select_transfile(lan1,lan2):
    file = askopenfile(mode='r', filetypes=[('Images', '*.png'), ('all files', '*.*')])
    if file is not None:
        print("File is selected",file)
        performtranslation(lan1,lan2,file)




def convert(scope, url, spreadsheet_name, credential_file, csv_file):
    credentials = ServiceAccountCredentials.from_json_keyfile_name(credential_file, scope)
    client = gspread.authorize(credentials)
    spreadsheet = client.open(spreadsheet_name)

    spreadsheet = client.open_by_url(url)
    sheetname=csv_file.split("/")[-1]
    print("CSV sheet name is",sheetname)
    worksheet = spreadsheet.add_worksheet(title=sheetname, rows="100", cols="20")
    # worksheet=spreadsheet.worksheet('data1.csv')
    print(spreadsheet)

    print(spreadsheet.worksheets())
    print(worksheet.id)
    print(dir(worksheet))

    with open(csv_file, 'r',encoding="utf8") as file_obj:
        print(file_obj)
        reader = my_csv.reader(file_obj)
        # worksheet.insert_rows(reader)

        ar = []
        for row in reader:
            # print(index)
            # worksheet.insert_row(row,index+1)
            ar.append(row)
        worksheet.insert_rows(ar, 1)

        '''content = file_obj.read()
        client.import_csv(worksheet.id, data=content)
        '''


def checktypeofscrapping(ar1,ar2):

        if ar1=="Amazon":
            AmazonScraper(ar2)
        elif ar1=="Ebay":
            EbayScraper(ar2)
        elif ar1=="Text":
            TextScraper(ar2)
        elif ar1=="Flipkart":
            FlipkartScraper(ar2)
        elif ar1=="Image":
            ImageDownload(ar2)
        elif ar1=="Walmart":
            WalmartScraper(ar2)

#Calling the Amazonscrapper Function

def AmazonScraper(url):

    url =url
    #url = input("Enter the url: ")

    def get_request(pageNo):

        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
                   "Accept-Encoding": "gzip, deflate",
                   "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                   "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}

        req = requests.get(url + str(pageNo), headers=headers)
        return req

    def get_content(req):
        return req.content

    def apply_beautifulsoup(content):
        return BeautifulSoup(content, 'lxml')

    def get_name(div):
        name_span = div.find('span', attrs={'class': 'a-size-medium a-color-base a-text-normal'})
        if name_span is not None:
            return name_span.text
        else:
            return 'no-info'

    def get_price(div):
        price_span = div.find('span', attrs={'class': 'a-offscreen'})
        if price_span is not None:
            return price_span.text
        else:
            return 'no-info'

    def get_rating(div):
        rating_span = div.find('span', attrs={'class': 'a-icon-alt'})
        if rating_span is not None:
            return rating_span.text
        else:
            return 'no-info'

    all_info = []
    for pageNo in range(1, 6):
        req = get_request(pageNo)
        content = get_content(req)
        soup = apply_beautifulsoup(content)
        for d in soup.findAll('div', attrs={
            'class': 'sg-col-4-of-12 sg-col-8-of-16 sg-col-16-of-24 sg-col-12-of-20 sg-col-24-of-32 sg-col sg-col-28-of-36 sg-col-20-of-28'}):
            name = get_name(d)
            price = get_price(d)
            rating = get_rating(d)
            all_info.append([name, price, rating])

    df= pd.DataFrame(all_info, columns=['ProductName', 'Price', 'Ratings'])
    #df

    # product_info['price_$'] = product_info['price_$'].apply(clean_price)
    #product_info.to_csv('D:\Amazon_products.csv')
    target_folder=os.path.join(home_path,'_'.join("Amazon_scraper".lower().split(' ')))
    if not os.path.exists(target_folder):
        os.makedirs(target_folder) # make dir if not present
    files ="{}".format(os.getpid())
    filename=os.path.join(target_folder,files)
    df.to_csv(filename+".csv") # writing data into csv file
    print("file name:",filename+".csv")
    return filename

    #print("If file is empty, try other links")



#Calling the EbayScrapper Function

def EbayScraper(url):
    #driver = 'C:\windows\chromedriver'
    #Base_url = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw={}&_sacat=0&_pgn=1'
    header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", 
               "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
               "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
    search = url
    #Mixing_url = Base_url.format(quote_plus(search))
    #Final_url = requests.get(Mixing_url)
    # print(Mixing_url)
    #print(Final_url)

    title = []
    price = []
    product_url = []
    product_image_url = []
    html = requests.get(search,headers=header)
    soup = BeautifulSoup(html.content, 'html.parser')
    

    # extracting the data
    def scrape_data(pass_soup):
        # get_url = requests.get(url)
        # soup = BeautifulSoup(get_url.content, 'html.parser')
        results = pass_soup.find(id="srp-river-results")
        product_list = results.find_all(class_='s-item')
        for item in product_list:
            title_text = item.find(class_='s-item__title').get_text()
            price_text = item.find(class_='s-item__price').get_text()
            # rating = item.find('div', attrs = {'s-item__reviews'}).find('span', attrs = {'class': 'clipped'}).text
            item_url = item.find('a').get('href')
            image_url = item.find('img')['src']
            title.append(title_text)
            price.append(price_text)
            # ratings.append(ratings)
            product_url.append(item_url)
            product_image_url.append(image_url)
            # print(len(title))

    scrape_data(soup)
    pages = soup.find(class_='pagination__items')
    print(len(pages))
    links = pages.find_all('a')
    # print(links)
    for link in links:
        href = link.get('href')
        if (href == search):
            print('')
            continue
        else:
            other_url = requests.get(href)
            print(other_url)
            soup1 = BeautifulSoup(other_url.content, 'html.parser')
            scrape_data(soup1)
    df = pd.DataFrame({
        'ProductName': title,
        'Price': price,
        # 'ratings':ratings,
        'Product_url': product_url,
        'Image_url': product_image_url,
    })
    #product_items.to_csv('D:\Ebay_product_list.csv')
    target_folder=os.path.join(home_path,'_'.join("Ebay_scraper".lower().split(' ')))
    if not os.path.exists(target_folder):
        os.makedirs(target_folder) # make dir if not present
    files ="{}".format(os.getpid())
    filename=os.path.join(target_folder,files)
    df.to_csv(filename+".csv") # writing data into csv file
    print("File name: ",filename+".csv")
    #print("If your file is empty, use anothor url")
    return filename

#Calling  the FlipkartScrapper Function

def FlipkartScraper(url):
    #driver = 'C:\windows\chromedriver'
    header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", 
               "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
               "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
#search="https://www.flipkart.com/search?q=mobil&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
    #search="https://www.flipkart.com/search?q=laptops&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_7_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_7_0_na_na_na&as-pos=7&as-type=TRENDING&suggestionId=laptops&requestId=a931c0b1-8729-4296-984f-7c17c5cf6cbb"
    search=url
    options = Options()
    options.add_argument('--headless')
    #options.add_argument('--disable-gpu')
    #browser = webdriver.Chrome(driver, chrome_options=options)
    ProductName = []
    ProductPrice = []
    ProductDescription = []
    ProductRating = []
    ProductReviewCount = []
    ProductPreviousPrice = []
    ProductPercentOff = []
    try:
            #browser.get('https://www.flipkart.com/search?as=off&as-show=on&otracker=start&page={}&q={}&viewType=grid'.format(x,Searchtext))
        addr=search
        html = requests.get(addr,headers=header) # get response from webpage
        mysoup = BeautifulSoup(html.content,'lxml')
    
        if mysoup.find("div",{"class": "_1-2Iqu row"}):
            allcards = mysoup.findAll("div", {"class": "_1-2Iqu row"})
            for i in allcards:
                            # Fetching Name of item
                    #print(i.find("div",{"class" : "_3wU53n"}).text)
                ProductName.append(i.find("div",{"class" : "_3wU53n"}).text)
                            #Fetching Price
                try:
                        #print(i.find("div",{'class':'_1vC4OE _2rQ-NK'}).text)
                    ProductPrice.append(i.find("div",{'class':'_1vC4OE _2rQ-NK'}).text)
                except:
                        #print("Either Price is not Available or Item out of Stock")
                    ProductPrice.append("Either Price is not Available or Item out of Stock")
                            #Short Description
                try:
                        #print(i.find("li",{"class" : "tVe95H"}).text)
                    ProductDescription.append(i.find("li",{"class" : "tVe95H"}).text)
                except:
                       # print("No Attribute is listed")
                    ProductDescription.append("No Attribute is listed")
                            #Fetching Star Rating (Out of 5)
                try:
                        #print(i.find("div",{"class" : "hGSR34 _2beYZw"}).text)
                    ProductRating.append(i.find("div",{"class" : "hGSR34 _2beYZw"}).text)
                except:
                        #print("No Rating")
                    ProductRating.append("No Rating")
                            #Fetching Count of review and Rating
                try:
                        #print(i.find('span',{'class':'_38sUEc'}).text)
                    ProductReviewCount.append(i.find("span",{"class" : "_38sUEc"}).text)
                except:
                        #print("No Review")
                    ProductReviewCount.append("No Review")
                            # Product Previous Price
                try:
                        #print(i.find('div',{'class':'_3auQ3N _2GcJzG'}).text)
                    ProductPreviousPrice.append(i.find("div",{"class" : "_3auQ3N _2GcJzG"}).text)
                except:
                        #print("No Previous Price")
                    ProductPreviousPrice.append("No Previous Price")
                        # Discount Off on Product
                try:
                        #print(i.find('div',{'class':'VGWI6T'}).text)
                    ProductPercentOff.append(i.find("div",{"class" : "VGWI6T"}).text)
                except:
                        #print("No Discount")
                    ProductPercentOff.append("No Discount")
    
            print("----------------------------------------------------------------")
                
        else:
            allcards = mysoup.findAll("div", {"class": "_3liAhj"})
            for i in allcards:
                        # Fetching Name of item
                    #print(i.find("a",{"class" : "_2cLu-l"}).text)
                ProductName.append(i.find("a",{"class" : "_2cLu-l"}).text)
                        # Below Code is For Fetching Price of item
                try:
                        #print(i.find("div",{"class" : "_1vC4OE"}).text)
                    ProductPrice.append(i.find("div",{"class" : "_1vC4OE"}).text)
                except:
                       # print("Either Price is not Available or Item out of Stock")
                    ProductPrice.append("Either Price is not Available or Item out of Stock")
                        #Short Description
                try:
                        #print(i.find("div",{"class" : "_1rcHFq"}).text)
                    ProductDescription.append(i.find("div",{"class" : "_1rcHFq"}).text)
                except:
                       # print("No Attribute is listed")
                    ProductDescription.append("No Attribute is listed")
                        #Fetching Star Rating (Out of 5)
                try:
                        #print(i.find('div',{'class':'hGSR34'}).text)
                    ProductRating.append(i.find("div",{"class" : "hGSR34 _2beYZw"}).text)
                except:
                        #print("No Rating")
                    ProductRating.append("No Rating")
                        #Fetching Count of review and Rating
                try:
                        #print(i.find('span',{'class':'_38sUEc'}).text)
                    ProductReviewCount.append(i.find("span",{"class" : "_38sUEc"}).text)
                except:
                        #print("No Review")
                    ProductReviewCount.append("No Review")
                        # Product Previous Price
                try:
                       # print(i.find('div',{'class':'_3auQ3N'}).text)
                    ProductPreviousPrice.append(i.find("div",{"class" : "_3auQ3N"}).text)
                except:
                        #print("No Previous Price")
                    ProductPreviousPrice.append("No Previous Price")
                        # Discount Off on Product
                try:
                       # print(i.find('div',{'class':'VGWI6T'}).text)
                    ProductPercentOff.append(i.find("div",{"class" : "VGWI6T"}).text)
                except:
                        #print("No Discount")
                    ProductPercentOff.append("No Discount")
    
            print("----------------------------------------------------------------\n")
        time.sleep(5)
    except HTTPError as e:
        print(e)
    except URLError:
        print("Server down or incorrect domain")
    else:
        print("Excel File Writing Started")
        df = DataFrame({'ProductName': ProductName,'Price': ProductPrice, 'Description': ProductDescription, 'Rating': ProductRating,'Product Rating & Review Count':ProductReviewCount,'Previous Price' : ProductPreviousPrice,'Product Percent Off': ProductPercentOff})
        df = df[["ProductName","Description","Price","Previous Price","Product Percent Off","Rating","Product Rating & Review Count"]]
        #df.to_excel('D:\FlipkartDataExtract.xlsx', sheet_name='Flipkart-Data', index=False)
        target_folder=os.path.join(home_path,'_'.join("Flipkart_scraper".lower().split(' ')))
        if not os.path.exists(target_folder):
            os.makedirs(target_folder) # make dir if not present
        files ="{}".format(os.getpid())
        filename=os.path.join(target_folder,files)
        df.to_csv(filename+".csv") # writing data into csv file
        #browser.close()
        print("file name:",filename+".csv")
        return filename
        #print("If Your scraped data file is empty, then use other things")
# Calling the Image Download Function

def ImageDownload(url):
    #driver = 'C:\windows\chromedriver'
    #imageno = int(input("how many images u need to download ( upto 50 images ) : "))

    def fetch_image_urls(query: str, max_links_to_fetch: int, wd: webdriver, sleep_between_interactions: int = 1):
        def scroll_to_end(wd):
            wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(sleep_between_interactions)

        search_url = "https://www.google.com/search?safe=off&site=&tbm=isch&source=hp&q={q}&oq={q}&gs_I=img"

        wd.get(search_url.format(q=query))
        image_urls = set()
        image_count = 0
        results_start = 0
        while image_count < max_links_to_fetch:
            scroll_to_end(wd)
            # get all image thumbnail results
            thumbnail_results = wd.find_elements_by_css_selector("img.Q4LuWd")
            number_results = len(thumbnail_results)
            print(f"Found:{number_results} search results. Extracting links from{results_start}:{number_results}")
            for img in thumbnail_results[results_start:number_results]:
                # try to click every thumbnail such that we can get the realimage behind it
                try:
                    img.click()
                    time.sleep(sleep_between_interactions)
                except Exception:
                    continue
                # extract image urls
                actual_images = wd.find_elements_by_css_selector('img.n3VNCb')
                for actual_image in actual_images:
                    if actual_image.get_attribute('src') and 'http' in actual_image.get_attribute('src'):
                        image_urls.add(actual_image.get_attribute('src'))
                image_count = len(image_urls)
                if len(image_urls) >= max_links_to_fetch:
                    print(f"Found: {len(image_urls)} image links Done...")
                    break
            else:
                print("Found:", len(image_urls), "image links, looking for more..")
                time.sleep(30)
                return
                load_more_button = wd.find_element_by_css_selector(".mye4qd")
                if load_more_button:
                    wd.execute_script("documnet.querySelector('.mye4qd').click();")
            results_start = len(thumbnail_results)
        return image_urls

    def persist_image(folder_path: str, url: str, counter):
        try:
            image_content = requests.get(url).content
        except Exception as e:
            print(f"Error-Could not download{url} - {e}")
        try:
            f = open(os.path.join(folder_path, 'jpg' + '_' + str(counter) + ".jpg"), 'wb')
            f.write(image_content)
            f.close()
            print(f"Success - saved {url} - as{folder_path}")
        except Exception as e:
            print(f"Error - Could not save {url} - {e}")

    def search_and_download(search_term: str, driver_path: str, target_path='E:\Image_scraper', number_images=50):

        target_folder = os.path.join(target_path, '_'.join(search_term.lower().split(' ')))
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)  # make dir if not present
        cap = DesiredCapabilities().FIREFOX
        cap["marionette"] = False
        with webdriver.Firefox(capabilities=cap, executable_path=driver_path) as wd:
            res = fetch_image_urls(search_term, number_images, wd=wd, sleep_between_interactions=0.5)

        counter = 0
        for elem in res:
            persist_image(target_folder, elem, counter)
            counter += 1

    # Inputs are given here

    DRIVER_PATH = driver
    search_term = url#input("Enter search term here : ")
    # images=input("enter number of images:")
    # imagesno=input("Enter the number of images u need")
    # num of images you can pass it from here by default it is 10 if you are not passing
    # number_images=10

    search_and_download(search_term=search_term, driver_path=DRIVER_PATH)

# Calling the TextScrapping Function

def TextScraper(url):
    url=url
    response=requests.get(url)
    html=response.content
    soup=BeautifulSoup(html,'lxml')
    title=soup.find('title')
    print(title.text)
    body=soup.find('body')
    for x in body.find_all('script'):
        x.decompose()
    text=body.getText(separator=u'\n').strip()
    pattern=re.compile(r'\n+', re.MULTILINE)
    text=pattern.sub('\n',text)
    print(text)
    
    target_folder=os.path.join(home_path,'_'.join("Text_scraper".lower().split(' ')))
    if not os.path.exists(target_folder):
        os.makedirs(target_folder) # make dir if not present
    files ="{}".format(os.getpid())
    filename=os.path.join(target_folder,files)
    file1 = open(filename + ".txt", "w",encoding="utf-8")
            # \n is placed to indicate EOL (End of Line)
    file1.writelines(text)
    file1.close()
    print(filename+".txt")
    return filename


#Calling Wallmart
def WalmartScraper(url):
        try:
            header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61  Safari/537.36'}
            #url="https://www.walmart.com/browse/household-essentials/air-fresheners/1115193_1025739?povid=1115193+%7C+2018-12-25+%7C+LHN%20- %20Best%20Sellers%20-%20Air%20Fresheners"
            #url=input("Enter required catagory url: ")
            url=url
            html = requests.get(url,headers=header) # get response from webpage
            data = soup(html.content,'lxml')
            url_list = [] # empty list to get sub urls or the given main url
            for i in range(1,26):
                url_list.append(url + str(i))
            # creating empty lists to store the data
            item_names = []
            price_list = []
            item_ratings = []
            item_reviews = []
            # loop for scrape the product data
            for url in url_list:
                result = requests.get(url)
                data = soup(result.content,'lxml')
                product_name = data.findAll('div',{'class':'search-result-product-title gridview'})
                product_rating = data.findAll('span',{'class':'seo-avg-rating'})
                product_reviews = data.findAll('span',{'class':'stars-reviews-count'})
                product_price = data.findAll('span',{'class':'price display-inline-block arrange-fit price price-main'})
                for names,rating,reviews,price in zip(product_name,product_rating,product_reviews,product_price):
                    item_names.append(names.a.span.text.strip())
                    item_ratings.append(rating.text)
                    item_reviews.append(reviews.text.replace('ratings',''))
                    price_list.append(price.findAll('span',{'class':'visuallyhidden'})[0].text)
    
        except HTTPError as e:
            print(e)
        except URLError:
            print("Server down or incorrect domain")
        else:
            # creating a dataframe 
            import pandas as pd
            df = pd.DataFrame({'ProductName':item_names, 'Price':price_list, 'Rating':item_ratings,'Product Reviews count':item_reviews}, columns=['ProductName', 'Price', 'Rating', 'Product Reviews count'])
            df
            #df.to_csv('D:\Walmart_product_list.csv') # writing data into csv file
            target_folder=os.path.join(home_path,'_'.join("Walmart_scraper".lower().split(' ')))
            if not os.path.exists(target_folder):
                os.makedirs(target_folder) # make dir if not present
            files ="{}".format(os.getpid())
            filename=os.path.join(target_folder,files)
            df.to_csv(filename+".csv") # writing data into csv file
            print("file name:",filename+".csv")
            return filename
            #print("If your file is empty! try another url")

def recognisetext(file,language):
    path =file
    print(path)
    lang=language
    print(lang)
    selected_lang = teslanguages.get(lang)
    extension = path.split('.')[1]  #slitting to get the extension
    print("File extension is " + extension)
    extensions = ["jpg", "png", "jpeg", "pdf"]
    # checking of the file extension is pdf and then calling the function convertpdftotext method
    if extension == 'pdf':
        print(path)
        text = convert_pdf_to_text_py(path)
        target_folder = os.path.join(home_path, '_'.join("TextRecognition".lower().split(' ')))
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)  # make dir if not present
        files = "{}".format(os.getpid())
        storagename = files + "_" + lang
        filename = os.path.join(target_folder, storagename)
        file1 = open(filename + ".txt", "w",encoding="utf8")    #writing the text to the file with the pid as the file name
            # \n is placed to indicate EOL (End of Line)
        file1.writelines(text)
        file1.close()  # to change file access modes
        print("filename is", file1)
       #print(text)
    else:
        # Reading the image and getting its attributes
        image = cv2.imread(path)
        w, h, c = image.shape
        print(w, h)
        # if (w, h) <= (300, 300):
        #    print("Please give good image")
        # else:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # cv2.imshow("Image", gray)
        # check to see if we should apply thresholding to preprocess the image
        gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

        # make a check to see if median blurring should be done to remove
        # noise
        gray = cv2.medianBlur(gray, 3)

        # write the grayscale image to disk as a temporary file so we can
        # apply OCR to it
        file_name = "{}".format(os.getpid())
        #cv2.imwrite(file_name, gray)

        # load the image as a PIL/Pillow image, apply OCR, and then delete
        # the temporary file
        # then running the pytesseract to get the string values from the image
        options = "-l {} ".format(selected_lang)
        text = pytesseract.image_to_string(Image.open(path), config=options)
        target_folder = os.path.join(home_path, '_'.join("TextRecognition".lower().split(' ')))
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)  # make dir if not present
        files = "{}".format(os.getpid())
        storagename = files+"_"+lang
        print("Storagename is",storagename)
        filename = os.path.join(target_folder, storagename)
        file1 = open(filename + ".txt", "w",encoding='utf8')  # writing the text to the file with the pid as the file name
        # \n is placed to indicate EOL (End of Line)
        file1.writelines(text)
        file1.close()  # to change file access modes
        print("filename is", file1)
        #name = file_name
        #print(name)
        #file1 = open(name + ".txt", "w")
        # \n is placed to indicate EOL (End of Line)
        #file1.writelines(text)
        #file1.close()  # to change file access modes
        #os.remove(name)
            # print(text)

            # show the output images
            # cv2.imshow("Image", image)
            # cv2.imshow("Output", gray)
            # cv2.waitKey(0)

#Function that will convert the pdf file to text
def convert_pdf_to_text_py(path):
        content = ""
        with open(path, "rb") as f:
            pdfDoc = PyPDF2.PdfFileReader(f, strict=True)
            for i in range(0, pdfDoc.getNumPages()):
                content += pdfDoc.getPage(i).extractText() + "\n"
                print("The contents of PDF are",content)
            return (content)


# Calling the Web scrapper Model
def callwebscrapper(var1, var2):
    url = var1
    typeo = var2
    #print(url)
    #print(typeo)
    filecreated=checktypeofscrapping(typeo,url)
    print("File created is",filecreated)
# Calling the function to get the input for the WebScraper
def scrapertype():
    top = tk.Tk()
    ttk.Label(top, text='Enter the Url: ').place(x=20, y=20)
    input_text = tk.StringVar()  # to treat the input as string
    entry1 = Entry(top, textvariable=input_text)
    entry1.focus_force()
    entry1.pack(pady=10)
    OptionList = ['Amazon', 'Ebay', 'Flipkart', 'Walmart', 'Text', 'Image']
    variable = tk.StringVar(top)
    variable.set(OptionList[0])
    opt = tk.OptionMenu(top, variable, *OptionList)
    opt.config(width=90, font=('Helvetica', 12))
    opt.pack(side="top")
    labelTest = tk.Label(text="", font=('Helvetica', 12), fg='red')
    labelTest.pack(side="top")
    buttoncallweb = tk.Button(top, text="Submit", command=lambda: callwebscrapper(entry1.get(), variable.get()))
    buttoncallweb.pack(pady=10)



def calltransformation(function, file):
    # Unpacking the tuple
    print("Function called is ",function)
    print("File to read is",file)
    file_name, file_ext = os.path.splitext(file)
    # Comparing the extension of the file
    if (file_ext==".txt"):
        words1 = open(file,"rt",encoding='utf-8')
        words1 = words1.read()

        # Transformation
        if function=="Remove_punctuation_txt":
            remove_punctuation_txt(words1)

        elif function=="Remove_numbers_txt":
            remove_number_txt(words1)

        elif function=="Lower_case_txt":
            lowercase_txt(words1)

        elif function=="Upper_case_txt":
            uppercase_txt(words1)

        elif function=="Remove_non_ASCII_txt":
            remove_non_ascii_txt(words1)

        elif function=="Convert_number_into_words_txt":
            replace_numbers_txt(words1)

        elif function=="Extract_date_txt":
            extract_date_txt(words1)


    elif (file_ext==".csv"):
        words3=open(file,"rt",encoding='utf-8')
        words3=words3.read()
        words2=read_csv(file)

        # Transformation
        if function=="Remove_numbers":
            remove_number(words3)

        elif function=="Lower_case":
            lowercase(words3)

        elif function=="Upper_case":
            uppercase(words3)

        elif function=="Remove_non_ASCII":
            remove_non_ascii(words3)

        elif function=="CSV_merge":
            csv_merge()

        elif function=="Column_remove":
            column_rem(words2)

        elif function=="Row_remove":
            row_rem(words2)

        elif function=="Remove_empty_cell":
            remove_empty(words2)

        elif function=="Merge_txt_csv":
            merge_tx_col()

        elif function=="Specific_column":
            specific_col(file)

        elif function=="Row_range":
            row_range(file)

    else:
        print("Error enter only text file or csv file ")


def savefile_txt(output):
    with open("F:\output.txt", "w", encoding='utf-8') as file:
        file.write(output)


def savefile_csv(output):
    with open("F:\output.csv", "w", encoding='utf-8') as file:
        file.write(output)


def savefile_csv2(output):
    output.to_csv("F:\output.csv", index=False, encoding='utf-8')


def remove_punctuation_txt(words1):
    #Remove punctuation from list of  words
    # remove punctuation from the string
    # define punctuation
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    no_punct = ""
    for char in words1:
        if char not in punctuations:
            no_punct = no_punct + char
    # display the unpunctuated string
    savefile_txt(output)

def remove_number_txt(words1):
    num = ''.join([i for i in words1 if not i.isdigit()])
    savefile_txt(output)

def lowercase_txt(words1):
    #Convert all characters to lowercase from list of  words
    for word in words1:
        new_word = words1.lower()
    # Saving the data in a file
    savefile_txt(output)

def uppercase_txt(words1):
    #Convert all characters to lowercase from list of  words
    for word in words1:
        output = words1.upper()
    # Saving the data in a file
    savefile_txt(output)


def remove_non_ascii_txt(words1):
    #Remove non-ASCII characters from list of  words
    for word in words1:
        output = unicodedata.normalize('NFKD', words1).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    # Saving the data in a file
    savefile_txt(output)

def replace_numbers_txt(words1):
    #Replace all interger occurrences in list of tokenized words with textual representation
    p = inflect.engine()
    # split string into list of words
    temp_str = words1.split()
    # initialise empty list
    new_string = []

    for word in temp_str:
        # if word is a digit, convert the digit
        # to numbers and append into the new_string list
        if word.isdigit():
            temp = p.number_to_words(word)
            new_string.append(temp)
        # append the word as it is
        else:
            new_string.append(word)

        # join the words of new_string to form a string
        temp_str = ' '.join(new_string)
            # Saving the data in a file
    savefile_txt(temp_str)

def extract_date_txt(words1):
    # The regex pattern that we created
    pattern = "\d+[/.-]\d+[/.-]\d+"
    # Will return all the strings that are matched
    dates = re.findall(pattern, words1)
    for date in dates:
        if "-" in date:
            ((year, day, month) or (day, month, year) or (month, year, day)) == map(int, date.split("-"))
        elif "/" in date:
            ((year, day, month) or (day, month, year) or (month, year, day)) == map(int, date.split("/"))
        else:
            ((year, day, month) or (day, month, year) or (month, year, day)) == map(int, date.split("."))

        if 1 <= day <= 31 and 1 <= month <= 12:
            extract=date
    # Saving the data in a file
    savefile_txt(extract)

def remove_number(words3):
    #Remove numbers from list of words
    new_word = ''.join([i for i in words3 if not i.isdigit()])
    # Saving the data in a file
    savefile_csv(new_word)

def lowercase(words3):
    #Convert all characters to lowercase from list of  words
    for word in words3:
        new_word = words3.lower()
    # Saving the data in a file
    savefile_csv(new_word)


def uppercase(words3):
    #Convert all characters to lowercase from list of  words
    for word in words3:
        new_word = words3.upper()
    # Saving the data in a file
    savefile_csv(new_word)


def remove_non_ascii(words3):
    #Remove non-ASCII characters from list of  words
    for word in words3:
        new_word = unicodedata.normalize('NFKD', words3).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    # Saving the data in a file
    savefile_csv(new_word)

def csv_merge(words3):
    # Reading data from file1
    data = words3
    # Initializing the file
    words4 = input("Enter the csv file name: ")
    words4=open(words4,'rt')
    # Reading data from file2
    data2 = words4.read()

    # Merging 2 files
    # To add the data of file2
    # from next line
    data += "\n"
    data += data2
    # Saving the data in a file
    savefile_csv(data)

def column_rem(words2):
    # The column to be removed from the data
    for row in words2:
        print(row)
    mention=input("Enter the column to be removed: ")
    colum=words2.drop([mention], axis=1)
    # Saving the data in a file
    savefile_csv2(colum)

def row_rem(words2):
    # The row to be removed from the data
    mention=int(input("Enter the row to be removed: "))
    row=words2.drop([mention], axis=0)
    # Saving the data in a file
    savefile_csv2(row)

def remove_empty(words2):
    # Remove empty column and row from the data
    filtered_data = words2.dropna(axis='columns',how='all')
    filtered_data = filtered_data.dropna(axis='rows',how='all')
    # Saving the data in a file
    savefile_csv2(filtered_data)

def merge_tx_col():
    # Initializing the file
    words4 = input("Enter the text file name: ")
    words4=open(words4,"rt",encoding='utf-8')

    # Reading data from file1
    data = words4.read()

    # Reading data from file2
    data2 =  words3

    # Merging 2 files
    # To add the data of file2
    # from next line
    data += "\n"
    data += data2
    # Saving the data in a file
    savefile_csv(data)

def specific_col(file):
    # To show the specific column in the output
    words3 = read_csv(file)
    for row in words3:
        print(row)
    col_name=input("Enter the column name: ")
    df = pd.read_csv(file, usecols = [col_name])
    # Saving the data in a file
    savefile_csv2(output)

def row_range(file):
    # To show the row from initial to certain range of in the output
    row_name=int(input("Enter the row range to be displayed: "))
    df = pd.read_csv(file, nrows = row_name)
    # Saving the data in a file
    savefile_csv2(df)

#Calling the to select the file for the transformation
def selectfile(function):
    file = askopenfile(mode='r', filetypes=[('CSV', '*.csv'), ('TEXT', '*.txt')])
    if file is not None:
        print(file.name)
        calltransformation(function, file.name)

#Calling the to select the file for the uploading to Google
def selectfilegoole():
    file = askopenfile(mode='r', filetypes=[('CSV' ,'*.csv')])
    if file is not None:
        print(file.name)
        convert(original_scope,url,spreadsheet_name,credential_file, file.name)

#Calling the function to get the transforamtion type from the user
def transforamtionSelection():
    top = tk.Tk()
    OptionList = ['Remove_punctuation_txt','Remove_numbers_txt','Lower_case_txt','Upper_case_txt','Remove_non_ASCII_txt','Convert_number_into_words_txt','Extract_date_txt'
                  ,'Remove_numbers','Lower_case','Upper_case','Remove_non_ASCII','CSV_merge','Column_remove','Row_remove','Remove_empty_cell','Merge_txt_csv',
                  'Specific_column','Row_range']
    variable = tk.StringVar(top)
    variable.set(OptionList[0])
    opt = tk.OptionMenu(top, variable, *OptionList)
    opt.config(width=90, font=('Helvetica', 12))
    opt.pack(side="top")
    labelTest = tk.Label(text="", font=('Helvetica', 12), fg='red')
    labelTest.pack(side="top")
    selectfilebutton = tk.Button(top, text="Select the file", command=lambda:selectfile(variable.get()))
    selectfilebutton.pack(pady=10)



# Calling the function to get the input for the Text Recognition
def callfileuploader(language):
    file = askopenfile(mode='r', filetypes=[('Images', '*.jpg'), ('PDF', '*.pdf')])
    if file is not None:
        print(file.name)
        recognisetext(file.name,language)
    # if file is not None:
        #content = file.read()
        #canvas = tk.Canvas(root, width=300, height=300)
        #canvas.pack()
        #img = (Image.open(content, errors='ignore'))
        #canvas.create_image(20, 20, anchor=NW, image=img)
        #print(content)

# class implemetation for the single Screen to accomodate the other screens
class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo,PageThree,PageFour,PageFive):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

# Code for the First page
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Welcome to the Automated Data Entry Tool ", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Web Scrapping",
                            command=lambda: controller.show_frame("PageOne"))
        button1.pack(pady=10)
        button2 = tk.Button(self, text="Text Recognition",
                            command=lambda: controller.show_frame("PageTwo"))
        button2.pack(pady=10)
        button3 = tk.Button(self, text="Transformation",
                            command=lambda: controller.show_frame("PageThree"))
        button3.pack(pady=10)
        button4 = tk.Button(self, text="Upload to Google",
                            command=lambda: controller.show_frame("PageFour"))
        button4.pack(pady=10)
        button5 = tk.Button(self, text="Translation",
                            command=lambda: controller.show_frame("PageFive"))
        button5.pack(pady=10)
        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()
        button5.pack()

# Code for the taking the input for the Webscrapping
class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Web Scrapping", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button2 = tk.Button(self, text="Select Scraper type", command=scrapertype)
        button2.pack(pady=10)

        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

# Code for  taking the input for the text Recognition
class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Text Recognition", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        ttk.Label(self, text='Select the language: ').place(x=20, y=60)
        OptionList = lanlist
        variable = tk.StringVar(self)
        variable.set(OptionList[0])
        opt = tk.OptionMenu(self, variable, *OptionList)
        opt.config(width=90, font=('Helvetica', 12))
        opt.pack(side="top",pady=25)
        button1 = tk.Button(self, text="Select File", command=lambda:callfileuploader(variable.get()))
        button1.pack(pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack(pady=10)
#Code for  talking the  transformation
class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Transformation", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        transforamtionbutton = tk.Button(self, text="Select Transforamtion type", command=transforamtionSelection)
        transforamtionbutton.pack(pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack(pady=10)
#Code for pushing the csv to google
class PageFour(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Upload to Google Sheets", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        selectfilebutton = tk.Button(self, text="Select File", command=selectfilegoole)
        selectfilebutton.pack(pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack(pady=10)
#Code for translation
class PageFive(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Translation", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        ttk.Label(self, text='Select the language of the File: ').place(x=20, y=60)
        OptionList = lanlist
        language1 = tk.StringVar(self)
        language1.set(OptionList[0])
        opt = tk.OptionMenu(self, language1, *OptionList)
        opt.config(width=90, font=('Helvetica', 12))
        opt.pack(side="top", pady=25)
        ttk.Label(self, text='Select the language that you need to Translate: ').place(x=20, y=140)
        OptionListTranslation = lanlist
        language2 = tk.StringVar(self)
        language2.set(OptionListTranslation[0])
        opt = tk.OptionMenu(self, language2, *OptionListTranslation)
        opt.config(width=90, font=('Helvetica', 12))
        opt.pack(side="top", pady=25)
        selectbutton = tk.Button(self, text="Select File", command=lambda :select_transfile(language1.get(),language2.get()))
        selectbutton.pack(pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack(pady=10)


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()