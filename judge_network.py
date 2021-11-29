import os
import requests
import re
import time

count_1 = 0
while True:
    res =requests.get('http://www.baidu.com')
    index_1 = res.text.find('http://192.168.50.3:8080')
    if index_1 != -1:
        #indicate that lossing the network
        print('retry to connect network')
        url  =  'http://192.168.50.3:8080/eportal/InterFace.do?method=login'
        header = {'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Content-Length': '879',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'EPORTAL_COOKIE_OPERATORPWD=; EPORTAL_AUTO_LAND=; EPORTAL_COOKIE_SERVER=; EPORTAL_COOKIE_USERNAME=M202172542; EPORTAL_COOKIE_DOMAIN=; EPORTAL_COOKIE_SAVEPASSWORD=true; EPORTAL_COOKIE_NEWV=true; EPORTAL_COOKIE_PASSWORD=710e5631d0e6859fd32c710937dd2ab6abd02b415b07152da2923229c67e79c8a9cbd192a0c728c7dce2ffcae685573929024faa10233598eb0f0e4ce202b132e8195b395235493042566df913837678b0c85b5108040c6cdc93a1aff03af4411f043feb0f166114591ef25286d1aad9d846860c6bbcfd72ef112426fe7e1cf2; EPORTAL_USER_GROUP=%E5%8D%8E%E4%B8%AD%E7%A7%91%E6%8A%80%E5%A4%A7%E5%AD%A6; EPORTAL_COOKIE_SERVER_NAME=; JSESSIONID=3EA91E9AAD22F6FF6303BB424C6FC427; JSESSIONID=AA7F784CA28945D6C2A808F91D8F60CB',
    'Host': '192.168.50.3:8080',
    'Origin': 'http://192.168.50.3:8080',
    'Referer': 'http://192.168.50.3:8080/eportal/index.jsp?wlanuserip=3a6835c7dbe3c1df99e4331c31d3a504&wlanacname=233322baafdcd02f08aefdb4dfeb70d5&ssid=&nasip=3d5b0623efdaf6f6c637fb1cd5f349ce&snmpagentip=&mac=448a28a6ad5c1d741fb905371ee8aea1&t=wireless-v2&url=2c0328164651e2b4f13b933ddf36628bea622dedcc302b30&apmac=&nasid=233322baafdcd02f08aefdb4dfeb70d5&vid=d0f9d58ab5ac1e97&port=fe5179d98e23daf6&nasportid=5b9da5b08a53a540806c821ff7c143817b8456636552c242e406f6e359fe6483',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Edg/94.0.992.38'
                  }


        data2 = {'userId': 'M202172542',
    'password': '74010639acf762c2722a594a50de0f9ad1ea1cc0c295ecdcdd2ad7b5a410ab8e28492b5200f93c95abeb155ce3b238738f297fc43b1e8de574f76b81e91998d68f18a0324f40e5a9379b1b41d19509dd67596a3651987fce470c4d50ea51868d0c42b74e7867aa10493ddbc6ea70f30bd15e4851943d09026f40eaf2c2b305fb',
    'service': '',
    'queryString': 'wlanuserip%3D3a6835c7dbe3c1dfeadb7de2be4d1a5e%26wlanacname%3D233322baafdcd02f08aefdb4dfeb70d5%26ssid%3D%26nasip%3D3d5b0623efdaf6f6c637fb1cd5f349ce%26snmpagentip%3D%26mac%3D586ca8af9cfad1e0676f4f57e76db78d%26t%3Dwireless-v2%26url%3D2c0328164651e2b4f13b933ddf36628bea622dedcc302b30%26apmac%3D%26nasid%3D233322baafdcd02f08aefdb4dfeb70d5%26vid%3Dd0f9d58ab5ac1e97%26port%3Dfe5179d98e23daf6%26nasportid%3D5b9da5b08a53a540806c821ff7c143817b8456636552c242e406f6e359fe6483',
    'operatorPwd': '',
    'operatorUserId': '',
    'validcode': '',
    'passwordEncrypt': 'true'}
        res = requests.post(url=url,headers=header,data=data2)
        print(res.status_code)
    else:
        print('network normal')
    print('judge {} count'.format(count_1))
    count_1 = count_1 + 1
    for i in range(30):
        time.sleep(60)
        
