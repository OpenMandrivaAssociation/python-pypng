Name:		python-pypng
Version:	0.20220715.0
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/p/pypng/pypng-%{version}.tar.gz
Summary:	Pure Python library for PNG image encoding/decoding
URL:		https://pypi.org/project/pypng/
License:	MIT
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(setuptools)
BuildArch:	noarch

%description
PNG module for Python. PyPNG is written entirely in Python.

%prep
%autosetup -p1 -n pypng-%{version}

%build
%py_build

%install
%py_install

#find %{buildroot} -name '__pycache__' -type d -exec rm -fr '{}' \;

%files
%license LICENCE
%doc README.md
%{_bindir}/*
%{py_puresitedir}/png.py
%{py_puresitedir}/pypng-*.*-info
%{py_puresitedir}/__pycache__/png*
