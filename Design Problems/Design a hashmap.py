"""
Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

MyHashMap() initializes the object with an empty map.
void put(int key, int value) inserts a (key, value) pair into the HashMap.
If the key already exists in the map, update the corresponding value.
int get(int key) returns the value to which the specified key is mapped,
or -1 if this map contains no mapping for the key.
void remove(key) removes the key and its corresponding value if the map
contains the mapping for the key.
 

Example 1:

Input
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
Output
[null, null, null, 1, -1, null, 1, null, -1]

Explanation
MyHashMap myHashMap = new MyHashMap();
myHashMap.put(1, 1); // The map is now [[1,1]]
myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]
"""

"""
1. What is the datatype of our keys?
2. What about our values?
3. How many calls will be made to this API?
4. What is the range of key?
5. Range of values? 
"""

class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:

    def __init__(self):
        self.hashmap = [ListNode(-1, -1) for _ in range(1000)]
        

    def put(self, key: int, value: int) -> None:
        idx = self.hash_function(key)
        cur = self.hashmap[idx]
        node = ListNode(key, value)

        while cur and cur.next:
            if cur.next.key == key:
                cur.next.val = value
                return
            cur = cur.next
        cur.next = node
        

    def get(self, key: int) -> int:
        idx = self.hash_function(key)
        cur = self.hashmap[idx]

        while cur:
            if cur.key == key:
                return cur.val
            cur = cur.next
        return -1
        

    def remove(self, key: int) -> None:
        idx = self.hash_function(key)
        cur = self.hashmap[idx]

        while cur and cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next

    def hash_function(self, key) -> int:
        return key % 1000
        

"""
[D]
[D] -> [100] -> [121] -> [N]
[D]
[D] -> [4] ->[8] -> [66]-> [N]
[D]

"""


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)