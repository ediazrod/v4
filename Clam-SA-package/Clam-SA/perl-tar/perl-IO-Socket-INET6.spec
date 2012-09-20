Summary: IO-Socket-INET6 Perl module
Name: perl-IO-Socket-INET6
Version: 2.57
Release: 1
Packager: mailscanner@ecs.soton.ac.uk
License: GPL or Artistic
Group: Development/Libraries
URL: http://search.cpan.org/dist/IO-Socket-INET6/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
#BuildRequires: perl >= 0:5.00503
Source0: IO-Socket-INET6-2.57.tar.gz

%description
IO-Socket-INET6 Perl module

%description
IO-Socket-INET6 Perl module
%prep
%setup -q -n IO-Socket-INET6-%{version} 1

%build
CFLAGS="$RPM_OPT_FLAGS" perl Makefile.PL PREFIX=$RPM_BUILD_ROOT/usr 
make
make test

%clean
rm -rf $RPM_BUILD_ROOT
%install

rm -rf $RPM_BUILD_ROOT
eval `perl '-V:installarchlib'`
mkdir -p $RPM_BUILD_ROOT/$installarchlib
make install

[ -x /usr/lib/rpm/brp-compress ] && /usr/lib/rpm/brp-compress

find $RPM_BUILD_ROOT/usr -type f -print | \
	sed "s@^$RPM_BUILD_ROOT@@g" | \
	grep -v perllocal.pod | \
	grep -v "\.packlist" > IO-Socket-INET6-%{version}-filelist
if [ "$(cat IO-Socket-INET6-%{version}-filelist)X" = "X" ] ; then
    echo "ERROR: EMPTY FILE LIST"
    exit 1
fi

%files -f IO-Socket-INET6-%{version}-filelist
%defattr(-,root,root)

%changelog
* Fri Mar 14 2008 Julian Field <mailscanner@ecs.soton.ac.uk>
- Specfile autogenerated
