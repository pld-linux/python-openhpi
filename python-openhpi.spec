Summary:	Python binding for OpenHPI
Summary(pl.UTF-8):	Wiązanie Pythona do OpenHPI
Name:		python-openhpi
Version:	1.1
Release:	1
License:	BSD
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/openhpi/py-openhpi-%{version}.tar.gz
# Source0-md5:	37cf9b0f2b22fea67c54cb6b638a1b27
URL:		http://openhpi.sourceforge.net/
BuildRequires:	glib2-devel >= 1:2.2.0
BuildRequires:	openhpi-devel >= 2.10.0
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	swig-python >= 1.3.29
%pyrequires_eq	python-libs
Requires:	openhpi >= 2.10.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python binding for OpenHPI.

%description -l pl.UTF-8
Wiązanie Pythona do OpenHPI.

%prep
%setup -q -n py-openhpi-%{version}

%build
CFLAGS="%{rpmcflags}" \
%{__python} setup.py build
	
%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/_openhpi.so
%{py_sitedir}/openhpi.py[co]
%{py_sitedir}/py_openhpi-*.egg-info
