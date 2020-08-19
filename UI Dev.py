import tkinter as tk  # python 3
from tkinter import font  as tkfont  # python 3
# import Tkinter as tk     # python 2
# import tkFont as tkfont  # python 2
from tkinter.filedialog import askopenfile
from tkinter.ttk import *
from tkinter import ttk
import Webscraper
global entry1, variable


def callwebscrapper(var1, var2):
    url = var1
    typeo = var2
    #print(url)
    #print(typeo)
    web=Webscraper(typeo,url)
    web.checktypeofscrapping()


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


def callfileuploader():
    file = askopenfile(mode='r', filetypes=[('Images', '*.jpg'), ('PDF', '*.pdf')])
    print(file)
    if file is not None:
        content = file.read()
        canvas = tk.Canvas(root, width=300, height=300)
        canvas.pack()
        img = (Image.open(content, errors='ignore'))
        canvas.create_image(20, 20, anchor=NW, image=img)
        print(content)

class Webscrapper():

    #Here the scrapertype refers the type of the scrapping that needs to be done
    #i.e text, image, shopping carts
    #The url mentions the url to be scrapped
    def __init__(self, scrapertype, url):
        # Attributes assignment
        self.scrapertype = scrapertype
        self.url = url

    def checktypeofscrapping(self):

        if self.scrapertype=="Amazon":
            AmazonScraper(self.url)
        elif self.scrapertype=="Ebay":
            EbayScraper(self.url)
        elif self.scrapertype=="Text":
            TextScraper(self.url)
        elif self.scrapertype=="Flipkart":
            FlipkartScraper(self.url)
        elif self.scrapertype=="Image":
            ImageDownload(self.url)

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

    product_info = pd.DataFrame(all_info, columns=['name', 'price', 'ratings'])
    product_info

    # product_info['price_$'] = product_info['price_$'].apply(clean_price)
    product_info.to_csv('D:\Amazon_products.csv')
    print("If file is empty, try other links")

#Calling the EbayScrapper Function

def EbayScraper(url):
    driver = 'C:\windows\chromedriver'
    Base_url = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw={}&_sacat=0&_pgn=1'
    search = url
    Mixing_url = Base_url.format(quote_plus(search))
    Final_url = requests.get(Mixing_url)
    # print(Mixing_url)
    print(Final_url)

    title = []
    price = []
    product_url = []
    product_image_url = []
    soup = BeautifulSoup(Final_url.content, 'html.parser')

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
        if (href == Mixing_url):
            print('')
            continue
        else:
            other_url = requests.get(href)
            print(other_url)
            soup1 = BeautifulSoup(other_url.content, 'html.parser')
            scrape_data(soup1)
    product_items = pd.DataFrame({
        'title': title,
        'price': price,
        # 'ratings':ratings,
        'product_url': product_url,
        'image_url': product_image_url,
    })
    product_items.to_csv('D:\Ebay_product_list.csv')

#Calling  the FlipkartScrapper Function

def FlipkartScraper(url):
    driver = 'C:\windows\chromedriver'
    while True:
        try:
            #userinput = #int(input("How Many Pages You Wants to Scrap (In Number) : "))
            Searchtext = url#input("What you want to Search (Text You wants to search) : ").replace(" ", "%20")

            if (userinput > 0) & (len(Searchtext) > 0) & (Searchtext.isalpha()) & (Searchtext != " "):
                break
            else:
                print("--- Please Enter Correct Values --- Try Again!")
                print()
        except:
            print("--- Please Enter Correct Values --- Try Again!")
            print()

    # Running headless Chrome (PhantomJS is Old Now and Deprecated)
    options = Options()
    options.add_argument('--headless')
    # options.add_argument('--disable-gpu')
    browser = webdriver.Chrome('C:\windows\chromedriver', chrome_options=options)

    # browser = webdriver.Chrome()

    ProductName = []
    ProductPrice = []
    ProductDescription = []
    ProductRating = []
    ProductReviewCount = []
    ProductPreviousPrice = []
    ProductPercentOff = []

    try:
        for x in range(1, userinput + 1):
            print('Page Number - ******************************************* {}'.format(x) + '\n')
            print()

            browser.get(
                'https://www.flipkart.com/search?as=off&as-show=on&otracker=start&page={}&q={}&viewType=grid'.format(x,
                                                                                                                     Searchtext))
            mysoup = BeautifulSoup(browser.page_source, 'html5lib')

            if mysoup.find("div", {"class": "_1-2Iqu row"}):
                allcards = mysoup.findAll("div", {"class": "_1-2Iqu row"})
                for i in allcards:
                    # Fetching Name of item
                    # print(i.find("div",{"class" : "_3wU53n"}).text)
                    ProductName.append(i.find("div", {"class": "_3wU53n"}).text)
                    # Fetching Price
                    try:
                        # print(i.find("div",{'class':'_1vC4OE _2rQ-NK'}).text)
                        ProductPrice.append(i.find("div", {'class': '_1vC4OE _2rQ-NK'}).text)
                    except:
                        # print("Either Price is not Available or Item out of Stock")
                        ProductPrice.append("Either Price is not Available or Item out of Stock")
                    # Short Description
                    try:
                        # print(i.find("li",{"class" : "tVe95H"}).text)
                        ProductDescription.append(i.find("li", {"class": "tVe95H"}).text)
                    except:
                        # print("No Attribute is listed")
                        ProductDescription.append("No Attribute is listed")
                    # Fetching Star Rating (Out of 5)
                    try:
                        # print(i.find("div",{"class" : "hGSR34 _2beYZw"}).text)
                        ProductRating.append(i.find("div", {"class": "hGSR34 _2beYZw"}).text)
                    except:
                        # print("No Rating")
                        ProductRating.append("No Rating")
                    # Fetching Count of review and Rating
                    try:
                        # print(i.find('span',{'class':'_38sUEc'}).text)
                        ProductReviewCount.append(i.find("span", {"class": "_38sUEc"}).text)
                    except:
                        # print("No Review")
                        ProductReviewCount.append("No Review")
                    # Product Previous Price
                    try:
                        # print(i.find('div',{'class':'_3auQ3N _2GcJzG'}).text)
                        ProductPreviousPrice.append(i.find("div", {"class": "_3auQ3N _2GcJzG"}).text)
                    except:
                        # print("No Previous Price")
                        ProductPreviousPrice.append("No Previous Price")
                    # Discount Off on Product
                    try:
                        # print(i.find('div',{'class':'VGWI6T'}).text)
                        ProductPercentOff.append(i.find("div", {"class": "VGWI6T"}).text)
                    except:
                        # print("No Discount")
                        ProductPercentOff.append("No Discount")

                print("----------------------------------------------------------------")
            else:
                allcards = mysoup.findAll("div", {"class": "_3liAhj"})
                for i in allcards:
                    # Fetching Name of item
                    # print(i.find("a",{"class" : "_2cLu-l"}).text)
                    ProductName.append(i.find("a", {"class": "_2cLu-l"}).text)
                    # Below Code is For Fetching Price of item
                    try:
                        # print(i.find("div",{"class" : "_1vC4OE"}).text)
                        ProductPrice.append(i.find("div", {"class": "_1vC4OE"}).text)
                    except:
                        # print("Either Price is not Available or Item out of Stock")
                        ProductPrice.append("Either Price is not Available or Item out of Stock")
                    # Short Description
                    try:
                        # print(i.find("div",{"class" : "_1rcHFq"}).text)
                        ProductDescription.append(i.find("div", {"class": "_1rcHFq"}).text)
                    except:
                        # print("No Attribute is listed")
                        ProductDescription.append("No Attribute is listed")
                    # Fetching Star Rating (Out of 5)
                    try:
                        # print(i.find('div',{'class':'hGSR34'}).text)
                        ProductRating.append((i.find('div', {'class': 'hGSR34'}).text))
                    except:
                        # print("No Rating")
                        ProductRating.append("No Rating")
                    # Fetching Count of review and Rating
                    try:
                        # print(i.find('span',{'class':'_38sUEc'}).text)
                        ProductReviewCount.append(i.find("span", {"class": "_38sUEc"}).text)
                    except:
                        # print("No Review")
                        ProductReviewCount.append("No Review")
                    # Product Previous Price
                    try:
                        # print(i.find('div',{'class':'_3auQ3N'}).text)
                        ProductPreviousPrice.append(i.find("div", {"class": "_3auQ3N"}).text)
                    except:
                        # print("No Previous Price")
                        ProductPreviousPrice.append("No Previous Price")
                    # Discount Off on Product
                    try:
                        # print(i.find('div',{'class':'VGWI6T'}).text)
                        ProductPercentOff.append(i.find("div", {"class": "VGWI6T"}).text)
                    except:
                        # print("No Discount")
                        ProductPercentOff.append("No Discount")

                print("----------------------------------------------------------------\n")
            time.sleep(5)
    except HTTPError as e:
        print(e)
    except URLError:
        print("Server down or incorrect domain")
    else:
        print("Excel File Writing Started")
        df = DataFrame({'Product Name': ProductName, 'Current Product Price': ProductPrice,
                        'Product Description': ProductDescription, 'Product Rating': ProductRating,
                        'Product Rating & Review Count': ProductReviewCount,
                        'Previous Product Price': ProductPreviousPrice, 'Product Percent Off': ProductPercentOff})
        df = df[["Product Name", "Product Description", "Current Product Price", "Previous Product Price",
                 "Product Percent Off", "Product Rating", "Product Rating & Review Count"]]
        df.to_excel('D:\FlipkartDataExtract.xlsx', sheet_name='Flipkart-Data', index=False)
        browser.close()
        print("Excel File Writing Completed")
        print("Page Scraping is Done")
        print("If Your scraped data file is empty, then use other things")

# Calling the Image Download Function

def ImageDownload(url):
    driver = 'C:\windows\chromedriver'
    imageno = int(input("how many images u need to download ( upto 50 images ) : "))

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

    def search_and_download(search_term: str, driver_path: str, target_path='D:\images', number_images=noimage):

        target_folder = os.path.join(target_path, '_'.join(search_term.lower().split(' ')))
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)  # make dir if not present

        with webdriver.Chrome(executable_path=driver_path) as wd:
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
    with open("D:\scraped_Text_data.txt", "w", encoding='utf-8') as file:
        file.write(text)


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
        for F in (StartPage, PageOne, PageTwo):
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
        button1.pack()
        button2.pack()


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


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Text Recognition", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Select File", command=callfileuploader)
        button1.pack(pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack(pady=10)


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()