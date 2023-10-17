1) itertools.product(iter, iter) - cartesian product of iterables (product([1,2], [3,4]) == [(1,3),(1,4),(2,3),(2,4)])
2) itertools.permutations(iterable, length of permutations) - return all permutations of iterable list elements 
     (permutations('abc',2) == [('a','b'), ('a','c'), ('b','a'), ('b','c'), ('c','a'), ('c','b')])
3) itertools.groupby(iterable, key=function) - группирует элементы последовательности по значению функции key.
     Возвращает key, group = groupby(iterable) - key -- признак группировки, group -- группа элементов (необходимо переводить, например list(group))
4) itertools.combinations('abc', 2) == [(a,b), (a,c), (b,c)] -- return all combinations of lenth 2 without repeated elements
5) itertools.combinations_with_replacement('abc', 2) == [(a,a), (a,b), (a,c), (b,b), (b,c), (c,c)] -- return all combinations of lenth 2 with repeated elements
