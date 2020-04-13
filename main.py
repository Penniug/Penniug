# -*- coding: utf-8 -*-
import requests
import time
import json
import time
import re
import os

def main():
    IOSapi = 'https://api2.day.app:4443/9oA97bG3feXsEG5vzX6tq6/'
    qiwang = input('期望的价格(买入价):')
    os.system("mode con cols=20 lines=12")
    qiwang = float(qiwang)
    jishi = 0
    try:
        requests.get( IOSapi + '开始监控/' + '期望价(买入价):' + str(qiwang))
    except:
        print('......')
    totaltime = 0
    ftime = 0
    trytime = 0
    while(True):
        #fa = open.
        flag1 = 0
        url = 'https://openapi.boc.cn/mobileplatform/forex/querySingelQuotation?clentid=%27%27&userid=%27%27&acton=%27%27&chnflg=sjyh&clientType=html5&ccygrp=035001&cardType=G&cardClass=R&callback=callback1'
        try :
            a = requests.get(url)
            p2 = re.compile(r'[(](.*)[)]', re.S)
            b = re.findall(p2, str(a.content,encoding = "utf8"))
            c = json.loads(b[0])
        except:
            continue
        if c['head']['result'] == '操作成功':
            flag1 = 1
        if flag1 == 0 :
            print('error with internet!')
            trytime = trytime + 1
            print('trytime:' + str(trytime) )
            continue
        if flag1 == 1 :
            buyRate =float(c['body']['buyRate'])
            sellRate =float(c['body']['sellRate'])
            currDiff = c['body']['currDiff']
            time2 = c['head']['date'][-8:]
            if totaltime == 0 :
                mbuyRate = buyRate
                msellRate =sellRate
                mcurrDiff =currDiff
                mtime = time2
            else:
                if mbuyRate > buyRate :
                    mbuyRate = buyRate
                    msellRate = sellRate
                    mcurrDiff = currDiff
                    mtime = time2
            print('期望价(买入价):' + str(qiwang) + '\n')
            print(c['head']['date'][-8:] + '\n')
            print('买:' + c['body']['buyRate'] + '\n')
            print('卖:' + c['body']['sellRate'] + '\n')
            print('涨跌:' + c['body']['currDiff'] + '\n')
            if qiwang > float(c['body']['buyRate']) :
                try :
                    requests.get( IOSapi + '期望价(买入价):'+ str(qiwang) +'买:' + c['body']['buyRate'] +'元'+',' + '涨跌:' + c['body']['currDiff']  +','+'时间:'+c['head']['date'][-8:])
                except:
                    continue
                ftime = ftime + 1
                if ftime < 3:
                    time.sleep(360)
                elif ftime >9:
                    time.sleep(3600)
                else :
                    time.sleep(1800)
            else:
                ftime = 0
        jishi = jishi + 2
        totaltime = totaltime + 1
        if jishi > 900 :
            jishi = 0
            try :
                totaltime = 0
                requests.get( IOSapi + '半小时播报(约)/' + '期望价(买入价):' + str(qiwang) + '半小时内最低买:' + str(mbuyRate) + '元' + ',' + '涨跌:' + mcurrDiff  + ',' + '时间:' + mtime)
            except :
                continue
        time.sleep(2)
        os.system('cls')


main()
