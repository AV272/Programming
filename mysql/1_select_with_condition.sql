SELECT *
FROM CITY
WHERE
    COUNTRYCODE = 'USA'
    AND POPULATION > 100000;


select distinct city from station where city regexp "^[aeiou].*"; # начинается с гласной

select distinct city from station where city regexp ".*[aeiou]$"; # заканчивается гласной

select distinct city from station where city regexp "^[aeiou].*[aeiou]$";

select distinct city from station where city regexp "^[^aeiou].*"; # не начинается на гласную

select distinct city from station where city regexp ".*[^aeiou]$";

select distinct city from station where city regexp "^[^aeiou].*|.*[^aeiou]$"; # не начинаются на гласную или не заканчиваются


select name from students where marks > 75 order by right(name,3), id; # сортировка по последним трем символам строки name.

select name from employee where salary > 2000 and months < 10 order by employee_id asc; # два условия через и.

# Условия
SELECT CASE             
            WHEN A + B > C AND B + C > A AND A + C > B THEN
                CASE 
                    WHEN A = B AND B = C THEN 'Equilateral'
                    WHEN A = B OR B = C OR A = C THEN 'Isosceles'
                    ELSE 'Scalene'
                END
            ELSE 'Not A Triangle'
        END
FROM TRIANGLES;

# После END стоит название столбца, в который записываются значения из условия 
SELECT
  ID,Name,Salary,

  CASE
    WHEN Salary>=3000 THEN 'ЗП >= 3000'
    WHEN Salary>=2000 THEN '2000 <= ЗП < 3000'
    ELSE 'ЗП < 2000'
  END SalaryTypeWithELSE,

  CASE
    WHEN Salary>=3000 THEN 'ЗП >= 3000'
    WHEN Salary>=2000 THEN '2000 <= ЗП < 3000'
  END SalaryTypeWithoutELSE

FROM Employees

SELECT
  ID,Name,Salary,DepartmentID,

  CASE
    WHEN DepartmentID=2 THEN '10%' -- 10% от ЗП выдать Бухгалтерам
    WHEN DepartmentID=3 THEN '15%' -- 15% от ЗП выдать ИТ-шникам
    ELSE '5%' -- всем остальным по 5%
  END NewYearBonusPercent,

  -- построим выражение с использованием CASE, чтобы увидеть сумму бонуса
  Salary/100*
  CASE
    WHEN DepartmentID=2 THEN 10 -- 10% от ЗП выдать Бухгалтерам
    WHEN DepartmentID=3 THEN 15 -- 15% от ЗП выдать ИТ-шникам
    ELSE 5 -- всем остальным по 5%
  END BonusAmount

FROM Employees

SELECT
  COUNT(*) [Общее кол-во сотрудников],
  COUNT(DISTINCT DepartmentID) [Число уникальных отделов],
  COUNT(DISTINCT PositionID) [Число уникальных должностей],
  COUNT(BonusPercent) [Кол-во сотрудников у которых указан % бонуса],
  MAX(BonusPercent) [Максимальный процент бонуса],
  MIN(BonusPercent) [Минимальный процент бонуса],
  SUM(Salary/100*BonusPercent) [Сумма всех бонусов],
  AVG(Salary/100*BonusPercent) [Средний размер бонуса],
  AVG(Salary) [Средний размер ЗП]
FROM Employees


# CONCAT - объединение выражений, SUBSTR - извлекает подстроку, LOWER - перевод в нижний регистр
select concat(name, '(', substr(occupation,1,1), ')')
from occupations
order by name asc;
select concat('There are a total of ', count(occupation), ' ' , lower(occupation), 's.')
from occupations
group by occupation
order by count(occupation) asc, occupation asc;


# сумма по столбцу
select sum(population) from city where district = 'California';

# среднее значение
select avg(population) from city where district = 'California';

# округление числа
select round(avg(population)) from city;

# max min
select max(population)-min(population) from city;

# Округление и замена символов
SELECT CEIL(AVG(Salary)-AVG(REPLACE(Salary,'0',''))) FROM EMPLOYEES;


# нахождение медианы
select round(s.lat_n, 4) 
from station as s 
where ( (select count(lat_n) from station where s.lat_n >= lat_n) - 
        (select count(lat_n)%2 from station) = 
        (select count(lat_n) from station where s.lat_n < lat_n) )

select city.name from city,country where city.countrycode = country.code and country.continent = "Africa";


# Группировка по континетнтам. Собираем все города для каждого из континентов.
select country.continent, floor(avg(city.population))
from city, country
where city.countrycode = country.code
group by country.continent;


# Сложное условие для двух таблиц
select
    case 
        when grades.grade >= 8 then students.name
        else NULL
    end, grades.grade, students.marks
from students, grades
where students.marks >= grades.min_mark and students.marks <= grades.max_mark
order by grades.grade desc, students.name;


# Объединение таблиц по некоторому столбцу. Группировка с условием.
select h.hacker_id, h.name
from submissions s
    inner join challenges c on s.challenge_id = c.challenge_id
    inner join difficulty d on c.difficulty_level = d.difficulty_level 
    inner join hackers h on s.hacker_id = h.hacker_id
where s.score = d.score and c.difficulty_level = d.difficulty_level
group by h.hacker_id, h.name having count(s.hacker_id) > 1
order by count(s.hacker_id) desc, s.hacker_id asc



SELECT CASE             
            WHEN P is NULL THEN CONCAT(N, ' Root')
            WHEN N in (select P from BST) THEN CONCAT(N, ' Inner')
            ELSE CONCAT(N, ' Leaf')
       END
FROM BST
ORDER BY N;


select c.company_code, c.founder, count(distinct em.lead_manager_code),
       count(distinct em.senior_manager_code), count(distinct em.manager_code), count(distinct employee_code)
from company as c
    inner join lead_manager as l on c.company_code = l.company_code
    inner join senior_manager as s on c.company_code = s.company_code
    inner join manager as m on c.company_code = m.company_code
    inner join employee as em on c.company_code = em.company_code    
group by c.company_code, c.founder
order by em.company_code;




select w.id, wp.age, w.coins_needed, w.power
from wands as w
    inner join wands_property as wp on w.code = wp.code
where wp.is_evil = 0 and w.coins_needed = 
    (select min(coins_needed) from wands as w2
     inner join wands_property as wp2 on w2.code = wp2.code
     where w2.power = w.power and wp2.age = wp.age)
order by w.power desc, wp.age desc;



# Задание переменных (set @variable=), создание новых столбцов функцией AS
set @r1=0, @r2=0, @r3=0, @r4=0;
select min(Doctor), min(Professor), min(Singer), min(Actor)
from(
  select case when Occupation='Doctor' then (@r1:=@r1+1)
              when Occupation='Professor' then (@r2:=@r2+1)
              when Occupation='Singer' then (@r3:=@r3+1)
              when Occupation='Actor' then (@r4:=@r4+1) 
         end as RowNumber,
    case when Occupation='Doctor' then Name end as Doctor,
    case when Occupation='Professor' then Name end as Professor,
    case when Occupation='Singer' then Name end as Singer,
    case when Occupation='Actor' then Name end as Actor
  from OCCUPATIONS
  order by Name
    ) temp
group by RowNumber;



# нАХОЖДЕНИЕ ПРОСТЫХ ЧИСЕЛ
SET @potential_prime = 1;
SET @divisor = 1;

SELECT GROUP_CONCAT(POTENTIAL_PRIME SEPARATOR '&') FROM
    (SELECT @potential_prime := @potential_prime + 1 AS POTENTIAL_PRIME FROM
    information_schema.tables t1,
    information_schema.tables t2
    LIMIT 1000) list_of_potential_primes
WHERE NOT EXISTS(
    SELECT * FROM
        (SELECT @divisor := @divisor + 1 AS DIVISOR FROM
        information_schema.tables t4,
        information_schema.tables t5
        LIMIT 1000) list_of_divisors
    WHERE POTENTIAL_PRIME%DIVISOR = 0 AND DIVISOR< POTENTIAL_PRIME);





