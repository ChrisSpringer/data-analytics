# Christopher Springer
# 11/11/2026
# Exercise 3B Lab 1

fav_movies = ['Rush Hour', 
              'The Incredibles', 
              'Mean Girls',
              'White Chicks', 
              'Shrek 2', 
              'Avengers: Endgame',
              'Austin Powers in Goldmember', 
              'The Spongebob Squarepants Movie'
              ]

print(f'The list fav_movies includes my top {len(fav_movies)} favorite movies.')
print(fav_movies)

# One list is alphabetically sorted and the other is listed how I wrote it
print(sorted(fav_movies))
print(fav_movies)

# The .sort method sorted the movies alphabetically and stores them in their new position.
# the sorted() function only worked on the list, but did not update anything
fav_movies.sort()
print(fav_movies)

fav_movies.append('Get Out')
print(f'The updated list fav_movies includes my top \
{len(fav_movies)} favorite movies.')
print(fav_movies)