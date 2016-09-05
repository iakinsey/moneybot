SELECT sum(amount)
FROM ledger
WHERE channel_id = ?
AND user_id = ?
