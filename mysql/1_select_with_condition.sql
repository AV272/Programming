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


