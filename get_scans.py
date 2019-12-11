import sys
import requests
from veracode_api_signing.plugin_requests import RequestsAuthPluginVeracodeHMAC


api_base = "https://api.veracode.com/was/configservice/v1"
headers = {"User-Agent": "Get Scans Example"}


if __name__ == "__main__":

    try:
        response = requests.get(api_base + "/analyses/294179c7084394f182fb6ec167f3d18e/scans", auth=RequestsAuthPluginVeracodeHMAC(), headers=headers)
    except requests.RequestException as e:
        print("Failed...")
        print(e)
        sys.exit(1)

    if response.ok:
        data = response.json()
        print (data)
        #for ws in data["_embedded"]["workspaces"]:
        #    print (ws["name"] + " --- " + ws["id"])
    else:
        print(response.status_code)
