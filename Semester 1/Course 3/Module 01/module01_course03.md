> # **```Time Complexity```**

- Time complexity is a parameter that determines comparison among algorithms, which algorithm will perform better in case of the input size increases drastically.

- Time complexity doesn't calculated in seconds, miliseconds or any other specific unit, rather use some asymptotic notations like Big Oh, Big Omega and Big Theta determine algorithm.

- The reason for not using unit specific notation in time complexity calculation is that computer devices defers by it's hardware.

- Time complexity of a program measures by the number of steps or iterations it used to accomplish the algorithm.

&nbsp;

**Some important rules to calculate time complexity:**

1. Always calculate for worst case.
2. Ignore the constants.
3. Complexity of a program with multiple loops is addition of complexity of each loop.

&nbsp;

## <p align="center"> **Determine the time complexity** </p>

### <p align="center"> **(1)** </p>

```cpp
for(int i = 0; i < n; ++i)
{
    if(arr[i] == x)
    {
        return i;
    }
}
```

**Time Complexity: O(N)**

### <p align="center"> **(2)** </p>

```cpp
for(int i = 0; i <= n/2; ++i)
{
    /// some works here
}
```

**Time Complexity: O(N)**

### <p align="center"> **(3)** </p>

```cpp
for(int i = 0; i <= n; ++i)
{
    /// some works here
}

for(int i = 0; i <= m; ++i)
{
    /// some works here
}
```

Time Complexity: O(N) + O(M) = O(N + M)
