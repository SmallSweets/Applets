import requests
import json
import re

headers = {"user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"}

def do(url,localhost,downloadtype):
    try:
        src = url
        # src = "https://v.douyin.com/J5Lj3N3/"
        href = localhost
        # type = input("下载有无水印(默认无水印,有水印请输入 1,默认直接回车):")

        if href == "不输入默认为：D://":
            href = "D://"

        response = requests.get(src,headers=headers)

        all_url = response.url
        # print(all_url)


        id = re.findall(r'/\d{19}',all_url)[0].replace("/","")

        file_url = "https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids=" + id

        data = requests.get(file_url,headers=headers).text
        data = json.loads(data)

        name = data["item_list"][0]["desc"]

        for i in ",.?!|\"':":
            if i in name:
                name.replace(i,"")

        if downloadtype == 1:
        # 有水印
            video_url = data["item_list"][0]["video"]["play_addr"]["url_list"][0]
        else:
        # 无水印
            video_url = data["item_list"][0]["video"]["play_addr"]["url_list"][0].replace("playwm","play")

        content_url = requests.get(video_url,headers=headers).content


        with open(href + name + ".mp4","wb") as f:
            f.write(content_url)

        return ("---------------------------执行成功--------------------------------")
    except:
        return ("---------------------------执行失败--------------------------------")