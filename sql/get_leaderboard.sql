SELECT count(amount)
FROM ledger
GROUP BY server_id
