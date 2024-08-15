CREATE TABLE `players` (
  id int(11) NOT NULL AUTO_INCREMENT,
  player_name varchar(255) DEFAULT NULL,
  realm varchar(255) DEFAULT NULL,
  class varchar(255) DEFAULT NULL,
  item_level int(11) DEFAULT NULL,
  level int(11) DEFAULT NULL,
  faction varchar(255) DEFAULT NULL,
  role varchar(255) DEFAULT NULL,
  specialisation varchar(255) DEFAULT NULL,
  race varchar(255) DEFAULT NULL,
  creation_datetime datetime DEFAULT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE items (
    item_id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    item_class VARCHAR(255),
    item_subclass VARCHAR(255),
    level INT,
    quality VARCHAR(50),
    quantity INT,
    modified_appearance_id INT,
    transmog_id INT,
    creation_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE item_stats (
    item_id INT,
    stat_type VARCHAR(255),
    value INT,
    FOREIGN KEY (item_id) REFERENCES items(item_id)
);

CREATE TABLE item_enchantments (
    item_id INT,
    enchantment_display_string TEXT,
    enchantment_source_item_id INT,
    FOREIGN KEY (item_id) REFERENCES items(item_id)
);

CREATE TABLE item_sockets (
    item_id INT,
    socket_type VARCHAR(255),
    socket_item_id INT,
    FOREIGN KEY (item_id) REFERENCES items(item_id)
);

CREATE TABLE item_sets (
    item_id INT,
    set_name VARCHAR(255),
    set_effects TEXT,
    FOREIGN KEY (item_id) REFERENCES items(item_id)
);

CREATE TABLE player_items (
    player_id INT,
    item_id INT,
    equipped BOOLEAN,
    FOREIGN KEY (player_id) REFERENCES players(player_id),
    FOREIGN KEY (item_id) REFERENCES items(item_id)
);

