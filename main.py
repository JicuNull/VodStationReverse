from client.vodafone_client import VodafoneClient as Client
import os

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pwd = os.environ.get('PASSWORD')

    client = Client()
    if client.login(pwd):
        print(client.toggle_led(False).body)
        print(client.toggle_firewall(False).body)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
