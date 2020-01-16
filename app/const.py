import re

# api
config_path = "/app/config.yml"
hatebu_prediction_path = "/v1/prediction"

# meta
title = "velvet"

# err
url_regex = re.compile(r"https?://[\w/:%#\$&\?~\.=\+\-]+")

# err msg
invalid_url_msg = "有効なURLではありません"