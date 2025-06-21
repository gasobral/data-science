select c.customer_city,
       c.customer_state,
       oi.price,
       oi.freight_value,
       p.product_category_name,
       op.payment_sequential,
       op.payment_type,
       op.payment_installments,
       op.payment_value
  from customers c
  inner join orders o on o.customer_id = c.customer_id
  inner join order_items oi on oi.order_id = o.order_id
  inner join products p on p.product_id = oi.product_id
  inner join order_payments op on op.order_id = o.order_id
  where o.order_status = 'delivered'
