def example_function(arg1, *, key_arg1=None, key_arg2=None):
    print("arg1:", arg1)
    print("key_arg1:", key_arg1)
    print("key_arg2:", key_arg2)
    

# 함수 호출
example_function("positional_argument", key_arg1="value1", key_arg2="value2")

# TypeError: example_function() takes 1 positional argument but 3 were given
example_function("positional_argument", "value1", "value2")