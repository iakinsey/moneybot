SELECT count(amount)
FROM ledger
WHERE channel_id = ?
GROUP BY user_id
