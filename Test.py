from geopy.geocoders import Nominatim

class Record():
    def __init__(self):
        pass

if __name__ == '__main__':
    # geolocator = Nominatim()
    # location = geolocator.geocode("ALLEN KY")
    # print(location.address)
    # print((location.latitude, location.longitude))
    record = Record()
    record.__setattr__("test", 123)
    print(record.test)