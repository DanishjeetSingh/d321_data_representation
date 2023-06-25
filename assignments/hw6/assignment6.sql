CREATE TABLE Student(sid integer,
                     sname text,
                     homeCity text,
                     primary key (sid));
					 
CREATE TABLE Department(deptName text,
                        mainOffice text,
                        primary key (deptName));

CREATE TABLE Major(major text,
                   primary key (major));


CREATE TABLE employedBy(sid integer,
                        deptName text,
                        salary integer,
                        primary key (sid),
                        foreign key (sid) references Student (sid));


CREATE TABLE departmentLocation(deptName text,
                                building text,
                                primary key (deptName, building),
                                foreign key (deptName) references Department (deptName));


CREATE TABLE studentMajor(sid integer,
                          major text,
                          primary key (sid, major),
                          foreign key (sid) references Student (sid),
                          foreign key (major) references Major (major));


CREATE TABLE hasFriend(sid1 integer,
                       sid2 integer,
                       primary key(sid1,sid2),
                       foreign key (sid1) references Student (sid),
                       foreign key (sid2) references Student (sid));

INSERT INTO Student VALUES
     (1001,'Jean','Cupertino'),
     (1002,'Vidya', 'Cupertino'),
     (1003,'Anna', 'Seattle'),
     (1004,'Qin', 'Seattle'),
     (1005,'Megan', 'MountainView'),
     (1006,'Ryan', 'Chicago'),
     (1007,'Danielle','LosGatos'),
     (1008,'Emma', 'Bloomington'),
     (1009,'Hasan', 'Bloomington'),
     (1010,'Linda', 'Chicago'),
     (1011,'Nick', 'MountainView'),
     (1012,'Eric', 'Cupertino'),
     (1013,'Lisa', 'Indianapolis'), 
     (1014,'Deepa', 'Bloomington'), 
     (1015,'Chris', 'Denver'),
     (1016,'YinYue', 'Chicago'),
     (1017,'Latha', 'LosGatos'),
     (1018,'Arif', 'Bloomington'),
     (1019,'John', 'NewYork');


INSERT INTO Department VALUES
     ('CS', 'LuddyHall'),
     ('DataScience', 'LuddyHall'),
     ('Mathematics', 'RawlesHall'),
     ('Physics', 'SwainHall'),
     ('Biology', 'JordanHall'),
     ('Chemistry', 'ChemistryBuilding'),
     ('Astronomy', 'SwainHall');


INSERT INTO employedBy VALUES
     (1001,'CS', 65000),
     (1002,'CS', 45000),
     (1003,'DataScience', 55000),
     (1004,'DataScience', 55000),
     (1005,'Mathematics', 60000),
     (1006,'DataScience', 55000),
     (1007,'Physics', 50000),
     (1008,'DataScience', 50000),
     (1009,'CS',60000),
     (1010,'DataScience', 55000),
     (1011,'Mathematics', 70000), 
     (1012,'CS', 50000),
     (1013,'Physics', 55000),
     (1014,'CS', 50000), 
     (1015,'DataScience', 60000),
     (1016,'DataScience', 55000),
     (1017,'Physics', 60000),
     (1018,'CS', 50000),
     (1019,'Biology', 50000);

INSERT INTO departmentLocation VALUES
   ('CS', 'LindleyHall'),
   ('DataScience', 'LuddyHall'),
   ('DataScience', 'Kinsey'),
   ('DataScience', 'WellsLibrary'),
   ('Mathematics', 'RawlesHall'),
   ('Physics', 'SwainHall'),
   ('Physics', 'ChemistryBuilding'),
   ('Biology', 'JordanHall'),
   ('CS', 'LuddyHall'),
   ('Mathematics', 'SwainHall'),
   ('Physics', 'RawlesHall'),
   ('Biology', 'MultiDisciplinaryBuilding'),
   ('Chemistry', 'ChemistryBuilding');

INSERT INTO Major VALUES
   ('CS'),
   ('DataScience'),
   ('Physics'),
   ('Chemistry'),
   ('Biology');

INSERT INTO studentMajor VALUES
 (1001,'CS'),
 (1001,'DataScience'),
 (1002,'CS'),
 (1002,'DataScience'),
 (1004,'DataScience'),
 (1004,'CS'),
 (1005,'DataScience'),
 (1005,'CS'),
 (1005,'Physics'),
 (1006,'CS'),
 (1006,'Chemistry'),
 (1007,'Chemistry'),
 (1007,'CS'),
 (1009,'Chemistry'),
 (1009,'Physics'),
 (1010,'Physics'),
 (1011,'Physics'),
 (1011,'Chemistry'),
 (1011,'DataScience'),
 (1011,'CS'),
 (1012,'DataScience'),
 (1012,'Chemistry'),
 (1012,'CS'),
 (1013,'CS'),
 (1013,'DataScience'),
 (1013,'Chemistry'),
 (1013,'Physics'),
 (1014,'Chemistry'),
 (1014,'DataScience'),
 (1014,'Physics'),
 (1015,'CS'),
 (1015,'DataScience'),
 (1016,'Chemistry'),
 (1016,'DataScience'),
 (1017,'Physics'),
 (1017,'CS'),
 (1018,'DataScience'),
 (1019,'Physics');

INSERT INTO hasFriend VALUES
 (1001,1008),
 (1001,1012),
 (1001,1014),
 (1001,1019),
 (1002,1001),
 (1002,1002),
 (1002,1011),
 (1002,1014),
 (1002,1015),
 (1003,1004),
 (1004,1002),
 (1004,1003),
 (1004,1012),
 (1004,1013),
 (1004,1014),
 (1004,1019),
 (1005,1015),
 (1006,1003),
 (1006,1004),
 (1006,1006),
 (1007,1008),
 (1007,1013),
 (1007,1016),
 (1007,1017),
 (1008,1001),
 (1008,1007),
 (1008,1015),
 (1008,1019),
 (1009,1001),
 (1009,1005),
 (1009,1013),
 (1010,1008),
 (1010,1013),
 (1010,1014),
 (1011,1005),
 (1011,1009),
 (1011,1010),
 (1011,1011),
 (1012,1011),
 (1013,1002),
 (1013,1007),
 (1013,1018),
 (1014,1005),
 (1014,1006),
 (1014,1012),
 (1014,1017),
 (1015,1002),
 (1015,1003),
 (1015,1005),
 (1015,1011),
 (1015,1015),
 (1015,1018),
 (1016,1004),
 (1016,1006),
 (1016,1015),
 (1017,1013),
 (1017,1014),
 (1017,1019),
 (1018,1004),
 (1018,1007),
 (1018,1009),
 (1018,1010),
 (1018,1013),
 (1019,1001),
 (1019,1006),
 (1019,1008),
 (1019,1013);
 
 
-- #1
SELECT s.sid, s.sname, w.deptName, w.salary
FROM Student s
JOIN employedBy w ON s.sid = w.sid
WHERE s.homeCity = 'Bloomington'
AND w.salary >= 10000
AND w.deptName != 'Mathematics';

-- #2
SELECT s.sid, s.sname
FROM Student s
WHERE EXISTS (
  SELECT 1
  FROM Department d
  JOIN employedBy w ON d.deptName = w.deptName
  JOIN hasFriend f ON f.sid1 = s.sid
  JOIN Student s1 ON f.sid2 = s1.sid
  WHERE w.sid = s.sid AND d.mainOffice = 'LuddyHall' AND s1.homeCity != 'Bloomington'
);

-- #3
SELECT m.major
FROM Major m
WHERE m.major NOT IN (
  SELECT m2.major
  FROM Major m2
  JOIN studentMajor sm ON m2.major = sm.major
  JOIN Student s ON sm.sid = s.sid
  WHERE s.homeCity = 'Bloomington'
);

-- #4
SELECT s.sid, s.sname
FROM Student s
WHERE NOT EXISTS (
  SELECT 1
  FROM hasFriend f
  WHERE f.sid2 = s.sid
    AND NOT EXISTS (
      SELECT 1
      FROM Student s1
      WHERE f.sid1 = s1.sid
        AND s.homeCity = s1.homeCity
    )
);

-- #5
SELECT sid, sname
FROM Student
WHERE homeCity = 'Bloomington' -- (a) has home city Bloomington
  AND EXISTS (
    SELECT 1
    FROM employedBy e, Department d
    WHERE e.sid = Student.sid
      AND e.deptName = d.deptName
      AND e.salary > 20000 -- (b) works for a department where salary > 20000
  )
  AND EXISTS (
    SELECT 1
    FROM hasFriend
    WHERE sid1 = Student.sid OR sid2 = Student.sid
  ); -- (c) has at least one friend

-- #6
SELECT d1.deptName, d2.deptName
FROM Department d1, Department d2
WHERE d1.deptName <> d2.deptName -- Compare different department names
  AND d1.mainOffice = d2.mainOffice -- Compare main office locations

-- #7
SELECT s.sid, s.sname
FROM Student s
WHERE s.homeCity NOT IN (SELECT homeCity
                     FROM Student
                     WHERE sid IN (SELECT sid2
                                    FROM hasFriend
                                    WHERE sid1 = s.sid)); -- subquery to retrieve cities of friends

-- #8
SELECT m.major 
FROM Major m
WHERE m.major not in (SELECT sm.major
					 	FROM studentMajor sm, studentMajor sm1, studentMajor sm2
					 	WHERE not sm.sid = sm1.sid AND not sm.sid = sm2.sid AND not sm1.sid = sm2.sid AND sm.major = sm1.major AND sm.major = sm2.major)

-- #9
SELECT s.sid, s.sname, w.salary
FROM Student s, employedBy w
WHERE s.sid = w.sid AND s.sid in (SELECT f.sid1 
								  FROM hasFriend f, hasFriend f1
								  WHERE f.sid1 = f1.sid1 AND not f.sid2 = f1.sid2 AND (f.sid2, f1.sid2) in (SELECT sm.sid, sm1.sid
FROM studentMajor sm, studentMajor sm1 WHERE sm.major = sm1.major AND not sm.major = 'Mathematics'))

-- #10
SELECT deptName
FROM Department
WHERE deptName IN (
    SELECT deptName
    FROM employedBy e, Student s
    WHERE e.sid = s.sid
      AND s.homeCity != 'Indianapolis'
)

-- #11
SELECT d.deptName, e.salary AS highest_salary
FROM Department d, employedBy e
WHERE d.deptName = e.deptName
AND NOT EXISTS (
  SELECT 1
  FROM employedBy e2
  WHERE d.deptName = e2.deptName
  AND e2.salary > e.salary
)

-- #12
SELECT DISTINCT s.sid, s.sname
FROM Student s, employedBy e, hasFriend f
WHERE s.sid = e.sid
AND s.sid = f.sid1
AND e.deptName = e.deptName
AND e.salary > ALL (
  SELECT e2.salary
  FROM employedBy e2, hasFriend f2
  WHERE s.sid = f2.sid1
  AND e2.sid = f2.sid2
  AND e.deptName = e2.deptName
)

-- #17
-- not considering self-friend(assumption)
select s.sid
from   Student s
where  (select count(1)
        from   hasFriend f
        where  s.sid = f.sid1 and
               f.sid2 in (select s1.sid
                          from   Student s1
                          where  (select count(1)
                                  from   studentMajor sm
                                  where  sm.sid = s1.sid) >= 2)) >= 3;





-- #18
WITH avg_salary_by_dept AS (
    SELECT deptName, AVG(salary) AS avg_salary
    FROM employedBy
    GROUP BY deptName
)
SELECT deptName
FROM avg_salary_by_dept
WHERE avg_salary = (
    SELECT MIN(avg_salary)
    FROM avg_salary_by_dept
);

-- #19

select s1.sid as friend1, s2.sid as friend2 
from   Student s1, Student s2
where  s1.sid <> s2.sid and
       (select count(f1.sid2)
        from   hasFriend f1
        where  f1.sid1 = s1.sid) =
       (select count(f2.sid2)
        from   hasFriend f2
        where  f2.sid1 = s2.sid);


-- #20
SELECT DISTINCT e.sid
FROM employedBy e
JOIN hasFriend hf ON e.sid = hf.sid1
JOIN employedBy friend_e ON hf.sid2 = friend_e.sid AND e.deptName = friend_e.deptName
WHERE e.salary < ALL (
    SELECT salary
    FROM employedBy
    WHERE sid = hf.sid2 AND deptName = e.deptName
);











					







 
 