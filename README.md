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
## System settings
The odroid, jetson tx2, dvl and nannopi are connected with etherne cables through a onboard swithc creating a small LAN with fixed IP setup.

| Computer  | IP address |
| ------------- | ------------- |
| Odroid  | 10.42.0.174  |
| Jetson tx2  | 10.42.0.216  |
| NanoPi  | 10.42.0.123  |
| DVL  | 10.42.0.96 |

The following network setup are used on the odroid /etc/network/interface:

    # interfaces(5) file used by ifup(8) and ifdown(8)
    # Include files from /etc/network/interfaces.d:
    source-directory /etc/network/interfaces.d

    auto lo
    iface lo inet loopback

    auto eth0
    iface eth0 inet static
    address 10.42.0.174
    netmask 255.255.255.0
    network 10.42.0.0
    broadcast 10.42.0.255
    gateway 10.42.0.1
    dns-nameservers 8.8.8.8 8.8.4.4

The four units synchronice their time using chrony. The jetson tx2 is apperantly the only one with a real time clock (little clock connected to battery capable of keeping time when the main power is off) thus act as a local NTP server for the other computers. Install with 

    apt install chrony

Then edit the setting file /etc/chrony/chrony.conf to the following:

    server 10.42.0.216 iburst
    driftfile /var/lib/chrony/drift
    keyfile /etc/chrony/chrony.keys
    commandkey 1
    makestep 1.0 3
    logdir /var/log/chrony
    allow 10.42.0.216
    
 


    
