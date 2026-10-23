/*
a) Inside the Columns table for actor, there are four fields: actor_id, first_name, last_name, and last_update
b) Inside the Columns table for film, there are many fields: film_id, title, description, release_year, language_id, original_language_id, rental_duration,
	rental_rate, length, replacement_cost, rating, special_features, and last_update.
c) film_actor contains columns for actor_id and film_id.
d) rental table includes a preview of 10 records with columns that hold: rental_id, rental_date, inventory_id, customer_id, return_date, staff_id, and last_update.
	This information is easy to read since it shows all fields with a clear formatting and a simple structure. It shows the rented date and return date,
    the customer id who purchased, the staff who handled the order as well as the inventory count. 
e) inventory table includes inventory_id, film_id, store_id, and last_update. 
f) I would need the film, inventory and the rental table. The film table holds the names of all of the films, the inventory table holds the film id and inventory id, 
	and the rental date shows when they were rented. These tables are related because: rental and inventory share inventory_id, and inventory and film share film_id, 
    All columns here are needed to find and connect the film titles to their respective rental dates.
*/

SELECT film_id, title FROM film;
SELECT inventory_id, film_id FROM inventory;
SELECT rental_date, inventory_id FROM rental; 

