# $Id$
# Authority: dries

Summary: Gift plugin to access the Gnutella network
Name: gift-gnutella
Version: 0.0.9.2
Release: 1
License: GPL
Group: Applications/Internet
URL: http://www.giftproject.org/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://dl.sf.net/gift/gift-gnutella-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: gift
BuildRequires: gift, gcc-c++, pkgconfig, zlib-devel

%description
giFT is a modular daemon capable of abstracting the communication between the
end user and specific filesharing protocols (peer-to-peer or otherwise). This
packages provides the plugin to access the Gnutella network.


%prep
%setup


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc README AUTHORS ChangeLog COPYING NEWS TODO
%{_libdir}/giFT/libGnutella.*
%config(noreplace) %{_datadir}/giFT/Gnutella/Gnutella.conf
%config            %{_datadir}/giFT/Gnutella/Gnutella.conf.template
%{_datadir}/giFT/Gnutella/gwebcaches
%{_datadir}/giFT/Gnutella/hostiles.txt


%changelog
* Fri Jul 16 2004 Matthias Saou <http://freshrpms.net/> 0.0.9.2-1
- Update to 0.0.9.2.
- Spec file cleanup.

* Mon Dec 29 2003 Dries Verachtert <dries@ulyssis.org> 0.0.8-1
- first packaging for Fedora Core 1

