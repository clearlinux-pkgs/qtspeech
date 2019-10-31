#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : qtspeech
Version  : 5.13.2
Release  : 14
URL      : https://download.qt.io/official_releases/qt/5.13/5.13.2/submodules/qtspeech-everywhere-src-5.13.2.tar.xz
Source0  : https://download.qt.io/official_releases/qt/5.13/5.13.2/submodules/qtspeech-everywhere-src-5.13.2.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.3 GPL-2.0 LGPL-3.0
Requires: qtspeech-lib = %{version}-%{release}
Requires: qtspeech-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-qmake
BuildRequires : pkgconfig(Qt5Core)
BuildRequires : pkgconfig(Qt5Multimedia)
BuildRequires : pkgconfig(Qt5Test)
BuildRequires : pkgconfig(Qt5Widgets)

%description
No detailed description available

%package dev
Summary: dev components for the qtspeech package.
Group: Development
Requires: qtspeech-lib = %{version}-%{release}
Provides: qtspeech-devel = %{version}-%{release}
Requires: qtspeech = %{version}-%{release}

%description dev
dev components for the qtspeech package.


%package lib
Summary: lib components for the qtspeech package.
Group: Libraries
Requires: qtspeech-license = %{version}-%{release}

%description lib
lib components for the qtspeech package.


%package license
Summary: license components for the qtspeech package.
Group: Default

%description license
license components for the qtspeech package.


%prep
%setup -q -n qtspeech-everywhere-src-5.13.2
cd %{_builddir}/qtspeech-everywhere-src-5.13.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export GCC_IGNORE_WERROR=1
%qmake QMAKE_CFLAGS+=-fno-lto QMAKE_CXXFLAGS+=-fno-lto
test -r config.log && cat config.log
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1572503625
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qtspeech
cp %{_builddir}/qtspeech-everywhere-src-5.13.2/LICENSE.FDL %{buildroot}/usr/share/package-licenses/qtspeech/61907422fefcd2313a9b570c31d203a6dbebd333
cp %{_builddir}/qtspeech-everywhere-src-5.13.2/LICENSE.GPLv2 %{buildroot}/usr/share/package-licenses/qtspeech/78287b08861c4e3c6393a7873c08bc3b8005d02c
cp %{_builddir}/qtspeech-everywhere-src-5.13.2/LICENSE.LGPLv3 %{buildroot}/usr/share/package-licenses/qtspeech/d8c5ba35d57eceb2e56ace166048cb901a2d12ed
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/qt5/QtTextToSpeech/5.13.2/QtTextToSpeech/private/qtexttospeech_p.h
/usr/include/qt5/QtTextToSpeech/5.13.2/QtTextToSpeech/private/qvoice_p.h
/usr/include/qt5/QtTextToSpeech/QTextToSpeech
/usr/include/qt5/QtTextToSpeech/QTextToSpeechEngine
/usr/include/qt5/QtTextToSpeech/QTextToSpeechPlugin
/usr/include/qt5/QtTextToSpeech/QVoice
/usr/include/qt5/QtTextToSpeech/QtTextToSpeech
/usr/include/qt5/QtTextToSpeech/QtTextToSpeechDepends
/usr/include/qt5/QtTextToSpeech/QtTextToSpeechVersion
/usr/include/qt5/QtTextToSpeech/qtexttospeech.h
/usr/include/qt5/QtTextToSpeech/qtexttospeech_global.h
/usr/include/qt5/QtTextToSpeech/qtexttospeechengine.h
/usr/include/qt5/QtTextToSpeech/qtexttospeechplugin.h
/usr/include/qt5/QtTextToSpeech/qttexttospeechversion.h
/usr/include/qt5/QtTextToSpeech/qvoice.h
/usr/lib64/cmake/Qt5TextToSpeech/Qt5TextToSpeechConfig.cmake
/usr/lib64/cmake/Qt5TextToSpeech/Qt5TextToSpeechConfigVersion.cmake
/usr/lib64/libQt5TextToSpeech.prl
/usr/lib64/libQt5TextToSpeech.so
/usr/lib64/pkgconfig/Qt5TextToSpeech.pc
/usr/lib64/qt5/mkspecs/modules/qt_lib_texttospeech.pri
/usr/lib64/qt5/mkspecs/modules/qt_lib_texttospeech_private.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libQt5TextToSpeech.so.5
/usr/lib64/libQt5TextToSpeech.so.5.13
/usr/lib64/libQt5TextToSpeech.so.5.13.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qtspeech/61907422fefcd2313a9b570c31d203a6dbebd333
/usr/share/package-licenses/qtspeech/78287b08861c4e3c6393a7873c08bc3b8005d02c
/usr/share/package-licenses/qtspeech/d8c5ba35d57eceb2e56ace166048cb901a2d12ed
