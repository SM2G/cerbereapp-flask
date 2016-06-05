CREATE TABLE users(
  user_id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(50),
  password VARCHAR(50) NOT NULL,
  email VARCHAR(100) NOT NULL,
  account_type INTEGER NOT NULL,
  registered_on DATE
);

CREATE TABLE account_types(
  account_type_id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
  account_type_name VARCHAR(50) NOT NULL,
  emp_limit INTEGER NOT NULL,
  adv_features INTEGER NOT NULL
);

CREATE TABLE employees(
  employee_id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
  user_id INTEGER NOT NULL,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  profile_id INTEGER NOT NULL
);

CREATE TABLE profiles(
  profile_id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
  user_id INTEGER NOT NULL,
  profile_name VARCHAR(50) NOT NULL
);

CREATE TABLE document_models(
  document_model_id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
  user_id INTEGER NOT NULL,
  document_model_name VARCHAR(50) NOT NULL,
  warning_days INTEGER NOT NULL,
  critical_days INTEGER NOT NULL
);

CREATE TABLE documents(
  document_id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
  employee_id INTEGER NOT NULL,
  expiration_date NOT NULL,
  document_scan BLOB
);
