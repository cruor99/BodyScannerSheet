CREATE DATABASE IF NOT EXISTS InnerBodyScanDB;

USE InnerBodyScanDB;

CREATE TABLE IF NOT EXISTS Users (
	user_id MEDIUMINT NOT NULL AUTO_INCREMENT,
	user_email TEXT NOT NULL,
	user_name TEXT NOT NULL,
	user_start_date DATE NOT NULL,
	user_sex VARCHAR(5), -- (MAN OR WOMAN)
	user_age int,
	user_height int, -- centimeters

	PRIMARY KEY (user_id)
	);

CREATE TABLE IF NOT EXISTS Friend_list (
	user_id MEDIUMINT NOT NULL PRIMARY KEY,
	friend_id MEDIUMINT NOT NULL,
	friend_status VARCHAR(6), -- (coach/friend)

	FOREIGN KEY (user_id) REFERENCES Users(user_id),
	FOREIGN KEY (friend_id) REFERENCES Users(user_id)
	);

CREATE TABLE IF NOT EXISTS Scan (
	scan_id MEDIUMINT AUTO_INCREMENT PRIMARY KEY,
	user_id MEDIUMINT NOT NULL,
	author_id MEDIUMINT NOT NULL,
	scan_date DATE NOT NULL,
	user_comment TEXT,
	coach_comment TEXT,
	weight DOUBLE, -- kg
	BMI DOUBLE,
	fat_percentage DOUBLE,
	metabolism INT,
	metabolic_age INT,
	water_percentage DOUBLE,
	visceral_fat DOUBLE,
	bone_mass DOUBLE,
	muscle_mass DOUBLE,
	physical_score DOUBLE,

	FOREIGN KEY (user_id) REFERENCES Users(user_id),
	FOREIGN KEY (author_id) REFERENCES Users(user_id)
	);
