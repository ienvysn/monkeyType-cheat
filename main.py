import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


#SETUPP
edge_option= webdriver.EdgeOptions()
edge_option.add_experimental_option("detach", True)
driver=webdriver.Edge(options=edge_option)
driver.get("https://monkeytype.com/")
print("hi")
time.sleep(1)

cookie_accept= driver.find_element(By.CLASS_NAME, value="acceptAll")
cookie_accept.click()

time.sleep(1)

# ------CUSTOMIZATION-----

fifty_words= driver.find_element(By.XPATH,value="//*[@id='testConfig']/div/div[3]/button[2]")
time.sleep(0.5)
fifty_words.click()
time.sleep(1)

# MAIN SCRIPT
while True:
    word_list=[]
    words= driver.find_elements(By.ID,value="words")
    text_box = driver.find_element(By.ID, 'wordsInput')
    for word in words:
            word_list.append(word.text)
            separated_words = word_list[0].split('\n')
    # print(separated_words)

    for i in range(len(separated_words)):
        text_box.send_keys(separated_words[i], Keys.SPACE)
        time.sleep(0.1)



# infinity= driver.find_element(By.XPATH,value="//html/body/div[10]/main/div/div[1]/div/div[5]/button[5]")
# infinity.click()
# time.sleep(0.2)
# infinity_input= driver.find_element(By.XPATH,value="/html/body/div[9]/dialog[2]/form/input")
# infinity_input.send_keys("0")
# time.sleep(0.2)
# ok_btn= driver.find_element(By.XPATH,value="/html/body/div[9]/dialog[2]/form/button")
# ok_btn.click()
# time.sleep(0.2)






# -----WORK IN PROGRESSS---------
# i=0
# last_word_count = 0
# while True:
#     word_list=[]
#     words= driver.find_elements(By.ID,value="words")
#     print(words)
#     text_box = driver.find_element(By.ID, 'wordsInput')
#     for word in words:
#             word_list.append(word.text)
#             separated_words = word_list[0].split('\n')
#     print(separated_words) ## this is the first iteration
#
#
#     if i!=0: ## this is for the remaing iteration
#         print(separated_words[:last_word_count])
#         del separated_words[:last_word_count]
#
#     for i in range(len(separated_words)):
#         text_box.send_keys(separated_words[i], Keys.SPACE)
#         time.sleep(0.01)
#     last_word_count = len(separated_words) + last_word_count
#     i+=1
#     time.sleep(0.1)
#





