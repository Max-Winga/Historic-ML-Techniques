import numpy
import pylab

def print_image_number(a):
	flat = numpy.ndarray.flatten(a)
	print(''.join(['0' if neuron == -1 else '1' for neuron in flat]))

def make_face():
    face=numpy.full((10,10),-1,dtype=int)
    face[9,0]=1
    face[8,1]=1
    face[7,2]=1
    face[6,3]=1
    face[6,4]=1
    face[6,5]=1
    face[7,6]=1
    face[8,7]=1
    face[8,8]=1
    face[9,9]=1
    face[1,3]=1
    face[1,7]=1
    face[4,4]=1
    return face

def make_tree():
    tree=numpy.full((10,10),-1,dtype=int)
    for i in range(0,10):
        tree[i,4]=1
        tree[i,5]=1
    for i in range(3,7):
        tree[1,i]=1
        tree[0,i]=1
    for i in range(2,9):
        tree[4,i]=1
    tree[5,8]=1
    return tree