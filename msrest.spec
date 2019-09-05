#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : msrest
Version  : 0.6.10
Release  : 13
URL      : https://files.pythonhosted.org/packages/08/5d/e22f815bc27ae7f9ae9eb22c0cd35f103ac481aa7d0cf644b7ea10f368f3/msrest-0.6.10.tar.gz
Source0  : https://files.pythonhosted.org/packages/08/5d/e22f815bc27ae7f9ae9eb22c0cd35f103ac481aa7d0cf644b7ea10f368f3/msrest-0.6.10.tar.gz
Summary  : AutoRest swagger generator Python client runtime.
Group    : Development/Tools
License  : MIT
Requires: msrest-python = %{version}-%{release}
Requires: msrest-python3 = %{version}-%{release}
Requires: aiohttp
Requires: certifi
Requires: enum34
Requires: isodate
Requires: requests-oauthlib
Requires: typing
BuildRequires : aiohttp
BuildRequires : buildreq-distutils3
BuildRequires : certifi
BuildRequires : enum34
BuildRequires : isodate
BuildRequires : requests-oauthlib
BuildRequires : typing

%description
AutoRest: Python Client Runtime
===============================
.. image:: https://travis-ci.org/Azure/msrest-for-python.svg?branch=master
:target: https://travis-ci.org/Azure/msrest-for-python

%package python
Summary: python components for the msrest package.
Group: Default
Requires: msrest-python3 = %{version}-%{release}

%description python
python components for the msrest package.


%package python3
Summary: python3 components for the msrest package.
Group: Default
Requires: python3-core

%description python3
python3 components for the msrest package.


%prep
%setup -q -n msrest-0.6.10

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1567647754
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
