select track,
case
when o.finished = true then 2
when o.cancelled = true then -1
when o."inDelivery" = true then 1
else 0
end status
from "Orders" o;