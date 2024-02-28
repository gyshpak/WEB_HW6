-- Table: students
DROP TABLE IF EXISTS students;
CREATE TABLE students (
    id_st INTEGER PRIMARY KEY AUTOINCREMENT,
    name_st VARCHAR(255) UNIQUE NOT NULL
);

-- Table: groups
DROP TABLE IF EXISTS groups;
CREATE TABLE groups (
    id_gr INTEGER PRIMARY KEY AUTOINCREMENT,
    number_gr INTEGER NOT NULL,
    fr_st INTEGER,
    FOREIGN KEY (fr_st) REFERENCES students (id_st)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

-- Table: teachers
DROP TABLE IF EXISTS teachers;
CREATE TABLE teachers (
    id_tc INTEGER PRIMARY KEY AUTOINCREMENT,
    name_tc VARCHAR(255) UNIQUE NOT NULL
);

-- Table: subjects
DROP TABLE IF EXISTS subjects;
CREATE TABLE subjects (
    id_sb INTEGER PRIMARY KEY AUTOINCREMENT,
    name_sb INTEGER NOT NULL,
    fr_tc INTEGER,
    FOREIGN KEY (fr_tc) REFERENCES teachers (id_tc)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);
-- Table: assessment_subj
DROP TABLE IF EXISTS assessment_subj;
CREATE TABLE assessment_subj (
    id_as INTEGER PRIMARY KEY AUTOINCREMENT,
    fr_st INTEGER NOT NULL,
    fr_sb INTEGER NOT NULL,
    assessment INTEGER NOT NULL,
    date_in DATE NOT NULL,
    FOREIGN KEY (fr_st) REFERENCES students (id_st)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
    FOREIGN KEY (fr_sb) REFERENCES subjects (id_sb)
);