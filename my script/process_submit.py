from AA_dict import AA_dict
from process import process_data
from section import quote
import json
import re
import requests
import http.cookiejar as cookielib

#grab the database
class database(object):
    def __init__(self):
        #header and CMS_session save
        self.url = "http://cms.novogene.com/"
        self.CMS_Session = requests.session()
        self.CMS_Session.cookies = cookielib.LWPCookieJar(filename="CMSCookies.txt")
        self.UserAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
        self.header = {
            #"Origin": "http://cms.novogene.com",
            "Referer": "http://cms.novogene.com/index.jsp",
            "User-Agent": self.UserAgent,
        }
    def login(self):
        print("login.....")
        postUrl = "http://cms.novogene.com/core/login/login!login.action"
        try:
            postData = {
                "loginInfo.usercode": "jerry.jie",
                "loginInfo.userpass": "1",
                "loginInfo.islocal": "1",
            }
            self.responseRes = self.CMS_Session.post(
                postUrl, data=postData, headers=self.header)
            print(f"statusCode = {self.responseRes.status_code}")
            print(f"text = {self.responseRes.text}")
            #CMS_Session.cookies.save(ignore_discard=True, ignore_expires=True)
        except KeyError as e:
            print(
                f"no such a person existed in database {self.searchObj[13].lower()}")
    def update_producttype(self):
        print("trying to grab all the data.......")
        process_info_url = 'http://cms.novogene.com/nhzy/qmprocess/process!selectProcessInfosForProcessname.action'
        processtype_url = 'http://cms.novogene.com/nhzy/qmprocess/process!selectProcessInfosForProcesstype.action'
        AA_url = 'http://cms.novogene.com/nhzy/qmproduct/product!selectProductInfosByCond.action'
        AA_dict = {}
        #search AA
        AA_post = {
            "cond.auditflag": '2',
            "cond.bcompany": '202',
            "cond.isnewversion": 'Y',
            "cond.salesid":	"",
            "jsonString": '{"cond":{"productcode":"AA"}}',
            "page": '1',
            "start": '0',
            "limit": '100'
        }
        #search product
        post = {
            "cond.productcode": "",
            "cond.isforprocess": "N",
            "cond.isstandard": "N",
            "page": '1',
            "start": '0',
            "limit": '25'
        }
        #search product_type
        post_type = {
            "cond.productcode": "",
            "cond.processname": "",
            "page": '1',
            "start": '0',
            "limit": '25'
        }
        #update AA list
        AA = self.CMS_Session.post(AA_url, headers=self.header, data=AA_post)
        #test if login
        assert (not("sessionisnull" in AA.text)), "please login first"
        #update producttype and AA_list
        for i in json.loads(AA.text)['productInfos']:
            #print(i['productcode']+':'+i['productdesc'])
            AA_dict.update({i['productcode']: {i['productcode']: {
                           i['productcode']: i['productdesc']}}})
        for x in AA_dict.keys():
            post.update({"cond.productcode": x})
            post_type.update({"cond.productcode": x})
            process = self.CMS_Session.post(
                process_info_url, headers=self.header, data=post)
            process_dict = json.loads(process.text)
            for i in process_dict['vmaps']:
                AA_dict[x].update(
                    {i['PROCESSNAME']: {i['PROCESSNAME']: i['PROCESSNAMEDESC']}})
                post_type.update({"cond.processname": i['PROCESSNAME']})
                processtype = self.CMS_Session.post(
                    processtype_url, headers=self.header, data=post_type)
                for p in json.loads(processtype.text)['vmaps']:
                    AA_dict[x][i['PROCESSNAME']].update(
                        {p['PROCESSTYPE']: p['PROCESSTYPEDESC']})
        with open("AA_dict.py", mode='w', encoding='utf-8') as i:
            i.write("AA_dict = " + str(AA_dict) + "\n")
