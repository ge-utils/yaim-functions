# glite-yaim-ge-utils v4.5.0

## Release notes 
 * Introduces an updated blah.config configuration for Grid Engine where GE environment variables are automatically loaded by blahd daemons. Yaim reconfiguration is mandatory.
 
 * In compliance with blah.config releases for other LRMS releases, it also introduces a different path for the blah job registry. Therefore, before reconfigure with yaim, please perform the following actions:
 
   1) Stop all gLite services

      /etc/init.d/gLite stop
 
   2) Copy the present blah registry to the new location making sure that all the permissions are correct
   
      mkdir /var/blah (if it doesn't exist)
      chown tomcat:tomcat /var/blah
      chmod 771 /var/blah
      cp -rp /var/tmp/cream_tomcat_registry.db /var/blah/user_blah_job_registry.bjr

   3) Reconfigure the node with yaim
   
      /opt/glite/yaim/bin/yaim -c -s site-info.def -n creamCE -n SGE_utils

 * Failure to complete the previous steps will result in the lost of all existing jobs. 

### New Features
 * None.

### Fixed Issues
 * Load of GE environment variables in blah.config (GGUS #102418).

### Available packages:
 * Scientific Linux 5: http://download.opensuse.org/repositories/home:/aloga:/ge-utils/sl5/noarch/glite-yaim-ge-utils-4.5.0-2.1.noarch.rpm 
 * Scientific Linux 6: http://download.opensuse.org/repositories/home:/aloga:/ge-utils/sl6/noarch/glite-yaim-ge-utils-4.5.0-2.1.noarch.rpm
