#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests (installed package required)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define module	zope.i18nmessageid
Summary:	Message Identifiers for internationalization
Summary(pl.UTF-8):	Identyfikatory komunikatów do lokalizacji
Name:		python-%{module}
# keep 5.x here for python2 support
Version:	5.1.1
Release:	2
License:	ZPL v2.1
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/z/zope.i18nmessageid/zope.i18nmessageid-%{version}.tar.gz
# Source0-md5:	96d1f677dcccd79b6917df3f4f86133e
URL:		https://www.zope.dev/
%if %{with python2}
BuildRequires:	python >= 1:2.7
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-coverage
BuildRequires:	python-six
BuildRequires:	python-zope.testing
BuildRequires:	python-zope.testrunner
%endif
%endif
%if %{with python3}
BuildRequires:	python3 >= 1:3.5
BuildRequires:	python3-devel >= 1:3.5
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-coverage
BuildRequires:	python3-six
BuildRequires:	python3-zope.testing
BuildRequires:	python3-zope.testrunner
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	sphinx-pdg
%endif
Requires:	python-modules >= 1:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Message Identifiers for internationalization.

%description -l pl.UTF-8
Identyfikatory komunikatów do lokalizacji.

%package -n python3-%{module}
Summary:	Message Identifiers for internationalization
Summary(pl.UTF-8):	Identyfikatory komunikatów do lokalizacji
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.5

%description -n python3-%{module}
Message Identifiers for internationalization.

%description -n python3-%{module} -l pl.UTF-8
Identyfikatory komunikatów do lokalizacji.

%package apidocs
Summary:	API documentation for Python zope.i18nmessageid module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona zope.i18nmessageid
Group:		Documentation

%description apidocs
API documentation for Python zope.i18nmessageid module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona zope.i18nmessageid.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%if %{with doc}
PYTHONPATH=$(pwd)/src \
%{__make} -C docs html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/zope/i18nmessageid/*.[ch]
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/zope/i18nmessageid/tests.*
%endif

%if %{with python3}
%py3_install

%{__rm} $RPM_BUILD_ROOT%{py3_sitedir}/zope/i18nmessageid/*.[ch]
%{__rm} $RPM_BUILD_ROOT%{py3_sitedir}/zope/i18nmessageid/tests.*
%{__rm} $RPM_BUILD_ROOT%{py3_sitedir}/zope/i18nmessageid/__pycache__/tests.*
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES.rst COPYRIGHT.txt LICENSE.txt README.rst
%dir %{py_sitedir}/zope/i18nmessageid
%{py_sitedir}/zope/i18nmessageid/*.py[co]
%attr(755,root,root) %{py_sitedir}/zope/i18nmessageid/_zope_i18nmessageid_message.so
%{py_sitedir}/zope.i18nmessageid-%{version}-py*.egg-info
%{py_sitedir}/zope.i18nmessageid-%{version}-py*-nspkg.pth
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc CHANGES.rst COPYRIGHT.txt LICENSE.txt README.rst
%dir %{py3_sitedir}/zope/i18nmessageid
%{py3_sitedir}/zope/i18nmessageid/*.py
%{py3_sitedir}/zope/i18nmessageid/__pycache__
%attr(755,root,root) %{py3_sitedir}/zope/i18nmessageid/_zope_i18nmessageid_message.cpython-*.so
%{py3_sitedir}/zope.i18nmessageid-%{version}-py*.egg-info
%{py3_sitedir}/zope.i18nmessageid-%{version}-py*-nspkg.pth
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_static,*.html,*.js}
%endif
