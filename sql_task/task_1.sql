select c.login, COUNT(o.id)
from "Couriers" c
left join "Orders" as o
on c.id = o."courierId" and o."inDelivery" = true
group by c.login;

# left join целесообразен потому что в условии говорится что нужно выбрать все логины курьеров, являющиеся в данном запросе левой таблицей
