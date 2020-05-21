import re
import requests


def get_awemes(user_id, max_cursor=0):
    requests.packages.urllib3.disable_warnings()
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "accept": "application/json",
        "accept-encoding": "gzip, deflate",
        "accept-language": "zh-CN,zh;q=0.9"
    }

    response = requests.get('https://www.iesdouyin.com/share/user/{}'.format(user_id), headers=headers, verify=False)
    html = response.text
    tac = re.search(r"tac='([\s\S]*?)'</script>", html).group(1)
    data = {
        "tac": tac.split("|")[0],
        'user_id': user_id
    }
    response = requests.post('http://49.233.200.77:5001', data=data)
    sign = response.json().get('signature')
    url_templete = "https://www.iesdouyin.com/web/api/v2/aweme/post/?user_id={}&sec_uid=&count=36&max_cursor={}&aid=1128&_signature={}"
    url = url_templete.format(user_id, max_cursor, sign)
    response = requests.get(url, headers=headers, verify=False)
    return response.json()
