import requests

header = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
        'Upgrade-Insecure-Requests': '1',
    }
url = "https://aweme.snssdk.com/aweme/v1/play/?video_id=v0200f670000bqlnqodp06vn5hl7uvhg&line=0&ratio=540p&watermark=1&media_type=4&vr_type=0&improve_bitrate=0&logo_name=aweme_search_suffix&is_support_h265=0&source=PackSourceEnum_PUBLISH"
r = requests.get(url, headers=header, stream=True)

with open(r"hh.mp4", "wb") as f:
    for chunk in r.iter_content(chunk_size=512):
        f.write(chunk)