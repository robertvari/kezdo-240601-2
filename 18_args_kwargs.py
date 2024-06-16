def my_function(*args, **kwargs):
    print(args)
    print(kwargs)


my_function(
    "Robert",
    "Budapest",
    1,
    234,
    20,
    name="Robert",
    address="Budapest",
    param1="Hello",
    param2="Hello 2"
)