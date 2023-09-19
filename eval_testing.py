import requests
requests.packages.urllib3.disable_warnings()

print("Test Eval")
def modify_value(x1,x2,x3, equation):
    result = eval(equation)
    print(result)
    return result

def init_global_equation():
    headers = {}
    aio_url = "https://io.adafruit.com/api/v2/kiin11/feeds/equation"
    x =requests.get(url=aio_url, headers = headers, verify = False)
    data = x.json()
    global_equation = data["last_value"]
    print("Get lastest value: ", global_equation)
    return  global_equation