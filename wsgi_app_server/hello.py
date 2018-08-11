

def main_app(environ, start_response):
    data = environ.get('QUERY_STRING')
    answer = '\n'.join(data.split('&'))
    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(data)))
    ]
    start_response(status, response_headers)
    return answer