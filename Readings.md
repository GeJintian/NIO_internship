# Notebook
### Perception Algorithm
#### Lidar and camera

#### Lidar only

#### Camera only
##### 1. [3D Bounding Box Estimation Using Deep Learning and Geometry](https://arxiv.org/pdf/1612.00496.pdf)
The author proposes an algorithm which project 2D bounding box to 3D dimension by using transfer function of camera. For projection formula, we have *x*=k*\[R T\]*x*, where k is the internal reference and \[R T\] is the external reference of the camera. Therefore, if a 3D bounding box have , we have: <br>
(x, y)=k*\[R T\](x',y',z')<br>
In this equation, R is rotation (in R<sup>3</sup>), T is translation (in R<sup>3</sup>) and the 3D coordinate is (x',y',z'), which is also in R<sup>3</sup>. Assume that the internal reference k and 2D bounding box is known, this equation leaves us with 9 unkown 

### Behavior Decision

### Loss and others
