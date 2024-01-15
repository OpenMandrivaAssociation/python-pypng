%global module pypng

Summary:	Pure Python library for PNG image encoding/decoding
Name:		python-pypng
Version:	0.20220715.0
Release:	2
Source0:	https://pypi.org/packages/source/p/%{module}/%{module}-%{version}.tar.gz
URL:		https://pypi.org/project/pypng/
License:	MIT
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(setuptools)
BuildArch:	noarch

%description
PNG module for Python. PyPNG is written entirely in Python.

%files
%license LICENCE
%doc README.md
%{_bindir}/*
%{py_puresitedir}/png.py
%{py_puresitedir}/%{module}-*.*-info
%{py_puresitedir}/__pycache__/png*

#----------------------------------------------------------------------

%prep
%autosetup -p1 -n pypng-%{version}

%build
%py_build

#find %{buildroot} -name '__pycache__' -type d -exec rm -fr '{}' \;

%install
%py_install

