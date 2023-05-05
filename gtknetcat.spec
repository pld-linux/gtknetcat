Summary:	GUI frontend for the old NIX command nc (netcat)
Summary(pl.UTF-8):	Graficzny interfejs do starego uniksowego polecenia nc (netcat)
Name:		gtknetcat
Version:	0.1
Release:	1
License:	GPL v2+
Group:		X11/Applications/Networking
Source0:	https://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.gz
# Source0-md5:	de545d2bce7878f0751e2cda3d2a4bce
URL:		http://www.lxde.org/
BuildRequires:	gettext-tools
BuildRequires:	intltool >= 0.21
BuildRequires:	python >= 2.2
BuildRequires:	sed >= 4.0
Requires:	python-pygtk >= 2:2.0
Requires:	python-pygtk-glade >= 2:2.0
Requires:	python-pygtk-gtk >= 2:2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# nothing to place there
%define		_enable_debug_packages	0

%description
GtkNetCat is a GUI frontend for the old UNIX command nc (netcat). This
tool can be used to transfer files to another computer via direct
wired connection.

%description -l pl.UTF-8
GtkNetCat to graficzny interfejs do starego uniksowego polecenia nc
(netcat). Można go użyć do przesyłania plików na inny komputer poprzez
połączenie sieciowe.

%prep
%setup -q

%{__sed} -i -e '1s,/usr/bin/env python,%{__python},' \
	src/gtknetcat.{in,py}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py_postclean

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/gtknetcat
%attr(755,root,root) %{_libexecdir}/gtknetcat.py
%{py_sitedir}/gtknetcat
%{_datadir}/gtknetcat
%{_desktopdir}/gtknetcat.desktop
