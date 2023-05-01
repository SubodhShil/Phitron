> # ```Functions```

Function are collection of statements work together to accomplish various task.

<ins>**Syntax**</ins>

```
return_type function_name(parameter_list or void)
{
    /// statements
}
```

1. C and C++ functions are only able to return a single value of any premitive or user defined type.

2. Function could be passed with user input values. In this regard we can divide functions into two parts:
    - **Call by value**
    - **Call by reference**

3. The parameter are variable that are local to the function, used to receive data passed by the caller.

4. Function parameter can be set to a default value (only works for C++, C don't support default argument values). If user or caller of the function don't pass any value then it will use the default value.

5. **return_type** is the data type the function tend to return

6. Function can have one parameter or multiple parameter (seperated by comma). In contrast, a functino without any parameter can be ommited with keyword **void**, alternatively you can also left the place blank. But both of them are not entirely similar.
    - using **void** keyword: Passing any value will cause error.

    ```
    string sayHello(void)
    {
        return "Hello";
    }

    int main()
    {
        cout << sayHello("David"); /// error
    }
    ```

    - blank parameter list: Even if caller passed value, the value won't be utilized rather ignored by the compiler.

    ```
    string sayHello()
    {
        return "Hello";
    }

    int main()
    {
        cout << sayHello("David"); /// won't create any error
    }
    ```

7. Four ways to use a function:
    1. Return type + parameter
    2. Return type + no parameter
    3. No return type + parameter
    4. No return type + parameter

8. Based on return type we can come into two conclusions:
    1. When a function returns some value, it must be stored or utilized, as the function generates a value in response to its invocation.

    &nbsp;

    By storing:  
    Value saved into a variable

    ```
    /// calling a user defined function and calling it into a variable
    int x = sum();
    ```

    By utilizing:  
    The function is called and its return value is printed to the console using cout

    ```
    /// calling a user defined function without saving into variable
    cout << sum << endl;
    ```

    2. You cannot assign a void function to a variable because it does not return a value. A void function can only be called as a standalone statement.  
    Usecase:  
    (1) Void function should be used when you're only about to execute the result in the console without storing it in any variable.  

    ```
    void helloWorld()
    {
        cout << "Hello world" <<endl;
    }

    int main()
    {
        helloWorld(); /// result will shown in the console
        // int result = helloWorld(); // shows error
        // cout << helloWorld(); // shows error
    }
    ```

    (2) Void functions can be used to modify the actual value of various data structures such as sorting of an array or updating values of a variable declared in the main function or local space without returning any value.

    ```
    vector<int> v{5, 1, 15, 7};

    /// built in STL function
    sort(v.begin(), v.end());
    ```

    3. 
