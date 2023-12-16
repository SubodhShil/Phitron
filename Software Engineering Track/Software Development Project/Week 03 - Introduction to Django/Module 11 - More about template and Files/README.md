## **```Django Static Files```**
1. Static files are: images, videos, audios, CSS stylesheet file, JS files

    **To work with static files in Django you need to create a folder namely static in the project root directory.**

## **```Django Dynamic Route```**
**Dynamic route or dyanmic URL**: Dynamic route or URL is a way, where data of various page will change on route or url basis. But you don't have to create mutliple html files to show differnet data, a single html can be utilized to serve this. There are mutliple types of routes:
1. int
2. str
3. slug: ../something-soothing-website/....

## **```Template Inheritance```**
একটা website এ এমন অনেকগুলো অংশ থাকে যেগুলো সব route বা link এ দেখা যায়, প্রতিটা link বা route এর জন্য আলাদা করে এই অংশগুলো যোগ না করে, একটি parent html file এর মধ্যে repetative অংশগুলো রেখে দিলে সেগুলো child html file চাইলে inherit করে নিবে । এর ফলে DRY (Don't Repeat Yourself) applicable হবে । 

> Template inheritance allows us to build a base "skeleton" template that contains all the common elements of our site and defines blocks that child template can override.

1. **To inherit template use extends tag.**  
2. **block tag** used for overriding specific part of a tmeplate.

## Rules:
1. **{% extends %}** must be the first template tag, otherwise inheritance won't work.
2. One should use **{% block %}** the most decrease app complexity and increase reusability.
3. We can't define multiple block tags with the same name in the same template.
4. If we need to get the content of the block from the parent template or keep the parent content as well the {{block.super}} variable will do the trick.

