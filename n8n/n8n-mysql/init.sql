-- MySQL 8.0 syntax - GRANT and ALTER USER are separate
GRANT ALL PRIVILEGES ON n8ndb.* TO 'n8nuser'@'%';
ALTER USER 'n8nuser'@'%' IDENTIFIED BY 'mma123';
FLUSH PRIVILEGES;

CREATE TABLE IF NOT EXISTS n8ndb.goods (
  id INT AUTO_INCREMENT PRIMARY KEY,
  item_name VARCHAR(255) NOT NULL,
  current_quantity INT DEFAULT 0,
  inventory_threshold INT DEFAULT 5
);