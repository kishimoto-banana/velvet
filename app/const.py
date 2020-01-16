import re

title = "velvet"

url_regex = re.compile(r"https?://[\w/:%#\$&\?~\.=\+\-]+")

invalid_url_msg = "有効なURLではありません"