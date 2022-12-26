class Value:
    def __init__(self, data, _children=(), _op=''):
        self.data = data
        self.grad = 0.0

        #internal vars for autograd graph
        self._prev = set(_children)
        self._backward = lambda: None #stores the _backward() function that updates the gradients
        self._op = _op
    
    def __repr__(self): #use to print out something nicely in python 
        return f"Value(data={self.data})"

    def __add__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        out = Value(self.data + other.data, (self, other), "+")

        def _backward():
            self.grad += out.grad
            other.grad += out.grad
        out._backward = _backward #the ._backward attribute of the output is a function that sets/updates the grad of it's children/Values that make up out
        return out

    def __mul__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        out = Value(self.data * other.data, (self, other), "*")
        def _backward():
            self.grad = other.data * out.grad
            other.grad = self.data * out.grad
        out._backward = _backward
        return out



    def backward(self):
        #backward pass: goes through network in reverse to calculate gradient
            #backward() only gets called on the final y prediction
        
        # create topological list in forward order to go through nodes (recursively)
        # then call _backward in reversed order
        topo = []
        visited = set()
        def topo_build(n):
            if n not in visited:
                visited.add(n)
                for child in n._prev:
                    topo_build(child)
                topo.append(n)
        topo_build(self)
        self.grad = 1 #initialize base case of grad = 1 for last node 
        for node in reversed(topo):
            node._backward()


    
a = Value(3.0)
b = Value(3.2)
c = a+b
print(a+b)
print(type(a+b))
print(c._op)