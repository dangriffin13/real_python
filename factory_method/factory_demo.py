from song_class import Song
import serializers as ser




if __name__ == '__main__':
    song = Song(1, 'Basket Case', 'Green Day')
    print('song:\n', song)
    serializer = ser.ObjectSerializer()
    product = serialzier.serialize(song, 'JSON')
    print('product (JSON):\n', product)