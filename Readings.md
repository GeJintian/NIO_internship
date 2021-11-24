# Readings Notebook
### Perception Algorithm
#### Lidar and camera
##### 1. [Deep Continuous Fusion for Multi-Sensor 3DObject Detection](https://arxiv.org/pdf/2012.10992.pdf)
>3D Object detection.

The author use two ResNet to extract feature maps from Lidar BEV and camera image. All feature maps of the image ResNet will be used to fused togather by a [feature pyramid network](https://openaccess.thecvf.com/content_cvpr_2017/papers/Lin_Feature_Pyramid_Networks_CVPR_2017_paper.pdf) and go through a continuous fusion layer to output into BEV space. Then, these features will be combined with BEV ResNet feature maps using FPN and then be putted into a Detection Header for final result. See the whole structure: [Network structure](./pictures/3.png)<br>
One important thing in this algorithm is the continuous fusion layer. It is used to project image feature maps into BEV space. Given a pixel in BEV space, it extract K nearest LIDAR points and project them to camera image. With these points, the corresponding image features can be found, and finally a MLP will be used to generate features for that pixel. See this layer at [Continuous fusion layer](./pictures/4.png)<br>


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
To train the model, the author construct a Gaussian Distribution Y<sub>gt</sub> for every object to describe the confidence of that object in any point of that image. The center of one distribution is at the center of that ground truth. If overlap, the max element will be used. For loss function, the author wants Y to estimate the center point. Therefore, if Y<sub>gt</sub> is not 1 at that point, the author wants Y<sub>e</sub> to be 0. See loss function: [loss function](./pictures/2.png)<br>

##### 3. [Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks](https://arxiv.org/pdf/1506.01497.pdf)
> 2D object detection



### Behavior Decision

### Loss and others
