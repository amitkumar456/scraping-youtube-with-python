from pytube import YouTube

#link of youtube video which we need to scrape using python
link=input("Enter Link of YouTube Video: ")

yt=YouTube(link)


# To Print title
print("Title :",yt.title)

# To get number of views
print("Views :",yt.views)

# To get Lenght of Video
print("Duration :",yt.length)

# To get descriptoin
print("Description :",yt.description)

# To get ratings
print("Ratings :", yt.rating)

