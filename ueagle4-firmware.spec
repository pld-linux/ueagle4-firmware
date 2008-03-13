Summary:	The firmware for eagle4 (SAGEM f@st 800) USB ADSL modem
Summary(pl.UTF-8):	Firmware dla modemów ADSL eagle4 (SAGEM f@st 800) USB
Name:		ueagle4-firmware
Version:	1.0
Release:	1
License:	distributable
Group:		Libraries
Source0:	http://download.gna.org/ueagleatm/ikanos/ueagle4-data-%{version}.tar.gz
# Source0-md5:	7b6b8b1dfe5faaab407c8e52638fa72b
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		hotplugfwdir	/lib/firmware

%description
The firmware for eagle4 (SAGEM f@st 800) USB ADSL modem.

%description -l pl.UTF-8
Firmware dla modemów ADSL eagle4 (SAGEM f@ast 800) USB.

%prep
%setup -q -n ueagle4-data-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{hotplugfwdir}/ueagle-atm

install *.bin* $RPM_BUILD_ROOT%{hotplugfwdir}/ueagle-atm
install *.fw $RPM_BUILD_ROOT%{hotplugfwdir}/ueagle-atm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Ikanos_license.txt
/lib/firmware/ueagle-atm
