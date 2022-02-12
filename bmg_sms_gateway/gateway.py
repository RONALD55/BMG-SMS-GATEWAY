import requests
import re
import json


def send_single_sms(username: str, password: str, body: dict):
    """
    :param username:str put your bmg username here
    :param password:str put your bmg password here
    :param body:dict put your message body here
    :return: number
    """

    if not isinstance(username, str):
        raise TypeError("Expected a string on username, got %s" % (type(username)))

    if not isinstance(password, str):
        raise TypeError("Expected a string on password, got %s" % (type(password)))

    if not isinstance(body, dict):
        raise TypeError("Expected a dictionary on the body, got %s" % (type(body)))

    keys = ['originator', "destination", "messageText", "messageReference", "messageDate", "messageValidity",
            "sendDateTime"]
    for i in keys:
        if i in body.keys():
            pass
        else:
            raise ValueError("A key `%s` is missing in the message body. Kindly restructure your message body." % i)

    pattern = re.compile(r"^2637[13478][0-9]{7}$")
    if re.fullmatch(pattern, body.get("destination")):
        pass
    else:
        raise ValueError("the destination : %s is not a valid Zimbabwean mobile number" % body.get("destination"))

    url = "https://mobile.esolutions.co.zw/bmg/api/single"
    headers = {'Content-Type': "application/json", 'Accept': "application/json"}

    # making sure that it's a dictionary of strings only and converting the result to json
    json_object = json.dumps({str(key): str(value) for key, value in body.items()})

    try:
        response = requests.post(url, headers=headers, data=json_object, auth=(username, password))
        print(json_object)
        response.raise_for_status()
        return response.status_code

    except ConnectionError as e:
        return "Failed to send the sms please check your internet connection"
