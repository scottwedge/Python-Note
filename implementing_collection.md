# implementing collection
the collection includes: tuple, str, range, list, dict, set
|protocl|implementing collection|
|------------|------------|
|container|str, list, dict, range, tuple, set, bytes|
|Sized| str, list, dict, range, tuple, set, bytes|
|Iterable|str, list, dict, range, tuple, set, bytes|
|Sequence|str, list, tuple, range, bytes|
|Mutable Sequence| List|
|Mutable Set| set|
|Mutable Mapping|dict|

* the Container protocol can be test using **in** and **not in** 
* the size Protocol can be sued with len(s)
* the iterable protocol can producean iterator with iter(s), for example:
```python
for item in iterable:
    do_something(item)
```
* for sequence protocol can be used with index, like:
```python
item = seq[index]
# or find item by value
index = seq.index(item)
#count items
num = seq.count(item)
#produce a reversed sequence
r = reversed(seq)
```
* set protocol can support various set operations, for example:
[check here for set function](https://blog.csdn.net/business122/article/details/7541486)


*python的set和其他语言类似, 是一个无序不重复元素集, 基本功能包括关系测试和消除重复元素. 集合对象还支持union(联合), intersection(交), difference(差)和sysmmetric difference(对称差集)等数学运算.
 
sets 支持 x in set, len(set),和 for x in set。作为一个无序的集合，sets不记录元素位置或者插入点。因此，sets不支持 indexing, slicing, 或其它类序列（sequence-like）的操作。

## collection construction
