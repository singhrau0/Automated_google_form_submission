from selenium import webdriver
import time
import random as rd
import pandas as pd
#Reading Our file data

data = pd.read_excel('covid.xlsx')
data.columns = ['s_no','name','age_group','gender','state','district']
name = data['name']
age_group = data['age_group']
gen = data['gender']
state = data['state']
district = data['district']
#maximizing window and automating bot

data_male = pd.read_csv("Indian-Male-Names.csv")
data_female = pd.read_csv("Indian-Female-Names.csv")

name_male = data_male["name"]
name_female = data_female["name"]

gender_male = data_male["gender"]
gender_female = data_female['gender']


chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("start-maximized")
driver = webdriver.Chrome(chrome_options=chromeOptions)
for i in range(1,len(name_male)):
    #opening form
    driver.get('https://docs.google.com/forms/d/1sj5dH2eWZ6EI1KS84HeS28uA0Qyh2MlvxwUVtPUoMkk/')
    #Choosing person type here
    time.sleep(2)
    choose_name = driver.find_element_by_xpath("//body/div/div/form/div/div/div[@role='list']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]")
    choose_name.click()
    time.sleep(2)
    n = rd.randint(0,1)
    print(n)
    if n ==0:
        choose_name_1 = driver.find_element_by_xpath("//body/div/div/form/div/div/div[@role='list']/div[@role='listitem']/div/div/div[@jscontroller='liFoG']/div[@role='listbox']/div[@role='presentation']/div[3]")
        choose_name_1.click()
    else:
        choose_name_2 = driver.find_element_by_xpath("//body/div/div/form/div/div/div[@role='list']/div[@role='listitem']/div/div/div[@jscontroller='liFoG']/div[@role='listbox']/div[@role='presentation']/div[4]")
        choose_name_2.click()
    #finding username here

    user_name = driver.find_element_by_xpath("//div[@role='list']//div[2]//div[1]//div[1]//div[2]//div[1]//div[1]//div[1]//div[1]//input[1]")

    #Taking gender randomly
    n1 = rd.randint(0,2)
    if gen[i] =="MALE":
        time.sleep(1)
        male = driver.find_element_by_xpath("//div[@aria-label='पुरुष']")
        male.click()
    elif gen[i]=="FEMALE":
        time.sleep(1)
        female = driver.find_element_by_xpath("//div[@aria-label='महिला']")
        female.click()
    else:
        others = driver.find_element_by_xpath("//div[@aria-label='अन्य']")
        others.click()

    #choosing option of covid positive or not
    time.sleep(1)
    choose_covid = driver.find_element_by_xpath("//body/div/div/form/div/div/div[@role='list']/div[7]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]")
    choose_covid.click()
    time.sleep(2)
    if n ==0:
        choose_covid_1 = driver.find_element_by_xpath("//body/div/div/form/div/div/div[@role='list']/div[@role='listitem']/div/div/div[@jscontroller='liFoG']/div[@role='listbox']/div[@role='presentation']/div[3]")
        choose_covid_1.click()
    else:
        choose_covid_2 = driver.find_element_by_xpath("//body/div/div/form/div/div/div[@role='list']/div[@role='listitem']/div/div/div[@jscontroller='liFoG']/div[@role='listbox']/div[@role='presentation']/div[4]")
        choose_covid_2.click()

    # taking effect of covid on health on both physically and mentally
    time.sleep(2)

    n1 = rd.randint(0,2)
    for k in range(1,3,1):
        print(i)
        if n1 ==0:
            effect1 = driver.find_element_by_xpath(f"(//span[@dir='auto'][contains(text(),'बुरा प्रभाव')])[{k}]")
            effect1.click()
        elif n1==1:
            effect2 = driver.find_element_by_xpath(f"(//span[@dir='auto'][contains(text(),'कोई प्रभाव नहीं पड़ा।')])[{k}]")
            effect2.click()
        elif n1==2:
            others = driver.find_element_by_xpath(f"(//span[@dir='auto'][normalize-space()='Other:'])[{k}]")
            others.click()
            time.sleep(1)
            others_text = driver.find_element_by_xpath(f"(//input[@aria-label='Other response'])[{k}]")

            others_text.send_keys("nothing")

    #Other diisease caused by covid 19


    if n ==0:
        choose_covid_1 = driver.find_element_by_xpath("//div[@aria-label='हाँ']")
        choose_covid_1.click()
    else:
        choose_covid_2 = driver.find_element_by_xpath("//div[@aria-label='नही']")
        choose_covid_2.click()
    # filling state
    sta = driver.find_element_by_xpath("//body/div/div/form/div/div/div[@role='list']/div[5]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]").click()
    time.sleep(1.5)
    sta2 = driver.find_element_by_xpath("//body/div/div/form/div/div/div[@role='list']/div[@role='listitem']/div/div/div[@jscontroller='liFoG']/div[@role='listbox']/div[@role='presentation']/div[29]").click()
    #treatment of covid 19
    n1 = rd.randint(0,2)
    if n1 ==0:
        time.sleep(1.5)
        effect1 = driver.find_element_by_xpath("//div[@aria-label='घर में एकांत रहकर ।']")
        effect1.click()
    elif n1==1:
        effect2 = driver.find_element_by_xpath("//div[@aria-label='अस्पताल में भर्ती होना पड़ा ।']")
        time.sleep(1.5)
        effect2.click()
    elif n1==2:
        time.sleep(1.5)
        others = driver.find_element_by_xpath("//div[@aria-label='लागू नहीं।']")
        others.click()
        time.sleep(1)
    # type of person
    n1 = 0
    if n1 ==0:
        effect1 = driver.find_element_by_xpath("//div[@aria-label='विद्यार्थी']")
        effect1.click()
    elif n1==1:
        effect2 = driver.find_element_by_xpath("//div[@aria-label='वेतनभोगी कर्मचारी']")
        effect2.click()
    elif n1==2:
        others = driver.find_element_by_xpath("//div[@aria-label='व्यवसायी']")
        others.click()

    elif n1==3:
        others = driver.find_element_by_xpath("//div[@aria-label='बेरोज़गार']")
        others.click()

    elif n1==4:
        others = driver.find_element_by_xpath("//div[@aria-label='गृहिणी']")
        others.click()

    user_name.send_keys(name[i])
    age = age_group[i]
    st = state[i]
    dt = district[i]
    if age == '15 -- 25 वर्ष':
        effect1 = driver.find_element_by_xpath("//div[@aria-label='15 -- 25 वर्ष']")
        effect1.click()
    elif age == '26 -- 45 वर्ष':
        effect2 = driver.find_element_by_xpath("//div[@aria-label='26 -- 45 वर्ष']")
        effect2.click()
    elif age == '45 -- 65 वर्ष':
        others = driver.find_element_by_xpath("//div[@aria-label='45 -- 65 वर्ष']")
        others.click()

    city = driver.find_element_by_xpath("//div[6]//div[1]//div[1]//div[2]//div[1]//div[1]//div[1]//div[1]//input[1]")
    city.send_keys(dt)

    next = driver.find_element_by_xpath("//body/div/div/form/div/div/div[@jscontroller='lSvzH']/div/div[1]/div[1]")
    time.sleep(1)
    next.click()

    # effect of covid 19 on person

    n1 = rd.randint(0,6)
    for j in range(n1):
        if j == 0:
            time.sleep(0.5)
            effect1 = driver.find_element_by_xpath("//span[contains(text(),'कोविड 19 महामारी में आप ठीक से पढाई नहीं कर पाए।')]")
            effect1.click()
        elif j == 1:
            time.sleep(0.5)
            effect2 = driver.find_element_by_xpath("//span[contains(text(),'ऑनलाइन कक्षाएं ठीक से नहीं चल रही है।')]")
            effect2.click()
        elif j == 2:
            time.sleep(0.5)
            others = driver.find_element_by_xpath("//span[contains(text(),'क्या आप अकेलापन महसूस कर रहे थे?')]")
            others.click()

        elif j == 3:
            time.sleep(0.5)
            others = driver.find_element_by_xpath("//span[contains(text(),'एकाग्रता पे कोई प्रभाव पड़ा।')]")
            others.click()

        elif j == 5:
            time.sleep(0.5)
            others = driver.find_element_by_xpath("//span[contains(text(),'फिटनेस पर नकारात्मक प्रभाव पड़ा')]")
            others.click()

    final_submit = driver.find_element_by_xpath("//body/div/div/form/div/div/div[@jscontroller='lSvzH']/div/div/div[2]")
    time.sleep(1)
    final_submit.click()
    time.sleep(2)
    new_response = driver.find_element_by_xpath("//a[normalize-space()='Submit another response']")
    new_response.click()

    time.sleep(3)








