%include	/usr/lib/rpm/macros.php
%define		_class		Math
%define		_subclass	Histogram
%define		_status		beta

%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_class}_%{_subclass} - Classes to calculate histogram distributions
Summary(pl):	%{_class}_%{_subclass} - klasa licz±ca rozk³ad histogramu
Name:		php-pear-%{_pearname}
Version:	0.9.0
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
# Source0-md5:	7735ea1665adbbf4b759e5e212a0b447
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Classes to calculate histogram distributions and associated
statistics. Supports simple and cummulative histograms. You can
generate regular (2D) histograms, 3D, or 4D histograms. Data must not
have nulls.

This class has in PEAR status: %{_status}.

%description -l pl
Klasy do obliczania rozk³adu histogramów oraz statystyk asocjacyjnych.
Wspiera proste oraz kumulacyjne histogramy. Mo¿na generowaæ regularne
histogramy (2D), 3D oraz 4D. Dane nie mog± zawieraæ zer.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php	$RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/{examples/*,README*}
%{php_pear_dir}/%{_class}/*.php
