# from: https://github.com/jcgregorio/httplib2/wiki/Examples
import httplib2
h = httplib2.Http(".cache")
resp, content = h.request("http://[2a03:7220:8081:c500::1]/", "GET")
print resp