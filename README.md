# manta_odroid

This repository should contain all packages needed on the ODROID-XU4, Manta's main computer.

## Prerequisites

* [Ubuntu](https://wiki.odroid.com/odroid-xu4/os_images/linux/ubuntu/ubuntu)
* [ROS Kinetic](http://wiki.ros.org/kinetic/Installation/Ubuntu)

## Installing

1. Clone the repository with submodules to the source directory of your [catkin workspace](http://wiki.ros.org/catkin/Tutorials/create_a_workspace)

   ```shell
   git clone --recurse-submodules https://github.com/vortexntnu/manta_odroid.git
   ```

2. Install dependencies

   ```shell
   sudo apt-get install ros-kinetic-geographic-msgs
   ```

3. Build the packages using [catkin_tools](https://catkin-tools.readthedocs.io/en/latest/installing.html)

   ```bash
   catkin build
   ```
