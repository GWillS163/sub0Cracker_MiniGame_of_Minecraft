## Introduce 
1. Input your map in your game

![img_4.png](md_src/img_4.png)

2. run the script

Then get the answer hint
```
that is also as following graph shown:
	0	1	2	3	4	5
0 	⑪	←	←	⑩	■	　	
1 	↓	　	■	⑨	⑧	　	
2 	E	■	③	　	↑	　	
3 	■	　	↓	　	↑	■	
4 	①	→	②	■	⑦	⑥	
5 	S	■	④	→	→	⑤	
```

the mean is that following the hint, you can get the answer
![img_1.png](md_src/img_1.png)



# How to use
1. Input your map in your game
border is 1, and the floor is 0, 6 is entrance and 9 is exit like this:
![img.png](md_src/img.png)
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
![img_2.png](md_src/img_2.png)

```python
map_lv11 = [
[0, 0, 1, 0, 0, 0],
[0, 0, 0, 0, 0, 1],
[0, 0, 0, 1, 0, 0],
[0, 0, 1, 0, 0, 0],
[0, 0, 0, 0, 0, 0],
[0, 1, 0, 0, 0, 0]]
```
![img_3.png](md_src/img_3.png)

```python
map_lv12 = [
[0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 1],
[1, 0, 0, 9, 0, 1],
[0, 0, 1, 0, 0, 0],
[6, 1, 0, 1, 0, 0]]
```

# bugFix
## before
cause the DFS algorithm iteration is not shortest.
![img.png](img.png)
```
	0	1	2	3	4	5
0 	⑫	　	　	⑪	■	　	
1 	　	　	■	⑧	⑦	　	
2 	E	■	　	　	　	　	
3 	■	⑩	　	⑨	　	■	
4 	①	　	②	■	⑥	⑤	
5 	S	■	③	　	　	④

```
## After
![img_1.png](img_1.png)
```
	0	1	2	3	4	5
0 	⑪	　	　	⑩	■	　	
1 	　	　	■	⑨	⑧	　	
2 	E	■	③	　	　	　	
3 	■	　	　	　	　	■	
4 	①	　	②	■	⑦	⑥	
5 	S	■	④	　	　	⑤	
```
