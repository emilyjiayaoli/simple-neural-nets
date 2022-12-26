from engine import Value
import random

class Neuron:
    def __init__(self, nin, nonlin=True):
        self.w = [ Value(random.uniform(-1,1)) for _ in range(nin) ]
        self.b = Value(0)
        self.nonlin = nonlin
    
    def __call__(self, x):
        act = sum((wi*xi for wi, xi in zip(self.w, x)), self.b)
        act = act.relu
        return act[0] if len(act) == 1 else act
    
    def parameters(self):
        return self.w + [self.b]

    def __repr__(self):
        return f"{'ReLu' if self.nonlin else 'Linear'}"

class Layer:
    def __init__(self, nin, nout, **kwargs):
        self.neurons = [Neuron(self, nin, **kwargs) for _ in range(nout)]

        #number of neurons in a layer
    
    def __call__(self, x):
        out = [neuron(x) for neuron in self.neurons]
        return out[0] if len(out) == 1 else out

    def parameters(self):
        #return [p.parameters for p in self.neurons]
        return [p for neuron in self.neurons for p in neuron.parameters()]

    def __repr__(self):
        return f"Layer of [{', '.join(str(n) for n in self.neurons)}]"

class MLP:
    def __init__(self, nin, nouts):
        self.layers = []


# 1:28:25