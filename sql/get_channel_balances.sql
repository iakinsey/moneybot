SELECT user_id, count(amount) as result
FROM ledger
WHERE channel_id = ?
GROUP BY user_id
ORDER BY result
