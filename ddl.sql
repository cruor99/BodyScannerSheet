CREATE DATABASE InnerBobyScanDB;

CREATE TABLE users (
	user_email TEXT NOT NULL PRIMARY KEY,
	user_name TEXT NOT NULL,
	start_date DATE NOT NULL,
	sex VARCHAR(5), -- (MAN OR WOMAN)
	age int,
	hight int -- centimeters
	);

CREATE TABLE user_settings (
	user_email TEXT PRIMARY KEY FOREIGN KEY REFERENCES users(user_email),
	friend_limited VARCHAR(20) -- (NO SCANES, LAST SCAN, LAST MONTH, ALL SCANES)
	friend VARCHAR(20) -- (NO SCANES, LAST SCAN, LAST MONTH, ALL SCANES)
	friend_trusted VARCHAR(20) -- (NO SCANES, LAST SCAN, LAST MONTH, ALL SCANES)
	coach VARCHAR(20) -- (NO SCANES, LAST SCAN, LAST MONTH, ALL SCANES)
	);

CREATE TABLE friend_list (
	user_email TEXT PRIMARY KEY FOREIGN KEY REFERENCES users(user_email),
	user_email_friend TEXT NOT NULL FOREIGN KEY users(user_email),
	friend_status VARCHAR(20) --(friend_limited, friend, friend_trusted, coach)
	);

CREATE TABLE scan (
	scan_ID INTEGER PRIMARY KEY,
	user_email TEXT NOT NULL FOREIGN KEY REFERENCES users(user_email),
	user_email_writer TEXT NOT NULL FOREIGN KEY REFERENCES users(user_email),
	scan_time TEXT NOT NULL,
	comment_user TEXT,
	comment_coach TEXT,
	weight DOUBLE,
	BMI DOUBLE,
	fat_procentage DOUBLE,
	metabolisme INT,
	metabolic_age INT,
	water_procentage DOUBLE,
	visceral_fat DOUBLE,
	bone_mass DOUBLE,
	muscle_mass DOUBLE,
	physical_score DOUBLE
	);
