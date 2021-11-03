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

INSERT INTO Account (account_number, username, account_type, currency, balance) VALUES ('002566978374', 'abc123', 'Saving', 'HKD', '30567.50');
INSERT INTO Account (account_number, username, account_type, currency, balance) VALUES ('003566978374', 'abc123', 'Current', 'HKD', '794.77');
INSERT INTO Account (account_number, username, account_type, currency, balance) VALUES ('102490957993', 'abc123', 'Saving', 'CNY', '455.23');
INSERT INTO Account (account_number, username, account_type, currency, balance) VALUES ('002566978375', 'hello', 'Saving', 'HKD', '9504.20');
INSERT INTO Account (account_number, username, account_type, currency, balance) VALUES ('002566978376', 'hello', 'Saving', 'HKD', '45697.23');
INSERT INTO Account (account_number, username, account_type, currency, balance) VALUES ('003566978375', 'bruhman', 'Current', 'USD', '47583.78');

INSERT INTO Transaction (transaction_id, amount, date_time, from_account, to_account) VALUES ('289304X90128Yxi', '5000.00', '2020-12-01 08:16:34', '002566978374', '002566978375');
INSERT INTO Transaction (transaction_id, amount, date_time, from_account, to_account) VALUES ('289304X9jio8Yxi', '2000.74', '2021-01-14 11:16:34', '002566978375', '002566978374');
INSERT INTO Transaction (transaction_id, amount, date_time, from_account, to_account) VALUES ('289kopk90128Yxi', '1000.00', '2021-02-16 22:16:34', '002566978375', '002566978376');
INSERT INTO Transaction (transaction_id, amount, date_time, from_account, to_account) VALUES ('289kook90128Yxi', '1000.00', '2021-02-16 22:17:34', '002566978376', '002566978375');