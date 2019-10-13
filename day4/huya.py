from selenium import webdriver
from lxml import  etree
import time
'''
driver = webdriver.PhantomJS()

driver.get('https://www.huya.com/l')

ret = driver.page_source.find('laypage_next')

#print(ret)

'''

class Huya(object):
    def __init__(self):
        self.driver = webdriver.PhantomJS()


    def start(self):
        #open webpage
        self.driver.get('https://www.huya.com/l')

        roomSum = 0
        hotSum = 0


        while True:
            time.sleep(1)

            content = etree.HTML(self.driver.page_source)


            #xpath
            liverName = content.xpath("//i[@class='nick']/text()")
            roomNames = content.xpath("//li[@class='game-live-item']/a[2]/text()")
            hots = content.xpath("//i[@class='js-num']/text()")
            liveType = content.xpath("//span[@class='game-type fr']/a/text()")

            #f = open('huya.txt', 'a+', encoding='utf-8')
            #loop
            for roomName, hot, liveType, liverName in zip(roomNames, hots, liveType, liverName):
                roomName = roomName.strip()
                print('直播类型:', liveType, '\n热度：', hot, '\n房间名: ', roomName, '\n\n')
                roomSum += 1
                f = open('huya.txt', 'a+', encoding='utf-8')
                #print(tiebaBlurb)

                f.write('主播名字' + liverName + '\n直播类型:' + liveType + '\n热度：' + hot + '\n房间名: ' + roomName + '\n\n')


                if hot[-1] == '万':
                    hot = hot[:-1]
                    hot = int(float(hot) * 10000)
                    hotSum += hot
                else:
                    hotSum += int(hot)

                print('Sum Room Num: ', roomSum)
                print('sum hot: ', hotSum)
                #f.write('----------------Next Page----------------')

            ret = self.driver.page_source.find('laypage_next')
            if ret > 0:
                self.driver.find_element_by_class_name('laypage_next')


                #f = open('huya.txt','a+', encoding='utf-8')
                #print(tiebaBlurb)

                #f.write('直播类型:', liveType, '\n热度：', hot, '\n房间名: ', roomName, '\n\n')
            else:
                exit()
            f.write('----------------Next Page----------------\n')
            f.close()



    

if __name__ == '__main__':
    huya = Huya()
    huya.start()