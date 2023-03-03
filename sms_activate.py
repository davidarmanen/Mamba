from smsactivate.api import SMSActivateAPI

API_KEY = "AceA53bffAA65Abf58fbc5f0f5f49bA0"
sa = SMSActivateAPI(API_KEY)
sa.debug_mode = True




def get_sms(var1, var2, var3, country1, country2, country3, contry_code1, contry_code2, contry_code3):
    number = sa.getNumberV2(service="fd", country=country1)
    var = contry_code1
    try:
        phone_number = number["phoneNumber"]
        id = number["activationId"]
        phone_number = phone_number[var:]
        country = var1
        return country, phone_number, id
    except:
        number = sa.getNumberV2(service="fd", country=country2)
        var = contry_code2
        try:
            phone_number = number["phoneNumber"]
            id = number["activationId"]
            phone_number = phone_number[var:]
            country = var2
            return country, phone_number, id
        except:
            number = sa.getNumberV2(service="fd", country=country3)
            var = contry_code3
            try:
                phone_number = number["phoneNumber"]
                id = number["activationId"]
                phone_number = phone_number[var:]
                country = var3
                return country, phone_number, id
            except:
                get_sms(var1, var2, var3, country1, country2, country3, contry_code1, contry_code2, contry_code3)



def get_code(id):
    status = sa.getStatus(id)
    code = sa.activationStatus(status)
    return code


#print(get_code(id))
