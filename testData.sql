INSERT INTO Customer (username, password, first_name, middle_name, last_name, custom_message) VALUES ('abc123', 'great9384', 'John', 'Fisher', 'Smith', 'Yo');
INSERT INTO Customer (username, password, first_name, last_name, custom_message) VALUES ('hello', 'Qwerty', 'James', 'Clinton', 'Nice');
INSERT INTO Customer (username, password, first_name, last_name) VALUES ('niceguys', 'Xtxt434312', 'Elizabeth', 'Crown');
INSERT INTO Customer (username, password, first_name, custom_message) VALUES ('bruhman', 'PpAaPepe', 'Andrew', 'This is a bank');

INSERT INTO LoginHistory (username, date_time) VALUES ('abc123', '2020-11-11 12:54:34');
INSERT INTO LoginHistory (username, date_time) VALUES ('niceguys', '2020-12-11 05:46:15');
INSERT INTO LoginHistory (username, date_time) VALUES ('abc123', '2021-01-01 08:12:45');
INSERT INTO LoginHistory (username, date_time) VALUES ('hello', '2021-01-11 08:46:15');
INSERT INTO LoginHistory (username, date_time) VALUES ('hello', '2021-01-11 08:46:59');
INSERT INTO LoginHistory (username, date_time) VALUES ('bruhman', '2021-02-10 05:12:32');
INSERT INTO LoginHistory (username, date_time) VALUES ('abc123', '2021-04-16 17:00:44');

INSERT INTO Branch (branch_id, branch_name, branch_location, contact_number) VALUES ('001', 'HKU', 'The University of Hong Kong, Hong Kong', '45672345');
INSERT INTO Branch (branch_id, branch_name, branch_location, contact_number) VALUES ('102', 'Central Plaza', '1/F Central Plaza, Wan Chai, Hong Kong', '98347893');

INSERT INTO Account (account_number, username, branch_id, balance, open_date) VALUES ('0025669783748493', 'abc123', '001', '30567.50', '2012-10-15');
INSERT INTO Account (account_number, username, branch_id, balance, open_date) VALUES ('0035669783747777', 'abc123', '001', '30567.50', '2012-10-15');
INSERT INTO Account (account_number, username, branch_id, balance, open_date) VALUES ('1024909579936666', 'abc123', '102', '30567.50', '2012-10-15');
INSERT INTO Account (account_number, username, branch_id, balance, open_date) VALUES ('0025669783755555', 'hello', '102', '30567.50', '2012-10-15');
INSERT INTO Account (account_number, username, branch_id, balance, open_date) VALUES ('0025669783764444', 'hello', '001', '30567.50', '2012-10-15');
INSERT INTO Account (account_number, username, branch_id, balance, open_date) VALUES ('0045669783753333', 'bruhman', '001', '30567.50', '2012-10-15');

INSERT INTO BankAccount (account_number, account_type) VALUES ('0025669783748493', 'Current');
INSERT INTO BankAccount (account_number, account_type) VALUES ('0035669783747777', 'USD');
INSERT INTO BankAccount (account_number, account_type) VALUES ('0025669783755555', 'Saving');
INSERT INTO BankAccount (account_number, account_type) VALUES ('0025669783764444', 'Current');
INSERT INTO BankAccount (account_number, account_type) VALUES ('0045669783753333', 'CNY');

INSERT INTO CreditCard (account_number, card_name, credit_limit, expiry_month, expiry_year) VALUES ('1024909579936666', 'Premium Mile', '10000.00', '09', '24');

INSERT INTO Transaction (transaction_id, amount, currency, date_time, from_account, to_account) VALUES ('289304X90128Yxi', '5000.00', 'HKD','2020-12-01 08:16:34', '0025669783748493', '0025669783755555');
INSERT INTO Transaction (transaction_id, amount, currency, date_time, from_account, to_account) VALUES ('289304X9jio8Yxi', '2000.74', 'HKD','2021-01-14 11:16:34', '0025669783764444', '1024909579936666');