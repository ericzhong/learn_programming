.code16

.section .data
msg:
	.ascii "Hello World!"

.section .text
.globl	_start
_start:
	mov	%cs, %ax
	mov	%ax, %ds
	mov	%ax, %es
	mov	$msg, %ax
	mov	%ax, %bp
	mov	$12, %cx
	mov	$0x1301, %ax
	mov	$0x000c, %bx
	movb	$0x00, %dl
	int	$0x10
idle:
	jmp	idle
