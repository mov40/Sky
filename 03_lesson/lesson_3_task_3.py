from mailing import Mailing
from address import Address

from_addr = Address(index="123456", city="Москва",
                    street="Ленинградская", house="10", apartment="5")
to_addr = Address(index="654321", city="Санкт-Петербург",
                  street="Невская", house="20", apartment="15")

mailing = Mailing(to_address=to_addr, from_address=from_addr,
                  cost=500, track="TRACK123456789")

print(f"Отправление {mailing.track} из {mailing.from_address.index}, "
      f"{mailing.from_address.city}, {mailing.from_address.street}, "
      f"{mailing.from_address.house}-{mailing.from_address.apartment} в "
      f"{mailing.to_address.index}, {mailing.to_address.city}, "
      f"{mailing.to_address.street}, {mailing.to_address.house}-"
      f"{mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")
