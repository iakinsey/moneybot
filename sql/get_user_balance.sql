SELECT sum(amount)
FROM ledger
WHERE server_id = ?
AND user_id = ?
