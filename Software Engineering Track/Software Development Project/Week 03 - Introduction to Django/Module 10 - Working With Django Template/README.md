> # **```Django Template Language```**
admin একটি project এ একটাই থাকে । 

templates folder এর মধ্যে আমরা HTML code গুলো লিখে রাখি । templates folder দুইটি জায়গায় রাখা  যায়ঃ   
১। Global templates folder যেটা root directory তে থাকে
২। app folder গুলোতে 

যখনই আমরা template folder বানাবো তখনই সেটা project folder এর settings.py তে **TEMPLATES** list টিতে mention করে দিতে হবে । 

Best practices:  
1. Global templates folder এর ভিতরের HTML file গুলোর নাম app folder এর নাম গুলোর মতো যেন না হয় । 

## What is Django Context
Django তে backend (views.py) থেকে frontend (home.html) এ আমরা data গুলো dictionary আকারে পাঠাই, একেই context বলা হয় । 

## Template Filtering
