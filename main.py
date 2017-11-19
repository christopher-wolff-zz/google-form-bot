import sys
import requests

# Target url
url = ""
# Form data
form_data = {"entry.xxxxx": "Response 1",
             "entry.xxxxx": "Response 2"}
# Number of requests
if len(sys.argv) > 1:
    n = int(sys.argv[1])
else:
    n = 1

if __name__ == "__main__":
    # Submit POST requests
    for k in range(n):
        r = requests.post(url, data=form_data)
        print("{}: {} {}".format(k, r.status_code, r.ok))
