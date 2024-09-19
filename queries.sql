-- Time delivering order
SELECT 
    a.order_id,
    TIMESTAMPDIFF(MINUTE, a.time, b.time) AS minutes_to_delivery
FROM delivery.courier_actions a
JOIN delivery.courier_actions b ON a.order_id = b.order_id
WHERE 
    a.action = 'accept_order' AND 
    b.action = 'deliver_order';
    
-- Average time delivering order
SELECT 
    AVG(TIMESTAMPDIFF(MINUTE, a.time, b.time)) AS avg_minutes_to_delivery
FROM delivery.courier_actions a
JOIN celivery.courier_actions b ON a.order_id = b.order_id
WHERE 
    a.action = 'accept_order' AND 
    b.action = 'deliver_order';

-- Cancel rate
SELECT 
       (SUM(CASE WHEN action = 'cancel_order' THEN 1 ELSE 0 END) / COUNT(distinct(order_id))) * 100 AS cancel_rate
FROM delivery.user_actions;

-- Time to cancel the order
SELECT 
	a.order_id,
    (TIMESTAMPDIFF(MINUTE, a.time, b.time)) AS minute_to_cancel
FROM delivery.user_actions a
JOIN delivery.user_actions b ON a.order_id = b.order_id
WHERE 
    a.action = 'create_order' AND 
    b.action = 'cancel_order';

-- Average time to cancel the order
SELECT 
    AVG(TIMESTAMPDIFF(MINUTE, a.time, b.time)) AS avg_minute_to_cancel
FROM delivery.user_actions a
JOIN delivery.user_actions b ON a.order_id = b.order_id
WHERE 
    a.action = 'create_order' AND 
    b.action = 'cancel_order';
    
-- Total orders by age and genre
SELECT u.sex, 
       TIMESTAMPDIFF(YEAR, u.birth_date, ua.time) AS age, 
       COUNT(distinct(ua.order_id)) AS num_orders
FROM delivery.users u
JOIN delivery.user_actions ua ON u.user_id = ua.user_id
GROUP BY u.sex, age;

-- Number of delivery by age and genre
SELECT c.sex, 
       TIMESTAMPDIFF(YEAR, c.birth_date, ca.time) AS age, 
       COUNT(distinct(ca.order_id)) AS num_orders
FROM delivery.couriers c
JOIN delivery.courier_actions ca ON c.courier_id = ca.courier_id
GROUP BY c.sex, age;


-- Avg delivery time by age and sex
SELECT c.sex, 
       TIMESTAMPDIFF(YEAR, c.birth_date, ca.time) AS age, 
       COUNT(distinct(ca.order_id)) AS num_orders,
       AVG(TIMESTAMPDIFF(MINUTE, ca.time, b.time)) AS avg_minutes_to_delivery
FROM delivery.couriers c
JOIN delivery.courier_actions ca ON c.courier_id = ca.courier_id
JOIN delivery.courier_actions b ON ca.order_id = b.order_id
WHERE 
    ca.action = 'accept_order' AND 
    b.action = 'deliver_order'
GROUP BY c.sex, age;

-- Total user vs total couriers
SELECT 
  (SELECT COUNT(*) FROM users) AS total_users,
  (SELECT COUNT(*) FROM couriers) AS total_couriers;

-- Total orders by hour
SELECT HOUR(creation_time) AS hour_of_day, COUNT(distinct(order_id)) AS total_orders
FROM delivery.orders
GROUP BY hour_of_day;

-- Total rders by day of the week
SELECT 
	DAYOFWEEK(creation_time) AS number_of_week,
    DATE_FORMAT(creation_time, '%W') AS day_of_week,
    COUNT(order_id) AS total_orders
FROM delivery.orders
GROUP BY 
    number_of_week, day_of_week
ORDER BY 
	number_of_week;

-- Total orders by day of the week and hour
SELECT 
    DAYOFWEEK(creation_time) AS number_of_week,
    DATE_FORMAT(creation_time, '%W') AS day_of_week,
    HOUR(creation_time) AS hour_of_day,
    COUNT(order_id) AS total_orders
FROM delivery.orders
GROUP BY 
    number_of_week, day_of_week, hour_of_day
ORDER BY 
    number_of_week, hour_of_day;

