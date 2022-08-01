import phonenumbers

from phonenumbers import geocoder

phone = input('Digite o telefone no formado +551140028993322')

phone_number = phonenumbers.parse(phone)

print(geocoder.description_for_number(phone_number, 'pt'))
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
