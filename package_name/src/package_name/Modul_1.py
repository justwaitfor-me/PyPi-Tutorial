import json
from termcolor import colored
from urllib.parse import urlparse
import requests
import xmltodict

with open('src/tools/errors.json', 'r') as f:
    errors = json.load(f)

def valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc, result.path])
    except ValueError:
        return False

def domain(url):
    if valid_url(url) == False:
        raise ValueError(colored(errors["ValueError"]["msg"], "red"))
    if "https://" in url:
        if "https://www." in url:
            change = url[12:]
        elif not "https://www." in url:
            change = url[8:]
        else:
            change = None
    elif "http://" in url:
        if "http://www." in url:
            change = url[11:]
        elif not "https://www." in url:
            change = url[7:]
        else:
            change = None
    else:
        if "www." in url:
            change = url[4:]
        elif not "www." in url:
            change = url
        else:
            change = None
    
    if change != None:
        if not "/" in change and not "." in change:
            return change
        else:
            end = ""
            for i in change:
                if i != "/" and i != ".":
                    end += i
                else:
                    break
            return end
            
    else:
        raise ValueError(colored(errors["ValueError"]["msg"], "red"))
    
def censor(string):
    if isinstance(string, str):
        exp = ['a', 'e', 'i', 'o', 'u', 'y']
        res  = ""
        for i in string:
            if not i.lower() in exp:
                res += i    
        return res
    else:
        raise TypeError(colored(errors["TypeError"]["msg"], "red"))
    
def online_url(url):
    if valid_url(url) == False:
        raise ValueError(colored(errors["ValueError"]["msg"], "red"))
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException:
        return False
    
def xml_json(path, file_name='output.json'):
    if not isinstance(path, str) or not isinstance(file_name, str):
        raise TypeError(colored(errors["TypeError"]["msg"], "red"))
    with open(path, 'r') as file:
        xml_data = file.read()
    try:
        data_dict = xmltodict.parse(xml_data)
    except:
        raise ValueError(colored(errors["ValueError"]["msg"] + "\n(the given .xml file is not valid)", "yellow"))
    
    json_data = json.dumps(data_dict)

    with open(file_name, 'w') as file:
        file.write(json_data)
        

