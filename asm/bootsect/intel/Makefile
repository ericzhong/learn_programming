image: boot.s
	nasm boot.s -o boot
	dd bs=512 count=2880 if=boot of=floppy.img 
	echo -ne "\x55\xaa" | dd seek=510 bs=1 of=floppy.img

clean:
	rm boot floppy.img
