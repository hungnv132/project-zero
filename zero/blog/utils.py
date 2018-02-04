import collections


def rename_object(obj):
    if isinstance(obj, collections.Iterable):
        return [{
            'name': item['tag__name'],
            'slug': item['tag__slug'],
            'count': item['count'],
        } for item in obj]
    else:
        print("This object is not iterable.")