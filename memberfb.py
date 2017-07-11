import requests
from urllib.parse import urlencode,quote_plus
import json

token = ''

names = ['Cherprang+Areekul',
            'Christin+Larsen',
            'Irada+Tavachphongsri',
            'Isarapa+Thawatpakdee',
            'Jennis+Oprasert',
            'Jetsupa+Kruetang',
            'Jiradapa+Intajak',
            'Kanteera+Wadcharathadsanakul',
            'Korapat+Nilprapa',
            'Kunjiranut+Intarasin',
            'Mananya+Kaoju',
            'Mesa+Chinavicharana',
            'Milin+Dokthian',
            'Miori+Ohkubo',
            'Napaphat+Worraphuttanon',
            'Natruja+Chutiwansopon',
            'Nayika+Srinian',
            'Panisa+Srilaloeng',
            'Patchanan+Jiajirachote',
            'Pichayapa+Natha',
            'Pimrapat+Phadungwatanachok',
            'Praewa+Suthamphongm',
            'Punsikorn+Tiyakorn',
            'Rinrada+Inthaisong',
            'Rina+Izuta',
            'Sawitchaya+Kajonrungsilp',
            'Suchaya+Saenkhot',
            'Vathusiri+Phuwapunyasiri',
            'Warattaya+Deesomlert',
            'Watsamon+Phongwanit']

for member in names:
    r = requests.get('https://graph.facebook.com/search?q='+member+'&type=user&access_token=' + token)
    r.encoding
    obj = r.json()
    if(obj['data'] == null):
        print(member + '= not found')
    j = json.dumps(obj)
    print(obj['data'][0])

