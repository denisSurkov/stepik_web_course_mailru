

def main_app(environ, start_response):
    data = environ.get('QUERY_STRING')
    answer = [bytes(i + '\n', 'ascii') for i in data.split('&')]
    status = '200 OK'
    response_headers = [
        ('Content-Type', 'text/plain')
    ]
    start_response(status, response_headers)
    return answer
