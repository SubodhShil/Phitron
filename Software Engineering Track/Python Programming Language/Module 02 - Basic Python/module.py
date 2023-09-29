# access and use function defined outside of the file
from built_in_functions import maxAge

if (maxAge(11, 2, 33, 18, 19) >= 18):
    print("You can drive")
else:
    print("You're not eligible")
