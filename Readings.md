# Readings Notebook
### Perception Algorithm
#### Lidar and camera
##### 1. [Deep Continuous Fusion for Multi-Sensor 3DObject Detection](https://arxiv.org/pdf/2012.10992.pdf)
>3D Object detection.

The author use two ResNet to process Lidar BEV and camera image. All feature maps of the image ResNet will be used to fused togather
[Network structure](./pictures/3.png)

[Continuous fusion layer](./pictures/4.png)
#### Lidar only

#### Camera only
##### 1. [3D Bounding Box Estimation Using Deep Learning and Geometry](https://arxiv.org/pdf/1612.00496.pdf)
>3D obeject detection.

The author proposes an algorithm which project 2D bounding box to 3D dimension by using transfer function of camera. For projection formula, we have *x<sub>2D</sub>*=k*\[R T\]*x<sub>3D</sub>*, where k is the internal reference and \[R T\] is the external reference of the camera. Therefore, if a 3D bounding box has size of (x',y',z') , we have: <br>
(x<sub>min</sub>, y<sub>min</sub>)=k*\[R T\](x'/2,y'/2,z'/2)<br>
In this equation, R is rotation (in R<sup>1</sup>, since pitch and roll could be omitted for a car), T is translation (in R<sup>3</sup>) and the 3D coordinate is (x',y',z'), which is also in R<sup>3</sup>. Assume that the internal reference k and 2D bounding box is known, this equation leaves us with 7 unkown variables. We could find 4 constraints like this, so we need to reduce variables.<br>
Therefore, the author uses a neural network to predict size (in R<sup>3</sup>) and angle, which means that only 3 variables remain, which could be obtained by solving constraint equations.<br>
[Network structure](./pictures/1.png)
##### 2. [Objects as Points](https://arxiv.org/pdf/1904.07850.pdf)
> 2D Object detection and 3D Object detection. This algorithm is also called CenterNet.<br>

For an image I in R<sup>W\*H\*3</sup>, the model will output keypoint heatmap Y<sub>e</sub> in \[0,1\] in R<sup>W/n\*H/n\*C</sup>. For 2D object detetion, c is object category. For 3D object detection, it should add depth and angle. Use [in-bin regression](https://arxiv.org/pdf/1612.00496.pdf) for orientation. The model is very simple, which combines ResNet and DLA.<br>
To train the model, the author construct a Gaussian Distribution Y<sub>gt</sub> for every object to describe the confidence of that object in any point of that image. The center of one distribution is at the center of that ground truth. If overlap, the max element will be used. For loss function, the author wants Y to estimate the center point. Therefore, if Y<sub>gt</sub> is not 1 at that point, the author wants Y<sub>e</sub> to be 0. See loss function: [loss function](./pictures/2.png)
### Behavior Decision

### Loss and others
