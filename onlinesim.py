from onlinesimru import FreeNumbersService, RentNumbersService, ProxyService, UserService, NumbersService


class online_sim():
    api_key = 'W9246j7k9QnEF4q-3CV9Y8aU-9VFjKKgp-8bGZbJ3D-Y3Zzbw2HjGvY7wu'
    numbers = NumbersService(api_key)

    def get_id(self, numbers, service, country):
        number = numbers.get(service=service, country=country)
        return number

    def get_sms(self, number):
        sms = number.state()
        print(sms)
        return sms



