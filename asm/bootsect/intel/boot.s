	org 7c00h
	mov ax, cs
	mov ds, ax
	mov es, ax
	mov ax, msg
	mov bp, ax
	mov cx, 12
	mov ax, 1301h
	mov bx, 000ch
	mov dl, 0
	int 10h
	jmp $
msg:			db "Hello World!"
times	510-($-$)	db 0
dw	0xaa55
