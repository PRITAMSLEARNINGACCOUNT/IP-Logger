import requests


def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    # print(type(response["ip"]))
    return response["ip"]


def get_location(IP=None):
    if IP:
        ip_address = IP
    else:
        ip_address = get_ip()
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    location_data = {
        "ip": ip_address,
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country_name")
    }
    return location_data


Boolean = input(
    "Do You Want To Track Information About A Particular IP Address(Give Answer In Yes Or No Only)??\n")
if Boolean == "yes" or Boolean == "Yes":
    IP = input("Enter A IP Address You Want To Track??\n")
    print("So The Location Of The IP Address Provided By You Is - ")
    print(get_location(IP))
if Boolean == "No" or Boolean == "no":
    # IP = input("Enter A IP Address You Want To Track??\n")
    print("So The Location Data Of Your Own IP Address Is - ")
    print(get_location())
