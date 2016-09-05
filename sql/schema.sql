CREATE TABLE ledger (
    user_id BIGINT NOT NULL,
    server_id BIGINT NOT NULL,
    amount INT NOT NULL
);

CREATE INDEX ledger_user_id_idx ON ledger(user_id);
CREATE INDEX ledger_server_id_idx ON ledger(server_id);
CREATE INDEX ledger_amount_idx ON ledger(amount);
