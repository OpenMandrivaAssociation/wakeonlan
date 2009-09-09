
%define name	wakeonlan
%define version	0.41
%define rel	3

Summary:	Wake-on-LAN magic packet sender
Name:		%{name}
Version:	%{version}
Release:	%mkrel %rel
Source:		http://gsd.di.uminho.pt/jpo/software/wakeonlan/downloads/%{name}-%{version}.tar.bz2
License:	Artistic
URL:		http://gsd.di.uminho.pt/jpo/software/wakeonlan/
Group:		Networking/Remote access
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildArch:	noarch
%description
Wakeonlan is a Perl script that sends 'magic packets' to
wake-on-LAN enabled ethernet adapters and motherboards, in
order to switch on remote computers.

%prep
%setup -q

%install
rm -rf %{buildroot}
%__install -D -m755 wakeonlan %{buildroot}%{_bindir}/wakeonlan

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc examples Changes README
%{_bindir}/wakeonlan
