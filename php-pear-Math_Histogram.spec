%include	/usr/lib/rpm/macros.php
%define		_class		Math
%define		_subclass	Histogram
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_class}_%{_subclass} - Classes to calculate histogram distributions
Summary(pl):	%{_class}_%{_subclass} - klasa licz±ca rozk³ad histogramu
Name:		php-pear-%{_pearname}
Version:	0.9.0
Release:	4
License:	PHP 2.02
Group:		Development/Languages/PHP
# Source0-md5:	7735ea1665adbbf4b759e5e212a0b447
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/package/Math_Histogram/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-pear-Math_Stats
BuildArch:	noarch
Requires:	php-common >= 3:4.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Classes to calculate histogram distributions and associated
statistics. Supports simple and cummulative histograms. You can
generate regular (2D) histograms, 3D, or 4D histograms. Data must not
have nulls.

In PEAR status of this package is: %{_status}.

%description -l pl
Klasy do obliczania rozk³adu histogramów oraz statystyk asocjacyjnych.
Wspiera proste oraz kumulacyjne histogramy. Mo¿na generowaæ regularne
histogramy (2D), 3D oraz 4D. Dane nie mog± zawieraæ zer.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup
install -d docs/%{_pearname}/data
mv ./%{php_pear_dir}/%{_class}/examples docs/%{_pearname}
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
%{php_pear_dir}/%{_class}/*.php
