## Introduce 
1. Input your map in your game

![img_4.png](img_4.png)

2. run the script

Then get the answer hint

![img_5.png](img_5.png)

the mean is that following the hint, you can get the answer
![img_1.png](img_1.png)

# How to use
1. Input your map in your game
border is 1, and the floor is 0, 6 is entrance and 9 is exit like this:
![img.png](img.png)
```python
[[0, 0, 0, 0, 0, 0],
[0, 1, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0],
[1, 0, 0, 0, 0, 0],
[0, 0, 0, 1, 0, 1]]
```

℗	℗	□	□	□	□	
□	□	□	□	□	■	
℗	□	□	□	℗	■	
■	□	□	E	□	■	
℗	℗	■	℗	□	℗	
S	■	□	■	℗	℗	



## The more instances
![img_2.png](img_2.png)

```python
map_lv11 = [
[0, 0, 1, 0, 0, 0],
[0, 0, 0, 0, 0, 1],
[0, 0, 0, 1, 0, 0],
[0, 0, 1, 0, 0, 0],
[0, 0, 0, 0, 0, 0],
[0, 1, 0, 0, 0, 0]]
```
![img_3.png](img_3.png)

```python
map_lv12 = [
[0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 1],
[1, 0, 0, 9, 0, 1],
[0, 0, 1, 0, 0, 0],
[6, 1, 0, 1, 0, 0]]
```