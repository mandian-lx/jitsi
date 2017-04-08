%{?_javapackages_macros:%_javapackages_macros}

%define debug_package  %{nil}

%define commit a07c8181f07d1e5874b3cd3de76f0558a39db6f6
%define shortcommit %(c=%{commit}; echo ${c:0:7})

# http://lists.jitsi.org/pipermail/dev/2017-February/031541.html
%define subversion 5550

%define oname Jitsi
%define name %(echo %oname | tr [:upper:] [:lower:])

%ifarch %{i?86}
 %define _jvm_lib_dir %{_jvmdir}/java/jre/lib/i386
 %define _jitsi_native_lib lib/native/linux
 %define jdic_misc_arch 32
%else
 %define _jvm_lib_dir %{_jvmdir}/java/jre/lib/amd64
 %define _jitsi_native_lib lib/native/linux-64
 %define jdic_misc_arch 64
%endif

# Use galagonotification
%bcond_without galagonotification

# Don't use growl4j
%bcond_with growl4j

# Split Jitsi common bundles
%bcond_without common

# Don't build documentation
%bcond_with docs

Summary:	Multi-protocol audio/video and chat communicator written in Java
Name:		%{name}
Version:	2.10.%{subversion}
Release:	0
License:	ASL 2.0
Group:		Development/Java
Url:		https://www.jitsi.org
Source0:	https://download.jitsi.org/%{name}/src/%{name}-src-%{version}.zip

Patch0:		%{name}-2.10.5550-resources-build_xml.patch
Patch1:		%{name}-2.10.5550-remove_jingle.patch 
Patch2:		%{name}-2.10.5550-junit3.patch
Patch3:		%{name}-2.10.5550-felix-osgi-core.patch
Patch4:		%{name}-2.10.5550-galagonotification.patch
Patch5:		%{name}-2.10.5550-hid.patch
Patch6:		%{name}-2.10.5550-use_system_myspell_dict.patch
Patch7:		%{name}-2.10.5550-use_system_jars.patch

Patch100:	%{name}-2.10.5550-use_system_jar_accountinfo_bundle.patch
Patch101:	%{name}-2.10.5550-use_system_jar_chatalerter_bundle.patch
Patch102:	%{name}-2.10.5550-use_system_jar_desktoputil_bundle.patch
Patch103:	%{name}-2.10.5550-use_system_jar_dhcp_bundle.patch
Patch104:	%{name}-2.10.5550-use_system_jar_googlecontacts_bundle.patch
Patch105:	%{name}-2.10.5550-use_system_jar_icq_bundle.patch
Patch106:	%{name}-2.10.5550-use_system_jar_icq_slick_bundle.patch
Patch107:	%{name}-2.10.5550-use_system_jar_jmdns_bundle.patch
Patch108:	%{name}-2.10.5550-use_system_jar_json_simple_bundle.patch
Patch109:	%{name}-2.10.5550-use_system_jar_junit_bundle.patch
Patch110:	%{name}-2.10.5550-use_system_jar_otr_bundle.patch
Patch111:	%{name}-2.10.5550-use_system_jar_phonenumbers_bundle.patch
Patch112:	%{name}-2.10.5550-use_system_jar_smacklib_bundle.patch
Patch113:	%{name}-2.10.5550-use_system_jar_spellcheck_bundle.patch
Patch114:	%{name}-2.10.5550-use_system_jar_swing_ui_bundle.patch
Patch115:	%{name}-2.10.5550-use_system_jar_sysactivity_bundle.patch

BuildRequires:  desktop-file-utils
BuildRequires:	imagemagick
BuildRequires:	javapackages-local
BuildRequires:	ant
BuildRequires:  maven-local
BuildRequires:	cpptasks
BuildRequires:	osgi(bcpkix)
BuildRequires:	osgi(bcprov)
BuildRequires:	osgi(ch.imvs.sdes4j)
BuildRequires:	osgi(com.explodingpixels.macwidgets)
BuildRequires:	osgi(com.googlecode.json-simple)
BuildRequires:	osgi(com.googlecode.libphonenumber)
BuildRequires:	osgi(com.google.gdata.client)
BuildRequires:	osgi(com.google.gdata.client.contacts)
BuildRequires:	osgi(com.google.gdata.data.extensions)
BuildRequires:	osgi(com.google.guava)
BuildRequires:	osgi(com.google.http-client.google-http-client)
BuildRequires:	osgi(com.google.http-client.google-http-client-jackson2)
BuildRequires:	osgi(com.google.oauth-client.google-oauth-client)
BuildRequires:	osgi(com.ircclouds.irc.api)
BuildRequires:	osgi(com.sun.jna)
BuildRequires:	osgi(com.sun.jna.platform)
BuildRequires:	osgi(com.toedter.jcalendar)
BuildRequires:	osgi(com.yuvimasory.orange-extensions) 
BuildRequires:	osgi(cx.ath.matthew.hexdump)
BuildRequires:	osgi(cx.ath.matthew.unix)
BuildRequires:	osgi(dhcp4java-1.00)
BuildRequires:	osgi(dnsjava)
BuildRequires:	osgi(javax.jmdns)
BuildRequires:	osgi(jdic_misc)
BuildRequires:	osgi(joscar-client)
BuildRequires:	osgi(joscar-common)
BuildRequires:	osgi(joscar-protocol)
BuildRequires:	osgi(jsocks)
BuildRequires:	osgi(net.java.dev.laf-widget) < 5
BuildRequires:	osgi(org.apache.commons.codec)
BuildRequires:	osgi(org.apache.commons.lang3)
BuildRequires:	osgi(org.apache.felix.bundlerepository)
BuildRequires:	osgi(org.apache.felix.framework)
BuildRequires:	osgi(org.apache.felix.main)
BuildRequires:	osgi(org.apache.httpcomponents.httpclient)
BuildRequires:	osgi(org.apache.httpcomponents.httpcore)
BuildRequires:	osgi(org.apache.httpcomponents.httpmime)
BuildRequires:	osgi(org.apache.logging.log4j.1.2-api)
BuildRequires:	osgi(org.bitlet.weupnp)
BuildRequires:	osgi(org.dts.spell.jmyspell-core)
BuildRequires:	osgi(org.easymock)
BuildRequires:	osgi(org.freedesktop.dbus)
%if %{with growl4j}
BuildRequires:	osgi(org.growl4j)
%endif
BuildRequires:	osgi(org.hsqldb.hsqldb)
BuildRequires:	osgi(org.jitsi.bccontrib)
BuildRequires:	osgi(org.jitsi.dnssecjava)
BuildRequires:	osgi(org.jitsi.fmj)
BuildRequires:	osgi(org.jitsi.gpl-dependencies)
BuildRequires:	osgi(org.jitsi.ice4j)
BuildRequires:	osgi(org.jitsi.jain-sip-ri-ossonly)
BuildRequires:	osgi(org.jitsi.jmork)
BuildRequires:	osgi(org.jitsi.lgpl-dependencies)
BuildRequires:	osgi(org.jitsi.libjitsi)
BuildRequires:	osgi(org.jitsi.org.otr4j)
BuildRequires:	osgi(org.jitsi.smack)
BuildRequires:	osgi(org.jitsi.smackx)
BuildRequires:	osgi(org.jitsi.zrtp4j-light)
BuildRequires:	osgi(org.junit)
#BuildRequires:	osgi(org.objenesis)
BuildRequires:	osgi(org.opentelecoms.sdp.java-sdp-nist-bridge)
BuildRequires:	osgi(org.opentelecoms.sdp.sdp-api)
BuildRequires:	osgi(org.opentelecoms.sip.sip-api-1.2)
BuildRequires:	osgi(org.xmlpull.minimal)
BuildRequires:	osgi(org.xmpp.jnsapi)
BuildRequires:	osgi(slf4j.api)
BuildRequires:	osgi(slf4j.jdk14)
BuildRequires:	swingworker
# natives
#    galagonotification
BuildRequires:	pkgconfig(dbus-1)
#    globalshortcut
BuildRequires:	pkgconfig(x11)
#    hid
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xtst)
#    hwaddressretriever
BuildRequires:	pkgconfig(x11)
#    sysactivitynotifications
BuildRequires:	pkgconfig(gtk+-x11-2.0)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xscrnsaver)

Requires:	osgi(bcpkix)
Requires:	osgi(bcprov)
Requires:	osgi(ch.imvs.sdes4j)
Requires:	osgi(com.explodingpixels.macwidgets)
Requires:	osgi(com.googlecode.json-simple)
Requires:	osgi(com.googlecode.libphonenumber) 
Requires:	osgi(com.google.gdata.client)
Requires:	osgi(com.google.gdata.client.contacts)
Requires:	osgi(com.google.gdata.data.extensions)
Requires:	osgi(com.google.guava)
Requires:	osgi(com.google.http-client.google-http-client)
Requires:	osgi(com.google.oauth-client.google-oauth-client)
Requires:	osgi(com.ircclouds.irc.api)
Requires:	osgi(com.jcraft.jzlib)
Requires:	osgi(com.jgoodies.common)
Requires:	osgi(com.jgoodies.forms)
Requires:	osgi(com.sun.jna)
Requires:	osgi(com.sun.jna.platform)
Requires:	osgi(com.toedter.jcalendar)
Requires:	osgi(cx.ath.matthew.hexdump)
Requires:	osgi(cx.ath.matthew.unix) 
Requires:	osgi(dhcp4java-1.00)
Requires:	osgi(javax.jmdns)
Requires:	osgi(jdic_misc)
Requires:	osgi(joscar-client)
Requires:	osgi(joscar-common)
Requires:	osgi(joscar-protocol)
Requires:	osgi(jsocks)
Requires:	osgi(net.java.dev.laf-widget)
Requires:	osgi(org.apache.commons.codec)
Requires:	osgi(org.apache.commons.lang3)
Requires:	osgi(org.apache.commons.logging)
Requires:	osgi(org.apache.httpcomponents.httpclient)
Requires:	osgi(org.apache.httpcomponents.httpcore)
Requires:	osgi(org.apache.httpcomponents.httpmime)
Requires:	osgi(org.apache.log4j)
Requires:	osgi(org.bitlet.weupnp)
Requires:	osgi(org.dts.spell.jmyspell-core)
Requires:	osgi(org.freedesktop.dbus)
%if %{with growl4j}
Requires:	osgi(org.growl4j)
%endif
Requires:	osgi(org.hsqldb.hsqldb)
Requires:	osgi(org.igniterealtime.jbosh)
Requires:	osgi(org.jitsi.bccontrib)
Requires:	osgi(org.jitsi.dnssecjava)
Requires:	osgi(org.jitsi.fmj)
Requires:	osgi(org.jitsi.gpl-dependencies)
Requires:	osgi(org.jitsi.ice4j)
Requires:	osgi(org.jitsi.jain-sip-ri-ossonly)
Requires:	osgi(org.jitsi.jmork)
Requires:	osgi(org.jitsi.lgpl-dependencies)
Requires:	osgi(org.jitsi.libjitsi)
Requires:	osgi(org.jitsi.org.otr4j)
Requires:	osgi(org.jitsi.smack)
Requires:	osgi(org.jitsi.zrtp4j-light)
Requires:	osgi(org.opentelecoms.sdp.java-sdp-nist-bridge)
Requires:	osgi(org.opentelecoms.sdp.sdp-api)
Requires:	osgi(org.opentelecoms.sip.sip-api-1.2)
Requires:	osgi(org.xmlpull.minimal)
Requires:	osgi(org.xmpp.jnsapi)
Requires:	osgi(slf4j.api)
Requires:	osgi(slf4j.jdk14)

# bundle
Requires:	osgi(org.apache.commons.logging)
Requires:	osgi(org.junit)
Requires:	osgi(org.apache.logging.log4j.1.2-api)
Requires:	osgi(org.apache.felix.bundlerepository)

# common
%if %{with common}
Requires:	osgi(net.java.sip.communicator.configuration)
Requires:	osgi(net.java.sip.communicator.credentialsstorage)
Requires:	osgi(net.java.sip.communicator.impl.dns)
Requires:	osgi(net.java.sip.communicator.service.dns)
Requires:	osgi(net.java.sip.communicator.fileaccess)
Requires:	osgi(net.java.sip.communicator.packetlogging)
Requires:	osgi(net.java.sip.communicator.protocol.jabber)
Requires:	osgi(net.java.sip.communicator.service.protocol.media)
Requires:	osgi(net.java.sip.communicator.service.protocol)
Requires:	osgi(net.java.sip.communicator.plugin.reconnectplugin)
Requires:	osgi(net.java.sip.communicator.resources)
Requires:	osgi(net.java.sip.communicator.sysactivity)
Requires:	osgi(net.java.sip.communicator.service.gui)
%endif

# natives
#    galagonotification
Requires:	%{_lib}dbus-1_3
#    globalshortcut
Requires:	%{_lib}x11_6
#    hid
Requires:	%{_lib}x11_6
Requires:	%{_lib}xtst6
#    hwaddressretriever
#    sysactivitynotifications
Requires:	%{_lib}gdk-x11_2.0_0
Requires:	%{_lib}x11_6
Requires:	%{_lib}xscrnsaver1

%description
Jitsi is a free open-source audio/video and chat communicator that
supports protocols such as SIP, XMPP/Jabber, AIM/ICQ, IRC and many
other useful features.

%files
%{_bindir}/%{name}
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*so
%dir %{_jnidir}/%{name}
%{_jnidir}/%{name}/lib/
%{_jnidir}/%{name}/sc-bundles/
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*gif
%{_datadir}/%{name}/lib/
%{_datadir}/applications/%{name}*
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_iconsdir}/hicolor/*/apps/%{name}.svg
%{_datadir}/pixmaps/%{name}.xpm
%{_mandir}/man1/%{name}.1.*
%doc README.md
%doc CONTRIBUTING.md
%doc LICENSE

#----------------------------------------------------------------------------

%if %{with common}
%package common
Summary:	Common files for Jitsi and Videobridge
Group:		Development/Java

Requires:	osgi(org.igniterealtime.jbosh)
Requires:	osgi(org.xmpp.jnsapi)
Requires:	osgi(com.jcraft.jzlib)
Requires:	osgi(org.jitsi.smack)
Requires:	osgi(org.jitsi.smackx)
Requires:	osgi(org.xmlpull.minimal)

%description common
Common files for Jitsi and Videobridge.

%files common
%{_jnidir}/%{name}-common
%doc LICENSE
%endif

#----------------------------------------------------------------------------

%if %{with docs}
%package javadoc
Summary:	Javadoc for %{name}
BuildArch:	noarch

%description javadoc
API documentation for %{name}.

%files javadoc
%{_javadocdir}/%{name}
%endif

#----------------------------------------------------------------------------

%prep
%setup -q -n %{name}
# Remove all pre-build binaries
find . -type f -name "*.jar" -delete
find . -type f -name "*.class" -delete
find . -type f -name "lib*.so*" -delete
find . -type f -name "*.a" -delete
find . -type f -name "*.exe" -delete
find . -type f -name "*.tlb" -delete
find . -type f -name "*.dll" -delete
find . -type f -name "*.dylib" -delete
find . -type f -name "*.jnilib" -delete
find . -type f -name "*.zip" -delete
find . -type f -name "*.tar.bz2" -delete
find . -type f -name "*.tar.gz" -delete

# Apply all patches
%patch0  -p1 -b .orig
%patch1  -p1 -b .jingle
%patch2  -p1 -b .junit3
%patch3  -p1 -b .felix
%if %{with galagonotification}
%patch4  -p1 -b .galagonotification
%endif
%patch6  -p1 -b .hid
%patch6  -p1 -b .dict
%patch7  -p1 -b .system_jars

%patch100  -p1 -b .accountinfo
%patch101  -p1 -b .chatalerter
%patch102  -p1 -b .desktoputil
%patch103  -p1 -b .dhcp
%patch104  -p1 -b .googlecontacts
%patch105  -p1 -b .icq
%patch106  -p1 -b .icq_slick
%patch107  -p1 -b .jmdns
%patch108  -p1 -b .json
%patch109  -p1 -b .junit
%patch110  -p1 -b .otr
%patch111  -p1 -b .phonenumbers
%patch112  -p1 -b .smack
%patch113  -p1 -b .spellcheck
%patch114  -p1 -b .swing
%patch115  -p1 -b .sysactivity

%if %{without growl4j}
rm -fr src/net/java/sip/communicator/impl/growlnotification/
rm -fr lib/native/mac/GrowlFramework
%endif

# Remove os-specific
#   macosx
rm -fr src/native/macosx
#   windows
rm -fr src/native/windows

#FIXME: felix-bundlerepository requires osgi(org.apache.felix.utils.collections) but
#       org.apache.felix.utils.jar provided by felix-util packade does not export it
sed -i -e '/bundlerepository.*\.jar/d' lib/felix.client.run.properties

# launcher script
sed -e '{
                # package name
		s|_PACKAGE_NAME_|%{name}|g
		# fix jars path
		s|SCDIR=/usr/share/jitsi|SCDIR=%{_jnidir}/%{name}|
		s|$JITSI_COMMON_DIR/util.jar/launchutils.jar|$SCDIR/sc-bundles/util.jar|
		# fix lib path
		s|LIBPATH=$SCDIR/lib|LIBPATH=%{_datadir}/%{name}/lib|
		/JITSI_COMMON_DIR=/d
		# fix natives dir
		s|/usr/lib/jni|%{_jvm_lib_dir}:%{_libdir}/%{name}|g
                # fix felix path
		s|/usr/share/java/org.apache.felix.framework.jar|%{_javadir}/felix/org.apache.felix.framework.jar|
		s|/usr/share/java/org.apache.felix.main.jar|%{_javadir}/felix/org.apache.felix.main.jar|
		# fix splash path
		s|-splash:splash.gif|-splash:../../../share/jitsi/splash.gif|
		# remove unused jar from classpath
		s|:$SCDIR/sc-bundles/dnsjava.jar||
	}' resources/install/debian/jitsi.sh.tmpl \
	>  resources/install/debian/jitsi.sh

# .desktop
cp  resources/install/debian/jitsi.desktop.tmpl %{name}.desktop

# manpage (fix according to the "dpkg-debianize" target from resources/install/build.xml)
sed -e  '{ s|_PACKAGE_NAME_|%{name}|g
	   s|_APP_NAME_|%{oname}|g
         }' resources/install/debian/%{name}.1.tmpl \
	 > resources/install/debian/%{name}.1
	 
# fix manpage-not-compressed xz warning
xz resources/install/debian/%{name}.1

# fix jar-not-indexed warnings
#sed -i -e 's|<jar |<jar index="true" |g' build.xml resources/install/build.xml

# fix unzipped-zip warning
#sed -i -e 's|compress="false"|compress="true"|g' build.xml

# fix common path
sed -i -e 's|/usr/share/jitsi-common|%{_jnidir}/jitsi-common|g' resources/install/build.xml

# use only system bundles
rm -f lib/installer-exclude/*manifest.mf
	
# classpath
build-jar-repository lib/installer-exclude/ \
		ant ant/cpptasks bccontrib bcpkix bcprov commons-codec commons-lang3 dbus-java/dbus	\
		dhcp4java dnsjava dnssecjava easymock felix/org.apache.felix.main fmj/fmj		\
		gdata/gdata-client-1.0 gdata/gdata-client-meta-1.0 gdata/gdata-contacts-3.0		\
		gdata/gdata-contacts-meta-3.0 gdata/gdata-core-1.0					\
		google-http-java-client/google-http-client						\
		google-http-java-client/google-http-client-jackson2					\
		google-oauth-java-client/google-oauth-client guava hexdump-0.2 hsqldb			\
		httpcomponents/httpclient httpcomponents/httpcore httpcomponents/httpmime ice4j irc-api	\
		jain-sip-ri-ossonly java-sdp-api/sdp-api java-sip-api/sip-api-1.2 java-sdp-nist-bridge	\
		jcalendar jdic-misc jitsi-lgpl-dependencies jitsi-smack/smack jitsi-smack/smackx jmdns	\
		jmork jmyspell-core jna jna/jna-platform jnsapi-java/jnsapi joscar-client joscar-common	\
		joscar-protocol jsocks json-simple junit laf-widget libjitsi libphonenumber log4j	\
		macwidgets orange-extensions felix/org.apache.felix.main otr4j/org.otr4j sdes4j		\
		slf4j/api slf4j/jdk14 swingworker unix-0.5 weupnp xpp3-minimal zrtp4j-light		\
		%{nil}

# use system native libs
ln -fs %{_libdir}/libmatthew-java/libunix-java.so %{_jitsi_native_lib}/libunix-java.so
ln -fs %{_libdir}/jdic_misc/libjdic_misc-%{jdic_misc_arch}.so %{_jitsi_native_lib}/libjdic_misc.so

%build
export ANT_OPTS=" -Dlabel=%{subversion} -Djava.sdk=%{java_home} -Ddynamic.linking=true "

# native libs
%ant galagonotification -Dsystem.JAVA_HOME=%{java_home}
%ant globalshortcut
%ant hid
%ant sysactivity
%ant hwaddressretriever

# jars
%ant rebuild

# javadoc
%if %{with docs}
%ant javadoc
%endif

# move common jars into a separate package
%if %{with common}
export ANT_OPTS="$ANT_OPTS -Ddebian.bundles.dest=sc-bundles -Ddebian.bundles.common.dest=%{name}-common "
%ant deb-bundle-common
%endif

%install
# launcher script
install -dm 0755 %{buildroot}%{_bindir}/
install -pm 0755 resources/install/debian/%{name}.sh %{buildroot}%{_bindir}/%{name}

# FIXME: jpackage_script fails
#% jpackage_script net.java.sip.communicator.launcher.SIPCommunicator "-Djna.library.path=%{_jnidir} -Dfelix.config.properties=file:%{_datadir}/%{name}/lib/felix.client.run.properties -Djava.util.logging.config.file=file:%{_datadir}/%{name}/lib/logging.properties" "-client -Xmx256m -splash:../../../share/%{name}/splash.gif" felix/org.apache.felix.framework.jar:felix/org.apache.felix.main.jar:../../lib/java/%{name}/sc-bundles/sc-launcher.jar:../../lib/java/%{name}/sc-bundles/sc-bundles/util.jar:../../lib/java/%{name}/lib %{name} true

# .desktop file

# jars
#  bundles
install -dm 755 %{buildroot}%{_jnidir}/%{name}/lib/bundle/
#ln -fs ../../../../../share/java/felix/felix-bundlerepository.jar %{buildroot}%{_jnidir}/%{name}/lib/bundle/org.apache.felix.bundlerepository.jar
#ln -fs ../../../../../share/java/log4j-1.2.17.jar %{buildroot}%{_jnidir}/%{name}/lib/bundle/log4j.jar
#ln -fs ../../../../../share/java/commons-logging.jar %{buildroot}%{_jnidir}/%{name}/lib/bundle/commons-logging.jar
ln -fs ../../../../../share/java/junit.jar %{buildroot}%{_jnidir}/%{name}/lib/bundle/junit.jar

#   sc-bundles
install -dm 0755 %{buildroot}%{_jnidir}/%{name}/sc-bundles/
install -pm 0644 sc-bundles/*jar %{buildroot}%{_jnidir}/%{name}/sc-bundles/

#   os-specific bundles
install -dm 0755 %{buildroot}%{_jnidir}/%{name}/sc-bundles/
install -pm 0644 sc-bundles/os-specific/linux/*jar %{buildroot}%{_jnidir}/%{name}/sc-bundles/

#   remove test jars from sc-bundles
rm -rf %{buildroot}%{_jnidir}/%{name}/sc-bundles/*-slick.jar
rm -rf %{buildroot}%{_jnidir}/%{name}/sc-bundles/slick*.jar

#  common
%if %{with common}
install -dm 0755 %{buildroot}%{_jnidir}/%{name}-common/
install -pm 0644 jitsi-common/*jar %{buildroot}%{_jnidir}/%{name}-common/
%endif

# native libs
install -dm 0755 %{buildroot}%{_libdir}/%{name}/
install -pm 0644 %{_jitsi_native_lib}/*so %{buildroot}%{_libdir}/%{name}/

# symlink system native libs
ln -fs %{_libdir}/libmatthew-java/libunix-java.so %{buildroot}%{_libdir}/%{name}/
ln -fs %{_libdir}/jdic_misc/libjdic_misc-%{jdic_misc_arch}.so %{buildroot}%{_libdir}/%{name}/libjdic_misc.so

# config properties
install -dm 0755 %{buildroot}%{_datadir}/%{name}/lib/
install -pm 0644 resources/install/logging.properties %{buildroot}%{_datadir}/%{name}/lib/
install -pm 0644 lib/logging.properties %{buildroot}%{_datadir}/%{name}/lib/
install -pm 0644 lib/felix.client.run.properties %{buildroot}%{_datadir}/%{name}/lib/
install -pm 0644 lib/jitsi-defaults.properties        %{buildroot}%{_datadir}/%{name}/lib/

# splash
install -dm 0755 %{buildroot}%{_datadir}/%{name}/
install -pm 0644 resources/install/resources/splash.gif %{buildroot}%{_datadir}/%{name}/

# icons
install -dm 0755 %{buildroot}%{_iconsdir}/hicolor/{16x16,32x32,64x64}/apps/%{name}.png
install -pm 0644 resources/images/logo/sc_logo16x16.png %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png
install -pm 0644 resources/images/logo/sc_logo_32x32.png %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
install -pm 0644 resources/images/logo/sc_logo_64x64.png %{buildroot}%{_iconsdir}/hicolor/64x64/apps/%{name}.png
#   pixmap
install -dm 0755 %{buildroot}%{_datadir}/pixmaps/
convert resources/images/logo/sc_logo_32x32.png %{buildroot}%{_datadir}/pixmaps/%{name}.xpm
#   scalable
install -dm 0755 %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
install -pm 0644 resources/images/logo/sc_logo.svg \
		%{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

# .desktop
install -dm 0755 %{buildroot}%{_datadir}/applications/
desktop-file-install \
    --set-name=%{oname} \
    --set-generic-name=%{oname} \
    --set-icon=%{name} \
    --set-key=Exec \
    --set-value="%{name} %u" \
    --dir %{buildroot}%{_datadir}/applications/ \
    %{name}.desktop

# manpage
install -dm 0755 %{buildroot}%{_mandir}/man1/
install -pm 0644 resources/install/debian/%{name}.1.xz %{buildroot}%{_mandir}/man1/

%if %{with docs}
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -far doc/api/* %{buildroot}%{_javadocdir}/%{name}/
%endif

