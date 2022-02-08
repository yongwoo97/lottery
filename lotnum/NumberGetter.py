import requests
import json
lotto_url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo="
NEED_COL = ['drwNoDate', 'drwNo', 'drwtNo1',
            'drwtNo2', 'drwtNo3', 'drwtNo4',
            'drwtNo5', 'drwtNo6', 'bnusNo']
result = {'date': None, 'number': None,
              'n1': None, 'n2': None, 'n3': None,
              'n4': None, 'n5': None, 'n6': None,
              'n7': None}

def picker(raw, choice, ret):
    for i, j in enumerate(ret):
        #if i == 0:
        #    ret[j] = raw[choice[i]] + " 00:00:00"
        #    continue
        ret[j] = raw[choice[i]]
    return ret

def numget(number):
    resp = requests.get(lotto_url + str(number))
    jsResult = picker(resp.json(), NEED_COL, result)
    return jsResult
