#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : qtspeech
Version  : 5.11.0
Release  : 2
URL      : http://download.qt.io/official_releases/qt/5.11/5.11.0/submodules/qtspeech-everywhere-src-5.11.0.tar.xz
Source0  : http://download.qt.io/official_releases/qt/5.11/5.11.0/submodules/qtspeech-everywhere-src-5.11.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.3 GPL-2.0 LGPL-3.0
Requires: qtspeech-lib
BuildRequires : cmake
BuildRequires : pkgconfig(Qt5Core)
BuildRequires : pkgconfig(Qt5Multimedia)
BuildRequires : pkgconfig(Qt5Test)
BuildRequires : pkgconfig(Qt5Widgets)
BuildRequires : qtbase-dev
BuildRequires : qtbase-extras

%description
No detailed description available

%package dev
Summary: dev components for the qtspeech package.
Group: Development
Requires: qtspeech-lib
Provides: qtspeech-devel

%description dev
dev components for the qtspeech package.


%package lib
Summary: lib components for the qtspeech package.
Group: Libraries

%description lib
lib components for the qtspeech package.


%prep
%setup -q -n qtspeech-everywhere-src-5.11.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
qmake QMAKE_CFLAGS="$CFLAGS" QMAKE_CXXFLAGS="$CXXFLAGS" QMAKE_LFLAGS="$LDFLAGS" \
    QMAKE_CFLAGS_RELEASE= QMAKE_CXXFLAGS_RELEASE=
test -r config.log && cat config.log
make  %{?_smp_mflags}

%install
make INSTALL_ROOT=%{buildroot} install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/qt5/QtTextToSpeech/5.11.0/QtTextToSpeech/private/qtexttospeech_p.h
/usr/include/qt5/QtTextToSpeech/5.11.0/QtTextToSpeech/private/qvoice_p.h
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
/usr/lib64/libQt5TextToSpeech.la
/usr/lib64/libQt5TextToSpeech.prl
/usr/lib64/libQt5TextToSpeech.so
/usr/lib64/pkgconfig/Qt5TextToSpeech.pc
/usr/lib64/qt5/mkspecs/modules/qt_lib_texttospeech.pri
/usr/lib64/qt5/mkspecs/modules/qt_lib_texttospeech_private.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libQt5TextToSpeech.so.5
/usr/lib64/libQt5TextToSpeech.so.5.11
/usr/lib64/libQt5TextToSpeech.so.5.11.0
