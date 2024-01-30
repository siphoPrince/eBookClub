CREATE DATABASE IF NOT EXISTS eBook_db;
CREATE USER IF NOT EXISTS 'ebook_user'@'localhost' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON eBook_db.* TO 'ebook_user'@'localhost';
GRANT SELECT ON performance_schema.* TO 'ebook_user'@'localhost';
