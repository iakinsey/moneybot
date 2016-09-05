SELECT count(amount)
FROM ledger
GROUP BY channel_id
