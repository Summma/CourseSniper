import requests
import time
from send_message import send_sms_via_email
import json
from constants import EMAIL, PASSWORD, NUMBER

CLASS_NAME = {
    "07232": "Data Structures GOOD",
    "07233": "Data Structures GOOD",
    "07234": "Data Structures GOOD",
    "07235": "Data Structures GOOD",
    "07236": "Data Structures GOOD",
    "07237": "Data Structures GOOD",
    "07238": "Data Structures GOOD",
    "07239": "Data Structures GOOD",
    "07240": "Data Structures GOOD",
    "07241": "Data Structures GOOD",
    "07242": "Data Structures GOOD",
    "07243": "Data Structures GOOD",
    "07244": "Data Structures GOOD",
    "07245": "Data Structures GOOD",
    "07246": "Data Structures GOOD",
    "07247": "Data Structures GOOD",
    "07248": "Data Structures GOOD",
    "07249": "Data Structures GOOD",
    "07250": "Data Structures GOOD",
    "07251": "Data Structures GOOD",
    "07252": "Data Structures GOOD",
    "07253": "Data Structures GOOD",
    "07254": "Data Structures GOOD",
    "07255": "Data Structures GOOD",
    "07256": "Data Structures GOOD",
    "07261": "Data Structures GOOD",
    "07262": "Data Structures GOOD",
    "07263": "Data Structures GOOD",
    "07264": "Data Structures GOOD",
    "07265": "Data Structures GOOD",
    "07270": "Data Structures GOOD",
    "07271": "Data Structures GOOD",
    "07272": "Data Structures GOOD",
    "07273": "Data Structures GOOD",
    "07274": "Data Structures GOOD",
    "07275": "Data Structures GOOD",
    "07276": "Data Structures GOOD",
    "07277": "Data Structures GOOD",
    "07278": "Data Structures GOOD",
    "07279": "Data Structures GOOD",
    "07326": "Discrete Structures GOOD",
    "07327": "Discrete Structures GOOD",
    "07328": "Discrete Structures GOOD",
    "07329": "Discrete Structures GOOD",
    "07330": "Discrete Structures GOOD",
    "07331": "Discrete Structures GOOD",
    "07332": "Discrete Structures BAD",
    "07333": "Discrete Structures BAD",
    "07334": "Discrete Structures BAD",
    "19848": "Discrete Structures BAD",
    "19849": "Discrete Structures BAD",
    "19922": "Discrete Structures BAD",
    "07283": "Data 101 GOOD",
    "07284": "Data 101 GOOD",
    "07285": "Data 101 GOOD",
    "07286": "Data 101 GOOD",
    "07288": "Data 101 GOOD",
    "07289": "Data 101 GOOD",
    "07282": "Data 101 BAD",
    "07287": "Data 101 BAD",
    "07290": "Data 101 BAD",
    "07291": "Data 101 BAD",
    "07292": "Data 101 BAD",
    "07293": "Data 101 BAD",
    "09120": "Intro Lin Alg GOOD",
    "09124": "Intro Lin Alg GOOD",
    "05703": "Test Successful",
}

class CallSniper:
    def __init__(self, calls_per_seconds):
        self.REQUESTS_PER_SECOND = 1

        self.interval = 1000 / self.REQUESTS_PER_SECOND
        self.total_time = 0

        self.send_interval = 1

        self.last_update = 0
        self.update_interval = 3600
    
    def send_message(self, index):
        number = NUMBER
        message = f"{CLASS_NAME[index]}:{index} has opened up as a class!"
        provider = "Verizon"

        sender_credentials = (EMAIL, PASSWORD)

        send_sms_via_email(number, message, provider, sender_credentials)
    
    def check_last_send(self, index):
        with open("indexes.json", "r") as f:
            data = json.load(f)

        if index in data:
            current_time = time.time()
            if current_time - data[index] > 3600 * self.send_interval:
                data[index] = current_time
                with open("indexes.json", "w") as f:
                    f.write("")
                    json.dump(data, f)

                return True
            return False

        data[index] = time.time()

        with open("indexes.json", "w") as f:
            f.write("")
            json.dump(data, f)
        return True
    
    def check_update(self):
        if time.time() - self.last_update > self.update_interval:
            print("Update > Time")
            print(self.last_update)
            print(time.time())
            self.last_update = time.time()
            number = NUMBER
            message = f"Program is still up and running!"
            provider = "Verizon"

            sender_credentials = (EMAIL, PASSWORD)

            send_sms_via_email(number, message, provider, sender_credentials)

    def run(self):
        n = 1
        while True:
            restart = time.perf_counter() * self.interval - self.total_time
            if restart > self.interval:
                n = 1
                restart %= self.interval
                self.total_time += self.interval

            if n > 0:
                self.check_update()
                n -= 1
                try:
                    open_classes_request = requests.get("https://sis.rutgers.edu/soc/api/openSections.json?year=2023&term=9&campus=NB")
                    open_classes = set(open_classes_request.json())

                    with open("indexes.txt", "r") as f:
                        for line in f.readlines():
                            real_line = line[:5]
                            if real_line in open_classes:
                                if self.check_last_send(real_line):
                                    self.send_message(real_line)
                except Exception as e:
                    pass

def main():
    snipe = CallSniper(2)
    snipe.run()

if __name__ == '__main__':
    main()
