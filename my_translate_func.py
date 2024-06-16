import urllib
import urllib.request
import urllib.parse

import json

from translate import Translator
# from googletrans import Translator
# translator = Translator()


def tran(text):
    # 指定要翻译成的语言
    translator = Translator(to_lang="Chinese")
    translation = translator.translate(text)

    # translation = translator.translate(text).text
    return translation

# 百度翻译方法
def baidu_translate(content, type=1):
    '''实现百度翻译'''
    baidu_url = 'http://fanyi.baidu.com/basetrans'
    data = {}

    data['from'] = 'en'
    data['to'] = 'zh'
    data['query'] = content
    data['transtype'] = 'translang'
    data['simple_means_flag'] = '3'
    data['sign'] = '94582.365127'
    data['token'] = 'ec980ef090b173ebdff2eea5ffd9a778'
    data = urllib.parse.urlencode(data).encode('utf-8')

    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Mobile Safari/537.36"}
    baidu_re = urllib.request.Request(baidu_url, data, headers)
    baidu_response = urllib.request.urlopen(baidu_re)
    baidu_html = baidu_response.read().decode('utf-8')
    target2 = json.loads(baidu_html)

    trans = target2['trans']
    ret = ''
    for i in range(len(trans)):
        ret += trans[i]['dst'] + '\n'

    return ret

# 有道翻译方法1
def translate_you_dao1(content):
    '''实现有道翻译的接口'''
    youdao_url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom='
    data = {}

    data['i'] = content
    data['from'] = 'AUTO'
    data['to'] = 'AUTO'
    data['smartresult'] = 'dict'
    data['client'] = 'fanyideskweb'
    data['salt'] = '1525141473246'
    data['sign'] = '47ee728a4465ef98ac06510bf67f3023'
    data['doctype'] = 'json'
    data['version'] = '2.1'
    data['keyfrom'] = 'fanyi.web'
    data['action'] = 'FY_BY_CLICKBUTTION'
    data['typoResult'] = 'false'
    data = urllib.parse.urlencode(data).encode('utf-8')

    youdao_response = urllib.request.urlopen(youdao_url, data)
    youdao_html = youdao_response.read().decode('utf-8')
    target = json.loads(youdao_html)

    trans = target['translateResult']
    ret = ''
    for i in range(len(trans)):
        line = ''
        for j in range(len(trans[i])):
            line = trans[i][j]['tgt']
        ret += line + '\n'

    return ret
# 有道翻译方法2
def translate_you_dao2(text):
    url_youdao = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom='\
    'http://www.youdao.com/'
    dict = {}
    dict['type'] = 'AUTO'
    dict['doctype'] = 'json'
    dict['xmlVersion'] = '1.8'
    dict['keyfrom'] = 'fanyi.web'
    dict['ue'] = 'UTF-8'
    dict['action'] = 'FY_BY_CLICKBUTTON'
    dict['typoResult'] = 'true'

    dict['i'] = text
    data = urllib.parse.urlencode(dict).encode('utf-8')
    response = urllib.request.urlopen(url_youdao, data)
    content = response.read().decode('utf-8')
    print(content)
    data = json.loads(str(content), strict=False)
    result = data['translateResult'][0][0]['tgt']
    print(result)
    return result