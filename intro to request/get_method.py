import requests

'''
Most commonly 2 types of requests are used:
- GET       -> used to retrieve information
- POST      -> used to send information

'''

# request.get(url) -- response object

response = requests.get('https://www.google.com')
#print(response)

#content
# response.content

print(response.content)


#Status codes

'''
1xx     Informational
2xx     Success
3xx     Redirection
4xx     Client Error
5xx     Server Error
'''