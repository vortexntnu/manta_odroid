# manta_odroid

This repository should contain all packages needed on the ODROID-XU4, Manta's main computer.

## Installing

1. Clone the repository to the source directory of your catkin workspace

   ```shell
   $ git clone git@github.com:vortexntnu/manta_odroid.git
   ```

2. Download the submodules

   ```shell
   $ cd manta_odroid
   $ git submodule update --init --recursive
   ```

3. Build the packages using [catkin_tools](https://catkin-tools.readthedocs.io/en/latest/installing.html)

   ```bash
   $ catkin build
   ```

