# Exercise 1

### 1-a - Printing Text ("Hello World!")

```
print("Hello World!")
```

### 1-b Assigning "Hello World!" to the variable *my_text*

```
my_text = "Hello World!"

print(my_text)
```

# Exercise 2

### 2-a

```
glass_of_water = "3"
    
print("I drank", glass_of_water, "glasses of water today.")
```

### 2-b

```
glass_of_water = "3"

glass_of_water =glass_of_water+1

print(glass_of_water)
```

# Exercise 3

### 3-a

```
men_stepped_on_the_moon=10

print(10)
```
#### *Note: I had no idea how many people stepped on the moon, so the number was wrong I guess*

### 3-b

```
my_reason_for_coding="I want better job opportunities and make silly little games so I can survive the 21st century!"

print(my_reason_for_coding)
```

### 3-c

```
global_mean_sea_level_2018=21.36

print(global_mean_sea_level_2018)
```

# Exercise 9

### 9-a

```
str="It's always darkest before dawn."

print(str)
```
### 9-b

```
str="It's always darkest before dawn"

ans_1=str[0]+str[1]+str[-1]

print(ans_1)
```

### 9-c

```
str="It's always darkest before dawn.'

str.replace(".", "!")  
```

#### *Note: This solution worked in Python on my laptop but not the website.*

# Exercise 10

### 10-a

```
lst=[11, 10, 12, 101, 99, 1000, 999]

answer_1=len(lst)

print(answer_1)
```
### 10-b

```
msg="Be yourself, everyone else is taken."

msg_lenght=len(msg)

print(msg_lenght)
```

### 10-c

```
dict=("Real Madrid": 13,"AC Milan": 7,"Bayern Munich":5 ,"Barcelona": 5, "Liverpool": 5)

ans_1=len(dict)

print(ans_1)
```

#### *Note: I didn't know what was mean't by keys. I am still a little confused about this exercise.*

# Exercise 11

### 11-a

```
lst=[11, 100, 99, 1000, 999]

lst.sort()

print(lst)
```
#### *Note: I forgot to put use the brackets the first time...*

### 11-b

```
lst=["Ukraine", "Japan", "Canada", "Kazakhstan", "Taiwan", "India", "Belize"]

lst.sort()

print(lst)
```

### 11-c

```
lst=[11, 100, 101, 999, 1001]

lst.reverse

print(lst)
```

#### *Note: Got here by trial and error, but hurray for intuition I guess!*

# Exercise 12

### 12-a

```
lst=[11, 100, 99, 1000, 999]

lst.pop(-1)

popped_item="999"

print(popped_item)

print(lst)
```

### 12-b

```
lst=["milk", "banana", "eggs", "bread", "broccoli", "lemons"]

lst.pop(-2)

item="broccoli"

print(lst, item)
```

### 12-c

```
GDP_2018=("US": 21, "China": 16, "Japan": 5, "Germany": 4, "India": 3, "France": 3, "UK": 3, "Italy": 2)
italy_gdp=GDP_2018.pop("Italy")
print(italy_gdp, "trillion USD")
```

#### *Note: This one confused me a little bit, because I wasnt sure why I couldnt just take the "2" at the end with .pop(-1). Had to consult the hint and solution on the website for this one.*

---

