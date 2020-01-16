import re

# api
config_path = "/app/config.yml"
hatebu_prediction_path = "/v1/prediction"

# meta
title = "velvet"

# err
url_regex = re.compile(r"https?://[\w/:%#\$&\?~\.=\+\-]+")


class InvalidUrlError(Exception):
    """有効なURLでは無かったときに投げるエラー"""


class CannotGetBlogContentError(Exception):
    """ページの情報の取得に失敗したときに投げるエラー"""


class UnexpectedError(Exception):
    """予期していないエラーのときに投げるエラー"""


# error code
invalid_url_code = 2001
exception_code = 1000
cannot_scrape_code = 1001
cannot_tokenize_code = 1002
cannot_predict_code = 1003

# error msg
invalid_url_msg = "有効なURLではありません"
cannot_get_blog_content_msg = "ブログの情報を取得できませんでした。URLを確認してみてください。"
unexpected_msg = "予期していないエラーが起きました。ちょっと諦めてください…"
