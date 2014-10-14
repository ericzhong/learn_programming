#! /bin/bash

FEDORA_VERSION=13
localbasedir=./fedora

SERVER_POOL="rsync://mirrors.sohu.com/fedora \
	rsync://ftp.riken.jp/fedora \
	rsync://mirrors.kernel.org/fedora \
	rsync://ftp.kddilabs.jp/fedora \
	rsync://ftp-stud.hs-esslingen.de/fedora/linux \
	rsync://ftp.jaist.ac.jp/pub/Linux/Fedora"

SRPMS_DIR="updates/$FEDORA_VERSION/SRPMS"
i386_DIR="updates/$FEDORA_VERSION/i386"
x86_64_DIR="updates/$FEDORA_VERSION/x86_64"

RSYNC_OPTIONS="--log-file=$localbasedir/fedora-$FEDORA_VERSION-updates.log -avH --delete --delete-after --delay-updates --exclude='repodata/' --exclude='debug/'"

for SOURCE in $SERVER_POOL
do
	echo rsync from $SOURCE
	#rsync SRPMS
	if [ ! -d $localbasedir/$SRPMS_DIR ]
	then 
		mkdir -p $localbasedir/$SRPMS_DIR
	fi
	if rsync $RSYNC_OPTIONS $SOURCE/$SRPMS_DIR/ $localbasedir/$SRPMS_DIR
	then 
		echo rsync $SOURCE/$SRPMS_DIR succeed!
		createrepo --update $localbasedir/$SRPMS_DIR
		break
	else
		echo rsync failed and try other mirrors
	fi	
done

for SOURCE in $SERVER_POOL
do
	#rsync i386
	if [ ! -d $localbasedir/$i386_DIR ]
	then 
		mkdir -p $localbasedir/$i386_DIR
	fi
	if rsync $RSYNC_OPTIONS $SOURCE/$i386_DIR/ $localbasedir/$i386_DIR
	then 
		echo rsync $SOURCE/$i386_DIR succeed!
		createrepo --update $localbasedir/$i386_DIR
		break
	else
		echo rsync failed and try other mirrors
	fi
done

for SOURCE in $SERVER_POOL
do
	#rsync x86_64
	if [ ! -d $localbasedir/$x86_64_DIR ]
	then 
		mkdir -p $localbasedir/$x86_64_DIR
	fi
	if rsync $RSYNC_OPTIONS $SOURCE/$x86_64_DIR/ $localbasedir/$x86_64_DIR
	then 
		echo rsync $SOURCE/$x86_64_DIR succeed!
		createrepo --update $localbasedir/$x86_64_DIR
		break
	else
		echo rsync failed and try other mirrors
	fi	
done
