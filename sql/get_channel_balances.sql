SELECT user_id, count(amount) as result
FROM ledger
WHERE server_id = ?
GROUP BY user_id
ORDER BY result
