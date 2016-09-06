SELECT user_id, sum(amount) as result
FROM ledger
WHERE server_id = ?
GROUP BY user_id
ORDER BY result DESC
