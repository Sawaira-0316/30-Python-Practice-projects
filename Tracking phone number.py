import phonenumbers
from phonenumbers import timezone, geocoder, carrier

number = input("Enter your No. with +-- ")
phone = phonenumbers.parse(number)
time_zones = timezone.time_zones_for_number(phone)
car = carrier.name_for_number(phone, "en")
reg = geocoder.description_for_number(phone, "en")

print("Country Code:", phone.country_code)
print("National Number:", phone.national_number)

if time_zones:
    print("Time Zones:", time_zones)
else:
    print("Time Zone: Unknown")

print("Carrier:", car)
print("Region:", reg)
