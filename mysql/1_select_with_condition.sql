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





