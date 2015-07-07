
-- -----------------------------------------------------------
-- Entities and relationships: The main elements
-- -----------------------------------------------------------

CREATE TABLE IF NOT EXISTS osoba_entities (
    id                      INT AUTO_INCREMENT,
    type                    CHAR(20),

    PRIMARY KEY (id),
    INDEX (type)
);

CREATE TABLE IF NOT EXISTS osoba_relationships (
    id                      INT AUTO_INCREMENT,
    _from                   INT,
    to                      INT,
    type                    CHAR(20),
    PRIMARY KEY (id),
    INDEX (from),
    INDEX (to),
    INDEX (type)
);

-- -----------------------------------------------------------
-- Sources: Database and file sources for entities
-- -----------------------------------------------------------

CREATE TABLE IF NOT EXISTS osoba_sources (
    id                      INT AUTO_INCREMENT,
    entity                  INT NULL,
    relationship            INT NULL,
    source_table            VARCHAR(100),
    source_field            VARCHAR(100),
    source_value            VARCHAR(100),
);

CREATE TABLE IF NOT EXISTS osoba_files (
    id                      INT AUTO_INCREMENT,
    entity                  INT NULL,
    relationship            INT NULL,
    podaci_url              VARCHAR(255) NOT NULL
);

-- -----------------------------------------------------------
-- Nodes: Detail classes for entities
-- -----------------------------------------------------------

CREATE TABLE IF NOT EXISTS osoba_node_person (
    id                      INT,
    nationality             CHAR(2),
    first_name              VARCHAR(40),
    middle_names            VARCHAR(120),
    last_name               VARCHAR(60),
);

CREATE TABLE IF NOT EXISTS osoba_node_company (
    id                      INT,
    name                    VARCHAR(120),
    country                 CHAR(2),
    incorporated_date       DATE,
    dissolved_date          DATE
);


-- -----------------------------------------------------------
-- Edges: Connections between nodes
-- -----------------------------------------------------------

CREATE TABLE IF NOT EXISTS osoba_edge_owns (
    id                      INT,
    share_percent           DOUBLE,
    started                 DATE,
    ended                   DATE
);

CREATE TABLE IF NOT EXISTS osoba_edge_is_director (
    id                      INT,
    started                 DATE,
    ended                   DATE,
    details                 VARCHAR(30)
);
