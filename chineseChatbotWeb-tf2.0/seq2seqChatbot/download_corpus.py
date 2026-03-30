# coding=utf-8
import os
import urllib.request

import getConfig


DEFAULT_URL = "https://raw.githubusercontent.com/pzy2000/-/main/xiaohuangji50w_nofenci.conv"


def main():
    g_config = getConfig.get_config()
    target_path = g_config["resource_data"]
    url = g_config.get("corpus_url", DEFAULT_URL)

    os.makedirs(os.path.dirname(target_path), exist_ok=True)
    print("开始下载语料：%s" % url)
    urllib.request.urlretrieve(url, target_path)

    file_size = os.path.getsize(target_path)
    if file_size == 0:
        raise ValueError("下载完成但语料为空，请检查下载链接或网络连接。")

    print("下载完成：%s（%.2f MB）" % (target_path, file_size / 1024 / 1024))


if __name__ == "__main__":
    main()
