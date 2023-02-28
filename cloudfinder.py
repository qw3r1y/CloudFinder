import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)



url_list = []
#It will be added here with the file location where our urls are.
with open(r"X:\Example\ex\Documents\Python\urller.txt") as file:
    for row in file:
        url_list.append(row.split("\n")[0])
        

# List of keywords to search for in headers
keyword_list = []
#It will be added here with the file location where our urls are.
with open(r"X:\Example\ex\Documents\Documents\Python\keyword.txt") as file:
    for row in file:
        keyword_list.append(row.split("\n")[0])


# Loop through the URLs and send requests
for url in url_list:
    response = requests.get(url , allow_redirects=False, verify=False, timeout=5)
    print(f'Send Request -----> {url}')
    headers = str(response.headers).lower()


    for keyword in keyword_list:
        if keyword in headers:
            print(f'Cloud service find {url}')
            print(keyword)
            print("-"*50)
            ths = open("cloudfound.txt", "a")
            ths.writelines(url + "\n")
            ths.close()
            break
        
    else:  
        print(f"Cloud service not found {url}")
        print("-"*50)


            



