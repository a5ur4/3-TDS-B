use sakila;

# primeira questao

select st.staff_id, st.first_name, py.payment_id, py.amount
from staff st 
right join payment py
on st.staff_id = py.staff_id
where py.amount = null;


# segunda questao

select st.first_name, st.picture, st.store_id, iv.inventory_id, f.title
from inventory iv

left join staff st
on iv.inventory_id = st.staff_id

left join film f
on iv.inventory_id = st.staff_id

where st.first_name = "Mike";

