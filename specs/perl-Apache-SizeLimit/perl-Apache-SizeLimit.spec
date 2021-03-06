Name:           perl-Apache-SizeLimit
Version:        0.92
Release:        1%{?dist}
Summary:        Module to kill off Apache httpd processes if they grow too large.
License:        Apache v2.0
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Apache-SizeLimit/

Source0: http://search.cpan.org/CPAN/authors/id/P/PH/PHRED/Apache-SizeLimit-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires:  mod_perl

Requires:       mod_perl
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module allows you to kill off Apache httpd processes if they grow too
large. You can make the decision to kill a process based on its overall size,
by setting a minimum limit on shared memory, or a maximum on unshared memory.

%prep
%setup -q -n Apache-SizeLimit-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Sep 27 2010 David Hrbáč <david@hrbac.cz> 0.92-1
- Specfile autogenerated by cpanspec 1.78.
