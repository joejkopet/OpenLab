#Create SELinux rule for OpenLab:

grep openlab /var/log/audit/audit.log | audit2allow -M openlab
semodule -i openlab.pp