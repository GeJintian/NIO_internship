# Readings Notebook
### Perception Algorithm
#### Lidar and camera
##### [Multi-Modal Fusion Transformer for End-to-End Autonomous Driving](https://arxiv.org/pdf/2104.09224.pdf)
> End to End waypoints prediction

This paper provides a method to use transformer as fusion machine to fuse lidar and camera signals. Lidar BEV and camera image are processed by two ResNet. After each convolutional layer, feature maps of these two inputs will be taken out and divided into several vectors. Then, these vectors will be inputted into a transformer. The transformer will output several vectors, and they are reshaped into two feature maps and putted back to ResNets. At the end of these two ResNets, the resulted feature maps will be added and a RNN is ultilized to predict waypoints.<br>
[Network structure](./pictures/7.png)

##### [Deep Continuous Fusion for Multi-Sensor 3DObject Detection](https://arxiv.org/pdf/2012.10992.pdf)
>3D Object detection.

The author use two ResNet to extract feature maps from Lidar BEV and camera image. All feature maps of the image ResNet will be used to fused togather by a [feature pyramid network](https://openaccess.thecvf.com/content_cvpr_2017/papers/Lin_Feature_Pyramid_Networks_CVPR_2017_paper.pdf) and go through a continuous fusion layer to output into BEV space. Then, these features will be combined with BEV ResNet feature maps using FPN and then be putted into a Detection Header for final result. See the whole structure: [Network structure](./pictures/3.png)<br>
One important thing in this algorithm is the continuous fusion layer. It is used to project image feature maps into BEV space. Given a pixel in BEV space, it extract K nearest LIDAR points and project them to camera image. With these points, the corresponding image features can be found, and finally a MLP will be used to generate features for that pixel. See this layer at [Continuous fusion layer](./pictures/4.png)<br>
[Network structure](./pictures/5.jpg)


#### Lidar only
##### [PV-RCNN: Point-Voxel Feature Set Abstraction for 3D Object Detection](https://arxiv.org/pdf/1912.13192.pdf)
> 3D object detection

There are two major methods used in Lidar point cloud object detection: point based and voxel based. This paper combines these two methods togather, and can divided into two stages. In the first stage, the raw cloud points are voxelized and putted into a 3D sparse convolutional neural network. Meanwhile, Furthest Point-Sampling (FPS) will be used to generate key points.
[Network structure](./pictures/8.png)

#### Camera only
##### [3D Bounding Box Estimation Using Deep Learning and Geometry](https://arxiv.org/pdf/1612.00496.pdf)
>3D obeject detection.

The author proposes an algorithm which project 2D bounding box to 3D dimension by using transfer function of camera. For projection formula, we have *x<sub>2D</sub>*=k*\[R T\]*x<sub>3D</sub>*, where k is the internal reference and \[R T\] is the external reference of the camera. Therefore, if a 3D bounding box has size of (x',y',z') , we have: <br>
(x<sub>min</sub>, y<sub>min</sub>)=k*\[R T\](x'/2,y'/2,z'/2)<br>
In this equation, R is rotation (in R<sup>1</sup>, since pitch and roll could be omitted for a car), T is translation (in R<sup>3</sup>) and the 3D coordinate is (x',y',z'), which is also in R<sup>3</sup>. Assume that the internal reference k and 2D bounding box is known, this equation leaves us with 7 unkown variables. We could find 4 constraints like this, so we need to reduce variables.<br>
Therefore, the author uses a neural network to predict size (in R<sup>3</sup>) and angle, which means that only 3 variables remain, which could be obtained by solving constraint equations.<br>
[Network structure](./pictures/1.png)

##### [Objects as Points](https://arxiv.org/pdf/1904.07850.pdf)
> 2D Object detection and 3D Object detection. This algorithm is also called CenterNet.<br>

For an image I in R<sup>W\*H\*3</sup>, the model will output keypoint heatmap Y<sub>e</sub> in \[0,1\] in R<sup>W/n\*H/n\*C</sup>. For 2D object detetion, c is object category. For 3D object detection, it should add depth and angle. Use [in-bin regression](https://arxiv.org/pdf/1612.00496.pdf) for orientation. The model is very simple, which combines ResNet and DLA.<br>
To train the model, the author construct a Gaussian Distribution Y<sub>gt</sub> for every object to describe the confidence of that object in any point of that image. The center of one distribution is at the center of that ground truth. If overlap, the max element will be used. For loss function, the author wants Y to estimate the center point. Therefore, if Y<sub>gt</sub> is not 1 at that point, the author wants Y<sub>e</sub> to be 0. It uses facol loss function. See loss function: [Loss function](./pictures/2.png)<br>

##### [Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks](https://arxiv.org/pdf/1506.01497.pdf)
> 2D object detection

Faster R-CNN is an anchor based 2D object detection algorithm. For an input image, it resize and normalize it into a fixed size. Then, in the first stage, a convolutional neural network is applied to the resized image. Notice that the convoluitonal layer is padded, so that the image will be downsampled only in pooling layer. The resulted feature map will be putted into a RPN, which predict positive/negative and bounding box regression for each anchor directly. The output of RPN will be processed in proposal layer, which takes a certain number of positive anchors according to scores, and do NMS. In the second stage, a ROI pooling layer will be used to process original feature map and the proposed bounding box. Then, for each bounding box, MLP is used to predict category and do bounding box regression.<br>
[Network structure](./pictures/5.jpg)

##### [Monocular Quasi-Dense 3D Object Tracking](https://arxiv.org/pdf/2103.07351.pdf)
> 3D object tracking

For N trajectories T={t<sup>1</sup>,t<sup>2</sup>,...,t<sup>n</sup>}, t<sup>i</sup><sub>a,b</sub>={s<sup>(i)</sup><sub>a</sub>,s<sup>(i)</sup><sub>a+1</sub>,...,s<sup>(i)</sup><sub>b</sub>}. s<sup>(i)</sup><sub>a</sub> contains position information, including 3D location, 3D size, angle, reference feature and velocity in 3D. Key idea is to find a similar object in adjacent frames, making sure that their features are as similar as possible. The author also proposes data association, which associate s<sup>(i)</sup><sub>a</sub> to a trajectory t<sup>i</sup>.<br>
[Network structure](./pictures/5.jpg)

### Reinforcement Learning

### Loss and others
