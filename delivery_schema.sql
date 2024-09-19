CREATE DATABASE IF NOT EXISTS delivery;
USE delivery ;

CREATE TABLE IF NOT EXISTS delivery.users (
  `user_id` INT NOT NULL,
  `birth_date` DATE,
  `sex` VARCHAR(50),
  PRIMARY KEY (`user_id`)
);

CREATE TABLE IF NOT EXISTS delivery.orders (
  `order_id` INT NOT NULL,
  `creation_time` TIMESTAMP,
  `product_id` VARCHAR(50),
  PRIMARY KEY (`order_id`)
);

CREATE TABLE IF NOT EXISTS delivery.user_actions (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `order_id` INT NOT NULL,
  `action` VARCHAR(50),
  `time` TIMESTAMP,
  PRIMARY KEY (`id`),
  CONSTRAINT `user_id`
    FOREIGN KEY (`user_id`)
    REFERENCES delivery.`users` (`user_id`),
  CONSTRAINT `oder_id`
    FOREIGN KEY (`order_id`)
    REFERENCES delivery.`orders` (`order_id`)
);

CREATE TABLE IF NOT EXISTS delivery.couriers (
  `courier_id` INT NOT NULL,
  `birth_date` DATE,
  `sex` VARCHAR(50),
  PRIMARY KEY (`courier_id`)
);

CREATE TABLE IF NOT EXISTS delivery.courier_actions (
  `id` INT NOT NULL AUTO_INCREMENT,
  `courier_id` INT NOT NULL,
  `order_id` INT NOT NULL,
  `action` VARCHAR(50),
  `time` TIMESTAMP,
  PRIMARY KEY (`id`),
  CONSTRAINT `courier_id`
    FOREIGN KEY (`courier_id`)
    REFERENCES delivery.`couriers` (`courier_id`),
  CONSTRAINT `order_id`
    FOREIGN KEY (`order_id`)
    REFERENCES delivery.`orders` (`order_id`)
);