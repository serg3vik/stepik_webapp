def app(environ, start_response):
    

    print ("Weeee are the champions my frieeeeeend!")
    data = 'Give me some params, please'
    querystr_raw = environ['QUERY_STRING']
    if querystr_raw:
        #pass
        data = querystr_raw.replace('&', '\n')
    
    
    
    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(data)))
    ]
    start_response(status, response_headers)
    return iter(data.encode('utf-8'))
