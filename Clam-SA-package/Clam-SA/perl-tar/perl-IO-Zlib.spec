Summary: IO-Zlib Perl module
Name: perl-IO-Zlib
Version: 1.04
Release: 1
Packager: mailscanner@ecs.soton.ac.uk
License: GPL or Artistic
Group: Development/Libraries
URL: http://search.cpan.org/dist/IO-Zlib/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
#BuildRequires: perl >= 0:5.00503
Source0: IO-Zlib-1.04.tar.gz

%description
IO-Zlib Perl module

%description
IO-Zlib Perl module
%prep
%setup -q -n IO-Zlib-%{version} 1

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
	grep -v "\.packlist" > IO-Zlib-%{version}-filelist
if [ "$(cat IO-Zlib-%{version}-filelist)X" = "X" ] ; then
    echo "ERROR: EMPTY FILE LIST"
    exit 1
fi

%files -f IO-Zlib-%{version}-filelist
%defattr(-,root,root)

%changelog
* Fri Mar 14 2008 Julian Field <mailscanner@ecs.soton.ac.uk>
- Specfile autogenerated
