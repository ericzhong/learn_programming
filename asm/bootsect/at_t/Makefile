image: boot.s
	as -o boot.o boot.s
	ld --oformat binary -Ttext 7c00 -Tdata 7c20 -o boot boot.o  
	dd bs=512 count=2880 if=boot of=floppy.img  
	echo -ne "\x55\xaa" | dd seek=510 bs=1 of=floppy.img

clean:
	rm boot boot.o floppy.img
