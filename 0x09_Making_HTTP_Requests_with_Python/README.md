# Making HTTP Requests With Python

## Http Introduction

- Describe What Happens When you Type a Url in the Url Bar
- Describe the request/response cycle
- Explain What a request or response header is, and give examples
- Explain the different categories of response codes
- Compare Get and Post requests

## what Happens when I hit google.com

- DNS LOOKUP : identifing ip address
- Computer makes a Request to a server
- Server processes the Request
- Server Issues a Response
the last the mention is call Request/Response cycle

## DNS LOOKUP

like a Phonebook for the internet
![SAMUEL_DNS](/image/dns%20lookup%20image.png)

## Resquest and Response

![samuel](/image/samuel_request.png)

## HTTP HEARDER

- Sent with both request and response
- Provide additional information about the request or response

### Header example

- the are like meta data sent with request and response
- Provide additional information about the request or response

#### request

![header request_samuel](/image/header%20example.png)

#### Response Status Code

![Response status code](/image/response.png)

## HTTP VERBS

![samueleffiong_httpverse](/image/http%20verbs.png)

## APIS

- API - application programming Interface
- Allows you to get data from another without needing to understand how the application works
- can often send data back in different formats
- Examples of companies with APIs: Github, spotify,Google
Json: javascript starndard object notation

## Using the requests Module

[SEE PYPI DOC](https://pypi.org/project/requests/)     [SEE PYTHON DOC](https://docs.python-requests.org/en/latest/)

```bash
# Installing request
$  python -m pip install requests

# using the request on terminal 
$ import requests
$ res = requests.get("https://news.ycombinator.com/")
# see the response with 
$ res
# verify response 
$ res.ok
# see headers
$ res.headers
# view data
$ r.encoding
$ res.text
$ res.json()
```

### requests module

- let us make http requests from python code
- useful for web scraping/crawling, grabbing data from other ApIs, etc

```bash
# Request Headesrs
$ import requests

$ response = request.get(
$    "https://www.example.com",
$    headers = {
$        "header1": "value",
$        "header2": "value"
$   }
$ )
```

## What"s A Query String?

- A way to pass data to the server as part of a Get request
- <http://www.example/com/?key1=value1&key2=value2>
