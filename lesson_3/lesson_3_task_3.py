from address import Address
from mailing import Mailing

first_address = Address("625415", "Екатеринбург", "Победы", "50", "105")
second_address = Address("102648", "Москва", "Ильича", "11А", "48")

dispatch = Mailing(first_address, second_address, 1000, "10202125")

print(f"Отправление {dispatch.track} из {dispatch.from_address.index}, {dispatch.from_address.city}, {dispatch.from_address.street}, {dispatch.from_address.house} - {dispatch.from_address.room} в {dispatch.to_address.index}, {dispatch.to_address.city}, {dispatch.to_address.street}, {dispatch.to_address.house} - {dispatch.to_address.room}. Стоимость {dispatch.cost} рублей.")