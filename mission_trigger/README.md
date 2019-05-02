# Mission Trigger Signal

This repository contains the script to interface the ADC-pins(Used as mission trigger) on the ODROID XU4 with ros.

## When used with our Hall-effect switch
The script publishes a Bool to /mission_trigger when the switch register a magnetic field strong enough.

## Dependencies

The WiringPi python wrapper is needed for this package:

    ```shell
    $ sudo apt install git python-dev python-setuptools python3-dev python3-setuptools swig
    $ git clone --recursive https://github.com/hardkernel/WiringPi2-Python
    $ cd WiringPi2-Python

    # Python 2
    $ sudo python setup.py install
    ```

## Give user access to the ADC-pins (NEEDED)

This is a solution to access the pins without using root. Needed since script is a rosnode.

###ONLY TESTED ON KERNEL 4.14.5-92

1. Create a gpio group
    ```shell
    $ sudo addgroup gpio
    $ sudo usermod -a -G gpio odroid   
    ```

2. Create rule file

    ```shell
    $ touch /etc/udev/rules.d/90-gpiomem.rules
    ```
3. Add this line to .rules file(root needed to open file)

    ```shell
        SUBSYSTEM=="exynos-gpiomem", GROUP="gpio", MODE="0660"
    ```
4. Reboot system to implement the new rules
