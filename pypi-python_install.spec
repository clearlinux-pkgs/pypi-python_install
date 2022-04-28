#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-python_install
Version  : 0.0.3
Release  : 5
URL      : https://files.pythonhosted.org/packages/11/7e/030d96eab01667d68a11be65ce01a62a9e4b0c3003d202d99a75d93fe824/python-install-0.0.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/11/7e/030d96eab01667d68a11be65ce01a62a9e4b0c3003d202d99a75d93fe824/python-install-0.0.3.tar.gz
Summary  : UNKNOWN
Group    : Development/Tools
License  : MIT
Requires: pypi-python_install-license = %{version}-%{release}
Requires: pypi-python_install-python = %{version}-%{release}
Requires: pypi-python_install-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(setuptools)
BuildRequires : pypi(wheel)

%description
A simple, correct PEP427 wheel installer.
        
        ```sh
        $ python -m install -h

%package license
Summary: license components for the pypi-python_install package.
Group: Default

%description license
license components for the pypi-python_install package.


%package python
Summary: python components for the pypi-python_install package.
Group: Default
Requires: pypi-python_install-python3 = %{version}-%{release}

%description python
python components for the pypi-python_install package.


%package python3
Summary: python3 components for the pypi-python_install package.
Group: Default
Requires: python3-core
Provides: pypi(python_install)

%description python3
python3 components for the pypi-python_install package.


%prep
%setup -q -n python-install-0.0.3
cd %{_builddir}/python-install-0.0.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1651170173
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-python_install
cp %{_builddir}/python-install-0.0.3/LICENSE %{buildroot}/usr/share/package-licenses/pypi-python_install/4339a5c41946d5ce6e23a8b8c4fff00d838d40c9
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-python_install/4339a5c41946d5ce6e23a8b8c4fff00d838d40c9

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
