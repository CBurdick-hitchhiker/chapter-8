def make_shirt(size="Large", text="I love Python!"):
    print(f"This shirt is {size} and says '{text}'")
    print(" ")


make_shirt()
make_shirt("Medium")
make_shirt("Small", "Coding is FUn!")


def describe_city(city, country='United States'):
    print(f"{city} is in {country}.")
    print(" ")


describe_city("New York")
describe_city("Chicago")
describe_city("Hotel", "Trivago")


def city_country(city, country):
    print(" ")
    return f"{city}, {country}"


print(city_country("New York", "USA"))
print(city_country("Chicago", "USA"))
print(city_country("Montreal", "Canada"))
print(" ")

def make_album(artist_name, album_title, song_count='None'):
    if song_count == 'None':
        album = {'name': artist_name, 'title': album_title}
    else:
        album = {'name': artist_name, 'title': album_title, 'Songs': song_count}
    return album


print(make_album("Corey Burdick", "Portals"))
print(make_album("Corey Burdick", "Canyons"))
print(make_album("Corey Burdick", "The Scream", 5))

while True:
    user_name = input("Enter Artist Name: ")
    album_name = input("Enter Album Title: ")
    if user_name.title() == "Quit" or album_name.title() == "Quit":
        break
    else:
        print(make_album(album_name, album_name))


messages = ["Hey.", "Hey There!", "I'm breaking up with you.", "Finally!"]


def show_messages():
    set_num = 0
    while set_num < len(messages):
        print(messages[set_num])
        print(" ")
        set_num = set_num + 1


show_messages()

