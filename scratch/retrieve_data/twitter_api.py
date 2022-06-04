import os
import webbrowser
from twython import Twython

# 获取的twitter开发者账号的key和secret，配置在环境变量中
CONSUMER_KEY = os.environ.get('TWITTER_CONSUMER_KEY')
CONSUMER_SECRET = os.environ.get('TWITTER_CONSUMER_SECRET')

# 实例化客户端
temp_client = Twython(CONSUMER_KEY, CONSUMER_SECRET)
temp_creds = temp_client.get_authentication_tokens()

url = temp_creds['auth_url']

print(f"go visit {url} and get the PIN CODE and paste it below")
webbrowser.open(url)
PIN_CODE = input('Please enter the PIN CODE: ')

auth_client = Twython(CONSUMER_KEY, CONSUMER_SECRET,
                      temp_creds['oauth_token'], temp_creds['oauth_token_secret'])
final_step = auth_client.get_authorized_tokens(PIN_CODE)

ACCESS_TOKEN = final_step['oauth_token']
ACCESS_TOKEN_SECRET = final_step['oauth_token_secret']
print(f"ACCESS_TOKEN: {ACCESS_TOKEN}")
print(f"ACCESS_TOKEN_SECRET: {ACCESS_TOKEN_SECRET}")
