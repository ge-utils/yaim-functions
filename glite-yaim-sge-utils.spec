%define topdir %(pwd)/rpmbuild
%define _topdir %{topdir} 
Summary: glite-yaim-sge-utils module configures the SGE utils. 
Name: glite-yaim-sge-utils
Version: x  
Vendor: EGEE
Release: x  
License: EGEE
Group: EGEE
Source: %{name}.src.tgz
BuildArch: noarch
Prefix: /opt/glite
Requires: glite-yaim-core
BuildRoot: %{_tmppath}/%{name}-%{version}-build
Packager: EGEE

%description
This package contains the yaim functions necessary to configure the SGE utils.

%prep

%setup -c

%build
make install prefix=%{buildroot}%{prefix}

%files
%defattr(-,root,root)
%{prefix}/yaim/functions/config_*
%{prefix}/yaim/node-info.d/glite-*
%config(noreplace) %{prefix}/yaim/services/glite-*
%doc LICENSE


%clean
rm -rf %{buildroot}

