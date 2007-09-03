%define topdir %(pwd)/rpmbuild
%define _topdir %{topdir} 
Summary: glite-yaim-sge-utils module configure SGE utils. 
Name: glite-yaim-sge-utils
Version: ame:
Vendor: EGEE
Release: ame:
License: EGEE
Group: EGEE
Source: %{name}.src.tgz
BuildArch: noarch
Prefix: /opt/glite
Requires: glite-yaim-core
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
%{prefix}/yaim/node-info.d/glite-*
%{prefix}/yaim/examples/siteinfo/services/glite-* 
%doc LICENSE


%clean
rm -rf %{buildroot}

