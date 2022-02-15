def check_above(d):
    for i, j in d.items():
        if i == 'imdb' and j > 5.5:
            return True
    return False

def list_of_movies(movies):
    c = []
    for i in movies:
        if check_above(i) == True:
            c.append(i['name'])
    return c

def category(movies, s):
    arr = []
    for i in movies:
        for k, v in i.items():
            if v == s:
                arr.append(i['name'])
    return arr

def average_imdb(movies):
    res, cnt = 0, 0
    for i in movies:
        for k, v in i.items():
            if k == 'imdb':
                cnt+= 1
                res += i['imdb']
    return (res/cnt)

def category_average(movies, s):
    res, cnt = 0, 0
    for i in movies:
        for k, v in i.items():
            if v == s:
                res += i['imdb']
                cnt += 1
    return (res/cnt)

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

print('List of all movies:',list_of_movies(movies))
cat = input()
print(f'Movies of category {cat}:',category(movies, cat))
print('Average value of all movies:',average_imdb(movies))
cat1 = input()
print(f'Average value of movies of category {cat1}:',category_average(movies, cat1))