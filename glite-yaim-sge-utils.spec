%define topdir %(pwd)/rpmbuild
%define _topdir %{topdir} 
Summary: glite-yaim-sge-utils module configure SGE utils. 
Name: glite-yaim-sge-utils
Version: x
Vendor: EGEE
Release: x
License: EGEE
Group: EGEE
Source: %{name}.src.tgz
BuildArch: noarch
Prefix: /opt/glite
Requires: glite-info-generic >= 2.0.2-2
Requires: glite-yaim-core >= 4.0.1-1
Requires: glite-yaim-lcg-ce >= 4.0.1-1
BuildRoot: %{_tmppath}/%{name}-%{version}-build
Packager: EGEE

%description
This package contains the yaim functions necessary to configure SGE utils.

%prep

%setup -c

%build
make install prefix=%{buildroot}%{prefix}

%files
%defattr(0644,root,root)
%{prefix}/yaim/functions/config_*
%config(noreplace) %{prefix}/yaim/node-info.d/glite*
%{prefix}/yaim/node-info.d/glite-*
%{prefix}/yaim/examples/siteinfo/services/glite-* 
/usr/share/man/man1/yaim-sge-utils.1
%doc LICENSE

%clean
rm -rf %{buildroot}

