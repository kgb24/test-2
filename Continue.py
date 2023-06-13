In [1]: i =1
In [3]: while i < 10 :
   ...:     print ('恭喜发财')
   ...:     i = i + 1 # i + =1
   ...:
恭喜发财
恭喜发财
恭喜发财
恭喜发财
恭喜发财
恭喜发财
恭喜发财
恭喜发财
恭喜发财
In [4]: i
Out[4]: 10
In [5]: i = 0
In [7]: if i<10 :
   ...:     print ('恭喜发财')
   ...:     i= i+1
   ...:
恭喜发财
In [8]: range (10)
Out[8]: range(0, 10)

In [9]: for i in range (10):
   ...:     print i
  File "<ipython-input-9-4c1f6bb80f4b>", line 2
    print i
          ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(i)?
In [10]: print ('i')
i

In [11]: for i in range (10):
    ...:     print ('i')
    ...:
i
i
i
i
i
i
i
i
i
i

In [12]: range (10)
Out[12]: range(0, 10)

In [13]: for i in range (10):
    ...:     print (i)
    ...:
0
1
2
3
4
5
6
7
8
9
In [19]:  for k in range (10):
    ...:     if k == 5:
    ...:         continue
    ...:     if k > 2 :
    ...:          break
    ...:     print (k)
0
1
2