> ## **```String```**

There are two types of string seen in C++:

1. C style strings: Implement by general array
2. String class: String is a dynamic array of character, thus no need to specify the size. In C++, string is implemented as a class object.

**What is the size of a newly declared empty string?**  
👉 0 byte.

```
    string firstString;
    cout << firstString.size() << endl;     // 0
    cout << sizeof(firstString) << endl;    // 32
```

**Why the string size shows 0, but the sizeof operator shows 32 bytes?**  
👉 The implementation of C++ string is a class, so it does contain various data members and member functions.

std::string object contains the following members:

- A pointer to the first character in the string.
- A pointer to the last character in the string.
- A pointer to the end of the allocated memory.
- The size of the string.
- Other member functions or methods

When you get the byte size of your string using the sizeof operator like this ```sizeof(string_name)``` you're actually getting the size of the object itself. Although the result of sizeof is not always 32 bytes. The specific size may vary depending on the implementation and platform.

- String class variable size is dynamic.

Both `cin.ignore()` and `getchar()` can be used to ignore a particular character.

`cin.ignore()` is a member function of the `std::cin` object. It takes two arguments: the number of characters to ignore and the character to ignore. For example, the following code will ignore the next two characters in the input stream:

```
cin.ignore(2);
```

`getchar()` is a standard library function that reads a single character from the input stream. It returns the character that was read. For example, the following code will read a character from the input stream and ignore it:

```
char ch = getchar();
```

The main difference between `cin.ignore()` and `getchar()` is that `cin.ignore()` can ignore multiple characters, while `getchar()` can only ignore one character.

In general, `cin.ignore()` is the preferred way to ignore characters. It is more efficient and easier to use. However, `getchar()` can be used in some cases where `cin.ignore()` cannot, such as when you need to read a character from the input stream and ignore it at the same time.

| Function | Description |
|---|---|
|**Capacity**|
| `s.size()` | Returns the size of the string. |
| `s.max_size()` | Returns the maximum size that string can hold. |
| `s.capacity()` | Returns current available capacity of the string. |
| `s.clear()` | Clear the string. |
| `s.empty()` | Return true/false if the string is empty. |
| `s.resize()` | Change the size of the string. |
|**Element access**|
| `S[i]` | Access the ith index of the string. |
| `s.at(i)` | Access the ith index of the string. |
| `s.back()` | Access the last element of the string. |
| `s.front()` | Access the first element of the string. |
|**Modifiers**|
| `s+=` | Append another string. |
| `s.append()` | Append another string. |
| `s.push_back()` | Add character to the last of the string. |
| `s.pop_back()` | Remove the last character of the string. |
| `s=` | Assign string. |
| `s.assign()` | Assign string. |
| `s.erase()` | Erase characters from the string. |
| `s.replace()` | Replace a portion of the string. |
| `s.insert()` | Insert a portion to a specific position. |
|**Iterators**|
| `s.begin()` | Pointer to the first element. |
| `s.end()` | Pointer to the next element after the last element of the string. |
