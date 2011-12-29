Name:           perl-Unicode-String
Version:        2.09
Release:        12%{?dist}

Summary:        Perl modules to handle various Unicode issues

Group:          Development/Libraries
# in CharName.pm is mentioned use of Unicode table, but fonts are not used
# so here can't be UCD license
# in String.xs is mentioned "same terms as Perl itself" which is this
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Unicode-String/
Source0:        http://www.cpan.org/authors/id/G/GA/GAAS/Unicode-String-2.09.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  %{_bindir}/iconv
# not detected by auto provide scripts:
Requires:       perl(MIME::Base64)
BuildRequires:  perl(ExtUtils::MakeMaker), perl(MIME::Base64)

%description
%{summary}.


%prep
%setup -q -n Unicode-String-%{version}
iconv -f ISO_8859-1 -t UTF-8 -o README.new README &&
mv README.new README

%build
CFLAGS="$RPM_OPT_FLAGS" %{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags} OPTIMIZE="$RPM_OPT_FLAGS"


%install
rm -rf $RPM_BUILD_ROOT
make install \
  DESTDIR=$RPM_BUILD_ROOT \
  INSTALLARCHLIB=$RPM_BUILD_ROOT%{perl_archlib}
find $RPM_BUILD_ROOT -type f \( -name perllocal.pod -o -name .packlist \
  -o \( -name '*.bs' -empty \) \) -exec rm {} ';'
find $RPM_BUILD_ROOT -depth -type d -empty -exec rmdir {} ';'
chmod -R u+w $RPM_BUILD_ROOT/*


%check
make test


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorarch}/auto/Unicode
%{perl_vendorarch}/Unicode
%{_mandir}/man3/*.3*


%changelog
* Wed Feb 17 2010 Marcela Mašláňová <mmaslano@redhat.com> - 2.09-12
- fix license
- better buildroot
- no need to define perl_vendorarch
- Related: rhbz#543948

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.09-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.09-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jun 05 2008 Aurelien Bompard <abompard@fedoraproject.org> 2.09-9
- fix build

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.09-8
- Rebuild for perl 5.10 (again)

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.09-7
- Autorebuild for GCC 4.3

* Mon Jan 28 2008 Tom "spot" Callaway <tcallawa@redhat.com> 2.09-6
- rebuild for new perl

* Thu Sep 27 2007 Aurelien Bompard <abompard@fedoraproject.org> 2.09-5
- fix license tag again (thanks Tom)

* Sun Aug 26 2007 Aurelien Bompard <abompard@fedoraproject.org> 2.09-4
- fix license tag (like perl itself)

* Mon Aug 13 2007 Aurelien Bompard <abompard@fedoraproject.org> 2.09-3
- BR: perl-devel

* Wed Aug 30 2006 Aurelien Bompard <abompard@fedoraproject.org> 2.09-2
- rebuild

* Tue Feb 21 2006 Aurelien Bompard <gauret[AT]free.fr> 2.09-1
- version 2.09

* Tue Feb 21 2006 Aurelien Bompard <gauret[AT]free.fr> 2.07-6
- rebuild for FC5

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Mon Feb  2 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:2.07-0.fdr.4
- Reduce directory ownership bloat.

* Sat Oct 11 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:2.07-0.fdr.3
- Install into vendor dirs.
- Spec cleanup.

* Mon Jul  7 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:2.07-0.fdr.2
- Regenerate %%install section with cpanflute2.

* Wed May  7 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:2.07-0.fdr.1
- Update to 2.07 and to current Fedora guidelines.

* Sun Mar  2 2003 Ville Skyttä <ville.skytta at iki.fi> - 2.06-1.fedora.1
- First Fedora release.
