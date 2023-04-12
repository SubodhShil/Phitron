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

4. **Inserting value to the array**: The operation is also known as insertion operation of array. We can initialize an array using following method.  

**(1) Initialize at time of declaration**

```
    int arr[5] = {1, 2, 3, 4, 5};
```

**(2) Initialized By index**

```
    int arr[3];
    arr[0] = 10, arr[1] = 20, arr[2] = 30;
```

5. The name of the array is only recognized the first element. All other elements are recognized by index.

***Traits of an array***

1. Array obeys the 0-based index system.
2. Array allocates memory of the size it’s been declared. If the array isn’t dynamic then the array size must be a constant unsigned integer value.
