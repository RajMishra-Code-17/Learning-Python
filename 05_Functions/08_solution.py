def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_kwargs(name = "thor", power = "lightining")
print_kwargs(name = "thor")
print_kwargs(name = "thor", power = "lightining", enemy = "haila")

# this is kwargs