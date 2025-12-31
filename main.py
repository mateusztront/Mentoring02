import requests

def main():
    # x = input('Gimme your PESEL:')
    # print('Your PESEL is: ', x)
    print('Requesting data for PESEL 12345')
    response = requests.get('http://127.0.0.2:8001/users/12345')
    data = response.json()
    print(data)

    print('Requesting data for PESEL 67890')
    response = requests.get('http://127.0.0.2:8001/users/67890')
    data = response.json()
    print(data)

if __name__ == "__main__":
    main()
