#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests

%define module	zope.i18nmessageid
Summary:	Message Identifiers for internationalization
Summary(pl.UTF-8):	Identyfikatory komunikatów do lokalizacji
Name:		python3-%{module}
Version:	7.0
Release:	1
License:	ZPL v2.1
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/z/zope.i18nmessageid/zope_i18nmessageid-%{version}.tar.gz
# Source0-md5:	e69426b19e72b06aa6c0e8c683fb9525
URL:		https://www.zope.dev/
BuildRequires:	python3 >= 1:3.8
BuildRequires:	python3-devel >= 1:3.8
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-coverage
BuildRequires:	python3-zope.testrunner
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	python3-sphinx_rtd_theme >= 1
BuildRequires:	sphinx-pdg-3
%endif
Requires:	python3-modules >= 1:3.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Message Identifiers for internationalization.

%description -l pl.UTF-8
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
%setup -q -n zope_i18nmessageid-%{version}

%build
%py3_build

%if %{with tests}
PYTHONPATH=$(echo $(pwd)/build-3/lib.*) \
zope-testrunner-3 --test-path=src
%endif

%if %{with doc}
PYTHONPATH=$(pwd)/src \
%{__make} -C docs html \
	SPHINXBUILD=sphinx-build-3
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%{__rm} $RPM_BUILD_ROOT%{py3_sitedir}/zope/i18nmessageid/*.[ch]
%{__rm} $RPM_BUILD_ROOT%{py3_sitedir}/zope/i18nmessageid/tests.*
%{__rm} $RPM_BUILD_ROOT%{py3_sitedir}/zope/i18nmessageid/__pycache__/tests.*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.rst COPYRIGHT.txt LICENSE.txt README.rst
%dir %{py3_sitedir}/zope/i18nmessageid
%{py3_sitedir}/zope/i18nmessageid/*.py
%{py3_sitedir}/zope/i18nmessageid/__pycache__
%attr(755,root,root) %{py3_sitedir}/zope/i18nmessageid/_zope_i18nmessageid_message.cpython-*.so
%{py3_sitedir}/zope.i18nmessageid-%{version}-py*.egg-info
%{py3_sitedir}/zope.i18nmessageid-%{version}-py*-nspkg.pth

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_static,*.html,*.js}
%endif
