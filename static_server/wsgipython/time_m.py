import time

def application(env, start_response):
    status = '200 ok'
    headers = [
        ('Content-type', 'text/plain')
    ]
    start_response(status, header)
    return time.ctime()