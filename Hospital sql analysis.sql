CREATE DATABASE hospital_db;
USE hospital_db;
CREATE TABLE patient_records (
    patient_id INT,
    patient_name VARCHAR(100),
    age INT,
    gender VARCHAR(10),
    diagnosis VARCHAR(100),
    department VARCHAR(50),
    doctor_name VARCHAR(100),
    admission_date DATE,
    discharge_date DATE,
    treatment_cost DECIMAL(10,2),
    payment_mode VARCHAR(20),
    city VARCHAR(50)
);
SELECT * FROM hospital_data_cleaned;
SELECT COUNT(*) FROM hospital_data_cleaned;

/*(total patient count)*/

SELECT COUNT(*) AS total_patients  
FROM hospital_data_cleaned;

/*Gender wise patient count Distribution*/

SELECT gender, COUNT(*) AS patient_count
FROM hospital_data_cleaned
GROUP BY gender;

/* Condition wise patient count */

SELECT `condition`, COUNT(*) AS total_patients
FROM hospital_data_cleaned
GROUP BY `condition`
ORDER BY total_patients DESC;

/* Procedure-wise Patient Count */

SELECT `procedure`, COUNT(*) AS total_patients
FROM hospital_data_cleaned
GROUP BY `procedure`
ORDER BY total_patients DESC;

/* City-wise Patients */

SELECT city, COUNT(*) AS total_patients
FROM hospital_data_cleaned
GROUP BY city
ORDER BY total_patients DESC;

/* Average Treatment Cost */

SELECT ROUND(AVG(cost), 2) AS avg_treatment_cost
FROM hospital_data_cleaned;

/* Condition-wise Average Cost*/

SELECT `condition`,
       ROUND(AVG(cost), 2) AS avg_cost
FROM hospital_data_cleaned
GROUP BY `condition`
ORDER BY avg_cost DESC;

/*Length of Stay Analysis*/

SELECT
  ROUND(AVG(length_of_stay), 2) AS avg_stay,
  MIN(length_of_stay) AS min_stay,
  MAX(length_of_stay) AS max_stay
FROM hospital_data_cleaned;

/*Readmission Analysis*/

SELECT readmission, COUNT(*) AS patient_count
FROM hospital_data_cleaned
GROUP BY readmission;

/* Outcome-wise Analysis */

SELECT outcome, COUNT(*) AS patient_count
FROM hospital_data_cleaned
GROUP BY outcome;

/*Satisfaction Level Distribution*/

SELECT satisfaction_label, COUNT(*) AS patient_count
FROM hospital_data_cleaned
GROUP BY satisfaction_label;

/*Doctor-wise Patient Load*/

SELECT doctor_name, COUNT(*) AS total_patients
FROM hospital_data_cleaned
GROUP BY doctor_name
ORDER BY total_patients DESC;

/* Payment Mode Analysis */

SELECT payment_mode, COUNT(*) AS total_patients
FROM hospital_data_cleaned
GROUP BY payment_mode;
/*Total cost wise payment mode*/
SELECT 
    payment_mode, 
    COUNT(*) AS total_patients, 
    SUM(cost) AS total_cost
FROM hospital_data_cleaned
GROUP BY payment_mode
ORDER BY total_cost DESC;
