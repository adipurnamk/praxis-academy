def hello_world(h):
    def world(w):
        print(h, w)
    return world # returning functions
h = hello_world # assigning
x = h("hello") # assigning
x
<function world at 0x7fec47afc668>
 x("world")
('hello', 'world')