%define module	BerkeleyDB
%define name	perl-%{module}
%define version	0.31
%define release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Perl module for BerkeleyDB 2.x and greater
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/BerkeleyDB/%{module}-%{version}.tar.bz2
BuildRequires:	db4-devel
BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

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
%setup -q -n %{module}-%{version}
chmod 644 Changes README

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
%{perl_vendorarch}/auto/BerkeleyDB
%{_mandir}/*/*



