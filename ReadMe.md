# Achievement First Coding Challenge
### Part 1 - SQL
** Please note syntax is for PostgreSQL and assumes a db table titled 'student_tests'. Column names are also reformatted to snake_case

1. ```SELECT quiz, score FROM (
    SELECT quiz, score, row_number() OVER (ORDER BY score) AS rn FROM student_tests
    WHERE name='Ana') AS a
    WHERE rn=2;

2. ```WITH temp_table AS (
    SELECT name, administration_date, score, dense_rank()
    OVER (PARTITION BY name ORDER BY administration_date DESC) AS rn
    FROM student_tests)
    SELECT a.name, a.administration_date AS administration_date_most_recent, a.score AS most_recent_score,
    b.administration_date_prior_attempt, b.prior_score
    FROM temp_table a
    INNER JOIN (
    SELECT name, administration_date AS administration_prior_attempt, score AS prior_score
    FROM temp_table
    WHERE rn=2) AS b
    ON b.name = a.name
    WHERE a.rn=1;

### Part 2 - GitHub API with Python
1. Clone down this repo, open your command line tool and cd into the directory
2. If you're using a mac simply type ```python fetch.py``` while with windows ```winpty python.exe fetch.py``` will be necessary
3. All of my public repos will print as a list to the console
