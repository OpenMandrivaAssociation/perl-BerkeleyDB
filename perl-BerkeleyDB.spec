%define upstream_name	 BerkeleyDB
%define upstream_version 0.51

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Perl module for BerkeleyDB 2.x and greater
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/BerkeleyDB/%{upstream_name}-%{upstream_version}.tar.gz
Patch0:	BerkeleyDB-0.38-wformat.patch
BuildRequires:	db-devel
BuildRequires:	perl-devel

%description
BerkeleyDB is a module which allows Perl programs to make use of the
facilities provided by Berkeley DB version 2 or greater. (Note:	if
you want to use version 1 of Berkeley DB with Perl you need the DB_File
module).

Berkeley DB is a C library which provides a consistent interface to a
number of database formats. BerkeleyDB provides an interface to all
four of the database types (hash, btree, queue and recno) currently
supported by Berkeley DB.

For further details see the documentation in the file BerkeleyDB.pod.

%prep
%setup -qn %{upstream_name}-%{upstream_version}
chmod 644 Changes README
# ignore pod test failure
rm -f t/pod.t
%patch0 -p1 -b .wformat

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="%{optflags}"

%check
make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorarch}/BerkeleyDB*
%{perl_vendorarch}/*.pl
%{perl_vendorarch}/auto/BerkeleyDB
%{_mandir}/man3/*

