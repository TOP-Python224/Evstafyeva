-- 1.
select `teachers`.`name` as `Teacher Name`,
	   `teachers`.`surname`as `Teacher Surname`,
       `groups`.`name` as `Groups`
  from `teachers`
  join `groups`;

-- 2
select `faculties`.`name` as 'Faculties',
	   `faculties`.`financing` as 'Financing'
  from `faculties`
  join `departments`
 where `faculties`.`financing` > `departments`.`financing`;
    
-- 3
select `curators`.`surname` as `Curators`,
        `groups`.`name` as `Groups`
  from `curators`
  join `groups`
  join `groups_curators`
  where `curators`.`id` = `groups`.`id`;

-- 4 
select `teachers`.`name` as `Teacher Name`,
	   `teachers`.`surname` as `Teacher Surname`,
       `groups`.`name` as `Group`
  from `teachers`
  join `groups`
  where `groups`.`name` = 'SE-023'
  -- группа 'P107' отсутствует в БД
order by `teachers`.`surname`;

-- 5
select `teachers`.`surname` as `Teacher Surname`,
		`faculties`.`name` as `Faculties`
  from `teachers`
  join `faculties`
  where `teachers`.`id` = `faculties`.`id`;
  
-- 6
select `departments`.`name` as `Departments`,
		`groups`.`name` as `Groups`
	from `departments`
    join `groups`
   where `departments`.`id` = `groups`.`department_id`;
   
-- 7
select `subjects`.`name` as `Subjects`,
		`teachers`.`name` as `Teacher Name`,
		`teachers`.`surname` as `Teacher Surname`
	from `subjects`
	join `teachers`
	where `teachers`.`name` = 'Montana' and `teachers`.`surname` = 'Abbott';
    -- преподаватель Samantha Adams отсутствует в БД

-- 8
  select `departments`.`name` as `Departments`,
		 `subjects`.`name` as `Subject`
    from `departments`
    join `subjects`
where `subjects`.`name` = 'Eget Lacus'
-- дисциплина 'Database Theory' отсутствует в БД
order by `departments`.`name`;

-- 9 
select `groups`.`name` as `Groups`,
		`faculties`.`name` as `Faculty`
  from `groups`
  join `faculties`
 where  `faculties`.`name` = 'School of Physics and Engineering';
  -- факультет'Computer Science' отсутствует в БД
  
-- 10
select `groups`.`name` as `Groups`,
		`faculties`.`name` as `Faculties`
  from `groups`
  join `faculties`
  where `groups`.`year`= 5;
  
-- 11 (аудитории "В103" нет в БД)
select `teachers`.`name` as `Teacher Name`,
	   `teachers`.`surname`as `Teacher Surname`,
       `groups`.`name` as `Groups`,
       `subjects`.`name` as `Subject`,
       `lectures`.`date` as `Shedule`
  from `teachers`
  join `subjects`
  join `groups`
  join `lectures`
  where `groups`.`id` = `subjects`.`id`