import time


def get_time():
    return time.ctime()


# 統一入口
# request: a dict
def application(env, handle_headers):
    env = {
        'query': '',
        'path': ''
    }
    status_code = 200
    'Content_Type': 'text/plain'
    'Content_Type': 'text/html'
    'Content_Type': 'image/*'
    'server': 'statick'

    handle_headers(status_code, [('Content_Type': 'text/plain'), ('server': 'statick')])

    return time.ctime()