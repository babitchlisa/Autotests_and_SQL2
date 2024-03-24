# Задание 1

Создала 2 заказа:
```
curl --location 'https://db4f7883-7576-4399-95e1-9984ad9a98ac.serverhub.praktikum-services.ru/api/v1/orders' \
--header 'Content-Type: application/json' \
--data '{
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": [
        "BLACK"
    ]
}'
```
```commandline
curl --location 'https://db4f7883-7576-4399-95e1-9984ad9a98ac.serverhub.praktikum-services.ru/api/v1/orders' \
--header 'Content-Type: application/json' \
--data '{
    "firstName": "Saske",
    "lastName": "Uzumaki",
    "address": "Konoha, 142 apt.",
    "metroStation": 2,
    "phone": "+7 800 355 35 55",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": [
        "WHITE"
    ]
}'
```
создала 2 курьера
````
curl --location 'https://db4f7883-7576-4399-95e1-9984ad9a98ac.serverhub.praktikum-services.ru/api/v1/courier' \
--header 'Content-Type: application/json' \
--data '{
    "login": "shinobi",
    "password": "1234",
    "firstName": "naruto"
}'
````
````
curl --location 'https://db4f7883-7576-4399-95e1-9984ad9a98ac.serverhub.praktikum-services.ru/api/v1/courier' \
--header 'Content-Type: application/json' \
--data '{
    "login": "ninja",
    "password": "1234",
    "firstName": "saske"
}'
````
приняла заказы
````
curl --location --request PUT 'https://db4f7883-7576-4399-95e1-9984ad9a98ac.serverhub.praktikum-services.ru/api/v1/orders/accept/5?courierId=3'
curl --location --request PUT 'https://db4f7883-7576-4399-95e1-9984ad9a98ac.serverhub.praktikum-services.ru/api/v1/orders/accept/6?courierId=4'
````
запрос на проверку
````
select c.login, COUNT(o."courierId") 
from "Couriers" c 
left join "Orders" as o 
on c.id = o."courierId" 
where o."inDelivery" = true 
group by c.login;
````

p.s Определила, что при привязке курьера к заказу создается дубль заказа

# Задание 2
запрос на проверку статусов
````
select track,
case
when o.finished = true then 2
when o.cancelled = true then -1
when o."inDelivery" = true then 1
else 0
end status
from "Orders" o;
````
