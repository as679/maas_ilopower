# maas_ilopower

**_Install_**

    pip3 install python-hpilo
    cd /opt
    git clone https://github.com/as679/maas_ilopower.git
    cp -r maas_ilopower/provisioningserver/* /usr/lib/python3/dist-packages/provisioningserver/
    cd /usr/lib/python3/dist-packages/provisioningserver/power/
    patch < /opt/maas_ilopower/power.diff
    cd /usr/lib/python3/dist-packages/provisioningserver/drivers/power
    patch < /opt/maas_ilopower/drivers.diff
    cd /opt
    for i in maas-regiond maas-rackd; do service $i restart; done
