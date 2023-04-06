select p.firstName, p.lastName, a.city, a.state from Person p
left join Address a
on p.personId = a.personId

















































































# Write your MySQL query statement below
# select firstname, lastname, CITY, STATE from person p
# left join address a
# on p.personId = a.personId



# select firstName, lastName, IFNULL(city,NULL) city, IFNULL(state,NULL) state from Person p
# left join Address a
# on p.personId = a.personId


# SELECT firstName, lastName, city, state
# FROM Person p
# left join Address a
# on p.personId = a.personId



