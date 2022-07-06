from xbmcgui import ListItem

def getArt(item: list):
    return {
        "poster": item["thumbnail"],
        "card": item["thumbnail"],
        "thumb": item["thumbnail"]
    }

def calcRating(likes: int, dislikes: int, views: int) -> int:
    return int((likes - dislikes) / views * 10)

def setInfoVideo(url: str, item: dict)-> ListItem:
    list_item = ListItem(item['title'], path=url)
    rating = calcRating(item['likeCount'], item['dislikeCount'], item['views'])
    info = {
        "title": item["title"],
        "plot": item["description"],
        "duration": item["duration"],
        "rating": rating,
        "userrating": rating
    }
    # ART
    list_item.setArt(getArt(item))
    list_item.setInfo('video', info)
    list_item.setProperty('isPlayable', 'true')
    list_item.setIsFolder(False)
    return list_item

def setInfoFolder(url: str, title: str)-> ListItem:
    list_item = ListItem(title, path=url)
    info = {
        "title": title
    }
    list_item.setInfo('video', info)

    return list_item
