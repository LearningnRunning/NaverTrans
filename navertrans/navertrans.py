# -*- coding: utf-8 -*-
"""
Naver Translator for Python
"""
import requests
import json
import time
import sys
import re
from cachetools import TTLCache
from urllib import parse
from collections import OrderedDict
import xml.etree.ElementTree as ET

from . import __version__
from .response import Checked
from .constants import base_url

_agent = requests.Session()
PY3 = sys.version_info[0] == 3
cache = TTLCache(maxsize = 10, ttl = 3600)

def read_token():
    try:
        TOKEN = cache.get('PASSPORT_TOKEN')
        return TOKEN
    except KeyError:
        return None

def update_token(agent):
    # https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%B2%88%EC%97%AD%EA%B8%B0&oquery=%EB%B2%88%EC%97%AD%EA%B8%B0&tqi=igm9gwqVOsCssd%2FtTphssssssAo-159358
    html = agent.get(url='https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=번역기') 

    match = re.search('passportKey=([a-zA-Z0-9]+)', html.text)
    if match is not None:
        TOKEN = parse.unquote(match.group(1))
        cache['PASSPORT_TOKEN'] = TOKEN
    return TOKEN

def get_response(TOKEN, text, src_lan, tar_lan):
    
    if TOKEN is None:
        TOKEN = update_token(_agent)
    
    payload = {
        'passportKey' : TOKEN,
        'query': text,
        'srcLang': src_lan,
        'tarLang': tar_lan
    }
    
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
        'referer': 'https://search.naver.com/',
    }
    
    r = _agent.get(base_url, params=payload, headers=headers)
    data = json.loads(r.text)
    
    if 'error' in data['message'] :
        r = get_response(update_token(_agent), text)
             
    return r


def translate(src_txt, src_lan = 'en', tar_lan = 'ko'):
    """
    Translate text from one language to another.

    Args:
        text (str): The text to be translated.
        src_lan (str, optional): The source language (default is 'ko' for Korean).
        tar_lan (str, optional): The target language (default is 'en' for English).

    Returns:
        str: The translated text in the target language.
    """
    if isinstance(src_txt, list):
        result = []
        for item in src_txt:
            checked = translate(item)
            result.append(checked)
        return result

    # # 최대 500자까지 가능.
    # if len(src_txt) > 500:
    #     return Checked(result=False)
    
    
    src_txt_list = []
    rlt_txt_list = []
    current_segment = ""
    if len(src_txt) > 500:
        split_txt = src_txt.split('.')  # Split the text using '.' as a delimiter
        
        
        for sentence in split_txt:
            if len(current_segment) + len(sentence) < 500:
                current_segment += sentence + '.'
            else:
                src_txt_list.append(current_segment)
                current_segment = ""
                current_segment = sentence + '.'

        start_time = time.time()  
        rlt_txt_list = []
        for src_txt in src_txt_list:
            r = get_response(read_token(), src_txt, src_lan, tar_lan) 
            data = json.loads(r.text)
            rlt_txt_list.append(data['message']['result']['translatedText'])
            
        trans_result = "".join(rlt_txt_list)
        passed_time = time.time() - start_time

    else:
        start_time = time.time()
        r = get_response(read_token(), src_txt, src_lan, tar_lan)
        passed_time = time.time() - start_time
        
        data = json.loads(r.text)
        trans_result = data['message']['result']['translatedText']

    result = {
        'result': True,
        'original': src_txt,
        'version': data['message']['@version'],
        'srcLangType': data['message']['result']['srcLangType'],
        'tarLangType': data['message']['result']['tarLangType'],
        'translatedText' : trans_result,
        'time': passed_time,
        'words': OrderedDict(),
    }

    # result = Checked(**result)

    return result['translatedText']
