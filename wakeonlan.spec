
%define name	wakeonlan
%define version	0.41
%define rel	3

Summary:	Wake-on-LAN magic packet sender
Name:		%{name}
Version:	%{version}
Release:	%mkrel %rel
Source:		http://gsd.di.uminho.pt/jpo/software/wakeonlan/downloads/%{name}-%{version}.tar.bz2
License:	Artistic
URL:		https://gsd.di.uminho.pt/jpo/software/wakeonlan/
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


%changelog
* Wed Sep 09 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.41-3mdv2010.0
+ Revision: 434699
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.41-2mdv2009.0
+ Revision: 136571
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Jun 03 2007 Anssi Hannula <anssi@mandriva.org> 0.41-2mdv2008.0
+ Revision: 34871
- annual rebuild
- Import wakeonlan



* Fri May 26 2006 Anssi Hannula <anssi@mandriva.org> 0.41-1mdv2007.0
- initial Mandriva release
