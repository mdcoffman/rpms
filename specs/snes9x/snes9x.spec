# $Id$
# Authority: matthias

#define prever -WIP1

Summary: Portable, freeware Super Nintendo Entertainment System (TM) emulator
Name: snes9x
Version: 1.43
Release: 1
License: Other
Group: Applications/Emulators
URL: http://www.snes9x.com/
Source: http://www.lysator.liu.se/snes9x/%{version}%{?prever}/snes9x-%{version}%{?prever}-src.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: XFree86-devel, gcc-c++, zlib-devel, libpng-devel
%ifarch %{ix86} x86_64
BuildRequires: nasm
%endif

%description
Snes9x is a portable, freeware Super Nintendo Entertainment System (SNES)
emulator. It basically allows you to play most games designed for the SNES
and Super Famicom Nintendo game systems on your PC or Workstation.

Snes9x is the result of well over six years worth of part-time hacking,
coding, recoding, debugging, etc. Snes9x is coded in C++, with three assembler
CPU emulation cores on the i386 Linux, DOS and Windows ports.


%prep
%setup -n %{name}-%{version}%{?prever:-dev}-src


%build
pushd snes9x
%configure
# Replace OPTIMISE here, it's the best I've found...
%{__perl} -pi.orig -e 's|^OPTIMISE.*|OPTIMISE = %{optflags}|g' Makefile
%{__make} %{?_smp_mflags}
popd


%install
%{__rm} -rf %{buildroot}
%{__install} -D -m 0755 snes9x/snes9x %{buildroot}%{_bindir}/snes9x


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc faqs.txt license.txt readme.txt readme.unix
%doc snes9x_default_config.cfg
%{_bindir}/snes9x


%changelog
* Sun Apr 17 2005 Matthias Saou <http://freshrpms.net/> 1.43-1
- Update to 1.43 final (was WIP1).

* Sat Dec 18 2004 Matthias Saou <http://freshrpms.net/> 1.43-0
- Initial RPM release.

