'''
script can used to submit the SIF automatically. import library from process_submit.py
author: Jerry
date: 1/16/2020
'''

from process_submit import *


class SIF(database):
    '''get database init'''
    def  __init__(self):
        super().__init__()
        self.contract_post = ""
    
    def json_post(self, data):
        '''transfer data to json format'''
        try:
            obj = {
                "jsonString": json.dumps(data),
                "limit": 1,
            }
        except TypeError as e:
            print(e)
            print("Please check data type!")
        return obj
    
    def contract_search(self, contract:str) -> str:
        contract_search_url = "http://cms.novogene.com/crm/contract/contractkefu!selectContractInfo4Batch.action"
        contract_info = {"cond":{"contractname":contract}}
        post = self.json_post(contract_info)
        search = self.CMS_Session.post(contract_search_url, headers = self.header, data = post)
        statusCode = search.status_code
        print(f"statusCode = {statusCode}")
        return json.loads(search.text)


contractid = search['contractInfos'][0]['contractid']
contractno = search['contractInfos'][0]['contractsno']
contractname = search['contractInfos'][0]['contractname']

# setup batch ID
# process_SIF_dict from process.py
SIF_batchID_url = "http://cms.novogene.com/nhzy/subproject/kfappointment!insertKfappointmentInfo.action"

#search batch ID
string = "kfappointmentInfo:{batchid:9C2DDE3FD26E35C8E053260811ACE00E,pageflag: 'zxmpcpage'}}"

SIF_batchID_search_url = "http://cms.novogene.com/nhzy/subproject/kfappointment!selectKfappointmentInfoById.action"


#save SIF and get batch ID
obj = {
    "con.batchid": "batchID"
}
SIF_batchID_save_url = "http://cms.novogene.com/nhzy/subproject/kfsampleinfo!selectKfsampleinfoInfosByCond.action"