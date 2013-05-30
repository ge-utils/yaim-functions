%define topdir %(pwd)/rpmbuild
%define _topdir %{topdir} 
Summary: glite-yaim-sge-utils module configure SGE utils. 
Name: glite-yaim-sge-utils
Version: 4.4.0
Release: 1.%{?dist}
BuildArch: noarch
License: Apache Software License
Group: System/Configuration
Source: %{name}.src.tgz
Prefix: /opt/glite
BuildRoot: %{_tmppath}/%{name}-%{version}-build
Vendor: CREAM GE utils <ge-support@listas.cesga.es>
Packager: Gonçalo Borges <goncalo@lip.pt> 

%description
This package contains the yaim functions necessary to configure SGE utils.

%prep

%setup -c

%build
make install prefix=%{buildroot}%{prefix}

%files
%defattr(0644,root,root)
%{prefix}/yaim/functions/*
%{prefix}/yaim/defaults/*
%{prefix}/yaim/etc/versions/%{name}
%config(noreplace) %{prefix}/yaim/node-info.d/glite*
%{prefix}/yaim/examples/siteinfo/services/glite-* 
%{prefix}/share/man/man1/yaim-sge-utils.1
%doc LICENSE

%clean
rm -rf %{buildroot}
