%define		_status		beta
%define		_pearname	Math_Histogram
Summary:	%{_pearname} - Classes to calculate histogram distributions
Summary(pl.UTF-8):	%{_pearname} - klasa licząca rozkład histogramu
Name:		php-pear-%{_pearname}
Version:	0.9.0
Release:	7
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	7735ea1665adbbf4b759e5e212a0b447
URL:		http://pear.php.net/package/Math_Histogram/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(core) >= 4.1
Requires:	php-pear
Requires:	php-pear-Math_Stats
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Classes to calculate histogram distributions and associated
statistics. Supports simple and cummulative histograms. You can
generate regular (2D) histograms, 3D, or 4D histograms. Data must not
have nulls.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Klasy do obliczania rozkładu histogramów oraz statystyk asocjacyjnych.
Wspiera proste oraz kumulacyjne histogramy. Można generować regularne
histogramy (2D), 3D oraz 4D. Dane nie mogą zawierać zer.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup
install -d docs/%{_pearname}/data
mv ./%{php_pear_dir}/Math/examples docs/%{_pearname}
mv ./%{php_pear_dir}/data/%{_pearname}/examples docs/%{_pearname}/examples/data

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Math/*.php
