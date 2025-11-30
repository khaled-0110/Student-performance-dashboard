{{ config(materialized='table') }}

SELECT
    student_id,
    name,
    subject,
    score,
    date,
    CASE
        WHEN attendance IS NULL OR TRIM(attendance) = '' THEN 'Absent'
        ELSE attendance
    END AS attendance
FROM {{ ref('raw_students') }}
WHERE
    student_id IS NOT NULL AND TRIM(CAST(student_id AS VARCHAR)) != ''
    AND name IS NOT NULL AND TRIM(name) != ''
    AND subject IS NOT NULL AND TRIM(subject) != ''
    AND score IS NOT NULL AND TRIM(CAST(COALESCE(score, '') AS VARCHAR)) != ''
    AND date IS NOT NULL