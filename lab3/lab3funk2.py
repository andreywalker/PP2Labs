# Dictionary of movies

from operator import truediv


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
def is_above55(movies, name):
    iss=False
    for d in movies:
        if d["name"]==name:
            if d["imdb"]>5.49:
                iss=True
                break
    return iss
print(is_above55(movies, "We Two"))
print(is_above55(movies,"Exam"))
def list_above55(movies):
    a=[]
    for d in movies:
        if d["imdb"]>5.49:
            a.append(d["name"])
    return(a)
print(list_above55(movies))
def category_listn(movies, category):
    a=[]
    for d in movies:
        if d["category"]==category:
            a.append(d["name"])
    return(a)
def category_list(movies, category):
    a=[]
    for d in movies:
        if d["category"]==category:
            a.append(d)
    return(a)
print(category_listn(movies,"Suspense"))
def av_imdb(movies):
    a=0
    n=0
    for d in movies:
        a+=d["imdb"]
        n+=1
    return(a/n)
print(av_imdb(movies))  #6.486666666667

def av_imdb_by_category(movies, category):
    return(av_imdb(category_list(movies, category)))
print(av_imdb_by_category(movies, "Suspense"))  #8.1
