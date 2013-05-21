%define upstream_name	 BerkeleyDB
%define upstream_version 0.51

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    2

Summary:	Perl module for BerkeleyDB 2.x and greater
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/BerkeleyDB/%{upstream_name}-%{upstream_version}.tar.gz
Patch0:		BerkeleyDB-0.38-wformat.patch
BuildRequires:	db-devel
BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
BerkeleyDB is a module which allows Perl programs to make use of the
facilities provided by Berkeley DB version 2 or greater. (Note: if
you want to use version 1 of Berkeley DB with Perl you need the DB_File
module).

Berkeley DB is a C library which provides a consistent interface to a
number of database formats. BerkeleyDB provides an interface to all
four of the database types (hash, btree, queue and recno) currently
supported by Berkeley DB.

For further details see the documentation in the file BerkeleyDB.pod.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
chmod 644 Changes README
# ignore pod test failure
rm -f t/pod.t
%patch0 -p1 -b .wformat

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="%{optflags}"

%check
%{__make} test

%clean 
%{__rm} -rf %{buildroot}

%install
%{__rm} -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorarch}/BerkeleyDB*
%{perl_vendorarch}/*.pl
%{perl_vendorarch}/auto/BerkeleyDB
%{_mandir}/*/*


%changelog
* Sun May 13 2012 Crispin Boylan <crisb@mandriva.org> 0.510.0-1
+ Revision: 798652
- New release

* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.480.0-3
+ Revision: 765074
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.480.0-2
+ Revision: 763490
- rebuilt for perl-5.14.x

* Fri Jul 01 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.480.0-1
+ Revision: 688498
- new version

* Mon Apr 11 2011 Funda Wang <fwang@mandriva.org> 0.430.0-2
+ Revision: 652450
- build with db 5.1

* Sun Aug 15 2010 Jérôme Quelin <jquelin@mandriva.org> 0.430.0-1mdv2011.0
+ Revision: 569930
- update to 0.43

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 0.420.0-3mdv2011.0
+ Revision: 564361
- rebuild for perl 5.12.1

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.420.0-2mdv2011.0
+ Revision: 555684
- rebuild

* Mon Mar 15 2010 Jérôme Quelin <jquelin@mandriva.org> 0.420.0-1mdv2010.1
+ Revision: 519948
- update to 0.42

* Sat Jan 09 2010 Jérôme Quelin <jquelin@mandriva.org> 0.410.0-1mdv2010.1
+ Revision: 487929
- update to 0.41

* Fri Jan 08 2010 Jérôme Quelin <jquelin@mandriva.org> 0.400.0-1mdv2010.1
+ Revision: 487475
- update to 0.40

* Wed Dec 30 2009 Jérôme Quelin <jquelin@mandriva.org> 0.390.0-2mdv2010.1
+ Revision: 483977
- rebuild

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.390.0-1mdv2010.0
+ Revision: 406862
- rebuild using %%perl_convert_version

* Sun Jun 07 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.39-1mdv2010.0
+ Revision: 383473
- update to new version 0.39

  + Christophe Fergeau <cfergeau@mandriva.com>
    - fix -Wformat warnings

* Sun Feb 22 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.38-1mdv2009.1
+ Revision: 343866
- update to new version 0.38

* Thu Feb 19 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.37-1mdv2009.1
+ Revision: 342831
- new version

* Mon Dec 15 2008 Oden Eriksson <oeriksson@mandriva.com> 0.36-2mdv2009.1
+ Revision: 314549
- rebuilt against db4.7

* Sat Oct 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.36-1mdv2009.1
+ Revision: 292029
- update to new version 0.36

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 0.34-2mdv2009.0
+ Revision: 265338
- rebuild early 2009.0 package (before pixel changes)

* Tue Apr 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.34-1mdv2009.0
+ Revision: 193745
- update to new version 0.34

* Tue Jan 22 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.33-1mdv2008.1
+ Revision: 156850
- new version

* Mon Jan 14 2008 Thierry Vignaud <tv@mandriva.org> 0.32-3mdv2008.1
+ Revision: 151851
- rebuild

* Sun Dec 23 2007 Oden Eriksson <oeriksson@mandriva.com> 0.32-2mdv2008.1
+ Revision: 137249
- rebuilt against bdb 4.6.x

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Jul 16 2007 Olivier Thauvin <nanardon@mandriva.org> 0.32-1mdv2008.0
+ Revision: 52437
- 0.32

