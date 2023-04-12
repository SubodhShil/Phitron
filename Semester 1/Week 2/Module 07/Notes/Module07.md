> # ```Module 07```

## <p align="center"><b>Array</b></p>

A linear fashion, continuous data structure that stores data of similar type (In most of the strongly typed languages like C, C++, Java. Python, JavaScript array can store various type of data).

**Array**: A convenient data structure that can store multiple values with the same data type. Basic arrays that store single value corresponds to an index is known as 1D array (single dimensional array).

### **Why do we require array**

1. We need to store a lot of data for our application, which can't be possible by making variable for each of the data. To avoid variable redundancy we have to use array.

&nbsp;

***Syntax***

```
///@syntax: data_type identifier[size];

/// create an array that stores student name (string)
string studentNames[1000];

/// creating an array of 1000 students age
int studentAges[1000];
```

***Notes***

1. The [] bracket is said to 'square bracket' but in context of array it also said 'subscript'.
2. The size of must be defined at the time of it's creation. That means leaving the [] empty will cause compilation error. **For example, ```int nums[]``` is wrong**.
3. The size of array is could be a constant.

```
int size;
cin >> size;
int arr[size];
```

```
const int size = 1000;
int arr[size];
```

```
int arr[1000];
```

```
int arr[]{5, 10, 15, 20};
```

👆 Aforementioned snippets are correct. But, following are not 👇

```
int arr[];
```

4. **Inserting value**: The operation is also known as insertion operation of array. We can initialize an array using following method.  

**(1) Initialize at time of declaration**

```
int arr[5] = {1, 2, 3, 4, 5};
```

**(2) Initialized By index**

```
int arr[3];
arr[0] = 10, arr[1] = 20, arr[2] = 30;
```

5. **Accessing value**: Each element of the array can be accessed by it's index. Array element accessing range: First array element = 0 and last array element = size - 1. So, the range of an array element is arr[0] to arr[size - 1]

```
int arr[]{10, 20, 30};

/// accessing the first element
printf("%d", arr[0]);

/// accessing the second element
printf("%d", arr[1]);

/// accessing the third element
printf("%d", arr[2]);
```

6. The name of the array is only recognized the first element. All other elements are recognized by index.

***Traits of an array***

1. Array obeys the 0-based index system.
2. Array allocates memory of the size it’s been declared. If the array isn’t dynamic then the array size must be a constant unsigned integer value.
3. In lcoal scope, for a size 'n', the array initializes with garbage value for each index. Try print out this:

```
int arr[5];

for(int i = 0; i < 5; i++)
{
    printf("%d\n", arr[i]);
}
```

4. Array stored in a contiguous memory location, which means you can track any array element without iteration or simply say random array element access is possible. The time complexity for randomly accessing an array element is O(1) or constant time access.

5. How compiler access an array element within constant time? => Behind the seen the compiler does some mathematical calculations to find the nth element of an array. The compiler does find the address of every array element thus we can access array elements randomly in constant time.

    - **Formula**: address_of_the_array + total_array_element_size *(target nth element - first_element)
Since, first element of an array starts with 0 so we can rewrite the formula as:
address_of_the_array (address of the first element)  + total_array_element_size* target_nth_element
For example: If the address of the array is 1000, the element size is 8 then find the address of the 7th element.
Calculation: 1000 + 8 * 6 = 1048
Keypoint: In C or C++ address of an array is represented by its 1st element or the 0th index element. Since we have the formula for tracking any array element we can now apply the first element’s address and find the address of the element at the nth index.

6. 
