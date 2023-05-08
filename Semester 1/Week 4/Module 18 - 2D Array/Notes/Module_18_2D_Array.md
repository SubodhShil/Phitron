> # ```Module 18```

Suppose you have been asked to create 100 arrays in your codebase. However, creating such a large number of arrays can be an overhead. To avoid the redundancy of array declaration, we can create an **array of arrays**. This is similar to a traditional array where variables are stored in a sequential manner. Similar to traditional arrays, where variables are stored sequentially, a 2D array can store multiple arrays in a sequential order.

### **Syntax:**  

```array[row][column]```  
The first subscript represents 'row' which is itself a 1D array and second subscript represents 'column', which indicates the number of elements in each row.

Total values in a 2D array: **row x column**

A 2D array is a 1D array if the column count is 1.

```
int arr[2][1] = {{1}, {2}};
for (int i = 0; i < 2; ++i)
{
    cout << arr[i][0] << endl;
}
```


