# Client Action
# You can use the test api at [site]/docs instead of this
import sys
import requests

def main():
    
    url = "https://manoplace.cs.usu.edu:9000/"

    # Change these credentials of course
    username = 'A02310135'
    password = '88893347'

    # login
    payload = {'username': username, 'password': password}
    response = requests.post(url + "login", data=payload)

    # Check login
    if response.status_code == 200:
        print("\tYou have successfully logged in as " + username + "\n")
    else:
        print("\tThere was an error logging in.")
        sys.exit(1)

    # Save authentication token
    response = response.json()
    header = {
        'Authorization': 'Bearer ' + response['access_token'],
    }

    # Option Menu Processing
    # 1) Reset your account with a new program and shellcode if the supplied arg1 is "reset"

    if len(sys.argv) > 1 and sys.argv[1] == "reset":
        response = requests.post(url + "reset", headers=header)
        if response.status_code == 200:
            print(response.json()['result'])
        else:
            print("There was a problem resetting your account")
        sys.exit(0)

    if len(sys.argv) > 1 and sys.argv[1] == "submit":
        #read result.txt
        with open('secret/results.txt', 'r') as myfile:
            ticket=myfile.read().replace('\n', '')
        
        #result.txt reads like this
        ##Congratulations!!! You completed your task in 0:00:00.837014
        #That qualifies you for 35 speed points. That's the max possible plus a bonus 10!!!
        #35$67$a02310135
        #Submit this ticket value to the website: a96945c86816d3c65c21ca2b1207d7c85841077215667217098f37b3:67:35:837014 

        #we only want the part after website: 
        #a96945c86816d3c65c21ca2b1207d7c85841077215667217098f37b3:67:35:837014

        ticket = ticket.split("website: ")[1]



        data = {
            'ticket': ticket
        }
        # Submit ticket
        response = requests.post(url + "submit", data=data, headers=header)
        if response.status_code == 200:
            print(response.json()['result'])
        else:
            print("There was a problem with your ticket submission")
        sys.exit(0)
    




    #response = requests.post(url + "sign", data=data, headers=header)

if __name__ == "__main__":
    main()

#./2.sh
